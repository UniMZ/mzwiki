# Acquisition learning batch

Content-only research and writing package for UniMZ/mzwiki, prepared 2026-10-06 against read-only main snapshot `141264f45b3b4c02a9c99104e999a2c6caa2446d`. No repository files were changed. No cloud coding task, commit, push, build, or deployment was performed.

## Reader outcome

The expanded acquisition Guide connects measurement scheduling to the evidence recorded by full-scan MS1, DDA, windowed DIA, SRM/MRM, and PRM. It separates MS level from event count and cycle duration, explains temporary DDA exclusion, distinguishes isolation/extraction/retention-time windows, and makes DIA's mixed-fragment problem explicit. A reproducible timing model includes overhead and explains why actual instrument timestamps are needed.

Exactly three nonduplicate terminology pairs are added: Acquisition cycle, Isolation window, and Extracted ion chromatogram. The baseline contains twelve terms; applying this batch would produce fifteen. Terms remain separate from the eight numbered Guides. There are no homepage, navigation, UI-language, styling, or product-comparison changes.

## Complete fragments and exact paths

Replace the two complete Guide fragments:

- `content/en/acquisition.html`
- `content/zh/acquisition.html`

Add the six complete term fragments:

- `content/terms/en/acquisition-cycle.html`
- `content/terms/zh/acquisition-cycle.html`
- `content/terms/en/isolation-window.html`
- `content/terms/zh/isolation-window.html`
- `content/terms/en/extracted-ion-chromatogram.html`
- `content/terms/zh/extracted-ion-chromatogram.html`

These are trusted article-body fragments for the existing builder, not generated pages. Each language has a separate article view. The English Guide is approximately 2,250 whitespace-delimited words including markup; the Chinese article is a complete matched translation, not a stub.

## Metadata application

1. Reconcile newer main changes before application. This packet's frozen baseline is an inspection point, not a claim that main will remain unchanged
2. Replace only the `slug: acquisition` object in `content/articles.json` using `metadata/acquisition.article.json`. Its title, group, prerequisite list, related list, and position are preserved; summary and ordered references change
3. Append the three objects in `metadata/terms.additions.json` to `content/terms.json` after confirming their slugs remain unique
4. Merge the eleven new keys in `metadata/references.additions.json` into `content/references.json`; do not replace the bibliography wholesale
5. `metadata/references.reused.json` is an inspection aid containing four unchanged baseline references, not an overwrite payload
6. Use the established builder for generated pages, search records, language switching, and reciprocal Guide/term links

The complete machine-readable instructions are in `application-manifest.json`.

## Anchors and routes

All six existing Guide anchors remain: `question`, `modes`, `example`, `design`, `practice`, `next-level`.

Ten new Guide anchors are paired between languages: `levels`, `full-scan`, `dda`, `exclusion`, `dia`, `windows`, `targeted`, `traces`, `sampling`, `overheads`.

Each term uses the established `definition`, `example`, `confusion`, and `guides` anchors.

English destinations are `/guides/acquisition/` and `/terms/<slug>/`; the matched Chinese destinations have the `/zh` prefix. Article-local references follow the exact metadata ordering. The Guide retains its existing reference numbers 1 and 2.

## Fixtures and evidence

- `tests/fixtures/acquisition.json`: sixteen constructed arithmetic or interpretation cases, with assumptions and expected outputs. Its schema is proposed data for the later engineering pass, not a claim that current repository tests already consume it
- `SOURCE-BOUNDARIES.md`: claim-to-source support and direct versus indexed-access limits
- `QA.md` and `validation-results.json`: completed packet checks and explicitly unrun integration checks
- `docs/content-batches/06-acquisition.md`: optional exact-path batch record
- `inspection/`: baseline snapshots and a local content-packet validator; none are source replacements

## Later acceptance work

After authorized application, extend the existing scientific/terminology checks to cover these fixtures, rebuild generated output, and run the repository's complete current structural and scientific checks. Test term discovery, reciprocal links, same-article language switching with anchors, citation order, and collection filters. Inspect mobile table/equation overflow and keyboard operation of the practice disclosures. Verify deployment and the live domain separately before describing the content as published.
