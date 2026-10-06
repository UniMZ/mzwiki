# Source and claim boundaries

Research date: 2026-10-06. The article text is original teaching prose with a matched Chinese version, not a translation or reproduction of a source report. No published spectra or figures are reproduced.

## IUPAC definitions and MS/MS sequence

Existing reference `iupac`: Murray et al. (2013), DOI https://doi.org/10.1351/PAC-REC-06-04-06. Official publication metadata: https://publications.iupac.org/pac/85/7/1515/index.html.

The official-host PDF returned HTTP 403 in this research session. The IUPAC advance-publication PDF mirrored by MSACL was readable and searched in full: https://www.msacl.org/documents/cms_guidance/Mass_Spectrometry_Definitions_and_Terms_IUPAC_2013.pdf. It has 95 pages and advance-publication pagination, so term numbers are the stable locators used here: 407 precursor ion, 412 product ion, 192 fragment ion, 363 neutral loss, 89 collision-induced dissociation, and 50/79/551/552 b/c/y/z ions.

The precursor and product definitions are reaction-relative. Product ion includes reactions changing charge and is broader than fragment ion. MS/MS can separate its operations in time or space. The Guide explicitly presents one common product-ion experiment, rather than claiming all tandem-MS scans follow the same acquisition logic.

Gold Book precursor P04807 and product P04864 give older synonym-only descriptions. They were not substituted for the substantive 2013 definitions.

New `neutral-loss-definition`: https://goldbook.iupac.org/terms/view/12505. The current indexed entry gives the 2013 definition and final-paper page 1571. Direct retrieval was intermittent; the indexed official entry and full IUPAC mirror agree. The page supports the definition. Multiplication by charge magnitude is the Guide's explicitly derived bookkeeping, not an empirical measurement from IUPAC.

## Collision-based activation

New `hcd-primary`: McAlister et al. (2011), https://pubmed.ncbi.nlm.nih.gov/21393638/, DOI https://doi.org/10.1074/mcp.O111.009456.

The PubMed-indexed abstract was inspected. Direct PubMed opening sometimes returned only a footer, while search retrieval exposed the abstract and metadata. Its explicit distinction between beam-type HCD and resonant-excitation collisional activation supports the method classification. The article does not transfer the source's comparative identification rates, reporter-ion improvements, hardware assertions, or energy settings to other instruments. No full-paper inspection is claimed for this source.

Olsen et al. (2007), https://pubmed.ncbi.nlm.nih.gov/17721543/, DOI 10.1038/nmeth1060, was checked as historical background but is not added as a redundant reference. Its subscription-limited main text was not used for detailed claims.

## ECD, ETD, and intact charge-reduced products

New `ecd-primary`: Zubarev, Kelleher & McLafferty (1998), DOI https://doi.org/10.1021/ja973478k. Full primary paper inspected at the institutional copy https://masspec.scripps.edu/learn/ms/pdf/1998_ZubarevRA.pdf.

Existing `etd`: Syka et al. (2004), DOI https://doi.org/10.1073/pnas.0402700101. Full primary paper inspected at https://masspec.scripps.edu/learn/ms/pdf/2004_Syka.pdf; verified metadata https://pubmed.ncbi.nlm.nih.gov/15210983/.

These papers support electron gain, loss of one unit of positive charge, common peptide c/z-type products, intact charge-reduced products, and the distinction between free-electron capture and electron delivery by a reagent anion. The Guide leaves the hydrogen count unchanged on immediate electron capture/transfer. It includes incoming electrons/reagent ions in charge bookkeeping and does not equate electron gain with proton loss.

The discussion is deliberately scoped to common positive-ion ECD/ETD peptide/protein applications. It does not claim that all analytes behave this way, that only c/z products occur, or that every labile modification survives. The detailed mechanistic/nonergodic interpretation in the ECD paper is not treated as a universally settled mechanism. Electron ionization is linked separately.

