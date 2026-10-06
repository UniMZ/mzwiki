# Structural and specialized proteomics learning expansion

Content-only packet prepared against UniMZ/mzwiki main commit `ecca2688d1c33ce5485e8497b6c3e8f498376cb3` on 2026-10-06. The inspected baseline contains 20 Guides and 44 terms. This packet is not applied, built, deployed, or live-site verified.

## Deliverables

- Three complete English/Chinese Guide pairs: crosslinking MS principles; glycoproteomics evidence and ambiguity; phosphoproteomics enrichment, localization and quantification
- Six complete term pairs: crosslinked peptide; crosslink-spectrum match; glycopeptide; glycoform; phosphosite; site occupancy
- Eighteen complete HTML source fragments
- Exact additive article and term metadata, 18 new `struct-` reference objects and three reused reference objects
- Fourteen original synthetic logic/arithmetic fixtures with assumptions and links to the relevant sections
- Source boundaries, application manifest and packet validation record

The existing general PTM Guide and site-localization term are linked rather than duplicated. Site occupancy is used instead of a separate localization-probability term because the existing site-localization entry already addresses that distinction.

Guide lengths are 876, 986 and 902 English words; terms are 166–186 English words. Every Chinese fragment translates all sections, examples, qualifications, citations and practice answers. The paired structure, anchors, citations, numeric sequences and normalized internal links pass automated parity checks. Translation meaning has also been reviewed in context; mechanical parity alone is not a translation-quality certificate.

## Scientific boundaries

Crosslinking distinguishes CSMs, peptide pairs, residue pairs, protein pairs and conditional structural restraints. Glycoproteomics distinguishes peptide identity, glycan composition, attachment position, glycan structure and whole-protein glycoform claims. Phosphoproteomics distinguishes enrichment composition from recovery, identification from localization, and phosphopeptide signal from relative or absolute occupancy. Constructed examples are explicitly synthetic and are not truth benchmarks or empirical method comparisons.

Only public primary research and official/community standards are used. The updated MIRAGE guideline is cited with its online 2025 and issue 2026 dates correctly distinguished. See `SOURCE-BOUNDARIES.md` for source-specific limits and access qualifications.

## Later application

Use `application-manifest.json` to add the fragments and narrowly merge metadata. Reconcile current main and any other packets before doing so. Applied alone to the pinned baseline, this packet would produce 23 Guides and 50 terms; this is not a claim about the live site or combined future packages.

The fixtures are a proposal for later test integration, not a claim that the existing build consumes them. A separately authorized integration must run the repository build and all checks, inspect generated pages, routes, language switching, references, search and navigation, and perform desktop/mobile reading checks before publishing.

Do not copy `inspection/` snapshots or `review/` preparation tools into the production repository.
