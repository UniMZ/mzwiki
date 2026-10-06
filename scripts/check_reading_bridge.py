#!/usr/bin/env python3
"""Recompute constructed reading examples and protect the bounded source edits."""
from collections import Counter
from decimal import Decimal as D
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
f=json.loads((ROOT/'tests/fixtures/reading-bridge.json').read_text(),parse_float=D)
assert len(f['cases'])==7
for c in f['cases']:
 i=c['input'];kind=c['kind']
 if kind=='base_peak_normalization':
  maximum=max(i['intensities']);relative=[D(x)*100/maximum for x in i['intensities']]
  o=dict(base_peak_mz=i['mz'][i['intensities'].index(maximum)],base_peak_intensity=maximum,relative_intensities_percent=relative,relative_sum_percent=sum(relative))
 elif kind=='xic':
  low=i['center_mz']-i['half_width_mz'];high=i['center_mz']+i['half_width_mz'];assert i['inclusive']
  selected=[n for n,x in enumerate(i['mz']) if low<=x<=high]
  o=dict(lower_mz=low,upper_mz=high,included_mz=[i['mz'][n] for n in selected],time_min=[s['time_min'] for s in i['scans']],signals=[sum(s['intensities'][n] for n in selected) for s in i['scans']])
 elif kind=='column_normalization':
  relative=[D(s)*100/m for s,m in zip(i['signal'],i['spectrum_maximum'])]
  o=dict(relative_intensities_percent=relative,same_as_original_xic=relative==i['signal'])
 elif kind=='ion_mass':
  mz=(i['neutral_monoisotopic_mass_da']+i['added_ion_mass_da'])/i['charge_magnitude']
  o=dict(mz=mz,display_four_decimals=f'{mz:.4f}')
 else:
  assert kind=='sodium_ion_mass'
  sodium=i['neutral_sodium23_mass_da']-i['electron_mass_da']
  mz=(i['neutral_monoisotopic_mass_da']+sodium)/i['charge_magnitude']
  o=dict(sodium_cation_mass_da=sodium,sodium_cation_display_nine_decimals=f'{sodium:.9f}',mz=mz,display_four_decimals=f'{mz:.4f}')
 assert o==c['expected'],(c['id'],o,c['expected'])
constants=f['source_constants']
assert constants['proton_mass_u_codata_2022_central'].quantize(D('.000000001'))==constants['proton_mass_da_adopted']
assert constants['electron_mass_u_codata_2022_central'].quantize(D('.000000000001'))==constants['electron_mass_da_adopted']
qa=json.loads((ROOT/'review/reading-bridge/validation-results.json').read_text())
hashes=json.loads((ROOT/'review/reading-bridge/packet-files.sha256.json').read_text())
for path,expected in hashes.items():
 if path.startswith(('content/','tests/fixtures/')):
  assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==expected,path
for path,guard in qa['unchanged_suffixes'].items():
 body=(ROOT/path).read_text();suffix=body[body.index('<h2 id="'+guard['from_anchor']+'"'):]
 assert hashlib.sha256(suffix.encode()).hexdigest()==guard['sha256'],path
for slug,folder in [('what-ms-measures',''),('spectrum-interpretation',''),('mass-spectrum','terms/'),('base-peak','terms/')]:
 bodies=[(ROOT/f'content/{folder}{lang}/{slug}.html').read_text() for lang in ('en','zh')]
 for body in bodies:ET.fromstring('<article>'+re.sub(r'<img ([^>]*?)(?<!/)>', r'<img \1/>', body.replace('<br>','<br/>'))+'</article>')
 ids=lambda b:re.findall(r'id="([^"]+)"',b)
 assert ids(bodies[0])==ids(bodies[1]),slug
 assert Counter(re.findall(r'\d+(?:\.\d+)?',bodies[0]))==Counter(re.findall(r'\d+(?:\.\d+)?',bodies[1].replace('ESI 一级谱','ESI MS1 谱'))),slug
 assert re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[0])==re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[1]),slug
 if slug in qa['preserved_guide_anchors']:assert set(qa['preserved_guide_anchors'][slug])<=set(ids(bodies[0]))
 for lang,body in zip(('en','zh'),bodies):
  route=('zh/' if lang=='zh' else '')+('terms/' if folder else 'guides/')+slug+'/index.html'
  assert body in (ROOT/route).read_text(),route
  if slug=='what-ms-measures':
   cells=[[D(v) for v in re.findall(r'<td>(.*?)</td>',row)] for row in re.findall(r'<tr>(.*?)</tr>',body) if '<td>' in row]
   assert cells==[[1,20,100,10],[2,80,40,20],[3,40,20,80]]
   for text in ('99.990–100.010','100 × 20 / 100 = 20%','100 × 80 / 80 = 100%','100 × 40 / 80 = 50%','301.0073','322.9892'):assert text in body,text
  if slug=='base-peak':
   for text in ('100%','50%','25%','175%'):assert text in body,text
print('PASS: 7 reading-bridge fixtures, adopted constant rounding, published table/equations, four bilingual pairs, original anchors, eight source hashes and four protected suffixes.')
