# Broad learning expansion: engineering integration

Source commit: `73e77489caaa2e7b82b9bb30dc7b88d13afb44b7`. Baseline main: `41af17b09a188ed7c884fcb99cfcea4efd1ef2a5`.

## Integrated scope

Four independently authored content packets add 12 Guide pairs and 24 terminology pairs covering separation/preparation, quantification/design/QC, proteomics, and small-molecule/lipid/mobility evidence. The resulting collection has 20 Guides, 44 terms, 143 reference records, 133 generated HTML pages, and 128 search records.

All 72 new article fragments and four supplied fixture files match their packet hashes. All 56 existing article fragments, the article template, existing metadata records and original eight-Guide sequence remain unchanged. This integration performs no independent scientific research or prose rewriting. Research retrieval qualifications remain in each `review/expansion-*/SOURCE-BOUNDARIES.md`.

## Engineering behavior

- Derive homepage counts and structural expectations from collection metadata
- Group the homepage and native disclosure navigation by Guide topic; group terminology alphabetically
- Open the current article's group; bound sidebar and mobile-menu height with independent scrolling
- Preserve English interface, same-article Chinese views, search, reciprocal links, bibliography and sitemap
- Wrap long reference URLs and article titles at narrow widths
- Accept the authored three-section term format as well as the existing four-section format; normalize equivalent translated labels only inside tests

## Verification

- `build.py` and `check.py`: 133 pages, 21,356 local links/assets/fragments, 64 translation pairs, 128 full-text search records and 143 bibliography entries pass; prerequisites are acyclic
- All prior checks pass: `check_science.py`, `check_ionization.py`, `check_terms.py`, `check_analyzers.py`, `check_fragmentation.py`, `check_acquisition.py`, `check_data_analysis.py`, and `check_reading_bridge.py`
- `check_expansion.py`: all 43 fixture cases pass (11 separation, 13 quantification, 12 proteomics, 7 small-molecule), including independent calculations/set logic, published quantification strings, bilingual numerical/citation/anchor parity, and source/fixture hashes
- `browser_check.py`: 1,361 Chromium scenarios pass, including every new article's bilingual section switches, exact-title search, desktop/390px/320px layouts, table scrolling, keyboard disclosures, long navigation lists and no-JavaScript reading; no script errors
- Inspected desktop topic groups, mobile navigation and English/Chinese article screenshots
- Final repeated build yields identical hashes; `git diff --check` passes

A 320px overflow from a long bibliography URL was fixed in shared CSS, then the full browser suite passed. No authored fixture or article needed correction. Arithmetic and semantic guards do not validate a real experiment or replace scientific review. Domain, hosting settings and security configuration are unchanged. Deployment and live-site verification follow a separate authorized merge.
