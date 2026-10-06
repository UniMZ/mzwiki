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
pages=[ROOT/'index.html',ROOT/'404.html',ROOT/'about/index.html',ROOT/'search/index.html',*sorted((ROOT/'guides').rglob('*.html')),*sorted((ROOT/'zh').rglob('*.html'))]
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
refs=json.loads((ROOT/'content/references.json').read_text())
index=json.loads((ROOT/'assets/search-index.json').read_text())
assert len(articles)==8 and len(index)==16
slugs={a['slug'] for a in articles}
assert len(slugs)==len(articles)
for a in articles:
    assert all(s in slugs for s in a['prereqs']+a['related'])
    assert all(r in refs for r in a['refs'])
    section_sets=[]
    for lang in ('en','zh'):
        path=('/zh' if lang=='zh' else '')+'/guides/'+a['slug']+'/'
        d=docs[ROOT/path.lstrip('/')/'index.html']
        assert d.lang==lang
        assert d.alternates['en']=='https://mzwiki.unimz.org/guides/'+a['slug']+'/'
        assert d.alternates['zh']=='https://mzwiki.unimz.org/zh/guides/'+a['slug']+'/'
        body=(ROOT/'content'/lang/(a['slug']+'.html')).read_text()
        section_sets.append(set(re.findall(r'<h2 id="([^"]+)"',body)))
        assert len(body)>(2000 if lang=='en' else 800),(a['slug'],lang,'article too short')
        for ref in re.findall(r'href="#ref-([^"]+)"',body):assert ref in a['refs']
        record=[r for r in index if r['url']==path]
        assert len(record)==1 and record[0]['lang']==lang and len(record[0]['text'])>(1000 if lang=='en' else 500)
    assert section_sets[0]==section_sets[1],(a['slug'],'unmatched sections')
assert (ROOT/'CNAME').read_text().strip()=='mzwiki.unimz.org'
assert (ROOT/'.nojekyll').exists()
assert not re.search(r'[\u4e00-\u9fff]',(ROOT/'index.html').read_text()),'Homepage must be English'
print(f'PASS: {len(pages)} pages, {links} local links/assets/fragments, 8 translation pairs, 16 full-text search records, 10 bibliography entries, and Pages files.')
