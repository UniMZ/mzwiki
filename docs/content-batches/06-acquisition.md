# Acquisition learning batch

Prepared against `141264f45b3b4c02a9c99104e999a2c6caa2446d` on 2026-10-06. This is a content application record proposal; the research packet itself did not modify or publish the repository.

## Scope

- Deepen the existing acquisition Guide in English and Chinese
- Preserve all six old anchors and add ten matched explanatory anchors
- Add Acquisition cycle, Isolation window, and Extracted ion chromatogram as three separate terminology pairs
- Preserve the eight-Guide sequence and English-primary interface
- Add eleven bibliography keys and sixteen constructed teaching fixtures

## Reader-facing changes

Explain selection and scheduling, MS levels versus events and cycles, bounded full-scan coverage, DDA eligibility and dynamic exclusion, DIA mixed evidence and windows, SRM/MRM versus PRM, and extraction versus acquisition. Make the sampling/time tradeoffs explicit without declaring one acquisition mode universally best.

The main serial toy model covers m/z 400–800 with 20 or 40 windows. The assumed survey, measurement blocks, and overhead give cycles of 1.20 s and 2.00 s, corresponding to approximately 10 and 6 opportunities across a consistently defined 12 s peak. A narrower-window fixed-budget variant, targeted dwell/pause examples, ideal isolation intervals, and invented XIC sums make the assumptions testable.

## Acceptance checklist for application

- Reconcile current main and retain existing metadata order and unrelated content
- Apply complete fragments and narrow metadata merges according to the manifest
- Add or adapt scientific tests for `tests/fixtures/acquisition.json`
- Regenerate pages, search records, and sitemap through the existing builder
- Run the full current structural/scientific suite, then browser checks
- Verify citation numbering, all old/new anchors, paired numeric content, language switching, reciprocal term links, and terminology filtering
- Inspect narrow-screen tables/equations and keyboard-accessible practice disclosures
- Report actual publication and live-site evidence separately

## Evidence limits

All examples are constructed, not measured data or validated methods. IUPAC, official instrument/software documentation, and primary DIA/PRM/coisolation/parallel-acquisition publications support the stable concepts. Source access limitations are retained in the package's source-boundary record; indexed access is not called a successful direct full-text read.

## Engineering integration

The supplied eight source fragments and metadata remain unchanged. SHA-256 comparisons against source commit `9f17f035ad3dc4fd061b9f5ca4785c982930f505` confirm the article bodies. `scripts/check_acquisition.py` adapts all sixteen fixtures, including the rounded recurring cycle-time ratio, checks displayed timing expressions and XIC table sums, and verifies paired numerical tokens, citations and original Guide anchors. HTML line breaks are normalized only for the XML-based test parser.

The existing builder regenerates the two collections, reciprocal links, search and sitemap; no framework or domain changes are needed. Browser coverage adds all ten new section switches, three term pairs, bilingual search, keyboard disclosures and table scrolling at 1440, 390 and 320 pixels. Local test results are distinct from remote CI and publication; the parent task handles merging and Pages verification.
