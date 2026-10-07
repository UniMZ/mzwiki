#!/usr/bin/env python3
"""Exercise the public static site in Chromium. Run a local server first."""
from pathlib import Path
import json
import os
import re
from playwright.sync_api import sync_playwright, expect
ROOT=Path(__file__).resolve().parents[1]
BASE=os.environ.get('MZWIKI_BASE_URL','http://127.0.0.1:8000').rstrip('/')
OUT=Path('/tmp/mzwiki-checks');OUT.mkdir(exist_ok=True)
articles=json.loads((ROOT/'content/articles.json').read_text())
terms=json.loads((ROOT/'content/terms.json').read_text())
def check_header(target, path):
    nav = target.get_by_role('navigation', name='Main navigation')
    active = nav.locator('[aria-current]')
    if path == '/404.html':
        expect(active).to_have_count(0)
        return
    if path.startswith(('/terms/', '/zh/terms/')):
        href, value = '/terms/', 'page' if path == '/terms/' else 'location'
    elif path in ('/about/', '/search/'):
        href, value = path, 'page'
    else:
        href, value = '/#guides', 'location'
    expect(active).to_have_count(1)
    expect(active).to_have_attribute('href', href)
    expect(active).to_have_attribute('aria-current', value)
    expect(nav.locator('.repo-nav')).not_to_have_attribute('aria-current', re.compile('.+'))
    style = active.evaluate('(el) => {const s=getComputedStyle(el); return [s.backgroundColor,s.color,s.borderRadius,s.fontWeight]}')
    assert style == ['rgb(231, 238, 229)', 'rgb(21, 59, 59)', '4px', '600'], (path, style)

