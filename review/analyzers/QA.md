# Content-level QA

Completed 2026-10-06. This is a research and writing check, not a repository build or deployment report.

## Passed

- Six complete HTML body fragments parse with correctly nested tags and no duplicate IDs
- All 16 Guide section IDs match between English and Chinese
- All eight pre-existing Guide IDs remain present
- Both new terminology pairs use matching four-section structures
- Citation keys and displayed reference numbers match each article's ordered metadata
- Citation sequences match between paired English and Chinese fragments
- English internal links use English routes; Chinese internal links use translated article routes
- Ten numerical examples were independently recalculated from the local JSON fixture inputs and all matched expected values within 1e-12 tolerance
- TOF energy is stated per charge, and the square-root flight-time direction is correct
- Orbitrap uses axial frequency and an inverse-square-root m/z law
- ICR teaching formula is explicitly ideal, unperturbed, uniform-field, and nonrelativistic; practical reduced frequency is distinguished
- Fourier-bin spacing, peak width, and a resolution guarantee are kept separate
- Zero-padded and genuinely longer time records remain distinct
- Existing resolution and accuracy examples are retained without creating a duplicate Resolving power term
- Source, analyzer, selection, and identification remain distinct concepts
- English-primary metadata and separate Chinese article translations follow the current collection convention

## Scientific review boundaries

Source-level caveats are in SOURCE-BOUNDARIES.md. No source figure or spectrum is copied. No product performance ranking, contemporary specification, or factual numerical benchmark is added.

The physical examples are constructed and dimensionally interpreted in the text. The Fourier examples use the conventional DFT duration N/fs; the first-to-last-sample interval differs by one sampling interval.

## Still required in the application pass

- Reconcile with current main before copying these complete fragments
- Adapt the ten fixtures to the repository's existing testing approach
- Run the real build, structural checks, existing science checks, and terminology checks
- Verify generated reference lists, all cross-links, reciprocal term/Guide links, and language-switch destinations
- Verify search indexing/classification and English-only navigation/index pages
- Inspect equations, tables, and detail controls at narrow viewport widths and by keyboard
- Confirm generated artifacts and deployment separately

No browser rendering, repository build, commit, push, or publication has been performed as part of this package.
