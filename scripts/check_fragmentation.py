#!/usr/bin/env python3
"""Validate supplied fragmentation fixtures, displayed values and paired content."""
from collections import Counter
from decimal import Decimal as D
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
f=json.loads((ROOT/'tests/fixtures/fragmentation.json').read_text())
qa=json.loads((ROOT/'review/fragmentation/validation-results.json').read_text())
for path,digest in qa['content_sha256'].items():
 assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
bodies=[(ROOT/f'content/{lang}/fragmentation.html').read_text() for lang in ('en','zh')]
assert len(f['cases'])==13
for c in f['cases']:
 op=c['operation'];display=[]
 if op=='isotope_sum':
  mass=sum(D(f['constants'][atom+'_Da'])*count for atom,count in c['atom_counts'].items())
  assert mass==D(c['expected_mass_Da'])
  assert f'{mass:.4f}'==c['display_4dp'];display=[str(mass)]
 elif op=='same_charge_neutral_loss':
  assert c['precursor_charge']==c['product_charge']
  gap=D(c['neutral_mass_Da'])/abs(c['precursor_charge']);product=D(c['precursor_mz'])-gap
  assert gap==D(c['expected_mz_decrease']) and product==D(c['expected_product_mz'])
  assert f'{product:.4f}'==c['product_display_4dp'];display=[str(gap),c['product_display_4dp']]
 elif op=='coordinate_difference':
  assert D(c['precursor_display'])-D(c['product_display'])==D(c['expected_gap']);display=[c['expected_gap']]
 elif op=='loss_mass_from_gap':
  assert D(c['mz_gap'])*c['charge_magnitude']==D(c['expected_neutral_mass_Da']);display=[c['mz_gap'],c['expected_neutral_mass_Da']]
 elif op=='mass_increment_to_mz_gap':
  gap=D(c['mass_increment_Da'])/c['charge_magnitude'];assert gap==D(c['expected_gap'])
  assert f'{gap:.4f}'==c['display_4dp'];display=[c['display_4dp']]
 elif op=='ion_mass_charge_balance':
  masses=list(map(D,c['product_masses_Da']));charges=c['product_charges']
  assert D(c['precursor_mass_Da'])/abs(c['precursor_charge'])==D(c['expected_precursor_mz'])
  assert [m/abs(z) for m,z in zip(masses,charges)]==list(map(D,c['expected_product_mz']))
  assert D(c['precursor_mass_Da'])-sum(masses)==D(c['expected_mass_balance_residual_Da'])
  assert c['precursor_charge']-sum(charges)==c['expected_charge_balance_residual'];display=c['product_masses_Da']+[c['precursor_mass_Da']]
 elif op=='rectangular_window':
  center=D(c['center_mz']);half=D(c['full_width_mz'])/2;lo=center-half;hi=center+half
  assert lo==D(c['expected_lower']) and hi==D(c['expected_upper'])
  assert [lo<=D(x)<=hi for x in c['candidate_mz']]==c['expected_pass'];display=[c['expected_lower'],c['expected_upper']]
 else:
  assert op=='charge_and_composition'
  assert c['precursor_charge']+c['incoming_electron_charge']==c['expected_initial_product_charge']
  assert c['precursor_added_hydrogen_count']==c['expected_initial_product_added_hydrogen_count']
  for body in bodies:assert '[M+3H]<sup>3+</sup>' in body and '[M+3H]<sup>2+•</sup>' in body
 for body in bodies:
  section=re.split(r'<h[23] ',body.split(f'id="{c["guide_anchor"]}">',1)[1],1)[0]
  for value in display:assert value in section,(c['id'],value)
for slug,folder in [('fragmentation',''),('precursor-ion','terms/'),('product-ion','terms/'),('neutral-loss','terms/')]:
 pair=[(ROOT/f'content/{folder}{lang}/{slug}.html').read_text() for lang in ('en','zh')]
 for body in pair:ET.fromstring('<article>'+body+'</article>')
 ids=lambda b:re.findall(r'id="([^"]+)"',b)
 assert ids(pair[0])==ids(pair[1])
 # English spells out this one-unit charge reduction; the translation uses a digit.
 assert Counter(re.findall(r'\d+(?:\.\d+)?',pair[0].replace('decreases by one','decreases by 1')))==Counter(re.findall(r'\d+(?:\.\d+)?',pair[1])),slug
 assert re.findall(r'<code>(.*?)</code>',pair[0])==re.findall(r'<code>(.*?)</code>',pair[1].replace('\u4e2d\u6027\u8d28\u91cf','neutral mass').replace('\u524d\u4f53','precursor').replace('\u4ea7\u7269','product')),slug
 assert re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',pair[0])==re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',pair[1])
 if slug=='fragmentation':assert set(qa['original_anchors_preserved'])<=set(ids(pair[0]))
print('PASS: 13 fragmentation fixtures; published values, four bilingual pairs, equations, citations, original anchors and eight supplied source hashes.')
