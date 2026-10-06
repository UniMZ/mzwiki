# Content batch 01: charge, isotopes, and measurement quality

Prepared on 2026-10-06 against main commit `2274495d0194d97ce721e92f482f327481d8a803`. This is one review batch; it does not create a publication schedule or deployment workflow.

## Reader-facing changes

Three existing guides are expanded without adding overlapping articles or changing their URLs:

- **m/z, charge & isotopes:** defined ion-mass variables, protonation/deprotonation calculations, proton versus neutral-hydrogen mass, charge inference, binomial carbon-isotope distributions, probability versus relative intensity, isotope fine structure, and common misconceptions.
- **Mass analyzers & resolution:** FWHM conventions, resolving power versus signed mass error and precision, narrow-but-offset versus broad-but-centered examples, and ppm matching windows.
- **Read a spectrum step by step:** an annotated Gaussian simulation and numeric table connect charge inference, isotope ratios, neutral-mass recovery, resolving power, and mass error. The simulation is explicitly distinguished from measured data in the prose, figure, alt text, and model inputs.

Each change has a matched Chinese article translation. Section IDs, decimal-valued examples, references, prerequisites, and cross-links are aligned. Interface and repository documentation remain English.

## Source checks

The new calculation inputs were checked directly against official public NIST resources:

- [CODATA constants table](https://physics.nist.gov/cuu/Constants/Table/allascii.txt): proton mass 1.0072764665789 u, rounded to 1.007276467 Da for the exercises; electron mass checked to explain the difference from neutral hydrogen.
- [Carbon isotope data](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=C): carbon-12 mass 12 Da; carbon-13 mass 13.00335483507 Da; representative carbon-13 fraction 0.0107. Abundance variation is explicitly acknowledged.
- [Hydrogen isotope data](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=H): neutral hydrogen-1 mass 1.00782503223 Da.
- [Waters official measurement primer](https://www.waters.com/nextgen/us/en/education/primers/the-mass-spectrometry-primer/mass-accuracy-and-resolution.html): calibration, interference, repeat measurements, and conditions for evaluating accuracy. Historical performance claims and a unit typo in its worked example were not adopted.

The existing [IUPAC recommendations](https://doi.org/10.1351/PAC-REC-06-04-06) remain the terminology citation. The official publication destination was inaccessible to the research browser; the IUPAC document hosted by MSACL was consulted for its m/z and peak-width/resolving-power entries. This was a source-access limitation, not evidence that the publisher's URL is broken.

The binomial derivation, constructed numerical comparisons, and plots are original educational calculations. No reference spectrum, private data, or third-party figure was imported.

## Reproduction and validation

- `python3 scripts/build.py`: deterministic generation of 20 HTML pages and 16 search records.
- `python3 scripts/check.py`: 769 local link, asset, and fragment checks; all eight EN/ZH pairs; 13 bibliography entries.
- `python3 scripts/check_science.py`: independent Decimal calculations and a probability recurrence verify ion masses, isotope probabilities and ratios, plotted coordinates, mass recovery, ppm errors, tolerance widths, Gaussian half-height behavior, and EN/ZH decimal parity.
- `scripts/browser_check.py`: 64 passing scenarios covering desktop/mobile navigation and search checks, paired section switching, table/figure containment, image loading and alt text, keyboard access, and no-JavaScript reading.
- English mobile and Chinese desktop figure screenshots were visually inspected; all enriched h2/h3 section IDs and their order match across languages.
- Original figure source: `scripts/render_spectrum.py`; documented model: `content/examples/charge-isotope-spectrum.json`; committed outputs: `assets/teaching-spectrum.svg` and `.png`.

## Scientific review follow-up

An independent read-only scientific review of the initial batch reported no blocking calculation errors or English/Chinese mismatch. Two wording fixes were applied in both languages: monoisotopic mass is distinguished from an arbitrary isotopologue's exact mass, and the M+2 example explicitly uses one oxygen-18 replacing oxygen-16. The definitions were checked against the IUPAC recommendations and the oxygen example against NIST's oxygen isotope table. Direct access to the requested Gold Book pages returned HTTP 403; the IUPAC document provided the definition check.

Final preparation also regenerated the website and teaching figure from their sources with no differences from the committed outputs. GitHub reported no PR comments or review threads; scientific review in the task context should not be confused with a submitted GitHub approval. No PR-head CI checks were reported, so validation evidence here and in the PR description is local.

## Limitations for review

The simulated neutral mass and carbon count are abstract inputs, not an assigned formula. Only carbon isotopes vary; response factors and widths are equal; no interference, noise, saturation, or baseline is modeled. Agreement with the model is expected by construction and cannot independently validate chemical identity. Constant coordinate offset is an illustrative calibration error, not a universal instrument model.

Automated checks establish arithmetic, structure, and browser behavior, not independent expert review of scientific prose or translation. The figure is an educational model, not an instrument qualification standard.
