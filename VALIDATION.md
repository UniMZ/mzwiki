# First-edition validation

Validated on 2026-10-06 in the dedicated UniMZ/mzwiki environment.

- Standard-library Python build generated 20 HTML pages and 16 full-text search records.
- Static validation passed 715 local links, asset references, and fragment targets across generated pages.
- All eight English/Chinese pairs have matching section IDs, reciprocal language alternatives, prerequisite links, and reference keys.
- Chromium passed 52 scenarios: every generated page at 1440px and 390px widths; no horizontal page overflow; English and Chinese search; no-results and query-safety behavior; deep-linked search; same-article/section language switching; mobile guide navigation; native answer disclosures; keyboard skip link; and article reading without JavaScript.
- No browser script errors were observed. Desktop homepage and mobile article screenshots were visually inspected.
- Bibliographic metadata was checked against NIST and HUPO-PSI official resources, primary-paper records in PubMed/publisher pages, and the IUPAC authors' university repository. Some DOI destinations were blocked by the research browser; metadata was checked through the corresponding authoritative record. External references were not all tested end-to-end from the deployment environment.
- `CNAME` contains `mzwiki.unimz.org`; `.nojekyll` is present.

Run `python3 scripts/build.py`, `python3 scripts/check.py`, and (with a running HTTP server and Playwright/Chromium) `python3 scripts/browser_check.py` to reproduce the checks. These are structural and behavioral checks, not a claim of independent expert scientific review.

Deployment must be verified separately against the pushed commit, GitHub deployment status, and the live domain. The supported branch-publishing configuration is `main` / repository root. See README.md.
