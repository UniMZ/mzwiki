# Packet QA

## Completed

- Read actual `content/articles.json`, `content/terms.json`, `content/references.json` and the existing general PTM article from the pinned main commit
- Confirmed 20 Guides/44 terms and no collision for any of the nine new slugs
- Reused exact metadata schemas; kept English interface fields and separate Chinese article metadata
- Checked all 18 new reference keys and URLs against the existing registry; no collisions
- Verified three complete Guide pairs and six complete term pairs, with requested English word ranges
- Parsed balanced HTML fragments; rejected document wrappers, scripts and styles
- Matched EN/ZH tag structures, IDs, citation sequences, numeric sequences and language-normalized links
- Resolved every internal route against actual baseline or packet metadata and every linked section against packet fragments
- Checked prerequisite graph for cycles and related metadata for missing routes
- Confirmed every new term is linked by a new Guide and links back to a new Guide
- Verified all 14 original arithmetic and logic fixtures under their explicit assumptions
- Reviewed the text for separation of identity/localization/quantity, glycan composition/structure, and XL-MS evidence/FDR levels
- An independent scientific read found no high-impact corrections; its suggested clarification was adopted: pGlyco 2.0 component error controls are explicitly identified at the GPSM reporting unit, with unique-entity aggregation kept separate

`review/validate_packet.py` reproduces the packet-only checks. Its result is saved in `validation-results.json`. It is preparation tooling, not production repository code.

## Deliberate limits

No repository changes, coding task, commit, push, build, deployment, browser session, generated-page check or live-site check was performed. The output is a research/writing package. Automated language pairing checks do not independently prove translation accuracy; the Chinese text is a full editorial translation with the same scientific qualifications.

Source inspection used public publisher, PubMed/PMC, standards and author-hosted material. Where direct HTML access failed or showed a browser check, only public indexed primary text and accessible primary/official records were used. No CAPTCHA, login or private-library access was attempted.

## Integration checks still required

1. Re-read current main and reconcile all slugs, keys, links and metadata with intervening changes
2. Copy only complete fragments and additive payloads; leave existing articles untouched
3. Integrate or adapt the scientific fixture checks, then run the repository's full existing test suite and production build
4. Inspect generated English/Chinese routes, anchors, reference lists, language switching, terminology backlinks, search and sitemap
5. Verify Guide count/navigation rather than assuming any count label is dynamic
6. Review long article layout, mobile reading, keyboard navigation and accessibility
7. Publish only under the applicable authorization and verify the resulting live pages separately
