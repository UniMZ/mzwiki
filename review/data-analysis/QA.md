# Quality checks

## Passed for this packet

- Pinned baseline inspection confirms eight Guides and 15 terms
- Exactly one Guide pair is replaced and three nonduplicate term pairs are added
- English Guide is approximately 1,950 words; each English term is approximately 190–200 words
- All seven prior Guide anchors are retained; eight new anchors match across languages
- Term anchors match the existing four-section convention
- HTML tags are balanced; no scripts, styles, page shells, or UI changes are introduced
- All reference keys exist after the additive merge; ten new keys do not collide with the baseline
- Guide reference numbers 1–3 are retained and all local citation numbers match metadata order
- Internal route slugs exist in the combined metadata, language prefixes match, and authored local anchor targets exist
- English article fragments contain no Chinese text; Chinese content is confined to translations and approved metadata fields
- Numeric-token multisets match across each English/Chinese pair; explicit published example strings are checked in all eight authored fragments
- Ten teaching fixtures pass: expected FDP, realized FDP, no-discovery convention, internal-standard ratios, median scaling, missing-value means, replicate hierarchy, exact-confounding matrix rank, feature identity boundary, and nominal-FDR interpretation
- Independent read-only scientific/translation review found no substantive scientific correction needed; its Chinese correction from “random decimals” to “randomly generated low values” was applied, and centroid-intensity wording was clarified in both languages

Run `python3 inspection/validate_packet.py` to regenerate `validation-results.json`. The final file records the actual checked content paths and counts. Two fixtures verify semantic guardrails rather than deriving scientific truth; these remain subject to human review.

## What was not run

No repository was changed. No repository build, structural check, existing scientific check, generated-search check, browser check, deployment check, or live-site check was run. The packet checker is not the project's acceptance suite. Rendered appearance, keyboard behavior, and language-switch behavior have not been verified here.

## Required later integration checks

1. Reconcile the current main branch with the pinned baseline before applying anything
2. Apply complete fragments and targeted metadata merges as specified; retain eight Guides and the separate Terminology collection
3. Add or adapt a repository checker for `tests/fixtures/data-analysis.json`; validate arithmetic and actual published example strings, not just fixture self-consistency
4. Run the established builder, structural checker, every existing scientific checker, and the new data-analysis check against final generated output
5. Run browser checks for term discovery, collection/language filters, reciprocal links, same-article anchor-preserving language switches, and no-JavaScript reading
6. Inspect long equation wrapping, small-screen reading, and practice disclosure keyboard operation
7. Treat remote commit, deployment completion, and live-domain verification as separate checks before saying published

## Scientific review boundaries

Sources were checked at the access level recorded in `SOURCE-BOUNDARIES.md`; some full texts were not directly retrievable. No inferred real-world numerical performance is used. The toy equations validate arithmetic under stated assumptions, not a real instrument, real FDR estimator, imputation method, or normalization protocol.
