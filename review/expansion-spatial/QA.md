# Packet QA and later integration requirements

## Completed in this content packet

- Confirmed baseline metadata inventory of 20 Guides and 44 terms and absence of all six proposed slugs
- Added exactly 2 Guide pairs, 4 term pairs and 12 balanced HTML fragments
- Checked exact metadata schemas, English-only nontranslation fields, prerequisite graph and route targets
- Checked 15 new reference keys use `spatial-`, with no key or URL collisions against pinned baseline references
- Reused `missingness-benchmark` unchanged; no broad replacement of reference objects is needed
- Checked each page's inline citation numbering against its metadata reference order
- Checked EN/ZH structure, anchors, normalized routes, citations and numeric sequence
- Checked Guide word counts (986 and 1,004) and term word counts (167–177)
- Evaluated all 12 original arithmetic/logic fixtures under their explicit assumptions
- Reviewed bilingual scientific correctness independently; incorporated the clarification that Poisson examples give relative standard deviation, not a 95% interval or ratio uncertainty
- Verified the official, term-specific CLSI limit-of-blank page directly; source link is no longer the broad terminology index

Run `python review/validate_packet.py` from any directory to repeat packet checks. The script intentionally targets this preparation packet, not the application repository.

## Must be done when integrating

1. Re-read current main and reconcile changes since the pinned baseline, including any simultaneous content packets
2. Confirm slug uniqueness and equivalence of any new reference already introduced elsewhere
3. Add full fragments and merge article/term/reference metadata narrowly; preserve existing content and prerequisite ordering
4. Reconcile navigation and any hard-coded Guide/term counts with the actual merged inventory
5. Run the repository build and every existing check; add or adapt fixture coverage rather than assuming the fixture file is automatically executed
6. Verify generated references, EN/ZH URLs, language switches, anchors, search, sitemap, related links and term backlinks
7. Inspect desktop/mobile typography, equation text, units, details/summary interaction and keyboard/accessibility behavior
8. Verify intended hosted deployment only after the separately authorized integration and publication process

## Not performed

No repository mutation, Git write, engineering task, repository build, existing test-suite run, generated-page test, browser layout check, deployment or live-site verification. Synthetic examples are neither experimental validation nor evidence for a recommended cell count, carrier ratio, instrument resolution, or analytical threshold.
