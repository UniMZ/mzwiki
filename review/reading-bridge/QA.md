# Packet quality assurance

Status: PASS for standalone content checks and independent read-only content review.

## Verified

- Pinned baseline: `4981636fdb9660cbc30bdff091ad94545bb7f435`
- Four matched EN/ZH pairs: two edited Guide pairs and exactly two new term pairs
- All original Guide anchors remain; one matching foundation anchor is added before `#example`
- `spectrum-interpretation` changes stay inside `#context`; everything from `#groups` onward is byte-identical
- Foundation content from `#limits` onward is byte-identical; existing ion-form rounded positions remain unchanged
- First-use foundation links cover adduct-ion, monoisotopic-mass, XIC, mass spectrum, and base peak
- Orientation links reach existing ionization, fragmentation, and acquisition anchors in the same language
- Balanced trusted HTML fragments; no script, style, wrapper document, or embedded app additions
- Citation keys resolve and displayed numbers follow the exact metadata order
- Paired numeric-token multisets match, including existing scientific examples and added arithmetic
- Three-scan table, extraction interval, intensity formulas, and retained ion-mass numbers match the fixtures
- Seven arithmetic cases pass: three per-spectrum normalizations, XIC extraction, changing-denominator comparison, protonated mass, and sodium-adduct mass
- Existing article metadata changes only by appended bibliography keys; no Guide reordering or prerequisite expansion
- Exactly two absent term slugs are added to a baseline of 18, giving 20 if applied; exactly three new reference keys have no collisions
- English article bodies contain no Chinese text; Chinese is confined to paired translations and title/summary metadata

The independent read-only review found no scientific, translation, teaching-flow, or scope blockers. It did not substitute for rendered-site inspection.

## How to repeat the checks

```sh
python3 inspection/validate_packet.py
```

Read `validation-results.json` for checked files, preserved-suffix hashes, and fixture results. Preparation scripts inside `inspection/` are packet-only authoring aids; they are not proposed site code changes.

## Still required when applying

- Reconcile current main and repeat collision checks
- Apply the exact fragments and narrow metadata merges
- Add or adapt a repository check for the proposed fixture schema
- Run the existing builder and structural/scientific checks
- Inspect generated EN/ZH pages, bibliography, anchor-preserving switches, new term index entries, reciprocal Guide links, search, and sitemap
- Check desktop/mobile layout, keyboard access, and no-JavaScript reading in the existing browser-check workflow
- Verify deployment and live content only if publication is separately authorized

None of those repository or live-site steps was run in this research/writing task. Passing arithmetic and structure checks does not prove chemical identity, quantitative validity, or visual quality.
