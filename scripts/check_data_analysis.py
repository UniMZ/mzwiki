#!/usr/bin/env python3
"""Recompute teaching models; semantic guards are not scientific validation."""
from collections import Counter
from decimal import Decimal as D
from fractions import Fraction
from pathlib import Path
from statistics import median
import json
import re
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
f = json.loads((ROOT/'tests/fixtures/data-analysis.json').read_text(), parse_float=D)
assert len(f['cases']) == 10

def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(r, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][col]
        a[r] = [x/scale for x in a[r]]
        for j in range(len(a)):
            if j != r:
                scale = a[j][col]
                a[j] = [x-scale*y for x, y in zip(a[j], a[r])]
        r += 1
    return r

for c in f['cases']:
    i, kind = c['input'], c['kind']
    if kind == 'expected_fdp':
        assert sum(i['probabilities']) == 1
        fdps = [D(v)/max(r, 1) for v, r in zip(i['false'], i['accepted'])]
        o = dict(fdps=fdps, fdr=sum(p*x for p,x in zip(i['probabilities'],fdps)), mean_false=sum(p*v for p,v in zip(i['probabilities'],i['false'])))
    elif kind == 'fdp':
        o = dict(fdp=D(i['false'])/max(i['accepted'],1))
    elif kind == 'internal_standard_ratio':
        normalized = [D(a)/s for a,s in zip(i['analyte'],i['standard'])]
        o = dict(raw_ratio=D(i['analyte'][0])/i['analyte'][1], normalized=normalized, ratio_of_ratios=normalized[0]/normalized[1])
    elif kind == 'median_scaling':
        rm, tm = D(median(i['reference'])), D(median(i['test']))
        factor = rm/tm
        scaled = [x*factor for x in i['test']]
        o = dict(reference_median=rm,test_median=tm,factor=factor,scaled_test=scaled,raw_ratios=[D(t)/r for t,r in zip(i['test'],i['reference'])],scaled_ratios=[t/r for t,r in zip(scaled,i['reference'])])
    elif kind == 'missing_means':
        observed = [x for x in i['values'] if x is not None]
        mean = D(sum(observed))/len(i['values'])
        assert abs(mean-c['expected']['zero_filled_mean']) < D('1e-14')
        o = dict(observed_count=len(observed),observed_mean=D(sum(observed))/len(observed),zero_filled_count=len(i['values']),zero_filled_mean=c['expected']['zero_filled_mean'],rounded_zero_filled_mean=mean.quantize(D('.1')))
        assert o['observed_mean'] != mean
    elif kind == 'replicate_count':
        o = dict(injections=i['biological_samples']*i['injections_per_sample'],independent_biological_samples=i['biological_samples'])
    elif kind == 'design_rank':
        r = rank([[1,c,b] for c,b in zip(i['condition'],i['batch'])])
        o = dict(columns=['intercept','condition','batch'],rank=r,column_count=3,separate_condition_and_batch_effects_identifiable=r==3)
    elif kind == 'record_boundary':
        assert i['identified_molecule'] is None and 'calibration' not in i
        o = dict(molecule_identified=False,concentration_established=False)
    else:
        assert kind == 'interpretation'
        assert set(i) == {'accepted_psms','nominal_fdr_threshold'}
        o = dict(actual_false_count_known=False,individual_correct_probability_known=False,protein_level_fdr_established=False)
    assert o == c['expected'], (c['id'],o,c['expected'])

for check in f['published_checks']:
    body = (ROOT/check['file']).read_text()
    for value in check['required_strings']:
        assert value in body,(check['file'],value)
for slug,folder in [('data-analysis',''),('feature','terms/'),('false-discovery-rate','terms/'),('missing-value','terms/')]:
    bodies = [(ROOT/f'content/{folder}{lang}/{slug}.html').read_text() for lang in ('en','zh')]
    for body in bodies:
        ET.fromstring('<article>'+body.replace('<br>','<br/>')+'</article>')
    ids = lambda b: re.findall(r'id="([^"]+)"',b)
    assert ids(bodies[0]) == ids(bodies[1]),slug
    assert Counter(re.findall(r'\d+(?:\.\d+)?',bodies[0])) == Counter(re.findall(r'\d+(?:\.\d+)?',bodies[1])),slug
    assert re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[0]) == re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[1]),slug
    if slug == 'data-analysis':
        assert {'layers','formats','identification','example','qc','advanced','practice'} <= set(ids(bodies[0]))
    for lang,body in zip(('en','zh'),bodies):
        route = ('zh/' if lang=='zh' else '')+('terms/' if folder else 'guides/')+slug+'/index.html'
        assert body in (ROOT/route).read_text(),route
print('PASS: 10 data-analysis fixtures (8 computations, 2 semantic guards); four article pairs, published values, numerical/citation parity, preserved anchors and generated bodies.')
