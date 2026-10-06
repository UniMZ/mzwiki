# Content-packet QA

Status: PASS for the bounded checks below. This is not a repository-build or deployment result.

## Completed

- Inspected acquisition EN/ZH, all twelve term metadata records, the bibliography, article metadata, README, and contribution rules at `141264f45b3b4c02a9c99104e999a2c6caa2446d`
- Inspected linked sections in both language versions of analyzers, fragmentation, spectrum interpretation, ionization, and data analysis at that same commit
- Parsed all eight new/replacement fragments with a local HTML parser; checked balanced tags and unique IDs
- Confirmed four EN/ZH pairs have identical section IDs and numeric-token multisets, including citation and table numbers
- Preserved all six original acquisition anchors
- Checked all article-local reference keys and displayed numbers against their exact per-article metadata order, with no unused reference keys
- Checked every internal link's collection, slug, language prefix, and any target anchor against packet or baseline source
- Confirmed three new term slugs do not duplicate the twelve existing terms
- Confirmed eleven new bibliography keys do not overwrite existing keys
- Independently recalculated all sixteen fixture cases, including DIA timing, fixed budgets, DDA timing and exclusion, MRM dwell/pause budgets, isolation bounds, ppm extraction, and XIC sums
- Reviewed wording for beginner scope, real-versus-constructed distinction, no universal mode ranking, no universal points-per-peak threshold, and no confusion between MS level and cycle count

The machine-readable result is `validation-results.json`. Recheck the packet locally with `python3 inspection/validate_packet.py` from any directory; this validator is an inspection-only helper, not a repository test addition.

## Scientific guardrails

- 21 spectra per DIA cycle does not mean 21 measurements of each individual window
- Top N is an event limit, not an identification count or guaranteed per-target sampling density
- Exclusion is a selection rule, not physical removal or identification confirmation
- Isolation width, software extraction tolerance, and retention-time scheduling are distinct operations
- SRM/MRM and PRM differ in what product evidence is acquired; neither is declared universally superior
- The timing table assumes serial occupied blocks and explicit additional overhead; real parallelism and early-ended ion accumulation can invalidate naive time summation
- Narrower windows can reduce coisolation but do not prove chemical purity or preserve all desired signal
- Invented XIC signals test a specified selection/summation rule; they do not establish concentration or identity

## Not run

No repository build, current `check.py`, existing scientific-check suite, search regeneration, browser test, layout review, Pages operation, or live-site check was run. Local structure and numeric parity do not establish browser rendering, scientific completeness, or actual method performance. Those checks belong to the later authorized application pass.

## Access qualification

Some primary/official pages were available only through indexed text, while direct requests failed, returned 403/429, or showed a browser challenge. The exact boundary for each source is recorded in `SOURCE-BOUNDARIES.md`. No failure is presented as successful direct full-text access, and no access-control challenge was bypassed.
