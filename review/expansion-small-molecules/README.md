# Small-molecule evidence expansion

Content-only packet for UniMZ/mzwiki, inspected at commit `41af17b09a188ed7c884fcb99cfcea4efd1ef2a5` on 2026-10-06. No repository or published-site changes were made.

## Deliverables

- Three new complete English/Chinese Guide pairs: small-molecule annotation, lipid structural evidence, and ion mobility/CCS
- Six new complete English/Chinese term pairs: molecular formula, isomer, spectral library, lipid shorthand notation, ion mobility, and collision cross section
- Exact additions arrays for `articles.json` and `terms.json`; 20 collision-free `small-` reference additions; unchanged reused references recorded separately
- Original constructed examples and a proposed scientific fixture
- Explicit source boundaries, application manifest, and packet-only validation results

Guide bodies are approximately 990 English words each. Terms are 197–210 words. Corresponding Chinese articles include the same examples, qualifications, section IDs, and citation sequences. No term duplicates existing adduct or isotopologue entries.

Use `application-manifest.json` for file and metadata operations. Do not copy the `inspection/` baseline snapshots into the repository. These fragments intentionally contain only article bodies; the existing builder supplies the English interface and references.

The new Guide-count UI copy, generated output, complete repository tests, and desktop/mobile checks remain future integration work. No integration or publication is claimed by this packet.
