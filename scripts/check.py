#!/usr/bin/env python3
"""Validate generated links, fragments, language pairing, bibliography, and search."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re
ROOT=Path(__file__).resolve().parents[1]
class Document(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=set();self.links=[];self.alternates={};self.lang=None;self.h1=0;self.duplicates=[]
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:
            if d['id'] in self.ids:self.duplicates.append(d['id'])
            self.ids.add(d['id'])
        if tag=='html':self.lang=d.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='link' and d.get('rel')=='alternate':self.alternates[d['hreflang']]=d['href']
        if tag in ('a','link') and 'href' in d:self.links.append(d['href'])
        if tag in ('script','img') and 'src' in d:self.links.append(d['src'])
pages=[ROOT/'index.html',ROOT/'404.html',ROOT/'about/index.html',ROOT/'search/index.html',*sorted((ROOT/'guides').rglob('*.html')),*sorted((ROOT/'terms').rglob('*.html')),*sorted((ROOT/'zh').rglob('*.html'))]
docs={p:Document(p.read_text()) for p in pages}
links=0
for p,d in docs.items():
    assert d.h1==1,(p,'h1 count',d.h1)
    assert not d.duplicates,(p,d.duplicates)
    for link in d.links:
        parsed=urlsplit(link)
        if parsed.scheme or parsed.netloc:continue
        links+=1
        path=unquote(parsed.path)
        target=ROOT/path.lstrip('/') if path.startswith('/') else (p.parent/path if path else p)
        if target.is_dir():target/= 'index.html'
        target=target.resolve()
        assert target.exists(),(p,link,'missing target')
        if parsed.fragment and target in docs:
            assert unquote(parsed.fragment) in docs[target].ids,(p,link,'missing fragment')
articles=json.loads((ROOT/'content/articles.json').read_text())
terms=json.loads((ROOT/'content/terms.json').read_text())
refs=json.loads((ROOT/'content/references.json').read_text())
index=json.loads((ROOT/'assets/search-index.json').read_text())
assert len(articles)==8 and len(index)==2*(len(articles)+len(terms))
slugs={a['slug'] for a in articles}
assert len(slugs)==len(articles)
term_slugs={a['slug'] for a in terms}
assert len(term_slugs)==len(terms)
for kind,a in [('guide',a) for a in articles]+[('term',t) for t in terms]:
    assert all(s in slugs for s in a.get('prereqs',[])+a.get('related',a.get('related_guides',[])))
    assert all(s in term_slugs for s in a.get('related_terms',[]))
    collection='terms' if kind=='term' else 'guides'
    assert all(r in refs for r in a['refs'])
    section_sets=[]
    for lang in ('en','zh'):
        path=('/zh' if lang=='zh' else '')+'/'+collection+'/'+a['slug']+'/'
        d=docs[ROOT/path.lstrip('/')/'index.html']
        assert d.lang==lang
        assert d.alternates['en']=='https://mzwiki.unimz.org/'+collection+'/'+a['slug']+'/'
        assert d.alternates['zh']=='https://mzwiki.unimz.org/zh/'+collection+'/'+a['slug']+'/'
        body=(ROOT/'content'/('terms' if kind=='term' else '')/lang/(a['slug']+'.html')).read_text()
        section_sets.append(set(re.findall(r'<h2 id="([^"]+)"',body)))
        assert len(body)>((2000 if lang=='en' else 800) if kind=='guide' else (900 if lang=='en' else 400)),(a['slug'],lang,'article too short')
        for ref,number in re.findall(r'href="#ref-([^\"]+)">\[(\d+)\]',body):
            assert a['refs'][int(number)-1]==ref,(a['slug'],ref,number)
        assert body.strip() in (ROOT/path.lstrip('/')/'index.html').read_text()
        assert not re.search(r'[\u3400-\u9fff]',body) if lang=='en' else True
        record=[r for r in index if r['url']==path]
        assert len(record)==1 and record[0]['lang']==lang and record[0]['kind']==kind and len(record[0]['text'])>((1000 if lang=='en' else 500) if kind=='guide' else (500 if lang=='en' else 250))
    assert section_sets[0]==section_sets[1],(a['slug'],'unmatched sections')
assert (ROOT/'CNAME').read_text().strip()=='mzwiki.unimz.org'
assert (ROOT/'.nojekyll').exists()
assert not re.search(r'[\u4e00-\u9fff]',(ROOT/'index.html').read_text()),'Homepage must be English'
from xml.etree import ElementTree as ET
sitemap=ET.parse(ROOT/'sitemap.xml')
locations={n.text for n in sitemap.findall('.//{*}loc')}
expected={'https://mzwiki.unimz.org'+r['url'] for r in index}|{'https://mzwiki.unimz.org'+p for p in ('/','/about/','/search/','/terms/')}
assert locations==expected
assert len({r['url'] for r in index})==len(index)
assert not re.search(r'[\u3400-\u9fff]',(ROOT/'terms/index.html').read_text())
print(f'PASS: {len(pages)} pages, {links} local links/assets/fragments, {len(articles)+len(terms)} translation pairs, {len(index)} full-text search records, {len(refs)} bibliography entries, and Pages files.')