New `etd-supplemental`: Swaney et al. (2007), https://pubmed.ncbi.nlm.nih.gov/17222010/, DOI https://doi.org/10.1021/ac061457f. The accessible PubMed-indexed abstract was inspected. It directly treats doubly protonated precursors, charge-reduced products, and supplemental activation. It supports the existence of ETnoD and the statement that 2+ is not an absolute exclusion. It does not establish universal efficiency thresholds or prescribe settings.

## Peptide notation

New `peptide-nomenclature`: Chu et al. (2015), DOI https://doi.org/10.1016/j.ijms.2015.07.021.

The publisher's indexed abstract, introduction, and beginning of the discussion were available at https://www.sciencedirect.com/science/article/pii/S1387380615002249; direct opening returned 403. Author, journal, year, pages, and DOI were corroborated by the author's institution: https://hub.hku.hk/handle/10722/218701. No complete subscription-paper inspection is claimed.

Used for terminal-series/subscript conventions and for distinguishing residue count, charge, radical, and hydrogen-transfer labels. It is a nomenclature proposal discussing conventional notation; the Guide does not declare its proposed system the only accepted standard. Peptide bond definitions were independently checked in the IUPAC report and official Gold Book b-ion 12347, y-ion 12613, and c-ion 12357 entries. Method associations cite the ECD/ETD primary studies separately. The A–G–S–K sequence is a naming illustration, not a measured spectrum or a fragmentation-yield prediction.

## Atomic masses and constructed arithmetic

Reused `hydrogen`, `oxygen`, and `carbon`; new `nitrogen`. Official NIST pages were directly readable:

- https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=H
- https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=O
- https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=C
- https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=N

The calculations use tabulated central values as fixed teaching constants, without propagating their uncertainties. Values in Da: carbon-12 12, hydrogen-1 1.00782503223, nitrogen-14 14.00307400443, oxygen-16 15.99491461957. Water uses two neutral hydrogen atoms, not two protons. The alanine residue increment is C3H5NO, not free alanine. Added-ion chemistry cancels only under the stated matched-series and unchanged-charge assumptions.

The water losses, residue gaps, two-product charge partition, and isolation windows are constructed arithmetic. They are neither empirical spectra nor validated molecular formulas. The +1 and +2 rows at the same starting m/z are separate hypothetical ion cases. Conventional isotope-sum/electron bookkeeping neglects chemical binding-energy mass contributions at the illustrated precision. Electron-transfer examples balance composition and charge only, not exact mass.

## Coisolation and interpretation

New `coisolation-primary`: Yu, Deng & Nesvizhskii (2025), https://www.nature.com/articles/s41467-025-58728-z, DOI https://doi.org/10.1038/s41467-025-58728-z. Full primary article inspected.

Used only to establish that different peptides can be coisolated/cofragmented into chimeric DDA spectra, including narrow-window data. Neither its prevalence nor algorithm performance is transferred to every instrument or mixture. The Guide separates ordinary multiple ionic forms/isotope peaks from cofragmentation of different analytes; it does not call every isotope envelope a chimeric spectrum.

The rectangular isolation examples are original idealized geometry, not measured instrument profiles. Higher resolving power during product measurement does not itself assign each product to its parent precursor.

Existing `nist`: official SRD 1A overview https://www.nist.gov/srd/nist-standard-reference-database-1a was directly inspected, supporting the existence of EI and tandem reference collections. The linked official tandem project page https://www.nist.gov/programs-projects/tandem-mass-spectral-library supports condition-dependent spectra. No commercial library spectra were opened, matched, or reproduced. No current library-size numbers are needed in this durable learning material.

The checklist is cautious analysis guidance: multiple consistent observations support a hypothesis, while missing peaks, shared fragments, coisolation, candidate-space limits, and incompatible conditions prevent overclaiming. It does not turn a single neutral loss, spectrum score, or residue gap into proof of identity.
