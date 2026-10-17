#!/usr/bin/env python3
"""Verify constructed interpretation examples and the new bilingual source packet."""
from pathlib import Path
from decimal import Decimal as D
from math import comb, log
from collections import Counter
import json, re, hashlib, xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
m=json.loads((R/'review/expansion-interpretation/manifest.json').read_text())
assert len(m['guides'])==6 and len(m['terms'])==12 and len(m['sha256'])==36
assert 100*(10+(6-5)/(7-5))==1050
assert 100*(10+log(2)/log(4))==1050
A=[1,2,1]; B=[0,1,2]
assert [3*a+2*b for a,b in zip(A,B)]==[3,8,7]
mass=8*D(12)+10*D('1.00782503223')+4*D('14.00307400443')+2*D('15.99491461957')
assert mass==D('194.08037557916')
assert (mass+D('1.007276467')).quantize(D('.000001'))==D('195.087652')
assert 1+8-10/2+4/2==6
assert (mass-D(194)).quantize(D('.000001'))==D('.080376')
p=D('.0107');assert 2*p*(1-p)==D('.02117102')
assert (8*p/(1-p)).quantize(D('.00001'))==D('.08653')
f=[D('.25'),D('.50'),D('.25')]
assert sum(f)==1 and 1-f[0]==D('.75') and sum(i*x for i,x in enumerate(f))/2==D('.5')
a=[-1,-1,1,1];b=[-10,10,-10,10]
assert sum(x*y for x,y in zip(a,b))==0
assert sum(x*x for x in b)/sum(x*x for x in a+b)==100/101
for N,num,den in [(20,155,4845),(100,955,3921225)]:
 assert sum(comb(5,k)*comb(N-5,4-k) for k in (3,4))==num and comb(N,4)==den
articles={x['slug']:x for x in json.loads((R/'content/articles.json').read_text())}
terms={x['slug']:x for x in json.loads((R/'content/terms.json').read_text())}
for path,sha in m['sha256'].items():assert hashlib.sha256((R/path).read_bytes()).hexdigest()==sha,path
for collection,slugs,meta in [('guides',m['guides'],articles),('terms',m['terms'],terms)]:
 for slug in slugs:
  paths=[R/(f'content/{lang}/{slug}.html' if collection=='guides' else f'content/terms/{lang}/{slug}.html') for lang in ['en','zh']]
  texts=[p.read_text() for p in paths]
  for lang,text in zip(['en','zh'],texts):
   ET.fromstring('<article>'+text+'</article>')
   assert set(re.findall(r'href="#ref-([^"]+)"',text))==set(meta[slug]['refs']),slug
   generated=R/(('' if lang=='en' else 'zh/')+collection+'/'+slug+'/index.html')
   assert text.strip() in generated.read_text(),slug
  assert re.findall(r'<h2 id="([^"]+)"',texts[0])==re.findall(r'<h2 id="([^"]+)"',texts[1]),slug
  assert Counter(re.findall(r'\d+(?:\.\d+)?',texts[0]))==Counter(re.findall(r'\d+(?:\.\d+)?',texts[1])),slug
  z=texts[1].replace('单同位素质量','monoisotopic mass').replace('标称质量','nominal mass').replace('均值','mean')
  assert re.findall(r'<code>(.*?)</code>',texts[0])==re.findall(r'<code>(.*?)</code>',z),slug
print('PASS: interpretation arithmetic, 36 source hashes, 18 bilingual pairs, citations, equations, anchors and generated bodies. These checks are not experimental validation.')
