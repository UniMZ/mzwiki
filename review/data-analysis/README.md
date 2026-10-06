# Data-analysis foundations learning batch

Content-only research and bilingual writing package for UniMZ/mzwiki, prepared 2026-10-06 against read-only main snapshot `baad05c164ab2151371732973b324c1ff4ce3ce2`. No repository mutation, cloud coding task, commit, push, build, deployment, or live-site verification was performed.

## Reader outcome

The expanded data-analysis Guide follows the evidence chain from preserved acquisition files to spectral representations, features, identity claims, quantitative signals, and study-level inference. It explains what centroiding does and does not do; why a feature need not equal a compound; why an identification score, FDR threshold, and concentration are different; and why normalization, missing-data handling, batches, and replication require explicit assumptions.

The English Guide is approximately 1,950 words. The matched Chinese article is complete, including the examples, qualifications, section IDs, and citations. Exactly three short terminology pairs are added: Feature, False discovery rate, and Missing value. The pinned baseline has 15 terms; application would produce 18 terms and retain eight numbered Guides. There is no Chinese UI, homepage restructuring, paper feed, new interactive calculator, or encyclopedic statistics section.

## Exact source fragments

Replace:

- `content/en/data-analysis.html`
- `content/zh/data-analysis.html`

Add paired term fragments at `content/terms/{en,zh}/`:

- `feature.html`
- `false-discovery-rate.html`
- `missing-value.html`

These are complete trusted article-body fragments, not standalone generated pages.

## Metadata merges

1. Reconcile current main with the pinned snapshot before application
2. In `content/articles.json`, replace only the `data-analysis` object with `metadata/data-analysis.article.json`; title, group, prerequisites, related Guides, and array position are preserved
3. Append the three objects from `metadata/terms.additions.json` to the separate `content/terms.json` collection after checking uniqueness
4. Merge the ten new keys from `metadata/references.additions.json` into `content/references.json`; never replace the complete bibliography
5. `metadata/references.reused.json` records three unchanged references for inspection and is not an overwrite payload
6. Rebuild generated output using the existing repository workflow

The exact operations and exclusions are in `application-manifest.json`.

## Anchors and routes

All seven existing Guide anchors are preserved: `layers`, `formats`, `identification`, `example`, `qc`, `advanced`, `practice`.

Eight paired anchors are added: `representation`, `features`, `error-control`, `quantification`, `normalization`, `design`, `missingness`, `reproducibility`.

Terms retain the established `definition`, `example`, `confusion`, and `guides` structure. English routes are `/guides/data-analysis/` and `/terms/<slug>/`; matched Chinese routes use the `/zh` prefix. The existing Guide citation numbers 1–3 remain unchanged.

## Evidence and checks

- `SOURCE-BOUNDARIES.md`: source authority, supported claims, access limits, and deliberately excluded interpretations
- `tests/fixtures/data-analysis.json`: ten explicit constructed arithmetic or interpretation fixtures, with assumptions
- `QA.md` and `validation-results.json`: packet checks and unrun integration checks
- `docs/content-batches/07-data-analysis.md`: optional repository-facing batch record
- `inspection/`: pinned source snapshots, metadata-preparation helper, and local packet checker; none are repository replacements

Run the content-packet checks locally with `python3 inspection/validate_packet.py`. This does not apply the packet or run the repository's tests.

## Later acceptance work

After authorized application, add the fixture checks to the repository's current science-check workflow, build generated pages, and run all current structural, scientific, and browser checks. Check reciprocal Guide/term links, reference numbering, search categories, term discovery, language-switch anchor preservation, no-JavaScript reading, and mobile/keyboard behavior. Inspect long equation wrapping in the FDR term and Guide. Publication requires separate verification of the expected commit, deployment, and live site.
