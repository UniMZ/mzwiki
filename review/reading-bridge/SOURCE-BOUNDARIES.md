# Source and example boundaries

## Pinned repository inspection

Repository: https://github.com/UniMZ/mzwiki

Baseline: https://github.com/UniMZ/mzwiki/tree/4981636fdb9660cbc30bdff091ad94545bb7f435

The inspected collection contains eight Guides and 18 terminology pairs; neither `mass-spectrum` nor `base-peak` exists. Snapshots under `inspection/content/` preserve the baseline needed to compare the edited fragments, metadata, and linked anchors. They are evidence for this packet, not replacement files to apply wholesale.

## New bibliography entries

- `base-peak-definition`: IUPAC Gold Book, Base peak in mass spectrometry, B00608. https://goldbook.iupac.org/terms/view/B00608 . The current entry retains the 1991 definition of the greatest-intensity peak. It supports a signal ranking, not a molecular assignment.
- `relative-intensity-definition`: IUPAC Gold Book, Intensity (relative to base peak) in mass spectrometry, I03073. https://goldbook.iupac.org/terms/view/I03073 . The denominator is the strongest resolved peak, with the base peak conventionally set to 100. The same definition is present in IUPAC 2013 entry 220. This is a peak-signal ratio, not a fraction of the sum or sample composition.
- `retention-time-definition`: IUPAC Gold Book, Total retention time in column chromatography, 10039. https://goldbook.iupac.org/terms/view/10039 . The 2017 recommendation measures time from injection to the relevant peak maximum, including hold-up time. The short orientation uses that conventional meaning; it does not discuss adjusted retention time or prescribe identification tolerances.

Official indexed text was verified for these definitions. Direct retrieval of these Gold Book pages returned HTTP 403 during this pass. That limitation is recorded rather than describing a full-page inspection that did not occur.

## Reused bibliography and scope

- `iupac`: Murray et al. (2013), Definitions of terms relating to mass spectrometry, DOI https://doi.org/10.1351/PAC-REC-06-04-06 . Official indexed definitions were checked at https://publications.iupac.org/pac/pdf/2013/pdf/8507x1515.pdf ; direct PDF retrieval returned HTTP 403. Entry 323 supports the modern mass-spectrum concept without restricting it to an ion beam. Entry 220 distinguishes detector-response intensity from ion abundance. The terminology also supports EI/ESI and precursor/product analysis. The packet reuses this existing key instead of creating a duplicate citation to the same paper. The older beam-only Gold Book mass-spectrum entry M03749 was not adopted as the primary definition.
- `extracted-ion-profile`: IUPAC Gold Book entry 12410, https://goldbook.iupac.org/terms/view/12410 . The definition includes chromatographic time traces of selected recorded m/z signals. Official indexed text verified; direct retrieval was unavailable. An XIC is a processed view, and the packet does not assert a universal extraction algorithm for all data representations.
- `ms-order`: Existing official Thermo Fisher Orbitrap Tribrid glossary citation. Its indexed notation was retained for successive stages of analysis. The new orientation links the already-reviewed `acquisition/#levels` explanation and does not duplicate acquisition mode, cycle, isolation-window, or timing lessons.
- `codata`: NIST 2022 CODATA table, https://physics.nist.gov/cuu/Constants/Table/allascii.txt . Directly inspected proton mass 1.007276466578 u and electron mass 0.0005485799090441 u. The adopted teaching constants remain 1.007276467 Da and 0.000548579909 Da, consistent with existing content; u and Da name the same unit.
- `sodium`: NIST sodium-23 table, https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Na . Neutral sodium-23 mass 22.9897692820 u. Subtracting the adopted electron mass gives approximately 22.989220702091 Da for sodium cation, displayed as 22.989220702 Da. Binding-energy mass corrections are omitted at this teaching precision.
- `nist`, `isotopes`, and `carbon` support unchanged source content and retain their baseline records verbatim. This packet does not present that unchanged content as a newly repeated complete scientific audit.

`metadata/references.reused.json` contains exact existing records for review only. Do not replace them merely to apply this packet.

## Constructed three-scan data

The three scans, times, peak positions, and signal intensities were invented for this packet. No source supplied measured spectra; no compound identity or formula is assigned.

The stated model lists all three peaks, holds acquisition settings and the arbitrary signal scale constant, and starts before per-scan normalization. Reading the three signals at m/z 100.000 gives the XIC values 20, 80, and 40. The explicitly inclusive extraction interval 99.990–100.010 contains exactly that peak in each scan. Summing discrete peak signals is the exercise's rule, not a claim about profile-data integration in all software.

The strongest signals are 100, 80, and 80, at m/z 200.000, 100.000, and 300.000. Dividing the 100.000 signal by each scan's own maximum gives 20%, 100%, and 50%. A different normalization of the entire XIC to its own maximum is outside this small lesson. Three points are sufficient for the arithmetic demonstration, not evidence of adequate chromatographic sampling, peak shape, integration accuracy, identity, or concentration.

The base-peak term uses the same middle scan. Its relative heights 100%, 50%, and 25% sum to 175% because the denominator is the maximum rather than the sum.

## Retained mass example

The foundation's abstract neutral mass of 300.0000 Da and displayed [M+H]+ / [M+Na]+ positions 301.0073 and 322.9892 are unchanged. The packet labels the example constructed, links monoisotopic mass and adduct definitions, and makes charge and mass corrections explicit. It does not propose a real molecular formula, claim either ion necessarily forms, predict intensities, or propagate constant uncertainties.

## Orientation boundaries

EI/ESI are source-method labels; MS1/MS2 are analysis-stage labels. Source-generated fragments do not by themselves make a spectrum MS2. The added orientation preserves the possibilities of source/transfer fragmentation, surviving precursors, and coisolated species. It does not imply chemical purity after isolation, require two separate instruments, or claim that all ESI analytes are intact.

Retention time describes a chromatographic peak maximum. The example's scan times locate spectral measurements along the same time coordinate but do not constitute experimentally established compound retention times.

## Protected scope

All original section IDs remain, with one added matching `spectra-and-traces` ID in the foundation pair. Spectrum-interpretation content beginning at `#groups` and foundation content beginning at `#limits` are byte-identical to the inspected baseline; hashes are recorded by validation. Existing calibration offsets, isotope probabilities, Gaussian model, FWHM, ppm arithmetic, images, and other worked examples are untouched. No third terminology page, new long Guide, user-interface translation, code change, or deployment is included.
