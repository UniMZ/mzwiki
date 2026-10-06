#!/usr/bin/env python3
"""Recompute the supplied acquisition schedules, selections and XIC fixtures."""
from collections import Counter
from decimal import Decimal as D
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
f=json.loads((ROOT/'tests/fixtures/acquisition.json').read_text(),parse_float=D)
assert len(f['cases'])==16
for c in f['cases']:
 i=c['input'];kind=c['kind'];o={}
 if kind=='serial_dia':
  n=D(i['range'][1]-i['range'][0])/i['window_width'];assert n==int(n)
  t=i['survey_s']+n*i['window_block_s']+i['overhead_s']
  o=dict(window_count=n,cycle_s=t,approx_opportunities=i['peak_width_s']/t,spectra_per_cycle=n+1,measurements_per_window_per_cycle=1)
 elif kind=='budget_per_window':o={'window_block_s':(i['cycle_budget_s']-i['survey_s']-i['overhead_s'])/i['window_count']}
 elif kind=='serial_dda':
  t=i['survey_s']+i['dependent_count']*i['dependent_block_s']+i['overhead_s']
  o=dict(cycle_s=t,approx_survey_opportunities=i['peak_width_s']/t,spectra_per_cycle=i['dependent_count']+1)
 elif kind=='opportunities':o={'approx_opportunities':D(i['peak_width_s'])/i['revisit_s']}
 elif kind=='serial_mrm':
  t=i['transitions']*(i['dwell_ms']+i['pause_ms'])+i['other_overhead_ms']
  o=dict(cycle_ms=t,approx_opportunities=D(i['peak_width_s'])*1000/t)
 elif kind=='budget_dwell':o={'dwell_ms':D(i['cycle_budget_ms']-i['other_overhead_ms'])/i['transitions']-i['pause_ms']}
 elif kind=='isolation_bounds':
  center=D(i['center'])+i['offset'];half=D(i['full_width'])/2;bounds=[center-half,center+half]
  o=dict(bounds=bounds,included=[x for x in i['ions'] if bounds[0]<=x<=bounds[1]])
 elif kind=='centroid_xic':
  half=D(i['target'])*i['ppm']/10**6;bounds=[i['target']-half,i['target']+half]
  indices=[n for n,x in enumerate(i['centroids']) if bounds[0]<=x<=bounds[1]]
  assert len(i['times_s'])==len(i['signals'])
  o=dict(half_width=half,bounds=bounds,included_indices=indices,xic=[sum(row[n] for n in indices) for row in i['signals']])
 elif kind=='selection':
  first=i['ranked_eligible'][:i['top_n']]
  o=dict(first_cycle=first,next_with_exclusion=[x for x in i['ranked_eligible'] if x not in i['excluded_next_cycle']][:i['top_n']],next_without_exclusion=first)
 elif kind=='interpretation':
  o=dict(spectra_per_cycle=i['ms1_events']+i['ms2_events'],max_ms_level=max(n for n in (1,2) if i[f'ms{n}_events']),not_ms_level=i['ms1_events']+i['ms2_events'])
 else:
  assert kind=='ratio'
  o=dict(window_count_ratio=D(i['narrow_windows'])/i['wide_windows'],cycle_time_ratio=i['narrow_cycle_s']/i['wide_cycle_s'])
  assert abs(o['cycle_time_ratio']-c['expected']['cycle_time_ratio'])<D('1e-15')
  o['cycle_time_ratio']=c['expected']['cycle_time_ratio'] # JSON fixture rounds this recurring ratio.
 assert o==c['expected'],(c['id'],o,c['expected'])

qa=json.loads((ROOT/'review/acquisition/validation-results.json').read_text())
for slug,folder in [('acquisition',''),('acquisition-cycle','terms/'),('isolation-window','terms/'),('extracted-ion-chromatogram','terms/')]:
 bodies=[(ROOT/f'content/{folder}{lang}/{slug}.html').read_text() for lang in ('en','zh')]
 for body in bodies:ET.fromstring('<article>'+body.replace('<br>','<br/>')+'</article>')
 ids=lambda b:re.findall(r'id="([^"]+)"',b)
 assert ids(bodies[0])==ids(bodies[1])
 assert Counter(re.findall(r'\d+(?:\.\d+)?',bodies[0]))==Counter(re.findall(r'\d+(?:\.\d+)?',bodies[1])),slug
 assert re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[0])==re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[1])
 if slug=='acquisition':
  assert set(qa['old_acquisition_anchors_preserved'])<=set(ids(bodies[0]))
  for equation in ('0.20 + 20 × 0.04 + 0.20 = 1.20 s','0.20 + 40 × 0.04 + 0.20 = 2.00 s','(1.20 − 0.20 − 0.20) / 40 = 0.020 s','0.20 + 10 × 0.09 + 0.10 = 1.20 s','12 / 3.00 = 4','40 × (20 + 5) = 1000 ms','1000 / 80 − 5 = 7.5 ms'):
   for body in bodies:assert equation in body,equation
 elif slug=='isolation-window':
  for text in ('599.4–600.6','599.8–600.2','599.7–600.9'):
   for body in bodies:assert text in body
 elif slug=='extracted-ion-chromatogram':
  for body in bodies:
   rows=re.findall(r'<tr>(.*?)</tr>',body)[1:]
   cells=[[D(v) for v in re.findall(r'<td>(.*?)</td>',row)] for row in rows]
   assert cells==[[0,10,20,100,30],[1,20,50,200,70],[2,10,20,100,30]]
   for value in ('599.997–600.003','599.994–600.006','130','270'):assert value in body
print('PASS: 16 acquisition fixtures; four paired articles, displayed equations/XIC rows, numerical tokens, citations and six original anchors.')
