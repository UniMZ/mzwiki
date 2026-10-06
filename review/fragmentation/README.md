# Fragmentation learning batch

Content-only research and writing package for UniMZ/mzwiki. Prepared 2026-10-06 against read-only main snapshot `973798e0fa8702ab54690b663d10a67cdde8e561`. No repository files were edited, no cloud coding task was created, and nothing was committed, pushed, built, or deployed.

## Reader outcome

The existing Fragmentation & tandem MS Guide is expanded into a beginner path from precursor isolation through activation and product-ion measurement. It distinguishes collision-based CID/HCD from the qualified peptide applications of ECD/ETD, explains conventional peptide labels without exporting them to all small molecules, and works through charge-aware mass and neutral-loss bookkeeping. It closes with coisolation and interpretation limits.

Exactly three independent terms are added: Precursor ion, Product ion, and Neutral loss. Existing mass, charge, isotope, analyzer, and acquisition content is linked rather than recreated. No empirical spectrum, peak intensity, instrument benchmark, or identification is invented.

## Complete article fragments and exact destinations

Copy each of these complete body fragments to its identical repository-relative path, after reconciling any later main changes:

- `content/en/fragmentation.html` — replace existing fragment
- `content/zh/fragmentation.html` — replace existing fragment
- `content/terms/en/precursor-ion.html` — add
- `content/terms/zh/precursor-ion.html` — add
- `content/terms/en/product-ion.html` — add
- `content/terms/zh/product-ion.html` — add
- `content/terms/en/neutral-loss.html` — add
- `content/terms/zh/neutral-loss.html` — add

These are article fragments, not generated pages. The Chinese files are matched translations of article content. This batch adds no bilingual navigation, UI labels, or translated README.

## Metadata application

1. In `content/articles.json`, replace only the object with `slug: fragmentation` using `metadata/fragmentation.article.json`. Preserve its position, prerequisites, group, and unrelated entries.
2. Append the three objects in `metadata/terms.additions.json` to `content/terms.json`. They belong in terminology, not the Guide sequence.
3. Merge the seven new keys in `metadata/references.additions.json` into `content/references.json`. Preserve all existing keys. `metadata/references.reused.json` is an inspection aid only; do not reapply it over newer references.
4. Citation numbers 1–3 retain the existing Guide's references. Added references follow in article-local order 4–13. Terms have their own ordered reference arrays.
5. Use the established builder for generated pages, reciprocal Guide/term links, search data, and language switching. No new navigation framework is requested.

## Anchors and routes

All seven existing Guide anchors are retained: `sequence`, `activation`, `peptides`, `example`, `interpretation`, `practice`, `next-level`.

New paired anchors: `measurement`, `collisions`, `electrons`, `residue-gap`, `conservation`, `coisolation`, `evidence`.

Every term pair uses `definition`, `example`, `confusion`, and `guides`.

English routes: `/guides/fragmentation/`, `/terms/precursor-ion/`, `/terms/product-ion/`, `/terms/neutral-loss/`.

Chinese article routes: the same paths prefixed by `/zh`.

## Fixtures and integration record

- `tests/fixtures/fragmentation.json`: proposed exact repository path for 13 constructed calculation/bookkeeping cases, with assumptions and expected outputs. It is data for the later engineering pass; its schema is not claimed to match existing test code without adaptation.
- `docs/content-batches/05-fragmentation.md`: optional exact-path batch record documenting the source scope and acceptance work.
- `SOURCE-BOUNDARIES.md`: claim-level citations, accessible copies, and limits on inspected material.
- `QA.md` and `validation-results.json`: content-packet checks, separated from repository build/runtime testing.
- `inspection/`: read-only baseline snapshots used to check nonduplication and linked anchors. Do not copy these snapshots into the repository as updates.

## Later acceptance work

Recheck main, apply the content and metadata, and extend existing science/terminology checks using the provided cases. Run the current complete build and structural/scientific checks, then regenerate pages and search assets together. Verify old/new anchors, citation numbers, reciprocal term links, translated article destinations, and English-primary indexes. Inspect narrow-screen table/equation overflow and keyboard-accessible disclosure controls. Report actual test and deployment results separately from this completed writing package.
