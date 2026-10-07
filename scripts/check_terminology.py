#!/usr/bin/env python3
"""Check the editorial taxonomy and both generated terminology inventories."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
ROOT=Path(__file__).resolve().parents[1]
terms=json.loads((ROOT/'content/terms.json').read_text());taxonomy=json.loads((ROOT/'content/term-topics.json').read_text())
assert set(taxonomy['assignments'])=={t['slug'] for t in terms}
topics=taxonomy['topics'];assert len({t['id'] for t in topics})==len(topics);assert len({t['label'] for t in topics})==len(topics)
assert set(taxonomy['assignments'].values())=={t['label'] for t in topics}
def natural(t):return tuple((1,int(p)) if p.isdigit() else (0,p) for p in re.split(r'(\d+)',t['title'].casefold())),t['slug']
class Inventory(HTMLParser):
 def __init__(self,text):
  super().__init__();self.groups=[];self.items=[];self.switches=[];self.in_list=False;self.in_switch=False;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='section' and 'data-topic' in a:self.groups.append(a['data-topic'])
  if tag=='ul' and 'term-list' in a.get('class','').split():self.in_list=True
  if tag=='nav' and a.get('aria-label')=='Terminology views':self.in_switch=True
  if tag=='a' and self.in_list:self.items.append(a['href'])
  if tag=='a' and self.in_switch:self.switches.append((a['href'],a.get('aria-current')))
 def handle_endtag(self,tag):
  if tag=='ul':self.in_list=False
  if tag=='nav':self.in_switch=False
for mode,path in [('topic','terms/index.html'),('az','terms/az/index.html')]:
 text=(ROOT/path).read_text();d=Inventory(text)
 ordered=sorted(terms,key=natural) if mode=='az' else [term for topic in topics for term in sorted((t for t in terms if taxonomy['assignments'][t['slug']]==topic['label']),key=natural)]
 assert d.items==['/terms/'+t['slug']+'/' for t in ordered],mode
 assert len(set(d.items))==len(terms)==len(d.items),mode
 assert d.groups==([t['id'] for t in topics] if mode=='topic' else []),mode
 assert d.switches==[('/terms/','page' if mode=='topic' else None),('/terms/az/','page' if mode=='az' else None)]
 assert not re.search(r'[\u3400-\u9fff]',text)
print(f'PASS: {len(topics)} editorial topics; all {len(terms)} terms exactly once in each view, canonical natural title ordering, stable URLs and current-view links.')
