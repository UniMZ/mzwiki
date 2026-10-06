# Batch 07: data-analysis foundations

Prepared 2026-10-06 against main `baad05c164ab2151371732973b324c1ff4ce3ce2`. Content-only packet; application and publication have not occurred.

## Reader-facing changes

- Expand the existing data-analysis Guide with raw-data provenance, centroid/profile boundaries, LC-MS features, identity evidence, and quantitative interpretation
- Clarify FDR as expected FDP for a defined discovery set, distinct from per-hit probability, realized errors, localization, and abundance-test error control
- Explain normalization assumptions, ambiguous missingness, control purposes, batch confounding, replication, and reproducibility without giving blanket recipes
- Add Feature, False discovery rate, and Missing value to the separate Terminology collection
- Supply complete matched Chinese articles while keeping UI and project documentation English

## Files to apply

Replace `content/en/data-analysis.html` and `content/zh/data-analysis.html`. Add paired files under `content/terms/{en,zh}/` for `feature`, `false-discovery-rate`, and `missing-value`.

Replace only the `data-analysis` object in `content/articles.json`; append three unique objects to `content/terms.json`; merge ten new reference keys into `content/references.json`. Use the packet's corresponding metadata payloads, never wholesale replacement of shared arrays or the bibliography. Preserve all seven former Guide anchors and the Guide's existing first three reference numbers.

Add `tests/fixtures/data-analysis.json` and integrate its ten cases into an appropriate repository checker. This file is proposed fixture data, not an existing executable test. Numeric examples are explicitly constructed and include assumptions and negative interpretations.

## Acceptance

Local packet checks pass for balanced HTML, paired structure and numeric tokens, anchor preservation, citation ordering, route slugs, reference uniqueness, and fixture arithmetic/semantics. Scientific/translation review found no substantive scientific issue; its wording correction was applied.

After authorized application, rebuild generated output and run the full current structural/scientific/browser suite plus the new data-analysis check. Verify search classification, reciprocal links, language-switch anchors, no-JavaScript reading, and responsive equation wrapping. No build, deployment, or live-site success is claimed by this content packet.

## Repository integration validation

Integrated against main `baad05c164ab2151371732973b324c1ff4ce3ce2` from the authored source commit `0b5748d8b90edcb67bb7b039adc89d99072bf103`. All eight article sources, shared content metadata, fixtures, and review packet remain byte-for-byte unchanged from that commit.

- Rebuilt 57 HTML pages: 8 Guide pairs, 18 Terminology pairs, and 52 search records
- Structural check: 4,621 local links/assets/fragments, 26 translation pairs, and 75 bibliography entries passed
- All existing scientific checks passed; `check_data_analysis.py` independently recomputes eight arithmetic/linear-algebra fixtures and checks two declared semantic boundaries, published examples, paired numeric/citation tokens, old anchors, and generated bodies
- Full Chromium suite passed 367 scenarios, including desktop, 390px and 320px layouts, English/Chinese search, same-article anchors, related links, keyboard disclosures, and no-JavaScript reading; no script errors
- English and Chinese 320px screenshots visually inspected; long equations wrap without page overflow
- Repeated build produced identical file hashes; `git diff --check` passed

Semantic guards protect authored distinctions; they do not independently validate identification evidence, concentration, FDR calibration, or an imputation method. Research source access limitations remain documented in `review/data-analysis/SOURCE-BOUNDARIES.md`. These checks are local; Pages deployment and live-site verification follow an authorized merge separately.
