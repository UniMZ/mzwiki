#!/usr/bin/env python3
"""Independently check the worked examples with Decimal and probability recurrence.

This validates calculations and EN/ZH numeric parity, not the adequacy of the
simplified model for real experimental spectra. No plotting dependency needed.
"""
from decimal import Decimal as D, getcontext
from pathlib import Path
from collections import Counter
import json
import math
import re
getcontext().prec=35
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'content/examples/charge-isotope-spectrum.json').read_text(),parse_float=D)
h=d['proton_mass_da'];mass=d['neutral_mass_da'];n=D(d['charge_magnitude']);shift=d['carbon_isotope_shift_da'];offset=d['coordinate_offset'];width=d['fwhm_coordinate']
# Verify constants against the cited values, including the deliberate rounding.
assert h == D('1.0072764665789').quantize(D('0.000000001'))
assert shift == D('13.00335483507')-D(12)
assert mass==D(1000) and n==2 and d['carbon_count']==50
assert d['carbon13_fraction']==D('0.0107') and offset==D('.002') and width==D('.010')
expected_positions=['501.007276','501.508954','502.010631']
expected_observed=['501.009276','501.510954','502.012631']
for k,(expected,observed) in enumerate(zip(expected_positions,expected_observed)):
 ref=(mass+n*h+D(k)*shift)/n
 obs=ref+offset
 assert f'{ref:.6f}'==expected
 assert f'{obs:.6f}'==observed
assert f'{mass/3+h:.6f}'=='334.340610'
assert f'{mass/3-h:.6f}'=='332.326057'
x0=mass/n+h
recovered=n*(x0+offset)-n*h
assert recovered==D('1000.004')
assert f'{offset/x0*D(10)**6:.3f}'=='3.992'
assert f'{(x0+offset)/width:.0f}'=='50101'
assert f'{x0*D(5)*D(10)**-6:.6f}'=='0.002505'
# Probability recurrence provides an independent route from the plot's comb().
def distribution(N,p):
 q=1-p;values=[q**N]
 for k in range(N):values.append(values[-1]*D(N-k)/D(k+1)*p/q)
 assert abs(sum(values)-1)<D('1e-30')
 return values
p=d['carbon13_fraction']
expected_percentages={10:['89.8008','9.7126','0.4727'],100:['34.1037','36.8856','19.7478']}
for N,expected in expected_percentages.items():
 vals=distribution(N,p)
 assert [f'{v*100:.4f}' for v in vals[:3]]==expected
vals=distribution(50,p)
assert [f'{100*v/vals[0]:.3f}' for v in vals[:3]]==['100.000','54.079','14.330']
assert f'{distribution(10,p)[1]/distribution(10,p)[0]*100:.4f}'=='10.8157'
# The Gaussian profile really has the stated half-height width.
assert math.isclose(math.exp(-4*math.log(2)*(.5**2)),.5,abs_tol=1e-14)
assert (D('500.002')-D(500))/D(500)*10**6==4
assert D(500)*5/D(10)**6==D('.0025')
assert D(1000)*5/D(10)**6==D('.005')
# Compare every decimal-valued token, including repetitions, across paired prose.
for slug in ['mz-charge-isotopes','analyzers','spectrum-interpretation']:
 en=(ROOT/'content/en'/f'{slug}.html').read_text();zh=(ROOT/'content/zh'/f'{slug}.html').read_text()
 numbers=lambda s:Counter(re.findall(r'\d+\.\d+',s))
 assert numbers(en)==numbers(zh),(slug,'numeric mismatch',numbers(en)-numbers(zh),numbers(zh)-numbers(en))
 for lang,body in [('en',en),('zh',zh)]:
  if slug=='spectrum-interpretation':
   for value in expected_positions+expected_observed+['54.079','14.330','3.992','50,101','0.002505','1000.004000']:
    assert value in body,(lang,value)
  if slug=='mz-charge-isotopes':
   for row in expected_percentages.values():
    for value in row:assert value+'%' in body,(lang,value)
print('PASS: charged-ion arithmetic, isotope probability normalization/ratios, all plotted centers, neutral-mass recovery, ppm error, FWHM, tolerance windows, and EN/ZH decimal parity.')