count=0
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=os.environ.get('MZWIKI_CHROMIUM','/usr/bin/chromium'),headless=True,args=['--no-sandbox'])
    context=browser.new_context(reduced_motion='reduce')
    page=context.new_page();errors=[]
    page.on('pageerror',lambda err:errors.append(str(err)))
    paths=['/','/about/','/search/','/404.html','/terms/','/terms/az/']+[('/zh' if lang=='zh' else '')+'/guides/'+a['slug']+'/' for a in articles for lang in ('en','zh')]
    paths += [('/zh' if lang=='zh' else '')+'/terms/'+t['slug']+'/' for t in terms for lang in ('en','zh')]
    for width,height in [(1440,1000),(390,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for path in paths:
            response=page.goto(BASE+path)
            assert response.status==200,(path,response.status)
            check_header(page, path)
            expect(page.locator('h1')).to_be_visible()
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(path,width,'horizontal overflow')
            if '/guides/' in path or (path.startswith(('/terms/','/zh/terms/')) and path not in ('/terms/','/terms/az/')):
                expect(page.locator('.language')).to_be_visible()
                expect(page.locator('.prose')).to_be_visible()
            count+=1
        page.goto(BASE+'/')
        page.screenshot(path=str(OUT/f'home-{width}.png'),full_page=True)
        page.goto(BASE+'/guides/mz-charge-isotopes/')
        page.screenshot(path=str(OUT/f'article-{width}.png'),full_page=True)
    # Header state is rendered into HTML and works without JavaScript or a mouse.
    for javascript in (True, False):
        header_context = browser.new_context(java_script_enabled=javascript, reduced_motion='reduce')
        header_page = header_context.new_page()
        for width in (1440, 390, 320):
            header_page.set_viewport_size({'width': width, 'height': 844})
            for path in ('/', '/#guides', '/terms/', '/terms/az/', '/about/', '/search/', '/guides/what-ms-measures/', '/zh/guides/what-ms-measures/', '/terms/detector/', '/zh/terms/detector/', '/404.html'):
                header_page.goto(BASE + path)
                check_header(header_page, path)
                assert header_page.evaluate('document.documentElement.scrollWidth <= innerWidth'), (path, width)
                nav = header_page.get_by_role('navigation', name='Main navigation')
                for link in nav.locator('a:visible').all():
                    link.focus()
                    expect(link).to_be_focused()
                    assert link.evaluate('getComputedStyle(document.activeElement).outlineStyle') != 'none'
                count += 1
            header_page.goto(BASE + '/terms/')
            explore = header_page.get_by_role('navigation', name='Main navigation').get_by_role('link', name='Explore', exact=True)
            explore.focus(); header_page.keyboard.press('Enter')
            expect(header_page).to_have_url(BASE + '/#guides')
            check_header(header_page, '/#guides')
            expect(header_page.locator('#guides')).to_be_in_viewport()
            header_page.screenshot(path=str(OUT / f'header-{javascript}-{width}.png'))
            count += 1
        header_context.close()
    # Terminology views use native URLs and remain complete without JavaScript.
    taxonomy=json.loads((ROOT/'content/term-topics.json').read_text())
    def term_key(term):
        return tuple((1,int(p)) if p.isdigit() else (0,p) for p in re.split(r'(\d+)',term['title'].casefold())),term['slug']
    az_terms=sorted(terms,key=term_key)
    topic_terms=[term for topic in taxonomy['topics'] for term in sorted((t for t in terms if taxonomy['assignments'][t['slug']]==topic['label']),key=term_key)]
    def check_term_view(target,mode):
        expect(target.locator('main')).to_have_attribute('data-term-view',mode)
        links=target.locator('.term-list a')
        expect(links).to_have_count(len(terms))
        actual=links.evaluate_all('(links) => links.map(a => a.getAttribute("href"))')
        expected=['/terms/'+t['slug']+'/' for t in (topic_terms if mode=='topic' else az_terms)]
        assert actual==expected and len(set(actual))==len(terms)
        for link in links.all():
            expect(link).to_be_visible()
            assert link.evaluate('(el) => el.getBoundingClientRect().height >= 44')
        assert target.evaluate('document.documentElement.scrollWidth <= innerWidth')
        switch=target.get_by_role('navigation',name='Terminology views')
        expect(switch.locator('[aria-current="page"]')).to_have_text('By topic' if mode=='topic' else 'A–Z')
        expect(switch.locator('[aria-current="page"]')).to_have_count(1)
        if mode=='topic':
            assert target.locator('.term-topic').evaluate_all('(items) => items.map(el => el.dataset.topic)')==[t['id'] for t in taxonomy['topics']]
        links.first.focus()
        target.keyboard.press('Tab')
        expect(links.nth(1)).to_be_focused()
    for javascript in (True,False):
        browse_context=browser.new_context(java_script_enabled=javascript,reduced_motion='reduce')
        browse=browse_context.new_page()
        for width in (1440,390,320):
            browse.set_viewport_size({'width':width,'height':844})
            browse.goto(BASE+'/terms/')
            check_term_view(browse,'topic');count+=1
            for mode,label,route in [('az','A–Z','/terms/az/'),('topic','By topic','/terms/'),('az','A–Z','/terms/az/'),('topic','By topic','/terms/')]:
                switch=browse.get_by_role('navigation',name='Terminology views').get_by_role('link',name=label,exact=True)
                switch.focus();browse.keyboard.press('Enter')
                expect(browse).to_have_url(BASE+route)
                check_term_view(browse,mode);count+=1
            browse.go_back();expect(browse).to_have_url(BASE+'/terms/az/');check_term_view(browse,'az');count+=1
            browse.go_forward();expect(browse).to_have_url(BASE+'/terms/');check_term_view(browse,'topic');count+=1
            for mode,route in [('topic','/terms/'),('az','/terms/az/')]:
                browse.goto(BASE+route);browse.reload();check_term_view(browse,mode);count+=1
                if javascript:
                    browse.evaluate('scrollTo(0,0)')
                    browse.screenshot(path=str(OUT/f'terminology-{mode}-{width}.png'),full_page=True)
            browse.locator('.term-list a[href="/terms/signal-to-noise-ratio/"]').click()
            expect(browse).to_have_url(BASE+'/terms/signal-to-noise-ratio/')
            browse.go_back();expect(browse).to_have_url(BASE+'/terms/az/');check_term_view(browse,'az');count+=1
            browse.goto(BASE+'/terms/#topic-instruments-signal')
            expect(browse.locator('#topic-instruments-signal')).to_be_visible();count+=1
            browse.goto(BASE+'/terms/detector/')
            nav=browse.locator('.sidebar' if width==1440 else '.mobile-index')
            if width!=1440:nav.locator(':scope > summary').click()
            groups=nav.locator('.term-nav-group')
            assert groups.evaluate_all('(items) => items.map(el => el.dataset.topic)')==[t['id'] for t in taxonomy['topics']]
            assert sorted(groups.locator('a').evaluate_all('(links) => links.map(el => el.getAttribute("href"))'))==sorted('/terms/'+t['slug']+'/' for t in terms)
            expect(nav.locator('a[aria-current="page"]')).to_be_visible()
            nav.locator('.term-nav-views a').filter(has_text='A–Z').click()
            expect(browse).to_have_url(BASE+'/terms/az/');check_term_view(browse,'az');count+=1
        browse_context.close()
    # Same article and same section survive language switches in both directions.
    page.goto(BASE+'/guides/mz-charge-isotopes/#example')
    page.locator('[data-language-switch]').click()
    expect(page).to_have_url(BASE+'/zh/guides/mz-charge-isotopes/#example')
    expect(page.locator('html')).to_have_attribute('lang','zh')
    page.locator('[data-language-switch]').click()
    expect(page).to_have_url(BASE+'/guides/mz-charge-isotopes/#example');count+=2
    # Native mobile guide navigation and disclosure answer.
    page.locator('.mobile-index > summary').click()
    page.locator('.mobile-index .nav-group:not(.term-nav-group)').filter(has=page.locator('summary',has_text='Instruments')).locator('summary').click()
    page.locator('.mobile-index a').filter(has_text='How molecules become ions').click()
    expect(page).to_have_url(BASE+'/guides/ionization/')
    page.locator('.prose summary').first.click()
    expect(page.locator('.prose details').first).to_have_attribute('open','');count+=2
    # Live search, language filtering, empty state, query safety, and deep links.
    page.goto(BASE+'/search/')
    expect(page.locator('#search-results li')).to_have_count(len(articles)+len(terms))
    page.locator('#kind-filter').select_option('guide')
    page.locator('#query').fill('isotopes')
    expect(page.locator('#search-results a').first).to_have_text('m/z, charge & isotopes');count+=1
    page.locator('#query').fill('false discovery')
    expect(page.locator('#search-results a').first).to_have_text('From raw data to reliable results');count+=1
    page.locator('#query').fill('')
    page.locator('#kind-filter').select_option('all')
    page.locator('#language-filter').select_option('zh')
    expect(page.locator('#search-results li')).to_have_count(len(articles)+len(terms))
    page.locator('#kind-filter').select_option('guide')
    page.locator('#query').fill('同位素')
    expect(page.locator('#search-results a').first).to_have_text('质荷比、电荷与同位素');count+=1
    page.locator('#query').fill('zzzz-no-match-123')
    expect(page.locator('#search-results li')).to_have_count(0)
    expect(page.locator('#search-status')).to_contain_text('No articles');count+=1
    page.locator('#query').fill('<img src=x onerror=alert(1)>')
    expect(page.locator('#search-results img')).to_have_count(0);count+=1
    page.goto(BASE+'/search/?q=DIA&lang=en')
    expect(page.locator('#query')).to_have_value('DIA')
    expect(page.locator('#search-results a').first).to_have_text('Acquisition: full scan, DDA, DIA & targeted');count+=1
    # Basic keyboard skip link.
    page.goto(BASE+'/');page.keyboard.press('Tab')
    expect(page.locator('.skip')).to_be_focused();count+=1
    nojs=browser.new_context(java_script_enabled=False,reduced_motion='reduce')
    reader=nojs.new_page();reader.goto(BASE+'/guides/fragmentation/')
    expect(reader.locator('.prose')).to_be_visible();expect(reader.locator('.language a')).to_be_visible();count+=1
    # Enriched teaching example: figure, local reproduction links, paired section
    # anchors, readable tables, and scientific terms in the full-text index.
    for width,height in [(1440,1000),(390,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for lang in ('en','zh'):
            prefix='/zh' if lang=='zh' else ''
            page.goto(BASE+prefix+'/guides/spectrum-interpretation/#example')
            figure=page.locator('.teaching-figure')
            expect(figure.locator('img')).to_be_visible()
            assert figure.locator('img').evaluate('(img) => img.complete && img.naturalWidth > 0')
            assert len(figure.locator('img').get_attribute('alt'))>50
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            expect(page.locator('.prose')).to_contain_text('501.009276')
            figure.screenshot(path=str(OUT/f'spectrum-{lang}-{width}.png'))
            count+=1
    for slug,anchor in [('mz-charge-isotopes','distribution'),('analyzers','resolution-accuracy'),('spectrum-interpretation','quality-step')]:
        page.goto(BASE+'/guides/'+slug+'/#'+anchor)
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/zh/guides/'+slug+'/#'+anchor)
        expect(page.locator('#'+anchor)).to_be_visible()
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/guides/'+slug+'/#'+anchor)
        count+=2
    page.goto(BASE+'/search/?q=binomial')
    expect(page.locator('#search-results li')).to_have_count(2);count+=1
    reader.goto(BASE+'/zh/guides/spectrum-interpretation/#example')
    expect(reader.locator('.teaching-figure img')).to_be_visible();count+=1
    # Ion forms: nine-row calculations, all disclosures, paired anchors and search.
    for width,height in [(1440,1000),(390,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for lang in ('en','zh'):
            prefix='/zh' if lang=='zh' else ''
            page.goto(BASE+prefix+'/guides/ionization/#example')
            table=page.locator('.prose table').nth(3)
            expect(table.locator('tbody tr')).to_have_count(9)
            expect(table).to_contain_text('161.998249')
            wrapper=table.locator('..')
            wrapper.evaluate('(el) => { el.scrollLeft = el.scrollWidth; }')
            assert wrapper.evaluate('(el) => el.scrollWidth <= el.clientWidth || el.scrollLeft > 0')
            wrapper.evaluate('(el) => { el.scrollLeft = 0; }')
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            page.locator('#example').scroll_into_view_if_needed()
            page.screenshot(path=str(OUT/f'ionization-{lang}-{width}.png'))
            details=page.locator('.prose details')
            expect(details).to_have_count(3)
            for i in range(3):
                details.nth(i).locator('summary').click()
                expect(details.nth(i).locator('p')).to_be_visible()
                details.nth(i).locator('summary').click()
            count+=1
    for anchor in ('maldi','ion-forms','mass-recovery','example-negative','misconceptions'):
        page.goto(BASE+'/guides/ionization/#'+anchor)
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/zh/guides/ionization/#'+anchor)
        expect(page.locator('#'+anchor)).to_be_visible()
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/guides/ionization/#'+anchor)
        count+=2
    for lang,query in [('en','chain ejection'),('zh','链排出')]:
        page.goto(BASE+'/search/?lang='+lang)
        page.locator('#query').fill(query)
        expect(page.locator('#search-results a').first).to_have_attribute('href',('/zh' if lang=='zh' else '')+'/guides/ionization/')
        count+=1
    for prefix in ('','/zh'):
        reader.goto(BASE+prefix+'/guides/ionization/#practice')
        reader.locator('.prose summary').last.click()
        expect(reader.locator('.prose details').last.locator('p')).to_be_visible()
        count+=1
    # Terminology collection stays separate from the numbered Guide sequence.
    for width,height in [(1440,1000),(390,844)]:
        page.set_viewport_size({'width':width,'height':height})
        page.goto(BASE+'/terms/')
        expect(page.locator('.term-list a')).to_have_count(len(terms))
        page.locator('.term-list a[href="/terms/mz/"]').click()
        expect(page).to_have_url(BASE+'/terms/mz/')
        expect(page.locator('.eyebrow').last).to_have_text('Terminology')
        page.screenshot(path=str(OUT/f'term-{width}.png'),full_page=True)
        count+=1
    for term in terms:
        slug=term['slug']
        page.goto(BASE+'/terms/'+slug+'/#example')
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/zh/terms/'+slug+'/#example')
        expect(page.locator('#example')).to_be_visible()
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/terms/'+slug+'/#example')
        expect(page.locator('.related-links a').first).to_have_attribute('href','/guides/'+term['related_guides'][0]+'/')
        count+=2
    page.goto(BASE+'/search/?kind=term')
    expect(page.locator('#kind-filter')).to_have_value('term')
    expect(page.locator('#search-results li')).to_have_count(len(terms))
    expect(page.locator('#search-results small').first).to_contain_text('Term')
    page.locator('#query').fill('monoisotopic')
    expect(page.locator('#search-results a').first).to_have_attribute('href','/terms/monoisotopic-mass/')
    page.locator('#language-filter').select_option('zh')
    page.locator('#query').fill('单同位素质量')
    expect(page.locator('#search-results a').first).to_have_attribute('href','/zh/terms/monoisotopic-mass/')
    page.reload()
    expect(page.locator('#kind-filter')).to_have_value('term')
    expect(page.locator('#language-filter')).to_have_value('zh')
    page.locator('#query').fill('')
    page.locator('#language-filter').select_option('all')
    expect(page.locator('#search-results li')).to_have_count(2*len(terms))
    page.locator('#kind-filter').select_option('guide')
    expect(page.locator('#search-results li')).to_have_count(2*len(articles))
    expect(page.locator('#search-results small').first).to_contain_text('Guide')
    count+=6
    reader.goto(BASE+'/terms/')
    reader.locator('.term-list a[href="/terms/mz/"]').click()
    expect(reader).to_have_url(BASE+'/terms/mz/')
    reader.locator('[data-language-switch]').click()
    expect(reader).to_have_url(BASE+'/zh/terms/mz/')
    count+=2
    page.goto(BASE+'/guides/ionization/')
    expect(page.locator('.related-links a[href="/terms/adduct-ion/"]')).to_have_count(1)
    count+=1
    # Analyzer additions: all new section switches and readable equations/tables.
    for anchor in ('quadrupole','tof','ion-traps','frequency','orbitrap','fticr','transient-time','hybrids'):
        page.goto(BASE+'/guides/analyzers/#'+anchor)
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/zh/guides/analyzers/#'+anchor)
        expect(page.locator('#'+anchor)).to_be_visible()
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/guides/analyzers/#'+anchor)
        count+=2
    for width,height in [(1440,1000),(390,844),(320,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for prefix in ('','/zh'):
            for route in ('/guides/analyzers/','/terms/mass-analyzer/','/terms/transient/'):
                page.goto(BASE+prefix+route)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,prefix,route)
                for code in page.locator('.prose code').all():
                    assert code.evaluate('(el) => el.scrollWidth <= el.clientWidth + 1 || getComputedStyle(el).display === "inline"')
                if route=='/guides/analyzers/':
                    expect(page.locator('.prose details')).to_have_count(3)
                    for detail in page.locator('.prose details').all():
                        detail.locator('summary').click()
                        expect(detail.locator('p')).to_be_visible()
                    expect(page.locator('.related-links a[href="'+prefix+'/terms/transient/"]')).to_have_count(1)
                    page.locator('#tof').scroll_into_view_if_needed()
                    page.screenshot(path=str(OUT/f'analyzers-{prefix.strip("/") or "en"}-{width}.png'))
                count+=1
    for lang,q,path in [('en','transient','/terms/transient/'),('zh','瞬态信号','/zh/terms/transient/')]:
        page.goto(BASE+'/search/?kind=term&lang='+lang)
        page.locator('#query').fill(q)
        expect(page.locator('#search-results a').first).to_have_attribute('href',path)
        count+=1
    # Fragmentation: reaction-relative terms, paired anchors and charge-aware tables.
    for anchor in ('measurement','collisions','electrons','residue-gap','conservation','coisolation','evidence'):
        page.goto(BASE+'/guides/fragmentation/#'+anchor)
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/zh/guides/fragmentation/#'+anchor)
        expect(page.locator('#'+anchor)).to_be_visible()
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/guides/fragmentation/#'+anchor)
        count+=2
    for width,height in [(1440,1000),(390,844),(320,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for prefix in ('','/zh'):
            for route in ('/guides/fragmentation/','/terms/precursor-ion/','/terms/product-ion/','/terms/neutral-loss/'):
                page.goto(BASE+prefix+route)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,prefix,route)
                if route=='/guides/fragmentation/':
                    expect(page.locator('.prose table').nth(1)).to_contain_text('292.0947')
                    for wrapper in page.locator('.prose .table-wrap').all():
                        wrapper.evaluate('(el) => {el.scrollLeft=el.scrollWidth;}')
                        assert wrapper.evaluate('(el) => el.scrollWidth <= el.clientWidth || el.scrollLeft > 0')
                    for slug in ('precursor-ion','product-ion','neutral-loss'):
                        expect(page.locator('.related-links a[href="'+prefix+'/terms/'+slug+'/"]')).to_have_count(1)
                    expect(page.locator('.prose details')).to_have_count(3)
                    for detail in page.locator('.prose details').all():
                        detail.locator('summary').focus()
                        page.keyboard.press('Enter')
                        expect(detail.locator('p')).to_be_visible()
                    page.emulate_media(reduced_motion='reduce')
                    page.locator('#example').scroll_into_view_if_needed()
                    page.screenshot(path=str(OUT/f'fragmentation-{prefix.strip("/") or "en"}-{width}.png'))
                count+=1
    for lang,q,path in [('en','neutral loss','/terms/neutral-loss/'),('zh','中性丢失','/zh/terms/neutral-loss/')]:
        page.goto(BASE+'/search/?kind=term&lang='+lang)
        page.locator('#query').fill(q)
        expect(page.locator('#search-results a').first).to_have_attribute('href',path)
        count+=1
    # Acquisition: sampling schedule, isolation and software extraction are distinct.
    for anchor in ('levels','full-scan','dda','exclusion','dia','windows','targeted','traces','sampling','overheads'):
        page.goto(BASE+'/guides/acquisition/#'+anchor)
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/zh/guides/acquisition/#'+anchor)
        expect(page.locator('#'+anchor)).to_be_visible()
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/guides/acquisition/#'+anchor)
        count+=2
    for width,height in [(1440,1000),(390,844),(320,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for prefix in ('','/zh'):
            for route in ('/guides/acquisition/','/terms/acquisition-cycle/','/terms/isolation-window/','/terms/extracted-ion-chromatogram/'):
                page.goto(BASE+prefix+route)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,prefix,route)
                for wrapper in page.locator('.prose .table-wrap').all():
                    wrapper.evaluate('(el) => {el.scrollLeft=el.scrollWidth;}')
                    assert wrapper.evaluate('(el) => el.scrollWidth <= el.clientWidth || el.scrollLeft > 0')
                    wrapper.evaluate('(el) => {el.scrollLeft=0;}')
                if route=='/guides/acquisition/':
                    for slug in ('acquisition-cycle','isolation-window','extracted-ion-chromatogram'):
                        expect(page.locator('.related-links a[href="'+prefix+'/terms/'+slug+'/"]')).to_have_count(1)
                    expect(page.locator('.prose details')).to_have_count(5)
                    for detail in page.locator('.prose details').all():
                        detail.locator('summary').focus()
                        page.keyboard.press('Enter')
                        expect(detail.locator('p')).to_be_visible()
                if route in ('/guides/acquisition/','/terms/extracted-ion-chromatogram/'):
                    page.locator('#example').scroll_into_view_if_needed()
                    page.screenshot(path=str(OUT/f'acquisition-{route.split("/")[-2]}-{prefix.strip("/") or "en"}-{width}.png'))
                count+=1
    for lang,q,path in [('en','extracted ion chromatogram','/terms/extracted-ion-chromatogram/'),('zh','提取离子色谱图','/zh/terms/extracted-ion-chromatogram/')]:
        page.goto(BASE+'/search/?kind=term&lang='+lang)
        page.locator('#query').fill(q)
        expect(page.locator('#search-results a').first).to_have_attribute('href',path)
        count+=1
    # Data analysis: evidence levels, missing values and paired article navigation.
    for anchor in ('representation','features','error-control','quantification','normalization','design','missingness','reproducibility'):
        page.goto(BASE+'/guides/data-analysis/#'+anchor)
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/zh/guides/data-analysis/#'+anchor)
        expect(page.locator('#'+anchor)).to_be_visible()
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/guides/data-analysis/#'+anchor)
        count+=2
    for width,height in [(1440,1000),(390,844),(320,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for prefix in ('','/zh'):
            for route in ('/guides/data-analysis/','/terms/feature/','/terms/false-discovery-rate/','/terms/missing-value/'):
                page.goto(BASE+prefix+route)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,prefix,route)
                for wrapper in page.locator('.prose .table-wrap').all():
                    wrapper.evaluate('(el) => {el.scrollLeft=el.scrollWidth;}')
                    assert wrapper.evaluate('(el) => el.scrollWidth <= el.clientWidth || el.scrollLeft > 0')
                if route=='/guides/data-analysis/':
                    for slug in ('feature','false-discovery-rate','missing-value'):
                        expect(page.locator('.related-links a[href="'+prefix+'/terms/'+slug+'/"]')).to_have_count(1)
                    for detail in page.locator('.prose details').all():
                        detail.locator('summary').focus()
                        page.keyboard.press('Enter')
                        expect(detail.locator('p').first).to_be_visible()
                    page.locator('#example').scroll_into_view_if_needed()
                    page.screenshot(path=str(OUT/f'data-analysis-{prefix.strip("/") or "en"}-{width}.png'))
                count+=1
    for lang,q,path in [('en','false discovery rate','/terms/false-discovery-rate/'),('zh','缺失值','/zh/terms/missing-value/')]:
        page.goto(BASE+'/search/?kind=term&lang='+lang)
        page.locator('#query').fill(q)
        expect(page.locator('#search-results a').first).to_have_attribute('href',path)
        count+=1
    # Beginner bridge: paired entrances, original signal table, and new terms.
    for slug,anchor in [('what-ms-measures','spectra-and-traces'),('spectrum-interpretation','context')]:
        page.goto(BASE+'/guides/'+slug+'/#'+anchor)
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/zh/guides/'+slug+'/#'+anchor)
        expect(page.locator('#'+anchor)).to_be_visible()
        page.locator('[data-language-switch]').click()
        expect(page).to_have_url(BASE+'/guides/'+slug+'/#'+anchor)
        count+=2
    for width,height in [(1440,1000),(390,844),(320,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for prefix in ('','/zh'):
            for route in ('/guides/what-ms-measures/','/guides/spectrum-interpretation/','/terms/mass-spectrum/','/terms/base-peak/'):
                page.goto(BASE+prefix+route)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,prefix,route)
                for wrapper in page.locator('.prose .table-wrap').all():
                    wrapper.evaluate('(el) => {el.scrollLeft=el.scrollWidth;}')
                    assert wrapper.evaluate('(el) => el.scrollWidth <= el.clientWidth || el.scrollLeft > 0')
                    wrapper.evaluate('(el) => {el.scrollLeft=0;}')
                for detail in page.locator('.prose details').all():
                    detail.locator('summary').focus()
                    page.keyboard.press('Enter')
                    expect(detail.locator('p').first).to_be_visible()
                if route=='/guides/what-ms-measures/':
                    expect(page.locator('.prose tbody tr')).to_have_count(3)
                    for slug in ('mass-spectrum','base-peak'):
                        expect(page.locator('.related-links a[href="'+prefix+'/terms/'+slug+'/"]')).to_have_count(1)
                    page.locator('#spectra-and-traces').scroll_into_view_if_needed()
                    page.screenshot(path=str(OUT/f'reading-bridge-{prefix.strip("/") or "en"}-{width}.png'))
                count+=1
    for lang,q,path in [('en','mass spectrum','/terms/mass-spectrum/'),('en','base peak','/terms/base-peak/'),('zh','质谱图','/zh/terms/mass-spectrum/'),('zh','基峰','/zh/terms/base-peak/')]:
        page.goto(BASE+'/search/?kind=term&lang='+lang)
        page.locator('#query').fill(q)
        expect(page.locator('#search-results a').first).to_have_attribute('href',path)
        count+=1
    # Expansion: exercise every new article, section switch and exact-title search.
    additions=[]
    for packet in sorted((ROOT/'review').glob('expansion-*')):
        for kind,filename in [('guide','articles'),('term','terms')]:
            additions.extend((kind,a) for a in json.loads((packet/f'metadata/{filename}.additions.json').read_text()))
    for kind,a in additions:
        collection='guides' if kind=='guide' else 'terms'
        route='/'+collection+'/'+a['slug']+'/'
        source=ROOT/'content'/('terms' if kind=='term' else '')/'en'/(a['slug']+'.html')
        import re
        for anchor in re.findall(r'<h[23] id="([^"]+)"',source.read_text()):
            page.goto(BASE+route+'#'+anchor)
            page.locator('[data-language-switch]').click()
            expect(page).to_have_url(BASE+'/zh'+route+'#'+anchor)
            expect(page.locator('#'+anchor)).to_be_visible()
            page.locator('[data-language-switch]').click()
            expect(page).to_have_url(BASE+route+'#'+anchor)
            count+=2
        for lang in ('en','zh'):
            prefix='/zh' if lang=='zh' else ''
            for width in (1440,390,320):
                page.set_viewport_size({'width':width,'height':844})
                page.goto(BASE+prefix+route)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(route,lang,width)
                for wrapper in page.locator('.prose .table-wrap').all():
                    wrapper.evaluate('(el) => {el.scrollLeft=el.scrollWidth;}')
                    assert wrapper.evaluate('(el) => el.scrollWidth <= el.clientWidth || el.scrollLeft > 0')
                for detail in page.locator('.prose details').all():
                    detail.locator('summary').focus()
                    page.keyboard.press('Enter')
                    expect(detail).to_have_attribute('open','')
                    expect(detail.locator('p').first).to_be_visible()
                nav=page.locator('.sidebar' if width==1440 else '.mobile-index')
                if width!=1440:
                    nav.locator(':scope > summary').focus()
                    page.keyboard.press('Enter')
                expect(nav.locator('a[aria-current="page"]')).to_be_visible()
                assert nav.evaluate('(el) => el.clientHeight <= innerHeight'),(route,width,'navigation height')
                if width==320 and kind=='guide':
                    nav.locator(':scope > summary').click()
                    page.locator('h1').scroll_into_view_if_needed()
                    page.screenshot(path=str(OUT/f'expansion-{a["slug"]}-{lang}-320.png'))
                count+=1
            page.goto(BASE+'/search/?kind='+kind+'&lang='+lang)
            page.locator('#query').fill(a['title'] if lang=='en' else a['zh_title'])
            expect(page.locator('#search-results a').first).to_have_attribute('href',prefix+route)
            count+=1
            reader.goto(BASE+prefix+route)
            expect(reader.locator('.prose')).to_be_visible()
            count+=1
    # Long navigation lists: every group opens by keyboard; links retain English labels.
    for width in (1440,320):
        page.set_viewport_size({'width':width,'height':844})
        page.goto(BASE+'/guides/what-ms-measures/')
        nav=page.locator('.sidebar' if width==1440 else '.mobile-index')
        if width==320:nav.locator(':scope > summary').click()
        for group in nav.locator('.nav-group').all():
            if group.get_attribute('open') is None:
                group.locator('summary').focus()
                page.keyboard.press('Enter')
            expect(group.locator('a').last).to_be_visible()
            group.locator('summary').focus()
            page.keyboard.press('Enter')
            assert group.get_attribute('open') is None
            count+=1
        page.goto(BASE+'/')
        expect(page.locator('#guides .article-card')).to_have_count(len(articles))
        expect(page.locator('.stats')).to_contain_text(str(len(articles)))
        expect(page.locator('.group-jumps a')).to_have_count(len(set(a['group'] for a in articles)))
        page.locator('.group-jumps a').last.click()
        expect(page.locator('.guide-group').last).to_be_visible()
        page.screenshot(path=str(OUT/f'expansion-home-{width}.png'))
        count+=1
    assert not errors,errors
    browser.close()
print(f'PASS: {count} browser scenarios; desktop/mobile pages, search, paired-language anchors, keyboard access, no-JavaScript reading; no script errors. Screenshots: {OUT}')
