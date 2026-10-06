# Packet quality assurance

## Verified scope

- Pinned repository baseline inspected: `ecca2688d1c33ce5485e8497b6c3e8f498376cb3`, 20 Guides and 44 terms
- Three Guide and six term slugs are absent from the baseline; all are additive
- All internal links target that baseline or this packet, including checked anchored links
- Eighteen complete HTML fragments; no stubs, runtime code, external images, or unpublished route dependencies
- Seventeen new `comp-` references and five exact reused baseline reference objects
- Every citation key, displayed reference number, and metadata reference set agrees
- Nine language pairs preserve tag structure, section identifiers, normalized links, citations and numeric token sequence
- English lengths: 960, 1,019, and 1,023 words for Guides; 187–208 words for terms
- Thirteen synthetic fixtures: arithmetic calculations executed, assumptions and logical boundaries checked, and content anchors resolved
- Packet validator passes with no errors; run `python review/validate_packet.py` from this packet or any directory

## Scientific review

Independent scientific and bilingual review found no blocking errors or material translation mismatches across all 18 fragments, metadata, source boundaries, and 13 fixtures. Three precision improvements were incorporated in both languages: identification-level FDR is distinguished from localization-error control; D and T are explicitly defined as winners at the same cutoff and reporting level; and the precision/recall example specifies one known answer and at most one reported candidate per case. All teaching arithmetic was reviewed, and the packet validator was rerun successfully after these changes.

## Checks deliberately not claimed

This is a content-only packet. No production build, browser rendering, deployment, live-site inspection, model run, conversion test, or empirical benchmark was performed. The fixture proposal has not been integrated into the repository’s existing test runner. Mechanical bilingual parity is not a translation-quality certificate.

## Integration acceptance checklist

1. Reconcile current main and other approved packets before adding files or metadata
2. Confirm that the reference renderer supplies `ref-KEY` anchors using each item’s ordered reference list
3. Run the repository build and every existing test; integrate or adapt the synthetic fixture checks without presenting them as experimental validation
4. Confirm English and Chinese pages, titles, summaries, prerequisites, related links, references, and language-switch destinations
5. Check navigation ordering and total counts, search indexing, terminology backlinks, sitemap entries, and page-local anchors
6. Check reading at desktop/mobile widths, long citations, keyboard focus, and expandable practice answers
7. Keep inspection snapshots and preparation scripts out of production
8. Report publication only after deployment and live-page verification actually succeed
