# Source and claim boundaries

Verified 2026-10-06 against primary methodological papers, community standards, and official resources. Reference records contain exact titles, stable DOI or official URLs, and bounded usage notes. `inspection/source-verification.json` records the sources and retrieval limitations. Text is original; no source figure, spectrum, table, or long quotation is reproduced.

## Small-molecule annotation

- Sumner et al.'s MSI recommendations support the distinction between identified compounds, putative compound annotations, class annotations, and unknowns, and the requirements for known-metabolite level-1 identification. The article explicitly names MSI; it does not mix incompatible numerical confidence scales.
- mzTab-M supports separation of molecule summaries, features, and identification evidence. It is a reporting format, not an identity validator.
- Kind and Fiehn support chemically constrained formula filtering. Heuristics are not universal exclusion laws; reported paper benchmark success rates are not generalized.
- MassBank's official description supports reference spectra plus chemical/experimental metadata. No coverage, ranking, or identification-performance claim is made.
- Existing NIST atomic-mass and CODATA references supply the constants for the constructed C6H12O6 calculation. Binding-energy mass corrections and full uncertainty propagation are outside this teaching example.
- IUPAC's strict MS definition of isobars is intentionally distinguished from structural isomers. Informal broader usage is acknowledged.

## Lipidomics

- LIPID MAPS and LSI provide the nomenclature and reporting hierarchy. The numerical composition examples apply to simple, unmodified diacyl PC. They are not a general formula generator for all lipid classes.
- The class-fragment source explicitly lists both PC and SM near m/z 184.0733. This shared fragment does not uniquely identify one PC molecular species.
- The three candidate chain combinations are constructed arithmetic examples. Chain identity does not itself establish sn order, double-bond location, or double-bond geometry.
- OzID and Paternò–Büchi sources support position-sensitive chemistry only. No universal coverage, instrument ranking, quantitative performance, or automatic complete-structure claim is made.
- LSI retention guidance and the 2024 reporting checklist support documenting method-specific evidence; neither is an automatic identification certificate.

## Ion mobility and CCS

- Gabelica et al. provide community reporting recommendations, including gas, temperature, reduced field, ion species, calibration, and uncertainty. CCS is presented as a model-derived ion–gas quantity, not a neutral-molecule silhouette.
- Shvartsburg and Smith, Fernandez-Lima et al., and Krylov et al. are original principles/method papers supporting distinct traveling-wave, trapped, and differential-mobility mechanisms. The drift-tube equation is not applied to their raw coordinates.
- Stow et al. support the need for comparable reference measurements and method validation. Their numerical interlaboratory performance is not claimed for unrelated workflows.
- Zheng et al. support using nitrogen CCS and ion-form-specific measurements as an additional small-molecule constraint. Matching CCS does not prove a unique structure.
- The 52 ms arrival/2 ms transport example and 202-versus-200 Å² comparison are original teaching constructions. They are not measured data, recommended operating parameters, or universal tolerances.

## Retrieval qualifications

Some direct Gold Book and PMC pages returned access or anti-bot responses. Relevant official indexed definitions, primary indexed text, publisher records, and institutional bibliographic records were used where available. No CAPTCHA was completed. The obsolete LIPID MAPS `/shorthand_nomenclature` route returned 404; the verified current nomenclature landing page is used. Unresolved guessed MassBank record-format paths are not cited. Source discovery alone is not treated as evidence for a detailed unsupported claim.
