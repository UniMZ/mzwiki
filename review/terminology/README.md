# Foundational terminology batch

Seven standalone terminology entries, each with a complete English article and corresponding Chinese translation. These are editorial source drafts, not published pages. No repository files were changed.

## Contents

- `en/` and `zh/`: 14 complete HTML body fragments, compatible with the site's existing trusted-fragment approach
- `terms.proposed.json`: seven proposed metadata records, including both titles and summaries, related Guides, related terms, and ordered reference keys
- `references.additions.json`: 15 proposed bibliography additions
- `references.reused.json`: three existing reference records copied for review; reuse their existing keys rather than duplicating them
- `numerical-examples.json`: independently calculated arithmetic behind the examples
- `repository-inspection.json`: inspected repository revision and verified existing Guide anchors
- `SOURCES.md`: source verification and terminology decisions
- `VALIDATION.md`: completed checks and remaining integration checks

## Entry manifest

| Slug | English title | Example | Main distinction |
|---|---|---|---|
| mz | m/z | A 600 Da ion with charge +2 has coordinate 300 | Ion mass versus neutral mass; dimensionless coordinate |
| charge-state | Charge state | Carbon-isotope spacing of approximately 0.250839 supports charge magnitude 4 | Net charge versus molecule count or oxidation state |
| adduct-ion | Adduct ion | A hypothetical 200 Da neutral gives a sodium adduct near 222.989221 | Added ion composition versus generic peak correction |
| isotopologue | Isotopologue | Carbon-12 versus carbon-13 methane | Isotope composition versus positional isotopomers |
| monoisotopic-mass | Monoisotopic mass | Ordinary water 18.010565 Da; oxygen-18 water 20.014810 Da | Monoisotopic versus exact versus average mass |
| mass-accuracy | Mass accuracy | 250.0010 compared with 250.0000 gives +4 ppm | Accuracy, signed error, precision, and tolerance |
| resolving-power | Resolving power | FWHM 0.005 at m/z 200 gives R = 40,000 | FWHM versus two-peak separation and mass error |

Each fragment has the same four section IDs in both languages: `definition`, `example`, `confusion`, `guides`. Reference sections, page title, navigation, and related-term links are intended to be rendered from metadata by the eventual site template, as they are for current Guides.

## Minimal metadata and routing proposal

Keep the existing eight-Guide learning path intact. Put these lookup pages in a separate `content/terms.json` collection with fragments at `content/terms/en/<slug>.html` and `content/terms/zh/<slug>.html`. Generate `/terms/<slug>/` and `/zh/terms/<slug>/`; provide an English Terminology index at `/terms/`. These are proposals only; none of these routes has been created.

The proposed record fields reuse the current editorial vocabulary: `slug`, `title`, `zh_title`, `summary`, `zh_summary`, `refs`. Add `related_guides` and `related_terms` to make cross-collection relationships unambiguous. Collection membership already establishes content type, so there is no need to repeat `type` in every source record, add a Guide sequence number, or create artificial prerequisites.

At build time, add `kind: "term"` or `kind: "guide"` to search records so results can distinguish the two formats. Add a separate Terminology link or section rather than inserting the terms into the numbered Guide list. Keep interface labels and project documentation English; Chinese appears only in matched article views and their corresponding title/summary metadata. Preserve matching anchors and EN/ZH switching.

Related-term lists deliberately refer only to terms delivered in this batch. An optional later alias field could support searches such as “mass-to-charge ratio,” “FWHM,” or “ppm error,” but aliases are not necessary for the minimal first implementation.

## Integration boundaries

The current builder assumes all articles use `/guides/`, derives numbering from the Guide array, and renders Guide-specific labels. Adding these records directly to `content/articles.json` would misclassify them. A single later engineering batch should extend collection handling, navigation, search, sitemap, language switching, and link checks together.

The content is intentionally narrower than the Guides: one definition, one compact example, one set of distinctions, and links into the longer lessons. Probability derivations, analyzer comparisons, ionization mechanisms, and multi-step spectrum interpretation stay in the Guides.
