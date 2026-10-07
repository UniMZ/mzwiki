# Detector and signal learning expansion

Content-only packet for UniMZ/mzwiki, prepared against verified main commit `31364d9d936eaf28c4a4e932026398101b645900` on 2026-10-07. The baseline contains 28 Guides and 60 terms. No repository files were changed, no Codex or cloud coding task was created, and nothing was built or published.

## Deliverables

- Two new complete English/Chinese Guide pairs: **Ion detection & signal formation** (951 English words) and **Profile, centroid & signal processing** (963 English words)
- Six new complete term pairs: detector, electron multiplier, image current, profile spectrum, centroid spectrum, and signal-to-noise ratio (174–184 English words each)
- Sixteen exact HTML fragments, additive article and term objects, thirteen new `signal-` references, and one unchanged reused reference
- Twelve independently checked synthetic teaching fixtures
- A separate English topic proposal, **Instruments & signal**, for all six terms, coordinated with the terminology-taxonomy work
- An application manifest, source boundaries, QA record, and packet-level validation results

The current term schema has no topic field. The topic proposal is intentionally separate from `metadata/terms.additions.json`; this packet implements no navigation, topic index, A–Z index, or functional code. The later authorized integration must reconcile the final topic mapping with the separate taxonomy deliverable.

## New teaching value

The detector Guide expands the chain from ion behavior to recorded intensity: direct charge collection, secondary-electron multiplication, analog versus pulse-counting readout, recovery/dead-time limitations, induced-current detection, coherence, clipping, and explicitly conditional counting statistics.

The processing Guide moves beyond the existing short representation overview. It compares weighted positions with peak maxima, distinguishes sampled sums from integrals, demonstrates baseline and smoothing effects, defines two different S/N denominators on the same residuals, and separates peak picking from feature finding and deconvolution.

The existing analyzer Guide's field equations, transient-grid examples, and resolving-power calculations are not duplicated. The existing data-analysis Guide's identification, FDR, normalization, missingness, and study-design lessons remain in their current articles. Necessary definitions are briefly reintroduced with links before the new reasoning.

## Scientific limits

Current, accepted-event counts, arbitrary intensity, and Fourier amplitude are not interchangeable. All numerical examples are constructed and carry explicit assumptions; none represents an experimental benchmark, operating recommendation, or validated detection/quantification limit. No universal S/N threshold or instrument ranking is proposed.

Chinese fragments translate every section, example, qualification, reference, and practice answer. The automated checks verify anchors, code, numeric sequences, citation order, and normalized links across languages. The translations were also reviewed in context; mechanical parity alone does not establish scientific equivalence.

## Later application

Use `application-manifest.json` for narrow integration after rereading current main. Applied alone to the pinned baseline, the packet would produce **30 Guides and 66 terms**. These are hypothetical post-application counts, not a live-site claim or a combined expansion total.

The fixtures are a proposed payload. No current repository checker is claimed to consume them. Later engineering must adapt fixture integration, run all existing checks, generate pages, and inspect routes, references, search, language switching, reciprocal links, accessibility, and narrow-screen readability before publication.

The `inspection/` snapshots and `review/` preparation/validation scripts are packet-only evidence. They are not production source replacements or functional site code.
