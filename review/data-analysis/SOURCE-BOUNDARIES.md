# Source boundaries and editorial decisions

Research date: 2026-10-06. Baseline: UniMZ/mzwiki main at `baad05c164ab2151371732973b324c1ff4ce3ce2`.

## Scope and authority

This is a beginner learning unit, not a literature digest. Sources are primary method/benchmark papers, standards-group recommendations, official format specifications, and first-party software documentation. No study's numeric performance is generalized to all instruments or experiments. All numerical examples are original, explicitly hypothetical teaching models. No experimental spectrum, figure, or extended text is copied.

## Reused references

- `mzml`: [HUPO-PSI mzML](https://www.psidev.info/mzML). Official specification portal, opened successfully. Supports spectra/acquisition metadata and the format's role; it does not promise lossless preservation of every proprietary vendor item or identification results
- `pwiz`: [Kessner et al. 2008](https://pubmed.ncbi.nlm.nih.gov/18606607/). Primary software publication; metadata/abstract checked. Supports ProteoWizard's processing infrastructure, not every current converter option
- `fdr`: [Elias and Gygi 2007](https://www.nature.com/articles/nmeth1019). Primary target–decoy methods paper; publisher record checked. Supports the role of decoys and analysis-level assumptions. This packet deliberately supplies no universal decoy-count formula, which would depend on competition, target/decoy sizing, corrections, and reporting level

## New reference keys

1. `psi-ms-representation`: [PSI-MS controlled vocabulary](https://raw.githubusercontent.com/HUPO-PSI/psi-ms-CV/master/psi-ms.obo), inspected version 4.2.2, dated 2026-09-18. Direct official text of MS:1000035, MS:1000127, and MS:1000128 was checked. Supports peak picking and centroid/profile representation. Does not specify one centroiding algorithm, reversible processing, or a universal intensity interpretation
2. `msconvert-filters`: [ProteoWizard msconvert documentation](https://proteowizard.sourceforge.io/tools/msconvert.html). Official indexed `peakPicking` text verified; direct extraction exposed minimal content. Supports selectable algorithms/MS levels and the need to record options. No command syntax, defaults, vendor dependency, or current platform compatibility is prescribed
3. `feature-finding`: [OpenMS FeatureFinderMetabo](https://openms.org/documentation/html/TOPP_FeatureFinderMetabo.html). Direct first-party documentation checked. Supports mass-trace assembly, isotope-group hypotheses, and elution-profile separation. It is an implementation example, not a universal feature definition, parameter set, or exact boundary between compounds
4. `msi-chemical-analysis`: [Sumner et al. 2007](https://doi.org/10.1007/s11306-007-0082-2). MSI Chemical Analysis Working Group reporting recommendations. Publisher metadata/abstract and indexed primary text at [PMC3772505](https://pmc.ncbi.nlm.nih.gov/articles/PMC3772505/) checked; direct PMC open encountered a bot check. The [UC Davis Fiehn Lab author-hosted manuscript](https://fiehnlab.ucdavis.edu/downloads/publications/MSI%20-%20chemical%20analysis%20-%2007-2007.pdf#page=12) was also read directly: page 12 verifies the two-orthogonal-property criterion for previously characterized metabolites. It is a revised author manuscript, not the final typeset article. Supports evidence-specific compound identification and calibration/validation reporting; novel compound elucidation has separate requirements. Its historical LOD/LLOQ numeric criteria are excluded. Identity evidence does not itself validate concentration, and a library label does not resolve every isomer
5. `fdr-original`: [Benjamini and Hochberg 1995](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). Original FDR definition; publisher metadata/abstract checked, with the primary PDF located through a university-hosted copy. Used for the expectation of FDP and no-discovery convention. The Guide does not teach the BH testing algorithm or claim its control holds for arbitrary dependence. The two-outcome example is a constructed probability distribution, not a target–decoy simulation
6. `normalization-comparison`: [Kauko et al. 2015](https://www.nature.com/articles/srep13099). Full primary publisher text checked. Demonstrates distortion from centering under large directional phosphoproteome changes. No claim is made that the authors' pairwise method is universally preferable. The three-feature vector is original algebra illustrating non-identifiability of biological versus technical scaling
7. `missingness-benchmark`: [Harris et al. 2023](https://doi.org/10.1021/acs.jproteome.3c00205). Original benchmark. [PubMed metadata/abstract](https://pubmed.ncbi.nlm.nih.gov/37861703/) and substantive indexed [primary PMC text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10949645/) checked; direct opens intermittently failed or encountered a bot check. Supports missingness across abundance levels and dependence of imputation performance on task/data. Its differential-expression comparisons are not a universal proof that imputation should never be used. No missingness taxonomy or software winner is prescribed
8. `mqacc-reporting`: [Kirwan et al. 2022](https://link.springer.com/article/10.1007/s11306-022-01926-3). Direct consortium recommendations checked. Supports control purposes, QC preparation/placement, acceptance criteria, and performance reporting in untargeted metabolomics. These are recommendations, not binding regulation. A pooled QC is not a biological replicate and cannot certify signals absent from it
9. `analysis-reporting`: [Goodacre et al. 2007](https://doi.org/10.1007/s11306-007-0081-3). Primary standards-group reporting paper; publisher text checked. Supports experimental design, scheduling, preprocessing, method parameters, and blind model testing. The exact-confounding example is elementary identifiability reasoning: identical condition and batch columns have no separate effects in an unconstrained additive model. Audit-log/checksum/environment guidance is a practical extension, not a quotation of a 2007 software standard
10. `mztab-m`: [HUPO-PSI/MSI mzTab-M 2.0 specification](https://hupo-psi.github.io/mzTab/2_0-metabolomics-release/mzTab_format_specification_2_0-M_release.html). Direct released specification checked, especially sections 5.2, 5.4, and 6.3–6.5. Supports links among samples, assays, runs, feature evidence, and molecule summaries, as well as distinct missing-data encoding. A format cannot infer biological independence, determine why a cell is empty, or dictate an imputation strategy

## Deliberate scientific boundaries

- Preserved raw files remain the provenance root; open-format conversion is useful but not a validation certificate
- Spectral centroiding is separate from isotope grouping, LC feature finding, cross-run matching, and chemical identification
- LC-MS feature is defined contextually; the broader machine-learning meaning is named rather than conflated
- FDR is an expected ratio. A fixed-list realized FDP, a nominal threshold, and an estimated FDR are distinct. The example does not replace expectation of a ratio with ratio of expectations
- FDR is not per-hit correctness, familywise probability of any error, localization confidence, or validation of an abundance test
- Internal-standard ratios require suitable standards and a relevant response model; equal normalized response alone does not establish equal concentration
- Normalization cannot decide whether a common multiplier is technical or real without additional evidence
- Missingness is not automatically low abundance, absence, or zero. The observed-only mean is not presented as automatically unbiased, and no blanket imputation recipe is offered
- A repeated injection is not another independent biological sample. Exact batch–condition confounding cannot be resolved from the same uninformative comparison alone
- No sample-size rule, QC threshold, normalization default, or imputation default is claimed universal

## Access and application limits

Source verification is separate from live-site testing. Bibliographic links are verified identifiers, not promises of unrestricted full-text access. No provider login, CAPTCHA completion, paywall bypass, or subscription was attempted. Local packet checks do not establish rendered layout, generated search behavior, or deployment success. The application manifest requires reconciling main before any later authorized application.
