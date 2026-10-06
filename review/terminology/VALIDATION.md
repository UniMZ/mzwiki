# Draft validation

Completed on 2026-10-06 against the inspected `main` revision `a9884e2da080667389c60c66d44ce4db72d4b0e5`.

## Passed

- Seven English and seven Chinese source fragments exist and parse as balanced XML-compatible HTML fragments
- Each pair has identical section IDs: definition, example, confusion, guides
- Every inline reference key exists, appears in that term's metadata, and has the correct displayed reference number
- Each metadata reference is actually cited in both translations
- Every related-term slug belongs to this seven-entry batch
- Every direct Guide link targets an existing Guide section verified through the GitHub connector in the corresponding language
- English fragments contain no Chinese article text
- Each translation pair has matching numerical-token counts and identical code-formatted equations; Chinese sentence order is allowed to differ
- Independent decimal arithmetic confirms m/z division, carbon-isotope differences, sodium-cation correction, both water masses, +4 ppm error, and R = 40,000
- Both languages explicitly identify constructed examples and retain the relevant qualifications

`validation-results.json` records per-entry counts. `numerical-examples.json` records independently computed values. The displayed six-decimal values all round correctly.

## Not yet performed

- Repository build, site link checker, science checks, or browser tests, because this assignment produced drafts without implementing the Terminology collection
- Integrated desktop/mobile review, no-JavaScript navigation, search filtering, language-switch anchor retention, or generated sitemap verification
- Independent external expert review of the final assembled site
- Successful direct access to every Gold Book or IUPAC PDF URL; some official endpoints returned access-block responses, although their indexed official definitions were readable

The later engineering batch should run the existing build and all applicable checks, add term-specific coverage, and verify the generated pages before any publication claim.
