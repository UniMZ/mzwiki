# Terminology browsing and detector/signal integration

Prepared 2026-10-07. Authored source and taxonomy: `bd0a3046fb599653bdc154c654d9c127eeaa36d0`. Baseline main: `31364d9d936eaf28c4a4e932026398101b645900`.

## Reader-facing behavior

The terminology directory defaults to **By topic** at `/terms/`. **A–Z** at `/terms/az/` lists every term alphabetically. Clearly labeled native links with `aria-current="page"` select the current view. Each view has a stable shareable URL, so refresh, Back/Forward and JavaScript-disabled browsing work without a separate client-side state store.

Both directories derive from the same term metadata. All 66 terms occur exactly once in each view. Topic order and membership use the supplied, unchanged `content/term-topics.json`: 11 ordered topics. Within topics and in A–Z, canonical English titles sort case-insensitively with natural numeric ordering and a stable slug tie-break. Article sidebar/mobile navigation uses the same topics and exposes both directory links.

Compact text lists replace large summary cards. Desktop uses three columns, intermediate widths two, and narrow screens one. Links retain at least 44px click height, visible keyboard focus, and wrapping for long titles. Existing article typography and spacing are unchanged. The `az` directory slug is reserved; article and EN/ZH translation routes are preserved.

## Content and integrity

Two new Guide pairs and six term pairs cover detector/readout and profile/centroid/noise reasoning. The collection now has 30 Guides, 66 terms, 206 reference records, 198 generated HTML pages (including both terminology directories) and 192 article search records.

All sixteen new article fragments and the supplied fixture file match the 17 packet hashes. All 176 existing article fragments, the template, existing metadata/order and the supplied taxonomy remain unchanged. No independent research or scientific prose/fixture rewriting was performed. Source-access boundaries remain in `review/expansion-signal/SOURCE-BOUNDARIES.md`.

## Checks

- All prior structural/scientific suites pass, including the 43-fixture broad expansion and 39-fixture advanced expansion suites
- `check_signal.py`: twelve cases pass (eleven numerical computations and one semantic guard), with source hashes, bilingual code/numeric/citation/anchor parity and generated-body checks
- `check_terminology.py`: eleven editorial topics, complete single-occurrence inventories in both views, ordering and stable current-view links pass
- Structural checks pass 44,613 local links/assets/fragments, 96 language pairs, 192 search records, all references/sitemap routes and acyclic prerequisites
- Chromium passes 2,263 scenarios with no script errors: desktop/390px/320px, repeated switching, Back/Forward, refresh, direct URLs, both JavaScript states, all entries visible, keyboard focus order, topic anchors, article return navigation, matching sidebar topics, search, long titles, tables and same-article language switches
- Desktop and mobile screenshots of both modes inspected; compact layout remains legible, with no horizontal overflow
- Repeated build produces identical hashes; `git diff --check` passes

Two test adaptations preserve accuracy: the old “Instruments” selector is now scoped to Guide groups, and the old Chinese ordinal normalization is restricted to the spectral-library term so it cannot alter unrelated electron-multiplier prose during comparison. Neither changes authored content.

These are local consistency and interaction checks, not validation of experimental data. Domain, security and hosting configuration are unchanged. Merge, Pages deployment and live-site verification follow separately.
