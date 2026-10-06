# Advanced learning expansion: engineering integration

Authored source: `f02c37031003fab0b3f93de3d395510f942180a4`. Baseline main: `ecca2688d1c33ce5485e8497b6c3e8f498376cb3`.

## Scope

Integrate three additive packets covering structural/specialized proteomics, spatial/single-cell measurement, and computational MS. Eight new Guide pairs and sixteen new term pairs bring the collection to 28 Guides, 60 terms, 193 reference records, 181 HTML pages and 176 search records.

All 48 new article fragments and three fixture files match their supplied hashes. All 128 existing article fragments, the article template and existing metadata records/order remain unchanged. No scientific prose or fixture was corrected, and no independent research was performed. Research-access qualifications remain in each packet's SOURCE-BOUNDARIES.md.

## Engineering changes

The existing dynamic builder and grouped navigation handle the larger collection without modification. Regenerate pages, navigation, references, reciprocal links, search and sitemap. Update README inventory and test commands.

Add `check_advanced_expansion.py` for 39 supplied cases: 14 structural, 12 spatial, 13 computational. Keep the prior expansion checker scoped to its original four packets, preserving all its assertions. Accept the new authored definition/example/boundary term section structure alongside the existing formats.

Give exact normalized title matches priority in search, then retain the existing keyword score. This fixes a regression where “Limit of blank” ranked ahead of the complete title “Blank”. No framework, CSS, domain, hosting or security changes are required.

## Verification

- All existing structural/scientific checks pass, including the previous 43-fixture expansion suite
- New 39-fixture suite passes arithmetic, combinatorial/set logic and declared interpretation guards; checks rendered bodies, complete ordered citations, numerical/anchor parity, and 51 source/fixture hashes
- Structural checks pass 37,680 local links/assets/fragments, 88 translation pairs, 176 full-text search records, 193 bibliography entries and acyclic prerequisites
- Chromium passes 1,981 scenarios, covering every new article's bilingual section switches, exact-title search, desktop/390px/320px layout, table scrolling, long navigation, keyboard disclosures and no-JavaScript reading; no script errors
- Additional targeted search checks pass for “Blank”, case/whitespace-normalized “BLANK”, and “Limit of blank”
- English/Chinese narrow-screen article and search screenshots inspected
- Repeated build produces identical hashes; `git diff --check` passes

These are local integration checks, not experimental validation, expert scientific review, or a deployment claim. Merge, Pages build and live-site verification follow separately.
