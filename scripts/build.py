#!/usr/bin/env python3
"""Build the committed static website using only the Python standard library."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://mzwiki.unimz.org'
REPO = 'https://github.com/UniMZ/mzwiki'
ARTICLES = json.loads((ROOT / 'content/articles.json').read_text())
TERMS = json.loads((ROOT / 'content/terms.json').read_text())
TERM_BY_SLUG = {a['slug']: a for a in TERMS}
REFS = json.loads((ROOT / 'content/references.json').read_text())
BY_SLUG = {a['slug']: a for a in ARTICLES}
e = html.escape

def url(slug, lang='en', kind='guide'):
    return ('/zh' if lang == 'zh' else '') + ('/terms/' if kind == 'term' else '/guides/') + slug + '/'

def plain(text):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', text))).strip()

def write(path, text):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding='utf-8')

HEADER = f'''<a class="skip" href="#main">Skip to content</a>
<header class="header" lang="en"><div class="header-inner">
<a class="brand" href="/" aria-label="mzwiki home"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span><em>mz</em>wiki</span></a>
<span class="tagline">A mass spectrometry<br>knowledge commons</span>
<nav class="topnav" aria-label="Main navigation"><a href="/#guides">Explore</a><a href="/terms/">Terminology</a><a class="about-nav" href="/about/">About</a><a class="repo-nav" href="{REPO}">GitHub →</a><a class="search-link" href="/search/">Search <span aria-hidden="true">/</span></a></nav>
</div></header>'''
FOOTER = f'''<footer lang="en"><div class="container footer-inner"><span><strong>mzwiki</strong> · A UniMZ knowledge project</span><div class="footer-links"><a href="/about/">About &amp; editorial approach</a><a href="{REPO}/blob/main/CONTRIBUTING.md">Contribute</a><a href="{REPO}">Source →</a></div></div></footer>'''

def page(title, description, body, path='/', lang='en', alternates=''):
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} · mzwiki</title><meta name="description" content="{e(description, quote=True)}">
<link rel="canonical" href="{SITE}{path}">{alternates}<meta name="theme-color" content="#176052">
<meta property="og:title" content="{e(title, quote=True)} · mzwiki"><meta property="og:description" content="{e(description, quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{SITE}{path}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css"><script defer src="/assets/site.js"></script></head>
<body>{HEADER}{body}{FOOTER}</body></html>\n'''

def guide_groups():
    groups = {}
    for article in ARTICLES:
        groups.setdefault(article['group'], []).append(article)
    return groups

def navigation(active='', kind='guide'):
    parts = ['<a class="browse-all" href="/#guides">All Guides</a>']
    for group, articles in guide_groups().items():
        opened = ' open' if kind == 'guide' and any(a['slug'] == active for a in articles) else ''
        links = []
        for a in articles:
            attrs = ' class="active" aria-current="page"' if kind == 'guide' and a['slug'] == active else ''
            links.append(f'<a{attrs} href="{url(a["slug"])}">{e(a["title"])}</a>')
        parts.append(f'<details class="nav-group"{opened}><summary>{e(group)} <span>{len(articles)}</span></summary>{"".join(links)}</details>')
    parts.append('<a class="browse-all" href="/terms/">All terminology</a>')
    for label, lower, upper in [('A–F','a','f'),('G–M','g','m'),('N–S','n','s'),('T–Z','t','z')]:
        entries = sorted((t for t in TERMS if lower <= t['title'][0].lower() <= upper), key=lambda t:t['title'].lower())
        if not entries:
            continue
        opened = ' open' if kind == 'term' and any(t['slug'] == active for t in entries) else ''
        links = []
        for t in entries:
            attrs = ' class="active" aria-current="page"' if kind == 'term' and t['slug'] == active else ''
            links.append(f'<a{attrs} href="{url(t["slug"],kind="term")}">{e(t["title"])}</a>')
        parts.append(f'<details class="nav-group"{opened}><summary>Terms {label} <span>{len(entries)}</span></summary>{"".join(links)}</details>')
    return ''.join(parts)

spectrum='''<figure class="spectrum-card"><div class="figure-top"><span>Reading the invisible</span><span class="figure-tag">MS / 001</span></div>
<svg viewBox="0 0 460 275" role="img" aria-labelledby="spectrum-title spectrum-desc"><title id="spectrum-title">An illustrative mass spectrum</title><desc id="spectrum-desc">Vertical peaks at different mass-to-charge ratios; height encodes relative signal. This is a schematic, not experimental data.</desc>
<g stroke="#d6e2d5" stroke-width="1"><path d="M44 53H438M44 103H438M44 153H438M44 203H438"/></g><path d="M44 30V222H438" fill="none" stroke="#6f8b7d"/>
<g fill="#526866" font-size="10" font-family="monospace"><text x="14" y="57">100</text><text x="20" y="156">40</text><text x="24" y="225">0</text><text x="74" y="243">100</text><text x="181" y="243">200</text><text x="286" y="243">300</text><text x="400" y="243">400</text><text x="227" y="266">m/z</text><text x="44" y="16">Relative intensity (%)</text></g>
<g stroke="#176052" stroke-width="2.5"><path d="M77 221V191M99 221V174M119 221V202M155 221V133M181 221V190M221 221V53M226 221V166M231 221V205M271 221V164M308 221V111M313 221V180M318 221V210M369 221V149M375 221V196M419 221V208"/></g>
<circle cx="221" cy="53" r="4" fill="#176052"/><path d="M228 49L251 30H310" fill="none" stroke="#176052"/><text x="257" y="23" font-size="11" font-family="monospace" fill="#176052">A peak is evidence.</text></svg>
<figcaption>Mass-to-charge ratio locates a signal. Context gives it meaning.<br>Illustrative spectrum · not experimental data</figcaption></figure>'''
cards = ''
for group, articles in guide_groups().items():
    group_cards = ''.join(f'<a class="article-card" href="{url(a["slug"])}"><span class="num">{ARTICLES.index(a)+1:02d}</span><div><h3>{e(a["title"])}</h3><p>{e(a["summary"])}</p><small>{e(a["group"]).upper()} · EN + ZH ARTICLES</small></div><span class="arrow" aria-hidden="true">→</span></a>' for a in articles)
    ident = 'group-' + re.sub(r'[^a-z0-9]+', '-', group.lower()).strip('-')
    cards += f'<section class="guide-group" id="{ident}" aria-labelledby="{ident}-title"><h3 id="{ident}-title">{e(group)}</h3><div class="article-grid">{group_cards}</div></section>'
group_jumps = ''.join(f'<a href="#group-{re.sub(r"[^a-z0-9]+", "-", group.lower()).strip("-")}">{e(group)}</a>' for group in guide_groups())

home=f'''<main id="main" class="container"><section class="hero"><div><div class="eyebrow">The fundamentals, connected</div><h1>Make sense<br>of <em>mass spectra.</em></h1><p class="lead">A practical knowledge wiki for understanding ions, instruments, and the evidence in your data. Start with the basics. Build toward better questions.</p><div class="actions"><a class="button" href="{url(ARTICLES[0]['slug'])}">Start learning <span aria-hidden="true">→</span></a><a class="text-link" href="#guides">Browse the guides</a></div></div>{spectrum}</section>
<div class="stats"><span><strong>{len(ARTICLES):02d}</strong> learning guides</span><span><strong>02</strong> article languages</span><span>From <strong>first principles</strong> to analysis</span></div>
<section class="section" aria-labelledby="path-title"><div class="section-head"><div><div class="eyebrow">Find your starting point</div><h2 id="path-title">A path through the spectrum</h2></div><p>Read in order, or pick up the concept you need. Each guide connects to the next.</p></div><div class="path">
<a class="path-card" href="/guides/what-ms-measures/"><span class="path-number">01 / UNDERSTAND</span><h3>New to mass spectrometry?</h3><p>Start with what we actually measure, then learn to recognize charge states and isotope patterns.</p><span class="path-foot">FOUNDATIONS <span aria-hidden="true">→</span></span></a>
<a class="path-card" href="/guides/ionization/"><span class="path-number">02 / CONNECT</span><h3>From sample to spectrum</h3><p>Follow ions through the source, analyzer, and fragmentation experiment. See how choices shape evidence.</p><span class="path-foot">INSTRUMENTS &amp; METHODS <span aria-hidden="true">→</span></span></a>
<a class="path-card" href="/guides/data-analysis/"><span class="path-number">03 / INTERPRET</span><h3>Make your data count</h3><p>Connect acquisition to analysis, confidence, and reproducibility—with routes into computational methods.</p><span class="path-foot">ANALYSIS &amp; COMPUTATION <span aria-hidden="true">→</span></span></a></div></section>
<section class="section" id="guides" aria-labelledby="guides-title"><div class="section-head"><div><div class="eyebrow">The knowledge base</div><h2 id="guides-title">Explore the guides</h2></div><a class="text-link" href="/search/">Find a concept →</a></div><nav class="group-jumps" aria-label="Guide topics">{group_jumps}</nav>{cards}</section>
<aside class="note-band"><h3>Built around understanding.</h3><p>Concepts, principles, and methods are the focus here. Worked examples connect the ideas; references let you go deeper. Chinese translations are available from each article, with the same topic one click away.</p></aside></main>'''
write('index.html',page('Understand mass spectrometry','A practical mass spectrometry wiki: foundational concepts, instruments, methods, and reliable data analysis.',home))
search_index=[]
for kind,a in [('guide',a) for a in ARTICLES]+[('term',t) for t in TERMS]:
    for lang in ('en','zh'):
        slug=a['slug'];title=a['title'] if lang=='en' else a['zh_title'];summary=a['summary'] if lang=='en' else a['zh_summary']
        source=Path('content')/('terms' if kind=='term' else '')/lang/(slug+'.html')
        body=(ROOT/source).read_text()
        heads=re.findall(r'<h2 id="([^"]+)">(.*?)</h2>',body)
        toc=''.join(f'<a href="#{ident}">{e(plain(label))}</a>' for ident,label in heads)
        prereqs=', '.join(f'<a href="{url(s,lang)}">{e(BY_SLUG[s]["title"] if lang=="en" else BY_SLUG[s]["zh_title"])}</a>' for s in a.get('prereqs',[])) or 'No prior MS knowledge needed.'
        refs=''.join(f'<li id="ref-{r}"><a href="{e(REFS[r]["url"],quote=True)}">{e(REFS[r]["title"])}</a><p>{e(REFS[r]["note"])}</p></li>' for r in a['refs'])
        related=''.join(f'<a href="{url(s,lang)}">{e(BY_SLUG[s]["title"] if lang=="en" else BY_SLUG[s]["zh_title"])} →</a>' for s in a.get('related',a.get('related_guides',[])))
        term_slugs=a['related_terms'] if kind=='term' else [t['slug'] for t in TERMS if slug in t['related_guides']]
        term_links=''.join(f'<a href="{url(t,lang,"term")}">{e(TERM_BY_SLUG[t]["title"] if lang=="en" else TERM_BY_SLUG[t]["zh_title"])} →</a>' for t in term_slugs)
        related_section=f'<section class="related"><h2>{"Related Guides" if kind=="term" else "Continue exploring"}</h2><div class="related-links">{related}</div></section>'
        if term_links:
            related_section+=f'<section class="related"><h2>Related terminology</h2><div class="related-links">{term_links}</div></section>'
        prereq_section=f'<div class="prerequisites"><strong>Before you begin: </strong>{prereqs}</div>' if kind=='guide' else ''
        collection='Terminology' if kind=='term' else 'Guides'
        collection_url='/terms/' if kind=='term' else '/#guides'
        eyebrow='Terminology' if kind=='term' else f'Guide {ARTICLES.index(a)+1:02d} · {e(a["group"])}'
        languages=''.join(f'<strong aria-current="page">{label}</strong>' if l==lang else f'<a data-language-switch href="{url(slug,l,kind)}" hreflang="{l}" lang="{l}" aria-label="Read this article in {"English" if l=="en" else "Chinese"}">{label}</a>' for l,label in [('en','EN'),('zh','ZH')])
        alternates=''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{url(slug,l,kind)}">' for l in ('en','zh'))+f'<link rel="alternate" hreflang="x-default" href="{SITE}{url(slug,kind=kind)}">'
        article=f'''<div class="page-layout"><aside class="sidebar" lang="en" aria-label="Knowledge navigation"><p class="sidebar-title">Explore the wiki</p>{navigation(slug,kind)}</aside><main id="main" class="article"><details class="mobile-index"><summary>Guides &amp; terminology</summary>{navigation(slug,kind)}</details><div class="breadcrumb"><a href="/">Home</a> / <a href="{collection_url}">{collection}</a></div><div class="eyebrow">{eyebrow}</div><h1 lang="{lang}">{e(title)}</h1><p class="article-lead" lang="{lang}">{e(summary)}</p><div class="article-meta" lang="en"><span>{"TERM ENTRY" if kind=="term" else "FOUNDATIONAL GUIDE"} · OCT 2026</span><nav class="language" aria-label="Article language">{languages}</nav></div>{prereq_section}<div class="prose" lang="{lang}">{body}</div><section class="references" lang="en" aria-labelledby="references"><h2 id="references">References &amp; further reading</h2><ol>{refs}</ol></section>{related_section}<div class="article-end"><span>Help make this article clearer.</span><a href="{REPO}/edit/main/{source.as_posix()}">Edit this article →</a><a href="{REPO}/issues/new?template=content.yml">Suggest a correction →</a></div></main><aside class="toc" aria-label="On this page"><p class="sidebar-title">On this page</p>{toc}<a href="#references">References</a></aside></div>'''
        write(url(slug,lang,kind).strip('/')+'/index.html',page(title,summary,article,url(slug,lang,kind),lang,alternates))
        search_index.append(dict(title=title,summary=summary,url=url(slug,lang,kind),lang=lang,group=a.get('group','Terminology'),kind=kind,text=plain(body)))
term_cards=''.join(f'<a class="article-card term-card" href="{url(t["slug"],kind="term")}"><div><h3>{e(t["title"])}</h3><p>{e(t["summary"])}</p><small>TERM · EN + ZH ARTICLES</small></div><span class="arrow" aria-hidden="true">→</span></a>' for t in TERMS)
term_index=f'<main id="main" class="simple"><div class="eyebrow">Look up a concept</div><h1>Terminology</h1><p class="lead">Short definitions and examples, connected to the <a href="/#guides">Guides</a>. Each entry has a matching Chinese translation.</p><div class="article-grid">{term_cards}</div></main>'
write('terms/index.html',page('Terminology','Mass spectrometry terms with definitions, examples, and links to the Guides.',term_index,'/terms/'))
write('assets/search-index.json',json.dumps(search_index,ensure_ascii=False,separators=(',',':'))+'\n')
search='''<main id="main" class="simple"><div class="eyebrow">Find a concept</div><h1>Search the wiki</h1><p class="lead">Search titles and full article text. Try “isotopes”, “DIA”, or “false discovery”.</p><form class="search-form" role="search"><label class="sr-only" for="query">Search articles</label><input id="query" type="search" name="q" placeholder="What would you like to understand?" autocomplete="off"><label class="sr-only" for="language-filter">Article language</label><select id="language-filter" name="lang"><option value="en">English articles</option><option value="zh">Chinese articles</option><option value="all">All articles</option></select><label class="sr-only" for="kind-filter">Content type</label><select id="kind-filter" name="kind"><option value="all">Guides and terms</option><option value="guide">Guides</option><option value="term">Terminology</option></select></form><p id="search-status" class="search-status" role="status" aria-live="polite">Loading the article index…</p><ul id="search-results" class="search-results"></ul><noscript><p>Search requires JavaScript. Browse the <a href="/#guides">Guides</a> or <a href="/terms/">Terminology index</a>.</p></noscript></main>'''
write('search/index.html',page('Search','Search all mass spectrometry guides in English and Chinese.',search,'/search/'))
about=f'''<main id="main" class="simple"><div class="eyebrow">About the project</div><h1>Knowledge that connects.</h1><p class="lead">mzwiki is a UniMZ knowledge project for learning mass spectrometry and revisiting its underlying principles.</p><div class="prose"><h2 id="scope">What belongs here</h2><p>Clear explanations of concepts, instrument principles, experimental methods, and computational reasoning. The first collection moves from ions and spectra to acquisition, interpretation, and reproducible analysis. It is a learning resource, not an instrument operating procedure or a publication feed.</p><h2 id="approach">How to read the guides</h2><p>Start with prerequisites, work through the examples, and use the questions to test your understanding. Examples labeled as constructed are educational illustrations. Follow the references for definitions and original methods; a citation is not an endorsement of every application.</p><h2 id="languages">One article, two languages</h2><p>The site interface and project documentation are English-first. Each guide has a matched Chinese translation. Use EN / ZH on an article to switch to the same topic. The translations are separate reading views, with corresponding sections and references.</p><h2 id="standards">Editorial standards</h2><p>Explain assumptions, separate observations from identifications, and qualify limits. Prefer standards, official documentation, and primary methodological sources. Do not reproduce copyrighted spectra, figures, or large passages without permission. This first edition is open to corrections; automated checks do not substitute for expert scientific review.</p><h2 id="contribute">Contribute a clearer explanation</h2><p>Fix a factual error, improve an example, update a reference, or refine a translation. Use the edit link on any article, or <a href="{REPO}/issues/new?template=content.yml">report an issue</a>. Read the <a href="{REPO}/blob/main/CONTRIBUTING.md">contribution guide</a> for the content structure and checks.</p><h2 id="privacy">A quiet reading experience</h2><p>The site uses no analytics, advertising, accounts, or third-party fonts. Search runs in your browser using a static article index. Hosting infrastructure may maintain its own access logs. External references open only when you follow their links.</p></div></main>'''
write('about/index.html',page('About','The scope, editorial approach, and contribution process for mzwiki.',about,'/about/'))
write('404.html',page('Page not found','Find your way back to the mass spectrometry guides.','<main id="main" class="simple"><p class="error-number">404 / PAGE NOT FOUND</p><h1>Let’s find your next guide.</h1><p class="lead">This address does not match a page in the wiki.</p><div class="actions"><a class="button" href="/">Return home →</a><a href="/search/">Search the guides</a></div></main>','/404.html'))
write('CNAME','mzwiki.unimz.org\n')
write('.nojekyll','')
write('robots.txt',f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
paths=['/','/about/','/search/','/terms/']+[url(a['slug'],l,k) for k,collection in [('guide',ARTICLES),('term',TERMS)] for a in collection for l in ('en','zh')]
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc></url>' for p in paths)+'</urlset>\n')
print(f'Built {len(ARTICLES)} paired guides, {len(TERMS)} paired terms, {len(paths)+1} HTML pages, and {len(search_index)} search records.')
