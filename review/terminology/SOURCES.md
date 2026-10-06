# Sources and scientific decisions

Checked on 2026-10-06. The bibliography keys and public links are in `references.additions.json` and `references.reused.json`. Definitions are paraphrased; examples are original calculations, not copied spectra or experimental claims.

## Primary references

1. Murray et al., Definitions of terms relating to mass spectrometry (IUPAC Recommendations 2013), DOI https://doi.org/10.1351/PAC-REC-06-04-06. Entry 356 supplies the m/z convention. The introduction explains the conflicting historical uses of resolution and resolving power. The adduct-ion and protonated-molecule entries establish the relevant names. The public author-formatted PDF at https://www.msacl.org/documents/cms_guidance/Mass_Spectrometry_Definitions_and_Terms_IUPAC_2013.pdf was readable; indexed text of the final publisher PDF confirmed entry 356. The IUPAC-hosted PDF and publisher full-PDF open requests were blocked by their web responses. Existing repository reference key: `iupac`.
2. IUPAC, Quantities and units for electrophoresis in the clinical laboratory, Pure Appl. Chem. 66 (1994), 891–896. The indexed official PDF page 893 explicitly states the signed charge-number definition. Its direct PDF open returned 403. This is the source of `charge-number`; the draft does not claim that charge state is the same as oxidation state.
3. IUPAC Glossary of Terms Used in Physical Organic Chemistry (1994), official nomenclature site at https://iupac.qmul.ac.uk/gtpoc/I.html. Full text was readable, including isotopologue and isotopomer. The isotope-composition/positional distinction is the relevant claim; no modern measurement-performance claim relies on this historical glossary.
4. IUPAC Gold Book individual entries: A00139 (adduct ion), 12495 (monoisotopic mass), 12407 (exact mass), 12341 (average mass), 12326 (accurate mass), and 09406 (mass accuracy). Definitions and entry identities were verified through indexed official-page text or the official entry PDF excerpt. Several direct page opens returned 403, so this is a content verification rather than a successful live-link availability check for every endpoint.
5. IUPAC Gold Book archived entry R05318, https://www.old.goldbook.iupac.org/html/R/R05318.html. Indexed official text explicitly defines FWHM and the 10% valley criterion. It is labeled archived in the bibliography and paired with the 2013 recommendations rather than used to assert one universal naming convention.
6. JCGM VIM3 entries 2.13 (accuracy), 2.15 (precision), and 2.16 (error), https://jcgm.bipm.org/vim/en/. Their official entry text was retrieved. These support the careful separation of the three concepts.
7. NIST Atomic Weights and Isotopic Compositions: individual C, H, O, and Na tables were opened and read. They supply the numerical isotope masses, not assumptions about the dominant ion in a real sample. C, H, O, and Na examples use explicitly identified isotopes.
8. NIST CODATA 2022 complete constants table, https://physics.nist.gov/cuu/Constants/Table/allascii.txt, was opened and read. Electron mass in u: 0.0005485799090441; the adduct example uses 0.000548579909. Existing repository keys `carbon` and `codata` are retained.

## Decisions that matter for review

- m/z follows the 2013 definition using ion mass relative to the unified atomic mass unit, divided by charge magnitude. The older Gold Book M03752 “mass number” wording is not used to teach decimal exact-mass calculations. The physical ratio in kg/C is distinguished from the dimensionless spectral coordinate. The algebra uses x as a coordinate variable.
- Charge magnitude inferred from carbon-isotope spacing is conditional on correct grouping. The spacing does not supply polarity, adduct composition, or identity.
- Adduct calculations use the sodium-cation mass, not the sodium-atom mass. Binding-energy mass corrections are explicitly omitted at the stated teaching precision. Proton removal is distinguished from attachment when M denotes a neutral molecule.
- Monoisotopic mass uses the most abundant isotope of each element; it is not generally the lightest-isotope composition, the isotope-weighted average, or the most intense peak. The heavy-water example has a calculated exact mass but does not redefine the conventional monoisotopic composition of ordinary water.
- Mass accuracy has genuinely different usage across authoritative glossaries. VIM3 is qualitative; the IUPAC surface-analysis entry 09406 defines a numerical difference. The draft states its convention and acknowledges the other, rather than claiming that all published ppm “accuracy” wording is simply wrong.
- A signed ppm result is conditional on a valid reference for the same ion form, charge, and isotope composition. One result is not an instrument performance bound, a precision estimate, or a statement of measurement uncertainty.
- FWHM resolving power is a peak-width metric. A width equal to a two-peak spacing does not guarantee baseline separation. A centroid stick's rendered width is not a profile measurement.

## Scope of verification

Arithmetic, source-definition alignment, matched translations, reference keys, and existing internal link targets were checked. Independent expert review and final integrated-site browser validation remain appropriate before publication. Gold Book endpoint accessibility can vary; an eventual external-link checker should distinguish access blocking from an invalid citation.
