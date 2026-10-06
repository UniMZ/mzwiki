# Quantification, experimental design, and QC content packet

This is a content-only addition packet for UniMZ/mzwiki, inspected at commit `41af17b09a188ed7c884fcb99cfcea4efd1ef2a5`. No repository, branch, pull request, deployment, or generated site file was modified.

## Deliverable

- 3 new English Guides with full matched Chinese articles: `quantitative-calibration`, `experimental-design`, `qc-normalization`
- 6 new paired terms: `calibration-curve`, `internal-standard`, `limit-of-detection`, `limit-of-quantification`, `biological-replicate`, `batch-effect`
- Exact metadata arrays in `metadata/articles.additions.json` and `metadata/terms.additions.json`
- 12 collision-free new references, each prefixed `quant-`, and 5 exact reused reference records
- 13 numeric teaching fixtures, scientific/source boundaries, application manifest, and local validation report

English Guide word counts are 915, 1,050, and 1,110. Term entries are 201–211 English words. Chinese articles preserve every section, example, citation, qualification, and internal destination. UI and generated navigation remain under the existing English-first builder.

## Application

Use `application-manifest.json` as the source of truth. Copy the 18 fragments and fixture to their matching repository-relative paths. Append the article and term arrays after checking current-main slug collisions; do not replace either full metadata collection. Merge the new reference dictionary into `content/references.json`; do not replace the full dictionary or duplicate reused keys. Reconcile any intervening upstream changes before applying. The ordered Guide additions establish their own prerequisite sequence.

The packet links only to topics present at the inspected baseline or created within this packet. It does not depend on unseen parallel content. No existing Guide or term replacement is requested. Existing FDR, missing-value, and mass-accuracy topics are linked.

Copy the content-batch note only if keeping these audit notes in the repository is desired. `inspection/`, this README, source boundaries, and local reports are review aids; they are not web content.

## Validation

Run `python3 inspection/validate_packet.py` from any directory. It validates fragment syntax, metadata/ref boundaries, language parity, word ranges, internal destinations, and numerical fixtures. `validation-results.json` records a pass.

The integration owner still needs to merge all concurrent additions, run the full repository build, structural/scientific checks, search checks, and desktop/mobile browser checks. Local content validation is not scientific peer review, assay validation, or proof of rendered-site behavior.
