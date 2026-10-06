# Computational mass-spectrometry learning expansion

Content-only packet prepared against UniMZ/mzwiki commit `ecca2688d1c33ce5485e8497b6c3e8f498376cb3` on 2026-10-06. The pinned baseline contains 20 Guides and 44 terms. This packet has not been applied, built, deployed, or live-site verified.

## Deliverables

- Three complete English/Chinese Guide pairs: spectrum prediction and machine-learning generalization; benchmarking computational MS; open data formats and analysis provenance
- Six complete term pairs: spectral similarity; retention-time prediction; data leakage; target-decoy competition; controlled vocabulary; provenance
- Eighteen complete HTML fragments
- Additive Guide and term metadata, 17 new `comp-` reference objects, and an exact snapshot of 5 reused reference objects
- Thirteen original arithmetic/logic fixtures, source boundaries, application manifest, and a reproducible packet validator

English Guides contain 960, 1,019, and 1,023 whitespace-delimited words after removing HTML tags. Terms contain 187–208 words. The Chinese companions include every section, qualification, constructed example, citation and practice answer. Mechanical parity checks support review but do not replace translation-quality judgment.

The existing introductory data-analysis Guide already introduces conversion, FDR and held-out evaluation. These new Guides deepen that coverage without replacing it: split design and pretraining overlap; independent reference truth and fair comparisons; and the detailed division of responsibilities among formats, vocabulary, sample maps and processing history. All six new terms were absent at the inspected baseline.

## Scientific boundaries

The material deliberately separates forward prediction from identification, molecule/peptide generalization from instrument transfer, discrimination from probability calibration, estimated FDR from actual errors, and file conformance from scientific validity. No model or similarity metric is promoted as universally best. All numerical examples are constructed and are not performance benchmarks.

## Later application

Follow `application-manifest.json`: add exactly the listed fragments and narrowly merge metadata. Re-read current main and reconcile with other approved packets before applying. Applied alone to the inspected baseline, this would yield 23 Guides and 50 terms; this is not a statement about the current live site or a combined batch.

The fixture file is proposed for later repository integration. `review/validate_packet.py` validates this packet only; it is not a production build or the repository test suite. Later authorized engineering must run all existing checks, adapt scientific fixtures, and inspect generated EN/ZH pages, navigation, language switching, reference sections, search, glossary backlinks, sitemap and desktop/mobile accessibility before publication.

Do not copy `inspection/` or `review/` into production. This folder is not a repository checkout and contains no mutation of UniMZ/mzwiki.
