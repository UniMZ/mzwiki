# Source and scientific boundaries

## Source verification

All source checks were made on 2026-10-06. URLs are preserved in `metadata/references.additions.json`; the existing `orbitrap`, `iupac`, and `measurement` records are reused unchanged.

- IUPAC Gold Book entries 12602, 12560, and 12577: complete entry text was available in indexed search results, with links to the 2013 recommendations and exact source pages. Direct web opening returned HTTP 403. Their definitions were checked through those indexed official excerpts; do not claim direct PDF inspection in this batch.
- Shimadzu Introduction to mass analyzers: directly read the Quadrupole MS section. It supports conventional RF/DC scanning and SIM. Excluded its rankings, model limits, and speed claims.
- JEOL Mass Spectrometry Basics: directly read the detailed Time-of-Flight Mass Analyzers and Reflectron sections. They support a timed launch, flight-time measurement, and energy-dependent penetration into an ion mirror.
- Schwartz, Senko & Syka (2002): PubMed abstract and bibliographic fields verified, DOI 10.1016/S1044-0305(02)00384-7. Used only for the demonstrated linear-trap operations.
- Makarov (2000): PubMed abstract verified, DOI 10.1021/ac991131p. It explicitly supports electrostatic trapping, the axial frequency proportional to (m/z)^(-1/2), and image-current/Fourier analysis.
- Thermo Fisher Operating Manual, Measuring principle: directly read the section supporting axial oscillations, split-electrode image-current detection, and Fourier transformation. Model-specific technical data are excluded.
- Comisarow & Marshall (1974): publisher abstract and bibliographic fields verified, DOI 10.1016/0009-2614(74)89137-2. Supports excitation, time-domain detection, and Fourier transformation. Historical sensitivity/resolution numbers are not used.
- Nagornov, Kozhinov & Tsybin (2017): PubMed abstract and bibliographic fields verified, DOI 10.1007/s13361-017-1598-y. Supports distinguishing unperturbed from ordinarily detected reduced cyclotron frequency. The paper's specialized detection mode is not generalized to all FT-ICR instruments.
- Michalski et al. (2012): PubMed abstract, indexed full-text excerpts, and author-repository metadata verified, DOI 10.1074/mcp.O111.013698. Supports processing dependence and overlapping acquisition, without importing product performance figures. Publication year follows the March 2012 journal issue; online publication was December 2011.
- Scripps institutional tutorial: directly read Mass Analyzers and the component descriptions. Supports the analyzer role and m/z interpretation only; dated comparisons, performance values, and universal identification claims are excluded.

## Important cautions found in official educational sources

“Official” is not treated as a guarantee that every sentence is scientifically precise:

- The Shimadzu page's ion-trap section labels a ring/end-cap description as a 2-D linear trap and describes FT-ICR detection in terms of ejection. Neither statement is used. The draft relies on the primary linear-trap study and primary FT-ICR work for those mechanisms.
- The JEOL introductory analogy section says flight time is inversely proportional to the square root of mass/charge. The correct ideal relation is directly proportional to the square root. The draft independently derives that relation from energy conservation and uses the detailed section only for launch and reflectron concepts.
- The Scripps overview simplifies kinetic energy and TOF width relationships in places. The draft does not reuse those formulas or numerical performance tables.
- None of these cautions needs to appear in the beginner article. They explain the narrow evidence use and protect the later reviewer from unintentionally broadening the claims.

## Equations are teaching derivations

The new arithmetic is derived within stated assumptions, not quoted as a measured instrument calibration.

1. Coordinate: x = M/(u n), n = abs(z). M is physical ion mass, u is one dalton, and n is dimensionless.
2. TOF: M v²/2 = n e V; tau = L/v; hence tau = L sqrt(u x/(2 e V)). Assumptions: negligible initial energy, controlled launch, fixed potential and field-free path, negligible collisions, nonrelativistic motion.
3. Orbitrap: ideal source law f = C/sqrt(x); rearrangement x = (C/f)². No real C or voltage is asserted.
4. Free ICR: n e v B = M v²/r and f_c = v/(2 pi r), hence f_c = e B/(2 pi u x). Assumptions: unperturbed nonrelativistic cyclotron motion in uniform B; not the full trapped-ion calibration relation.
5. Unpadded DFT grid: N samples at f_s define T = N/f_s and bin spacing f_s/N = 1/T. With padding, replace N by the transform length for the grid but retain the actually recorded N for observation duration.
6. No Fourier grid interval is labeled FWHM, resolving power, mass accuracy, uncertainty, or a universal two-peak resolution threshold.
7. The two 100 kHz frequency examples normalize separate ideal models; they are not one experiment or a product comparison.

## Scope limits

- The Guide introduces families and measurement mechanisms, not Mathieu stability-region mathematics, instrument tuning instructions, complete ICR eigenmotions, advanced Fourier algorithms, or universal scan-rate recommendations.
- RF ion trap is explicitly qualified to avoid implying that all trapped-ion analyzers use ejection detection.
- Ion identity remains distinct from selection or a measured m/z coordinate.
- Image-current detection does not require an ion to hit a detector; the text does not promise indefinite ion survival or perfectly nondestructive whole-experiment behavior.
- Longer useful observation can help frequency discrimination, but decay, noise, ion population, field quality, and processing can limit the benefit.
- Transient duration is not assumed equal to accumulation time or acquisition cycle time.
- Chinese translations preserve the equations, examples, anchors, citations, and qualifications of the English originals.

