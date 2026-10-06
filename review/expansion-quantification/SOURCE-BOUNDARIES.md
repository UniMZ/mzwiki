# Source boundaries: quantification, design, and QC expansion

Research checked on 2026-10-06 against UniMZ/mzwiki commit `41af17b09a188ed7c884fcb99cfcea4efd1ef2a5`. This packet contains original educational prose and matched Chinese translations. It adds no sample-preparation, recovery, matrix-effect, or chromatography terms. It reuses the existing mass-accuracy, FDR, and missing-value entries rather than duplicating them. No instrument product-performance claims are made.

## New references and supported boundaries

- `quant-vim-calibration` and `quant-vim-curve`: official JCGM definitions of calibration and calibration curve. Support the distinction from instrument adjustment and the absence of uncertainty information in a curve alone. They are not used to claim that a chosen assay is traceable or validated.
- `quant-ich-m10`: ICH M10 final version adopted 24 May 2022, official ICH-hosted PDF. Sections 1.3, 3.1, 3.2.4–3.2.7 were checked for scope, internal standards, calibration, QC, and dilution. The Guide expressly restricts the regulatory scope to drug bioanalysis. No M10 numerical acceptance threshold or required number of standards is imported into an exploratory-omics recipe. ICH copyright is acknowledged in the reference record. The articles are original explanations, not official or endorsed guideline translations.
- `quant-nist-residuals`: official NIST handbook section 4.4.4. Supports residual diagnostics and why R-squared alone does not validate a model. No source dataset, figure, or empirical fit is reproduced.
- `quant-nist-weighted`: official NIST handbook section 4.1.4.3. Supports weights as a variance/precision model and cautions about estimating weights with few replicates. The articles do not prescribe 1/c or 1/c² weighting.
- `quant-ich-q2`: official ICH Q2(R2) final document, adopted 2023 with 2025 error corrections. Sections 3.2.3.3–3.2.3.5 support the DL = 3.3σ/S and QL = 10σ/S estimates and validation boundary. The current EMA listing was checked; its PDF retrieval returned HTTP 429, so the official ICH-hosted final PDF was read. The older indexed Step 2b draft was not used. ICH copyright is acknowledged. These estimates do not extend the constructed 1–10 ng/mL calibration range or establish a universal false-positive/false-negative probability.
- `quant-vim-detection`: official JCGM VIM 4.18 definition. Supports procedure- and decision-dependent detection capability with two error probabilities. The articles do not treat LOD as an invariant instrument specification or proof of absence.
- `quant-experimental-units`: Lazic, Clarke-Williams & Munafò, PLOS Biology 2018, DOI 10.1371/journal.pbio.2005282. Full publisher article checked. Supports biological/experimental/observational units and genuine replication. The donor hierarchy and other MS teaching examples are new constructions; the paper's prevalence findings are not repeated or generalized.
- `quant-nist-blocking`: official NIST randomized-block guidance. Supports nuisance-factor blocking and randomization. The twelve-unit allocation is newly constructed, not a sufficient-sample-size recommendation.
- `quant-nist-nested`: official NIST nested-variation guidance. Supports distinct variation and experimental-unit levels; used as statistical background, not as a universal mixed-effects-model prescription.
- `quant-nist-sample-size`: official NIST sample-size guidance. Used only for dependence on variance, effect/precision targets, and decision errors. The source's equations, industrial example, and count recommendations are not reproduced.
- `quant-batch-correction`: Wehrens et al., Metabolomics 2016, DOI 10.1007/s11306-016-1015-8. Full publisher article and PubMed bibliographic record checked. Supports data-, design-, and QC-dependent correction performance. No universal algorithm ranking, QC frequency, or imputation prescription is inferred from its three plant-metabolomics datasets.

## Reused references

The five reused entries are copied exactly from the pinned reference dictionary for inspection, not re-added under new keys.

- `vim-precision`: official VIM precision definition and its condition dependence; direct page rechecked.
- `mqacc-reporting`: Kirwan et al. 2022 consortium recommendations; full publisher text rechecked, especially control roles, pool origin, pooling stage, placement, and reporting. These are recommendations, not binding rules. Pool coverage does not guarantee every analyte's performance.
- `normalization-comparison`: Kauko et al. 2015 primary phosphoproteomics study; full publisher text rechecked. Supports the possibility that centering conflicts with real global changes; does not establish a universal replacement method.
- `missingness-benchmark`: Harris et al. 2023 original proteomics benchmark. DOI retrieval was unavailable in this pass; indexed primary PMC article PMC10949645 was rechecked for dependence on evaluation task/workflow and the unimputed comparison. Its method rankings are not generalized.
- `analysis-reporting`: Goodacre et al. 2007 MSI reporting recommendations. Publisher abstract and metadata rechecked. Supports reporting design, acquisition scheduling, processing, and model-validation splits. The practical leakage and audit cautions are methodological consequences, not claimed quotations or a new universal validation protocol.

## Independently constructed teaching material

All numeric values, allocations, matrices, and questions are original synthetic examples. No measured spectra or study observations are presented as new data. The fixture file records inputs, outputs, and assumptions for thirteen examples:

1. Linear calibration inversion, fivefold dilution, and the zero-intercept error
2. Linear-response DL/QL estimates
3. Close repeated values with a mean below the reference
4. Eight donors, sixteen preparations, forty-eight injections
5. Rank-four balanced additive design with twelve units
6. Rank-two exactly confounded additive design
7. Paired log-ratio versus absolute-change estimands
8. Linear drift interpolation and response correction
9. Median scaling with biological/technical ambiguity
10. Sample-standard-deviation CV
11. Shared internal-standard response multiplier
12. LOQ conversion onto the original-sample scale after dilution
13. Two indistinguishable biological/batch multiplier explanations

Validation checks arithmetic, not whether a real method meets these assumptions. Two QC endpoints do not validate a drift curve. Four illustrated calibration rows do not validate an assay. No blanket normalization, imputation, sample-size, or acceptance rule is recommended.
