# Analyzer learning batch

Prepared 2026-10-06. Content-only package for UniMZ/mzwiki, inspected read-only at main commit `9866af0db25c5740fea30ad85cf21e4bcba0f0d6`.

## Reader outcome

The existing analyzer Guide gains beginner explanations of quadrupole filtering, TOF timing, RF ion-trap sequencing, and Orbitrap/FT-ICR frequency measurement. Original resolution, accuracy, tolerance, and comparison material stays in place. Two independent terminology entries explain Mass analyzer and Transient. Scan is deferred to an acquisition-focused batch because its physical and software meanings need their own context.

All examples are constructed. No empirical spectrum, instrument benchmark, vendor performance ranking, or product recommendation is added.

## Complete source fragments

Copy these six draft fragments to the identical repository-relative paths after reviewing current main for intervening edits:

- `content/en/analyzers.html`
- `content/zh/analyzers.html`
- `content/terms/en/mass-analyzer.html`
- `content/terms/zh/mass-analyzer.html`
- `content/terms/en/transient.html`
- `content/terms/zh/transient.html`

These are complete article-body fragments, not patches or full generated pages. Each Chinese file is a matched article translation. The package adds no bilingual navigation, README text, or user-interface elements.

## Metadata application

- In `content/articles.json`, replace only the object whose `slug` is `analyzers` with `metadata/analyzers.article.json`. Preserve its position in the Guide learning path.
- Append the two objects from `metadata/terms.additions.json` to `content/terms.json`; do not add them to the Guide array.
- Merge the unique keys in `metadata/references.additions.json` into `content/references.json`. Preserve every existing key.
- New reference keys are scoped for reuse. Citation numbering follows each article's own ordered `refs` array.
- Existing Guide references remain numbers 1–3. The new Guide references use numbers 4–13.
- Existing terminology remains unchanged, including Resolving power. Links to it use its existing route.
- The current builder already generates reciprocal Guide/term links and search classifications. Use that existing pipeline; no new framework or navigation behavior is requested.

## Anchors and routes

Preserved Guide IDs: `idea`, `comparison`, `example`, `resolution-accuracy`, `tolerance`, `tradeoffs`, `practice`, `next-level`.

New paired Guide IDs: `quadrupole`, `tof`, `ion-traps`, `frequency`, `orbitrap`, `fticr`, `transient-time`, `hybrids`.

Both term pairs use `definition`, `example`, `confusion`, `guides`.

English paths: `/guides/analyzers/`, `/terms/mass-analyzer/`, `/terms/transient/`.
Chinese article paths: `/zh/guides/analyzers/`, `/zh/terms/mass-analyzer/`, `/zh/terms/transient/`.

## Scientific validation inputs

`analyzer-arithmetic-fixtures.json` records all ten new arithmetic cases, explicit model assumptions, and expected results. These are data for the later implementation/test pass, not an executable check and not additions to an existing schema without adaptation.

`SOURCE-BOUNDARIES.md` records the claim-level research boundaries. `QA.md` records the content-level checks completed here.

## Later application and acceptance checks

1. Recheck current main, apply only this content scope, and preserve unrelated updates.
2. Extend the existing science/terminology fixture checks using the provided cases and assumptions.
3. Run the current build and all existing structural/scientific checks; regenerate generated pages and search data together.
4. Verify all old and new anchors, article-local reference numbers, term routes, reciprocal Guide/term links, and language-switch destinations.
5. Check English-primary navigation/indexes, separate translated article views, keyboard interaction, search results, and narrow-screen equation/table overflow.
6. Report actual test results and deployment status. This package has not been built, committed, pushed, or deployed.

