#!/usr/bin/env python3
"""Regression checks for the supplied terminology examples and paired sources."""
from collections import Counter
from decimal import Decimal as D
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
f=json.loads((ROOT/'review/terminology/numerical-examples.json').read_text())['examples']
x=f['mz'];assert D(x['ion_mass_Da'])/abs(x['charge_number'])==D(x['mz'])
c=f['carbon_spacing_charge4'];shift=D(c['C13'])-D(c['C12'])
assert shift/c['charge_magnitude']==D(c['spacing'])
assert shift==D(f['methane_isotopologue_difference_Da'])
a=f['sodium_adduct'];ionic=D(a['Na23_atom_mass_Da'])-D(a['electron_mass_Da'])
assert ionic==D(a['ionic_mass_Da'])
assert D(a['neutral_mass_Da'])+ionic==D(a['mz'])
assert 2*D('1.00782503223')+D('15.99491461957')==D(f['water_monoisotopic_mass_Da'])
assert 2*D('1.00782503223')+D('17.99915961286')==D(f['water_O18_exact_mass_Da'])
assert (D('250.0010')-D('250.0000'))/D('250.0000')*10**6==D(f['mass_error_ppm'])
assert D('200.000')/D('0.005')==D(f['resolving_power_FWHM'])
expected={
 'mz':['600.0000','300.0000'],
 'charge-state':[f'{D(c["spacing"]):.6f}'],
 'adduct-ion':[f'{ionic:.9f}',f'{D(a["mz"]):.6f}'],
 'isotopologue':[str(shift),f'{shift:.6f}'],
 'monoisotopic-mass':[f'{D(f["water_monoisotopic_mass_Da"]):.6f}',f'{D(f["water_O18_exact_mass_Da"]):.6f}'],
 'mass-accuracy':['250.0010','250.0000','+4 ppm'],
 'resolving-power':['200.000','0.005','40,000'],
}
terms=json.loads((ROOT/'content/terms.json').read_text())
for term in terms:
 slug=term['slug'];texts=[]
 for lang in ('en','zh'):
  body=(ROOT/f'content/terms/{lang}/{slug}.html').read_text();texts.append(body)
  root=ET.fromstring('<article>'+body+'</article>')
  assert [h.get('id') for h in root.findall('h2')] in (['definition','example','confusion','guides'], ['definition','example','limits'], ['definition','example','boundary'])
  assert set(re.findall(r'href="#ref-([^"]+)"',body))==set(term['refs'])
  for v in expected.get(slug,[]):assert v in body,(slug,lang,v)
 assert Counter(re.findall(r'\d+(?:\.\d+)?',texts[0].replace('decreases by one','decreases by 1')))==Counter(re.findall(r'\d+(?:\.\d+)?',(texts[1].replace('一级','level-1') if slug=='spectral-library' else texts[1]))),slug
 assert re.findall(r'<code>(.*?)</code>',texts[0])==re.findall(r'<code>(.*?)</code>',texts[1].replace('次进样', 'injections').replace('相对强度（%）=', 'relative intensity (%) =').replace('基峰强度', 'base-peak intensity').replace('峰强度', 'peak intensity').replace('\u4e2d\u6027\u8d28\u91cf','neutral mass').replace('\u524d\u4f53','precursor').replace('\u4ea7\u7269','product')),slug
print(f'PASS: terminology Decimal fixtures and displayed rounding; {len(terms)} paired entries with balanced markup, matching numerical tokens, equations, sections and complete citations.')
