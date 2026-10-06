# Quantification, design, and QC expansion

Baseline inspected: `41af17b09a188ed7c884fcb99cfcea4efd1ef2a5` (2026-10-06).

Adds three bilingual Guides and six bilingual terminology entries. Content remains English-primary, with complete Chinese article views and no interface-language changes. The new Guides explain how calibration turns response into concentration, why experimental units matter more than raw-file counts, and how controls support conditional normalization and batch correction.

Examples are explicitly constructed. Thirteen machine-readable fixtures cover inverse calibration and dilution, lower-limit estimates, repeatability versus reference difference, hierarchical replication, design ranks, paired estimands, drift interpolation, median-scaling ambiguity, CV, internal-standard ratios, and confounded multiplicative effects.

Source boundaries: VIM definitions, official NIST statistical guidance, ICH M10/Q2(R2) within their declared scopes, and original experimental-unit and metabolomics correction studies. Existing mQACC, normalization, imputation, and analysis-reporting references are reused. No blanket normalization/imputation rule, universal replicate count, or assay acceptance threshold is introduced.

Validation before handoff: all 18 fragments have matched language section IDs, citations and link destinations; references are collision-free; Guide and term lengths meet their requested ranges; 13 arithmetic/interpretation fixtures and 18 bilingual published-value checks pass. Full repository and browser checks remain part of integration.
