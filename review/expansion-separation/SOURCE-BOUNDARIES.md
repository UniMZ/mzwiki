# Source boundaries and verification

Checked 2026-10-06. The explanations and numerical exercises are newly written. No protected figure, spectrum, application data table or extended passage is reproduced. Sources supply definitions, factual constraints and comparison designs; the examples and diagnostic reasoning are explicitly constructed. All new bibliography IDs use sep-.

## Preparation and recovery

- sep-sample-handbook: Agilent's official Sample Preparation Fundamentals for Chromatography PDF. Cover and text checked; relevant material includes preparation categories and chapters on LLE/SPE. Supports general operations, not a universal best method. No hazardous procedure is reproduced
- sep-ppt-study: official Waters 2020 phospholipid-removal application note. Supports the limited proposition that precipitation can leave soluble matrix constituents. Product superiority, the experimental recipe and measured performance are not imported
- sep-matrix-assessment: Matuszewski, Constanzer and Chavez-Eng, Analytical Chemistry 75(13), 3019–3030 (2003), DOI 10.1021/ac020361s. PubMed PMID 12964746 verifies authors, title, bibliographic details and abstract. ACS full text was not accessible, so the article is cited only for its conceptual distinction between matrix effect and true recovery
- sep-recovery-matrix: Waters reference card 720006298. Full official PDF inspected, including PDF pages 10–12 for response comparisons and page 2 for peptide surface binding. Independently verifies pre/post/neat definitions used in the constructed ratios. No peptide-specific container or solvent prescription is generalized
- sep-m10: FDA's final ICH M10 PDF, November 2022. Sections 3.2.6, 3.2.8 and 7.3 inspected. Supports scoped carryover assessment, handling/storage stability and consistent recovery rather than a demand for 100%. No numerical regulatory limit is presented as a universal MS criterion
- Reused esi-suppression: King et al. (2000); PubMed PMID 11073257 rechecked. Supports a role for nonvolatile solutes/droplet properties in investigated ESI suppression, not the only possible matrix-effect mechanism

## Liquid chromatography

- Reused retention-time-definition: IUPAC entry 10039. Official indexed definition rechecked: injection to relevant maximum, including hold-up time. Direct page and JSON retrieval returned access errors; no claim of direct full-page inspection
- sep-retention-factor: IUPAC R05359. Official indexed text and legacy page confirm adjusted time/hold-up time. Numerical use is explicitly isocratic, with no universal constant-k claim across gradients
- sep-separation-modes: official Waters overview. Supports qualitative reversed-phase/HILIC stationary/mobile-phase distinctions and common gradient direction. Does not justify universal elution order or a recommended product
- sep-lc-handbook: official Agilent LC Handbook. Full PDF inspected for dwell volume/flow delay, method transfer, injection/extra-column dispersion and MS-compatible mobile phases. The glossary's apparent product-versus-quotient typo for dwell time is not used; dimensional analysis and the main discussion support volume/flow
- sep-peak-definition: IUPAC P04451. Official indexed PDF and legacy HTML checked, including unresolved multicomponent peaks. Current page returned 403. This supports a chromatographic signal definition, not automatic identification
- sep-peak-area: IUPAC P04453 official indexed PDF checked. Supports peak/baseline area only. Triangle shapes and areas are original arithmetic, not empirical peak models
- Reused targeted-timing: official SCIEX article rechecked. Supports channel revisit/cycle-time reasoning. No platform default or universal minimum number of points is adopted

## Blanks and carryover

- Reused mqacc-reporting: Kirwan et al. (2022), DOI 10.1007/s11306-022-01926-3. Full publisher text rechecked, especially the true/process blank distinction. It is a consortium recommendation, not binding regulation
- sep-epa-blanks: EPA SW-846 Chapter Three, Revision 6 (December 2018), section 3.1. Official PDF checked. Cited only for method blanks covering preparation/equipment/reagent contamination; inorganic-method procedures or limits are not transferred to LC-MS
- sep-carryover: official Waters Alliance iS support page, topic LCI-USG-0023. Defines prior-injection contribution and residual material. Instrument carryover specifications and maintenance settings are deliberately excluded
- sep-carryover-diagnostics: official Waters WKB246120. Supports controlled comparisons of gradient behavior, injection volume and vial materials. The guide uses the reasoning without reproducing an operational protocol or treating a pattern as unique source localization

## Important interpretation limits

- Recovery/matrix-factor arithmetic assumes matched final amount, solvent and injection conditions, comparable extracted matrix, linear response, and adequate handling of endogenous analyte/interference/background
- An internal standard cannot experience an earlier step if added afterward; ratio stability alone is not validation across matrices
- LC retention and software alignment are different operations. Chromatographic peak width is on the time axis; mass peak width is on m/z
- Gradient delay examples are ideal transport estimates. Peak-area triangles and cycle-interval ratios are teaching models, not analysis software prescriptions
- Carryover percentages in examples are uncorrected signal ratios with explicit denominators. No threshold, subtraction policy, or acceptance criterion is silently imported
- A declining blank sequence suggests history dependence but does not prove a unique physical source. A clean later blank does not validate an earlier affected sample
- The wiki remains conceptual; no detailed hazardous sample-processing or maintenance protocol is given
