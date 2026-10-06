# Source boundaries and verification record

Prepared 2026-10-06. The teaching prose and all worked examples are newly written; no source tables, figures, datasets, or extended quotations are reproduced. Bibliographic titles identify the sources. The calculations are deliberately synthetic and are not empirical method comparisons.

## Interpretation rules

- “Spatial resolution” terminology differs among publications. The packet explicitly separates programmed pitch, sampling footprint and demonstrated lateral resolving capability; it imposes no universal numerical criterion
- Oversampling benefits depend on acquisition and extraction/depletion behavior. A finer grid is neither automatically useless nor automatically a valid resolution improvement
- Formula-level annotation confidence is not unique-structure evidence, and an ion image is not automatically a concentration map
- A carrier channel can aid pooled identification without supplying missing single-cell reporter measurements. Reference and carrier roles remain distinct
- The Ctortecka study uses controlled low-input bulk-digest aliquots. It is never portrayed as a test of individually isolated cells
- The pseudoreplication study concerns single-cell RNA sequencing. Only the experimental-unit principle is transferred, not distributions, power estimates, or RNA-specific methods
- LoB, LoD, LoQ, identification FDR and reporter-quality filtering answer different questions. Public CLSI definitions are used without claiming complete access to the paid standard
- Poisson arithmetic concerns relative standard deviation of counts under an ideal model. It is not a 95% interval, ratio uncertainty, real-platform performance claim or conversion from arbitrary intensity
- More pixels or cells do not automatically create independent specimens or donors. The experimental unit depends on the intervention, sampling and inferential question

## Source-by-source boundaries

### spatial-msi-reporting

McDonnell et al. (2015; published online 2014). Discussion point: reporting guidelines for mass spectrometry imaging. Analytical and Bioanalytical Chemistry 407, 2035–2045.

https://doi.org/10.1007/s00216-014-8322-6

Community reporting proposal. Supports reporting preparation, acquisition, extraction, normalization, scales and image processing. Institutional full-text PDF inspected. Not a certification that an image represents concentration or a clinical conclusion.

### spatial-resolution-pattern

Fagerer et al. (2015). Resolution pattern for mass spectrometry imaging. Rapid Communications in Mass Spectrometry 29, 1019–1024.

https://doi.org/10.1002/rcm.7191

Primary resolution-test-pattern study; publisher abstract and metadata verified. Supports testing actual feature separation. The packet does not impose a universal terminology convention, edge criterion, or resolution limit.

### spatial-oversampling

Duncan and Lanekoff (2018). Oversampling To Improve Spatial Resolution for Liquid Extraction Mass Spectrometry Imaging. Analytical Chemistry 90, 2451–2455.

https://doi.org/10.1021/acs.analchem.7b04687

Primary nano-DESI study demonstrating conditional benefit of oversampling. Publisher abstract inspected. No universal improvement, depletion mechanism, pixel pitch, or instrument capability is inferred.

### spatial-msi-annotation

Palmer et al. (2017; published online 2016). FDR-controlled metabolite annotation for high-resolution imaging mass spectrometry. Nature Methods 14, 57–60.

https://doi.org/10.1038/nmeth.4072

Primary framework for molecular-sum-formula-level annotation. PubMed abstract and publisher metadata checked; direct publisher open encountered an access redirect. No unique-isomer or concentration claim is inferred from formula-level FDR.

### spatial-msi-normalization

Deininger et al. (2011). Normalization in MALDI-TOF imaging datasets of proteins: practical considerations. Analytical and Bioanalytical Chemistry 401, 167–181.

https://doi.org/10.1007/s00216-011-4929-z

Primary analysis of normalization artifacts. Publisher full text and indexed PMC text inspected; direct PMC access encountered a bot check. Supports denominator-dependent distortion, not a universal ranking of normalization procedures. The 10/100 and 10/200 example is original.

### spatial-autocorrelation

Cassese et al. (2016). Spatial Autocorrelation in Mass Spectrometry Imaging. Analytical Chemistry 88, 5871–5878.

https://doi.org/10.1021/acs.analchem.6b00672

Primary within-sample statistical study; publisher abstract and metadata checked. Supports spatial dependence of neighboring MSI observations. No numerical discovery-rate improvement or mandatory model is transferred to this guide.

### spatial-imzml

Schramm et al. (2012). imzML—a common data format for the flexible exchange and processing of mass spectrometry imaging data. Journal of Proteomics 75, 5106–5110.

https://doi.org/10.1016/j.jprot.2012.07.026

Original community format description; PubMed indexed abstract/metadata and official imzML repository inspected. Supports exchange of metadata and spectral data, not validation of chemical identity or biological conclusions.

### spatial-scp-recommendations

Gatto et al. (2023). Initial recommendations for performing, benchmarking and reporting single-cell proteomics experiments. Nature Methods 20, 375–386.

