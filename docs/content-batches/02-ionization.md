# Ionization and ion forms

This batch applies the finalized paired article text and reference mapping. It expands the existing ionization guide without adding another guide. All seven original section anchors remain available; the new sections cover MALDI, ion forms, mass recovery, and misconceptions. Existing article titles, summaries, prerequisites, related-guide metadata, bibliography entries, and domain configuration are preserved.

## Evidence and scope

The supplied source-verification record, dated October 6, 2026, maps thirteen references to claims. IUPAC supports terminology; Fenn supports biomolecular ESI charge-state sequences; the cited ESI and MALDI reviews describe qualified mechanism models; the Trimpin and Leite experiments support specialized multiple charging and adduct/interference examples; King supports the bounded suppression discussion. NIST provides the mass constants and separate library families.

Verification used publisher, author, IUPAC, NIST, and PubMed metadata or abstracts. Some relevant passages were available only through indexed text. Direct IUPAC PDF and some publisher retrievals were blocked; not every full text was downloaded. These are the supplied editorial evidence boundaries, not a claim of a new literature review during implementation. Per-reference notes remain in the shared bibliography.

The nine numerical examples are constructed mass-accounting exercises, not measured peaks or a molecular formula. Their constants, assumptions, predictions, inversions, and derived differences are retained in `tests/fixtures/ionization.json`.

## Reproduce engineering checks

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 scripts/check_science.py
python3 scripts/check_ionization.py
```

Run `scripts/browser_check.py` against a local server as described in the README. It checks both languages and viewport widths, all three new disclosures, search, language switching at the new anchors, horizontal table scrolling, and reading with JavaScript disabled. The no-JavaScript context uses the browser's reduced-motion preference to avoid smooth-scroll instability during automated clicks.

Automated checks validate arithmetic, structural parity, rendered output, and behavior. They do not independently establish scientific correctness or translation equivalence. This batch is submitted for review; it does not merge or deploy changes.
