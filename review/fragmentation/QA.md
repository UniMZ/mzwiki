# Content-packet QA

Checked 2026-10-06 against the read-only repository snapshot `973798e0fa8702ab54690b663d10a67cdde8e561`.

## Completed

- Eight complete HTML article fragments: one Guide pair and three terminology pairs
- All seven original Guide anchors retained; seven new anchors match across languages
- All four standard term anchors match in each English/Chinese pair
- No duplicate term slugs or reference keys against the inspected metadata
- All article-local citation labels agree with their ordered metadata reference arrays
- Every declared reference is used, and every citation key resolves in existing plus proposed references
- All 38 internal article/term links resolve to an existing or proposed route; targeted Guide anchors were checked against the inspected source fragments
- All links from Chinese articles lead to Chinese article routes
- HTML opening/closing tag balance and unique IDs checked in all eight fragments
- Thirteen numerical, isolation-window, or charge/composition fixtures independently recalculated using decimal arithmetic; all expected values and displayed rounding passed
- Scientific review checked electron versus proton bookkeeping, charge-aware losses, peptide-only scope, activation qualifications, and English/Chinese consistency
- The review's coisolation ambiguity was corrected: ordinary isotope-envelope transmission is explicitly separated from cofragmentation of different analytes

## Important retained boundaries

There are no empirical spectra or invented intensities. Every numerical example is labeled constructed or ideal. The isotope-mass central values are treated as fixed teaching constants without uncertainty propagation. Generic charge-partition masses are not asserted molecular formulas. The electron example is charge/composition bookkeeping rather than an exact-mass calculation.

HCD remains in the collisional family, ETD at 2+ is not categorically excluded, and product ion remains broader than fragment ion. Precursor/product labels are relative to a reaction step. Peptide series labels are not exported to all small-molecule chemistry. Matching one product, residue gap, or neutral loss never becomes proof of a unique identity.

## Not run

- No repository build or test suite
- No generated-page/search-index regeneration
- No browser rendering, mobile-layout, keyboard, or accessibility pass
- No commit, push, or deployment verification

This is completed research/writing and local content QA. The parent can apply the finished source text directly and batch the listed engineering checks separately. See `validation-results.json` for the checked cases and final fragment hashes.