https://doi.org/10.1038/s41592-023-01785-3

Original community recommendations/Perspective. Supports randomization, quantitative quality, negative controls, missingness and filtering sensitivity. Public primary text inspected during research; publisher open may redirect. Not an experimental performance benchmark or mandatory universal threshold.

### spatial-scope2

Specht et al. (2021). Single-cell proteomic and transcriptomic analysis of macrophage heterogeneity using SCoPE2. Genome Biology 22, 50.

https://doi.org/10.1186/s13059-021-02267-5

Primary method; publisher full text inspected. Supports isobaric channel workflow, carrier versus reference roles, reporter-ion quantification and coisolation. Diluted bulk standards are distinguished from real single cells; no dataset-wide coverage is attributed to every cell.

### spatial-carrier-limit

Cheung et al. (2021; published online 2020). Defining the carrier proteome limit for single-cell proteomics. Nature Methods 18, 76–83.

https://doi.org/10.1038/s41592-020-01002-5

Primary controlled carrier and ion-sampling study, verified through public primary records. Supports setup-dependent quantitative tradeoffs; no universal carrier ratio is recommended. The Poisson calculation is an independent idealized model, not experimental counts from the paper.

### spatial-scp-accuracy

Ctortecka et al. (2022). Quantitative Accuracy and Precision in Multiplexed Single-Cell Proteomics. Analytical Chemistry 94, 2434–2443.

https://doi.org/10.1021/acs.analchem.1c04174

Primary analytical study using low-input bulk HeLa digest aliquots, not individually isolated cells. PubMed metadata and public primary full text verified. Supports separating identification counts from quantitative usability; no numerical carrier limit or method ranking is generalized.

### spatial-clsi-ep17

CLSI (2012). EP17-A2: Evaluation of Detection Capability for Clinical Laboratory Measurement Procedures; Approved Guideline—Second Edition.

https://clsi.org/shop/standards/ep17/

Official standard overview and public scope verified; second edition published 2012 and reaffirmed 2017. Full paid standard not claimed to have been inspected. Supports distinguishing blank, detection and quantification capability; not a universal discovery-proteomics acceptance rule.

### spatial-pseudoreplication

Zimmerman, Espeland and Langefeld (2021). A practical solution to pseudoreplication bias in single-cell studies. Nature Communications 12, 738.

https://doi.org/10.1038/s41467-021-21038-1

Primary analysis in single-cell RNA sequencing. Only the hierarchical experimental-unit principle is transferred to proteomics. No RNA-specific model, power result or threshold is transferred. Donor/cell counts are original teaching examples.

### spatial-clsi-terminology

CLSI Harmonized Terminology Database. Limit of blank entry.

https://htd.clsi.org/listterms.asp?button=Submit&searchdterm=8

Official term-specific public entry inspected directly on 2026-10-06. Supports a probability-defined upper boundary for blank results and distinction from detection capability. The known-normal percentile arithmetic is original and explicitly excludes finite-sample estimation uncertainty.

### spatial-msi-preparation

Yang and Caprioli (2011). Matrix Sublimation/Recrystallization for Imaging Proteins by Mass Spectrometry at High Spatial Resolution. Analytical Chemistry 83, 5728–5734.

https://doi.org/10.1021/ac200998a

Primary preparation study; publisher abstract and indexed public full text inspected. Examines washing, section thickness, matrix amount and recrystallization. No numerical protocol, universal preparation optimum or resolution specification is transferred.

## Reused existing source

### missingness-benchmark

Harris, Fondrie, Oh & Noble (2023). Evaluating Proteomics Imputation Methods with Improved Criteria. Journal of Proteome Research 22, 3427–3438.

https://doi.org/10.1021/acs.jproteome.3c00205

Original benchmark across proteomics workflows. Supports experiment- and task-dependent imputation performance and the need for an unimputed comparator. Metadata/abstract and indexed primary PMC text (PMC10949645) verified; direct PMC access encountered a bot check. No method is recommended universally. This is reused from the inspected baseline without changing its reference object.

## Evidence access limits

Metadata and claim scope were cross-checked through publisher pages, PubMed, available institutional copies, official format resources and the CLSI public overview/terminology. Several direct Nature opens redirected, and a direct PMC page displayed a bot check; no login, CAPTCHA or paywall was bypassed. Claims are limited to what the accessible primary material supports. Unverified source-specific operating details, numerical performance results and universal method rankings are omitted.

## Synthetic fixture ownership

All 12 fixtures originate in this packet. They check arithmetic and stated logic only: grid position counting, normalization denominators, specimen and donor units, pitch versus tested feature size, extraction-window membership, ideal Poisson counting, additive interference, channel-quality counting, a known-distribution blank percentile, complete batch confounding, and missingness ambiguity. Passing these checks does not validate any instrument, assay, software pipeline or biological claim.
