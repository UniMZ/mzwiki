# Sources, attribution boundaries, and originality

Research date: 2026-10-07 UTC. Only original standards/controlled vocabularies and official developer or instrument-manufacturer documentation support the content. Search snippets from third-party sites were not used as scientific authority. No vendor plots, protected illustrations, measured spectra, or copied prose are included. Chinese pages are translations of the packet's original teaching explanations, not official translations of the cited documents.

## New references

| Reference key | Verification and permitted claim | Boundary |
|---|---|---|
| signal-faraday | SRS RGA manual revision 1.9, September 2026; PDF pages 57–58, collector and multiplier-current descriptions | Mechanism only; no pressure specification, universal collection efficiency, service instructions, or detector ranking |
| signal-charge | BIPM defining-constants page, fixed elementary charge | The original current calculation separately assumes complete collection and known charge |
| signal-multiplier | IUPAC S05517 indexed/plain definition | Repeated secondary emission only; the 4-to-the-5th calculation is an ideal cascade |
| signal-detector-families | Hamamatsu official mass-spectrometry technology page | Architectures and secondary-electron mechanisms; no purchasing advice or comparative superiority |
| signal-dual-mode | Hamamatsu R13733 official product page | Existence of analog/counting modes; no generalized voltage, gain, timing, lifetime, or dynamic range |
| signal-tof-readout | Agilent technical overview 5989-0373EN, author John Fjeldsted, publication December 11, 2003; PDF pages 7–11 | TDC/ADC distinctions and finite readout behavior only; historical product claims, timing assumptions and numeric limits excluded |
| signal-image-detection | Thermo Orbitrap Astral manual, **Orbitrap analyzer → Ion detection** | Differential image-current detection, digitization, coherent axial motion; this does not describe the instrument's separate Astral detector |
| signal-poisson | NIST/SEMATECH statistical handbook Poisson distribution entry | Mathematical mean/variance/CV model only; arbitrary spectral intensity is not assumed Poisson |
| signal-hires-picker | OpenMS PeakPickerHiRes official class documentation, generated September 30, 2026 | Cubic-spline maximum and data assumptions; no universal centroid algorithm or recommended defaults |
| signal-smoothing | Official OpenMS TOPPView Smoothing Raw Data tutorial indexed text | Existence of filter width/order choices; direct open returned an extraction error. The moving-average calculation is independent original mathematics, not OpenMS output |
| signal-snr-definition | IUPAC 08282 indexed definition and notes, source recommendations published 2021 | Power/amplitude convention distinction; direct open returned 403. The explicit height/RMS and peak-to-peak formulas are teaching conventions, not a universal IUPAC analytical formula |
| signal-icis-noise | Official Thermo FreeStyle 1.8 SP3 QF1 page, full text | Different neighboring-point/iterative chromatogram-noise estimators; no formula, software threshold or default generalized to all spectral noise |
| signal-filter-order | Official ProteoWizard direct Filters page, full text | Sequential filters and algorithm choice; no version-dependent command recipe or defaults |

## Reused reference

`psi-ms-representation` is copied unchanged from the baseline reference registry, not added under a second identity. The official vocabulary was checked at data version **4.2.2**, dated **2026-09-18**. Entries MS:1000035, MS:1000127, MS:1000128, MS:1000801 and MS:1000802 support peak-picking and representation terminology, including height/area distinctions. They do not prescribe one numerical centroid estimator or establish feature detection, identification, or concentration.

Two new references are deliberately more specific than nearby existing references: `signal-image-detection` names the directly inspected Orbitrap detection page rather than the existing measuring-principle page; `signal-filter-order` names the direct ProteoWizard Filters page rather than the existing msconvert overview. Exact URLs and keys do not collide. An integrator may consolidate equivalent references deliberately, but must preserve the claim/source mapping and citation ordering.

## Original calculations and reasoning

All twelve fixtures originate in this packet. They cover complete-collection current; charge scaling; mean cascade gain; clipping; ideal sinusoidal phase addition; Poisson relative uncertainty; weighted position, apex, sum and trapezoidal area; baseline-induced estimator movement; zero-padded moving-average behavior; two noise denominators; term-level ratio conventions; and representation boundaries.

The electrical and arithmetic models are deliberately simpler than real measurement systems. They do not validate collection efficiency, detector response, Poisson applicability, deconvolution, a real background model, or analytical detection/quantification thresholds. The distinction between an irreversible many-to-one representation and reconstruction is an original explanatory inference from the defined representations and examples.

## Current-content boundary

Baseline content inspected: article/term/reference inventories, the complete English analyzer and data-analysis Guides, and CONTRIBUTING.md. All proposed slugs are absent. Existing analyzer physics and broad data-analysis stages are prerequisites; this packet adds measurement/readout and estimator/noise depth rather than replacing those articles. No live-site state is inferred from repository inspection.
