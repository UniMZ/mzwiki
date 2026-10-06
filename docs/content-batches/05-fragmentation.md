# Fragmentation learning batch

Prepared 2026-10-06 against main `973798e0fa8702ab54690b663d10a67cdde8e561`.

## Scope

- Replace the English and Chinese Fragmentation & tandem MS article fragments while preserving all seven original anchors
- Add separate Precursor ion, Product ion, and Neutral loss term pairs
- Keep Guide and terminology metadata separate; reuse existing mass/charge/isotope/analyzer terms
- Add seven reference records while retaining the existing Guide's first three references
- Provide 13 constructed numerical or charge/composition fixtures for the later engineering checks

## Scientific boundaries

The Guide follows one common product-ion MS/MS experiment rather than defining every tandem acquisition as a three-step scan. CID/HCD remain collision-based; ECD/ETD discussion is qualified to common positive peptide applications. Electron gain changes charge without deleting a proton. Product ion is broader than fragment ion.

Peptide b/y and c/z-type labels illustrate peptide backbone nomenclature only. Residue counts, charge states, and radical notation are distinguished. Charge-aware neutral-loss arithmetic requires a matched precursor/product relationship, retained charge, consistent isotope assignments, and no additional exchanged species. Exact-mass arithmetic uses NIST tabulated central values as fixed teaching constants; uncertainties are not propagated.

All numerical examples are constructed. The arbitrary 1000/600/400 Da charge-partition example asserts neither molecular formulas nor observed peaks. Isolation windows are ideal rectangles. Coisolation of different analytes can produce chimeric spectra; ordinary isotope peaks alone do not establish that several analytes were fragmented. No single product, loss, or library score is presented as proof of a structure.

## Evidence access

Substantive terminology was verified in the IUPAC 2013 report via the MSACL-hosted PDF mirror after the official PDF returned 403. Full institutional copies of the original ECD and ETD papers were inspected. HCD and supplemental ETD claims remain within inspected primary abstracts. The peptide-nomenclature paper's indexed introduction was available, but its complete subscription text was not inspected. The coisolation primary article and official NIST isotope pages were readable. No commercial spectral-library content was inspected.

## Acceptance work

The writing package checks numerical arithmetic, article-local citation order, translated-anchor parity, old-anchor preservation, and linked destinations against the inspected source snapshot. These checks do not constitute a repository build, runtime QA, deployment, or independent experimental validation.

The implementation pass should adapt the supplied fixture data to existing tests, run the full current build and structural/scientific checks, regenerate public pages and search assets, and verify glossary links, language switches, English-primary navigation, keyboard disclosure controls, and narrow-screen readability. Record actual test results and final commit/deployment separately.
