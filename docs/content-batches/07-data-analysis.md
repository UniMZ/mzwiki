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
