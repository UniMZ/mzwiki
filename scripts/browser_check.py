#!/usr/bin/env python3
"""Exercise the public static site in Chromium. Run a local server first."""
from pathlib import Path
import json
import os
from playwright.sync_api import sync_playwright, expect
ROOT=Path(__file__).resolve().parents[1]
BASE=os.environ.get('MZWIKI_BASE_URL','http://127.0.0.1:8000').rstrip('/')
OUT=Path('/tmp/mzwiki-checks');OUT.mkdir(exist_ok=True)
articles=json.loads((ROOT/'content/articles.json').read_text())
count=0
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=os.environ.get('MZWIKI_CHROMIUM','/usr/bin/chromium'),headless=True,args=['--no-sandbox'])
    context=browser.new_context()
    page=context.new_page();errors=[]
    page.on('pageerror',lambda err:errors.append(str(err)))
    paths=['/','/about/','/search/','/404.html']+[('/zh' if lang=='zh' else '')+'/guides/'+a['slug']+'/' for a in articles for lang in ('en','zh')]
    for width,height in [(1440,1000),(390,844)]:
        page.set_viewport_size({'width':width,'height':height})
        for path in paths:
            response=page.goto(BASE+path)
            assert response.status==200,(path,response.status)
            expect(page.locator('h1')).to_be_visible()
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(path,width,'horizontal overflow')
            if '/guides/' in path:
                expect(page.locator('.language')).to_be_visible()
                expect(page.locator('.prose')).to_be_visible()
            count+=1
        page.goto(BASE+'/')
        page.screenshot(path=str(OUT/f'home-{width}.png'),full_page=True)
        page.goto(BASE+'/guides/mz-charge-isotopes/')
        page.screenshot(path=str(OUT/f'article-{width}.png'),full_page=True)
    # Same article and same section survive language switches in both directions.
    page.goto(BASE+'/guides/mz-charge-isotopes/#example')
    page.locator('[data-language-switch]').click()
    expect(page).to_have_url(BASE+'/zh/guides/mz-charge-isotopes/#example')
    expect(page.locator('html')).to_have_attribute('lang','zh')
    page.locator('[data-language-switch]').click()
    expect(page).to_have_url(BASE+'/guides/mz-charge-isotopes/#example');count+=2
    # Native mobile guide navigation and disclosure answer.
    page.locator('.mobile-index summary').click()
    page.locator('.mobile-index a').filter(has_text='How molecules become ions').click()
    expect(page).to_have_url(BASE+'/guides/ionization/')
    page.locator('.prose summary').click()
    expect(page.locator('.prose details')).to_have_attribute('open','');count+=2
    # Live search, language filtering, empty state, query safety, and deep links.
    page.goto(BASE+'/search/')
    expect(page.locator('#search-results li')).to_have_count(8)
    page.locator('#query').fill('isotopes')
    expect(page.locator('#search-results a').first).to_have_text('m/z, charge & isotopes');count+=1
    page.locator('#query').fill('false discovery')
    expect(page.locator('#search-results a').first).to_have_text('From raw data to reliable results');count+=1
    page.locator('#query').fill('')
    page.locator('#language-filter').select_option('zh')
    expect(page.locator('#search-results li')).to_have_count(8)
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
    nojs=browser.new_context(java_script_enabled=False)
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
    assert not errors,errors
    browser.close()
print(f'PASS: {count} browser scenarios; desktop/mobile pages, search, paired-language anchors, keyboard access, no-JavaScript reading; no script errors. Screenshots: {OUT}')
