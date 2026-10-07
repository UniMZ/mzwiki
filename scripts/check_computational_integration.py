#!/usr/bin/env python3
"""Preserve the supplied computational learning packet through integration."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / 'review/expansion-computational-learning'
manifest = json.loads((PACKET / 'source-manifest.json').read_text())
for name, expected in manifest['sha256'].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
pairs = 0
for kind, filename in [('guide', 'articles'), ('term', 'terms')]:
    supplied = json.loads((PACKET / f'metadata/{filename}.additions.json').read_text())
    current = {a['slug']: a for a in json.loads((ROOT / f'content/{filename}.json').read_text())}
    for item in supplied:
        slug = item['slug']
        assert current[slug] == item, (slug, 'supplied metadata changed')
        sections = []
        for lang in ('en', 'zh'):
            source = ROOT / 'content' / ('terms' if kind == 'term' else '') / lang / (slug + '.html')
            body = source.read_text().strip()
            route = ('zh/' if lang == 'zh' else '') + ('terms/' if kind == 'term' else 'guides/') + slug
            generated = (ROOT / route / 'index.html').read_text()
            assert body in generated, (slug, lang, 'body changed or missing')
            assert set(re.findall(r'href="#ref-([^"]+)"', body)) == set(item['refs']), (slug, lang)
            sections.append(re.findall(r'<h[23] id="([^"]+)"', body))
            assert '<title>mzwiki</title>' in generated
        assert sections[0] == sections[1], slug
        pairs += 1
assert pairs == 18 and len(manifest['sha256']) == 36
print('PASS: 18 supplied computational pairs, 36 source hashes, metadata, generated bodies, complete citations and matched section anchors. Scientific review remains external.')
