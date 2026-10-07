#!/usr/bin/env python3
"""Recompute the supplied detector/signal teaching cases and source integrity."""
from collections import Counter
from decimal import Decimal as D
from pathlib import Path
import cmath
import hashlib
import json
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
f=json.loads((ROOT/'tests/fixtures/signal.json').read_text(),parse_float=D)
assert len(f['fixtures'])==12
for c in f['fixtures']:
 i=c['inputs'];k=c['id']
 if k=='current-complete-collection':
  current=i['rate_per_second']*i['charge_magnitude']*i['elementary_charge_C'];o=dict(current_A=current,current_fA=current*10**15)
 elif k=='charge-current-scaling':o=dict(current_ratio=D(i['charge_magnitudes'][1])/i['charge_magnitudes'][0])
 elif k=='multiplier-gain':o=dict(mean_output_electrons=i['initiating_electrons']*i['mean_yield_per_stage']**i['stages'])
 elif k=='clipping-ratio':
  output=[min(x,i['ceiling']) for x in i['input']];o=dict(output=output,input_ratio=D(i['input'][1])/i['input'][0],output_ratio=D(output[1])/output[0])
 elif k=='phase-addition':o=dict(resultant_amplitudes=[D(str(abs(i['equal_amplitudes'][0]+i['equal_amplitudes'][1]*cmath.exp(1j*float(p))))) for p in i['phase_differences_radians']])
 elif k=='poisson-relative-uncertainty':
  sd=[D(x).sqrt() for x in i['expected_counts']];o=dict(standard_deviations=sd,relative_standard_deviations=[s/n for s,n in zip(sd,i['expected_counts'])])
 elif k in ('weighted-centroid','baseline-pulls-estimator'):
  x,y=i['coordinates'],i['intensities'];o=dict(weighted_coordinate=sum(a*b for a,b in zip(x,y))/sum(y),sum=sum(y))
  if k=='weighted-centroid':o.update(sample_apex_coordinate=x[y.index(max(y))],height=max(y),trapezoidal_area=sum((b-a)*(u+v)/2 for a,b,u,v in zip(x,x[1:],y,y[1:])))
 elif k=='moving-average-height':
  values=i['input'];width=i['width'];assert width%2==1;half=width//2;output=[D(sum(values[j] if 0<=j<len(values) else 0 for j in range(n-half,n+half+1)))/width for n in range(len(values))];o=dict(output=output,input_sum=sum(values),output_sum=sum(output),input_maximum=max(values),output_maximum=max(output))
 elif k=='noise-denominator-choice':
  r=i['baseline_residuals'];rms=(D(sum(v*v for v in r))/len(r)).sqrt();spread=max(r)-min(r);o=dict(rms_noise=rms,peak_to_peak_noise=spread,height_over_rms=i['height']/rms,height_over_peak_to_peak=D(i['height'])/spread)
 elif k=='snr-term-conventions':o=dict(height_over_rms=D(i['height'])/i['rms_noise'],height_over_peak_to_peak=D(i['height'])/i['peak_to_peak_noise'])
 else:
  assert k=='representation-boundaries' and i['operation']=='centroiding';o=dict(does_identify_molecule=False,does_imply_chromatographic_integration=False,does_guarantee_unresolved_species_separation=False,does_recover_discarded_profile_exactly=False)
 assert set(o)==set(c['expected'])
 approximate=k in ('phase-addition','weighted-centroid','baseline-pulls-estimator','noise-denominator-choice')
 for key,expected in c['expected'].items():
  actual=o[key]
  if approximate:
   pairs=zip(actual,expected) if isinstance(expected,list) else [(actual,expected)]
   assert all(abs(D(a)-D(b))<=f['numeric_tolerance'] for a,b in pairs),(k,key,actual,expected)
  else:assert actual==expected,(k,key,actual,expected)
 slug,anchor=c['section'].split('#');is_guide=(ROOT/'content/en'/f'{slug}.html').exists()
 for lang in ('en','zh'):
  body=(ROOT/'content'/('' if is_guide else 'terms')/lang/f'{slug}.html').read_text();assert f'id="{anchor}"' in body,(k,lang)
packet=ROOT/'review/expansion-signal';hashes=json.loads((packet/'packet-files.sha256.json').read_text());count=0
for path,digest in hashes.items():
 if path.startswith(('content/','tests/fixtures/')):
  assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path;count+=1
assert count==17
for kind,filename in [('guide','articles'),('term','terms')]:
 for a in json.loads((packet/f'metadata/{filename}.additions.json').read_text()):
  bodies=[]
  for lang in ('en','zh'):
   body=(ROOT/'content'/('terms' if kind=='term' else '')/lang/f'{a["slug"]}.html').read_text();bodies.append(body);ET.fromstring('<article>'+body+'</article>')
   citations=re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',body);assert {r for r,n in citations}==set(a['refs']);assert all(a['refs'][int(n)-1]==r for r,n in citations)
   assert body in (ROOT/('zh' if lang=='zh' else '')/('terms' if kind=='term' else 'guides')/a['slug']/'index.html').read_text()
  for pattern in (r'id="([^"]+)"',r'<code>(.*?)</code>',r'href="#ref-([^"]+)">\[(\d+)\]'):
   assert re.findall(pattern,bodies[0])==re.findall(pattern,bodies[1]),a['slug']
  assert Counter(re.findall(r'\d+(?:\.\d+)?',bodies[0]))==Counter(re.findall(r'\d+(?:\.\d+)?',bodies[1])),a['slug']
print('PASS: 12 signal fixtures (11 computations, one semantic guard), eight bilingual pairs, published sections, code/citation/numerical parity and 17 source/fixture hashes.')
