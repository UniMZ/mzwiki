#!/usr/bin/env python3
"""Check supplied ion-form fixtures, rendered tables, citations and language parity.

Arithmetic regression does not establish a real ion assignment or validate the
scientific literature. All constants and expectations come from the authored packet.
"""
from collections import Counter
from decimal import Decimal as D, ROUND_HALF_UP, getcontext
from html import unescape
from pathlib import Path
import json
import re

getcontext().prec = 35
ROOT = Path(__file__).resolve().parents[1]
f = json.loads((ROOT / 'tests/fixtures/ionization.json').read_text())
mass = D(f['neutral_mass_da'])
c = {k: D(v) for k, v in f['constants_da'].items()}
h, na = c['proton'], c['sodium_23_cation']
electron = D('0.0005485799090441')
round9 = lambda x: x.quantize(D('0.000000001'), rounding=ROUND_HALF_UP)
assert h == round9(D('1.0072764665789'))
assert na == round9(D('22.9897692820') - electron)
assert c['ammonium_14N_1H4_cation'] == round9(D('14.00307400443') + 4 * D('1.00782503223') - electron)
assert c['chlorine_35_anion'] == round9(D('34.968852682') + electron)
deltas = [h, na, c['ammonium_14N_1H4_cation'], -h,
          c['chlorine_35_anion'], 2*h, -2*h, h+na, h]
assert len(f['ions']) == 9
for ion, delta in zip(f['ions'], deltas):
    assert ion['n'] == abs(ion['z'])
    assert D(ion['delta_da']) == delta
    x = (ion['k'] * mass + delta) / ion['n']
    assert x == D(ion['x'])
    assert f'{x:.6f}' == ion['display_x']
    assert (ion['n'] * x - delta) / ion['k'] == mass
checks = f['checks']
assert na - h == D(checks['sodium_minus_proton_da'])
assert (na-h)/2 == D(checks['sodium_replacing_proton_at_charge_2_delta_x'])
assert round9((na-h)/2) == D(checks['charge_2_difference_rounded_9_places'])
assert mass + na - h == D(checks['sodium_peak_misassigned_as_protonated_neutral_mass_da'])

def text(s):
    return unescape(re.sub('<[^>]+>', '', s)).replace('−', '-').strip()

def section(s, anchor):
    return re.split(r'<h[23] ', s.split(f'id="{anchor}">', 1)[1], 1)[0]

articles = json.loads((ROOT/'content/articles.json').read_text())
refs = next(a['refs'] for a in articles if a['slug'] == 'ionization')
bodies = [(ROOT/f'content/{lang}/ionization.html').read_text() for lang in ('en', 'zh')]
ids = lambda s: re.findall(r'<h[23] id="([^"]+)"', s)
assert ids(bodies[0]) == ids(bodies[1])
assert {'idea','methods','esi','example','troubleshooting','practice','next-level'} <= set(ids(bodies[0]))
citations = lambda s: re.findall(r'href="#ref-([^"]+)">\[(\d+)\]', s)
assert citations(bodies[0]) == citations(bodies[1])
assert Counter(re.findall(r'\d+\.\d+', bodies[0])) == Counter(re.findall(r'\d+\.\d+', bodies[1]))
assert re.findall(r'<code>(.*?)</code>', bodies[0]) == re.findall(r'<code>(.*?)</code>', bodies[1])
for lang, body in zip(('en','zh'), bodies):
    assert 'tokens truncated' not in body and '&lt;' not in body
    for key, number in citations(body):
        assert refs[int(number)-1] == key
    rows = re.findall(r'<tr>(.*?)</tr>', section(body, 'example'), re.S)[1:]
    assert len(rows) == 9
    for row, ion in zip(rows, f['ions']):
        cells = [text(t) for t in re.findall(r'<td>(.*?)</td>', row)]
        assert cells[0] == ion['notation'], (lang,cells,ion)
        assert int(cells[1]) == ion['n']
        assert D(cells[2]) == D(ion['delta_da'])
        assert cells[3] == ion['display_x']
    for value in f['constants_da'].values():
        assert value in section(body, 'mass-recovery')
    for key in ('sodium_minus_proton_da','charge_2_difference_rounded_9_places','sodium_peak_misassigned_as_protonated_neutral_mass_da'):
        assert checks[key] in section(body, 'example-adduct')
    prefix = 'zh/' if lang == 'zh' else ''
    rendered = (ROOT/f'{prefix}guides/ionization/index.html').read_text()
    assert body.strip() in rendered
    for href in re.findall(r'href="(/[^\"]+)"', body):
        assert href.startswith('/zh/guides/' if lang == 'zh' else '/guides/')
    if lang == 'en':
        assert not re.search(r'[\u3400-\u9fff]', body)
print('PASS: 9 ion predictions and inversions; 4 ionic constants; 4 derived checks; EN/ZH tables, equations, citations, anchors and generated-body parity.')
