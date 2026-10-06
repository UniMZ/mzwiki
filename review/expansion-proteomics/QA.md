# Packet quality review

Status: passed local content-packet checks on 2026-10-06. No repository or deployment action was performed.

## Completed checks

- Pinned baseline inventory: eight Guides and 20 terms; all three Guide slugs and six terminology slugs are new
- Three English Guides at 1,020, 1,037 and 1,017 words; six English terms at 185–206 words
- Eighteen balanced HTML fragments with no outer document shell, embedded scripts or styles
- Matched English/Chinese tag structures, section identifiers, reference labels, numeric sequences and language-adjusted internal links
- Every citation resolves to its ordered metadata key; all 20 new reference keys are prefixed `prot-`, with no pinned-baseline key collisions
- Existing `fdr` and `etd` references reused rather than duplicated
- Metadata conforms to the existing Guide/term schema; only translated title/summary values contain Chinese
- All related links and prerequisites resolve to the pinned baseline or this packet; prerequisite graph is acyclic
- Every linked fragment anchor exists in the inspected baseline or completed package content
- All twelve constructed arithmetic and logic fixtures passed the local verifier

## Scientific review

The prose consistently separates peptide-spectrum matches, distinct peptide sequences, modified forms, protein groups, localization and quantity. Shared peptides never establish uniquely identified parents by repetition alone. Protein-group representatives are reporting labels. The known-truth error examples illustrate denominators and do not pretend to estimate FDR from real data. Sequence coverage uses an interval union. The positional fragment example declares one phosphate, only S2/S3 candidate sites, +1 b/y products and retention of the modification. Occupancy examples distinguish protein amount and modified amount from response and absolute occupancy.

Preparation and enrichment sources are used as examples and evidence of tradeoffs, with no universal method ranking. Standards are cited for representations and reporting, not as proof of validity or assertions about newest releases. Unimod accession 35 has a record-level Verified field of No, disclosed in its metadata and source boundary; its use is limited to possible modification classifications.

Chinese counterparts were reviewed for full section, example, assumption and qualification alignment. Matching tag/numeric checks support that review but do not replace scientific translation judgment.

## Reproduce package checks

Run `python3 review/validate_packet.py` from any working directory in the same workspace, or adjust the script's package-root path after moving it. This is a local review utility, not a proposed production-repository script. See `validation-results.json` for the exact checked inventory and counts.

## Remaining later-integration checks

The production build, repository scientific tests, generated search and sitemap, reciprocal UI links, browser layout, keyboard access, language switching and live publication were not run. This packet deliberately does not claim those outcomes. A later authorized integration must reconcile current main, merge additive metadata, integrate the proposed fixture schema, rebuild, run every existing check, and inspect the rendered English/Chinese pages.
