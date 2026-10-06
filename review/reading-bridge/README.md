# Beginner reading bridge

This is a bounded, content-only packet for UniMZ/mzwiki, prepared against main commit `4981636fdb9660cbc30bdff091ad94545bb7f435` on 2026-10-06. It has not been applied, built, committed, pushed, or published.

## Reader-facing changes

1. The foundation Guide introduces the base-peak denominator and walks through three constructed scans before its existing monoisotopic ion-form arithmetic. Readers learn to read a row as a spectrum and a selected m/z column as an XIC. Existing adduct-ion, monoisotopic-mass, and extracted-ion-chromatogram entries are linked at first use.
2. The spectrum-reading Guide gains a short orientation inside `#context`: EI and ESI describe ion formation; MS1 and product-ion MS2 describe stages; retention time belongs to the chromatographic time axis. It links the existing ionization, fragmentation, and acquisition explanations. All content from `#groups` onward is byte-identical to the pinned source.
3. Exactly two short terminology entries, Mass spectrum and Base peak, receive matched English/Chinese articles. Both slugs were absent from the inspected 18-term collection. No Guide is added; applying this packet would leave eight Guides and create 20 term pairs.

English remains primary. Chinese appears only in matched article translations and their title/summary metadata. Existing figures, scientific examples, and unrelated content remain unchanged.

## Apply later

`application-manifest.json` specifies the four complete Guide fragment replacements, four complete new term fragments, two narrow article-metadata replacements, two term additions, three new bibliography keys, fixture proposal, and batch record. Re-read current main before applying and reconcile any drift. Do not copy `inspection/` into the repository.

The article metadata payloads change only the ordered reference lists. The existing eight-Guide order, titles, summaries, prerequisites, and related-Guide metadata are unchanged. The 18 existing term records are unchanged.

## Verification

Run the standalone package audit:

```sh
python3 inspection/validate_packet.py
```

It checks paired anchors, balanced HTML, citation numbering, local routes, first-use links, numeric-token parity, preserved source suffixes, published examples, and seven arithmetic fixtures. See `QA.md` and `validation-results.json`.

The proposed `tests/fixtures/reading-bridge.json` does not pretend to be consumed by an existing repository check. Later implementation must add or adapt a check, then run the site's builder, all existing checks, and browser checks. No build, rendering, generated search, deployment, or live-site success is claimed here.

`SOURCE-BOUNDARIES.md` distinguishes authoritative definitions, original constructed data, retained examples, and source-access limitations. `packet-files.sha256.json` records package integrity.
