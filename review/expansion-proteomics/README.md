# Proteomics learning expansion

Prepared against UniMZ/mzwiki main commit `41af17b09a188ed7c884fcb99cfcea4efd1ef2a5` on 2026-10-06. This is a content-only packet, ready for later integration review. It has not been applied to the repository, built, deployed, or verified on the live website.

## Additions

- Three new Guide pairs: bottom-up workflow; peptide identification and protein inference; PTM analysis and site localization
- Six new term pairs: peptide-spectrum match; protein inference; proteotypic peptide; post-translational modification; site localization; sequence coverage
- Eighteen complete English/Chinese source fragments
- Exact additive metadata using the existing schema, 20 new `prot-` reference keys, and two reused existing references
- Twelve original arithmetic or logic fixtures, with assumptions and limits

Each English Guide is 800–1,200 words. Each English term is 150–250 words. Chinese articles translate all sections, examples, qualifications, references and practice answers, with matching anchors. Existing public routes or content within this packet are the only link targets.

The inspected baseline has eight Guides and 20 terms. All nine proposed slugs are absent from that baseline. This packet alone would add three Guides and six terms; any combined expansion count must include the other packets separately.

## Teaching boundaries

The workflow Guide covers preparation and the evidence chain, rather than repeating the existing acquisition chapter. Identification separates search scores, PSM confidence, peptide/protein error levels, shared-peptide ambiguity, grouping and coverage. PTM analysis separates chemical assignment, localization and occupancy. Examples are constructed, not experimental results. No method is presented as universally best, and no list of disease markers is included.

Read `SOURCE-BOUNDARIES.md` for precisely what the sources support. Read `QA.md` and `validation-results.json` for the completed packet checks and their limits.

## Later application

Use `application-manifest.json`. Add the complete fragments and merge only the supplied metadata objects. Keep terminology separate from the numbered Guide array. Reconcile current main and other packets before merging. The fixture JSON is a proposal for later test integration, not a claim that the existing build consumes it.

Do not copy `inspection/` snapshots or `review/` preparation tooling into the production repository. A later authorized engineering task must run the repository build and checks, inspect generated routes and reading layout, and publish only within its authorization.
