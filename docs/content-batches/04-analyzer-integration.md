# Analyzer principles integration

Regenerates the existing static pipeline for the supplied analyzer Guide expansion and the Mass analyzer and Transient terminology entries. Content and metadata were supplied at commit `9b72e4f7ca7cc30179d3c70a1f4ab308a31f0173`, based on main `9866af0db25c5740fea30ad85cf21e4bcba0f0d6`. The six article fragments, metadata and bibliography remain unchanged during engineering integration. No framework or domain change is included.

`python3 scripts/check_analyzers.py` adapts all ten supplied arithmetic cases: equal coordinates at different charges, TOF time scaling, ideal Orbitrap and ICR frequency scaling, real transient duration, and zero-padded Fourier grid spacing. It also checks paired numerical tokens, equations, citations, markup and preserved Guide anchors. Existing scientific and terminology checks remain applicable.

The browser suite now derives collection counts from metadata and covers new analyzer anchors, reciprocal Guide/term links, search results, disclosures, and desktop/mobile equation/table layout. The source-verification limitations and model assumptions remain in `review/analyzers/SOURCE-BOUNDARIES.md` and the fixture. These tests do not constitute independent scientific review, remote CI success, or deployment verification.

Run the build, `check.py`, `check_science.py`, `check_ionization.py`, `check_terms.py`, `check_analyzers.py`, and the browser suite before submitting changes. Commit generated pages, search index and sitemap with source changes. This engineering batch leaves merging and deployment verification to the parent task.
