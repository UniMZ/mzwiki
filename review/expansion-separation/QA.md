# Content QA

## Completed package-level checks

The package-only validator passes 426 checks with zero errors and zero warnings. It checks:

- Three Guide slugs and six term slugs are absent from the pinned baseline collections
- Thirteen new bibliography IDs are absent from the baseline and use sep-; four reused entries match the baseline exactly
- All 18 complete HTML fragments have balanced nesting, unique section IDs and no page shell, inline script or style
- English and Chinese pairs have identical section IDs, numerical tokens and normalized link/citation sequences
- Citations match each item's ordered refs array, with every listed reference used
- Guide/term metadata cross-references resolve to the inspected baseline or this package's additions
- Linked local anchors resolve, and prerequisite relationships remain acyclic
- Manifest destinations cover all authored fragments
- Eleven constructed fixtures contain 23 passing arithmetic assertions

## English word counts

- Sample preparation & recovery: 1126
- Liquid chromatography for MS: 1184
- Blanks, carryover & contamination: 1169
- Retention time: 203
- Chromatographic peak: 205
- Recovery: 210
- Matrix effect: 220
- Carryover: 202
- Blank: 221

Counts include headings and reader exercises. Chinese articles are complete matched translations, not summaries or placeholders.

## Editorial/scientific review

- Meaning, qualifications and examples were reviewed across language pairs; automated token equality alone does not establish translation quality
- Recovery and matrix effects remain separate; pre/post/neat assumptions accompany ratio calculations
- Peptide/protein inference, endogenous analyte, internal-standard timing and low-response limitations are explicit
- No universal separation mode, equilibration time, integration algorithm, scan-count minimum or blank threshold is prescribed
- The gradient-delay calculation is dimensionally volume/flow; retention time and delay are not conflated
- Triangle area calculations explain height versus area without representing measured spectra
- Sequence patterns support hypotheses but do not uniquely identify contamination sources
- Regulatory and method-specific sources have explicit applicability boundaries
- No empirical sample data, private information, copied figure, or detailed hazardous laboratory procedure is included

## Remaining integration checks

No repository build, repository mutation, production fixture-runner integration, browser rendering, interaction/accessibility test, deployment, or live-site check was performed. The integrator must apply the additive manifest, reconcile simultaneous topic additions, update tests that assume collection counts, and perform the repository's established checks. Review the one table at narrow widths and test the details/summary exercises in generated views.
