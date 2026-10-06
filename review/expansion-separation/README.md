# Sample preparation and separation content expansion

Prepared 2026-10-06 for UniMZ/mzwiki at baseline 41af17b09a188ed7c884fcb99cfcea4efd1ef2a5.

This is an additive, content-only package: three complete English/Chinese Guide pairs and six complete terminology pairs. It contains no repository writes, implementation task, commit, generated site, or deployment.

## Apply later

Use application-manifest.json for exact destinations. Copy the 18 complete HTML fragments without adding page shells or duplicate reference sections; the existing builder supplies those. Append metadata objects rather than replacing whole collections. Merge the 13 new bibliography keys and retain the four reused references unchanged. Keep the new terms in content/terms.json, outside the numbered Guides collection.

The baseline contains eight Guides and 20 terms; applying this package alone would produce 11 Guides and 26 terms. Other expansion packages must be reconciled independently. This package links only to its own new topics and verified baseline topics.

## Review

- SOURCE-BOUNDARIES.md: source support, verification limits and exclusions
- QA.md and validation-results.json: content-level checks and remaining integration work
- tests/fixtures/separation.json: eleven constructed numerical or reasoning fixtures
- inspection/baseline: read-only source snapshots used to verify schema, uniqueness and links
- inspection/validate_packet.py: local package-only validation

Run python3 inspection/validate_packet.py from this package directory. This does not build or change the repository. The final integrator still needs the repository's build, scientific tests and browser checks.
