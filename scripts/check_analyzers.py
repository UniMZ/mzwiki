#!/usr/bin/env python3
"""Recalculate the supplied ideal-model fixtures and check article parity."""
from collections import Counter
from decimal import Decimal as D
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
fixture=json.loads((ROOT/'review/analyzers/analyzer-arithmetic-fixtures.json').read_text(),parse_float=D,parse_int=D)
assert len(fixture['cases'])==10
for case in fixture['cases']:
 i=case['inputs'];ident=case['id']
 if ident.startswith('same-coordinate'):
  result={'x':i['ion_mass_u']/abs(i['charge_number'])}
 elif ident.startswith('tof-'):
  result={'tau_us':i['tau_ref_us']*(i['x']/i['x_ref']).sqrt()}
 elif ident.startswith('orbitrap-'):
  result={'frequency_kHz':i['frequency_ref_kHz']*(i['x_ref']/i['x']).sqrt()}
 elif ident.startswith('ideal-icr-'):
  result={'frequency_kHz':i['frequency_ref_kHz']*i['x_ref']/i['x']}
 else:
  assert i['dft_length']>=i['recorded_samples']
  result={'duration_s':i['recorded_samples']/i['sampling_rate_Hz'],'grid_spacing_Hz':i['sampling_rate_Hz']/i['dft_length']}
 assert result==case['expected'],(ident,result)

for path in ('analyzers','terms/mass-analyzer','terms/transient'):
 folder,slug=('terms/',path.split('/')[1]) if '/' in path else ('',path)
 bodies=[(ROOT/f'content/{folder}{lang}/{slug}.html').read_text() for lang in ('en','zh')]
 for body in bodies:
  ET.fromstring('<article>'+body+'</article>')
  assert 'truncated' not in body
 assert re.findall(r'id="([^"]+)"',bodies[0])==re.findall(r'id="([^"]+)"',bodies[1])
 assert re.findall(r'<code>(.*?)</code>',bodies[0])==re.findall(r'<code>(.*?)</code>',bodies[1])
 assert re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[0])==re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[1])
 assert Counter(re.findall(r'\d+(?:\.\d+)?',bodies[0]))==Counter(re.findall(r'\d+(?:\.\d+)?',bodies[1])),path
 if slug=='analyzers':
  assert {'idea','comparison','example','resolution-accuracy','tolerance','tradeoffs','practice','next-level'}<=set(re.findall(r'id="([^"]+)"',bodies[0]))
  # Bind fixture results to the published expressions/values, not only the JSON.
  for text in ('x = 100','τ = 10','20','x = 400','30','x = 900','x = 200','100 kHz','x = 800','50 kHz','25 kHz','0.10','10 Hz','0.20','5 Hz'):
   assert text in bodies[0],text
 elif slug=='mass-analyzer':
  assert 'x = 800 / 2 = 400' in bodies[0]
 else:
  for text in ('100,000','1,000,000','200,000','T = N / f_s = 0.10 s','Δf_grid = 1 / T = 10 Hz','0.20 s','5 Hz'):
   assert text in bodies[0],text
print('PASS: 10 analyzer arithmetic fixtures; 3 EN/ZH article pairs, equations, numerical tokens, references and preserved Guide anchors.')
