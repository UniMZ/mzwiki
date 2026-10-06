# Contributing to mzwiki

Help readers understand mass spectrometry through clear explanations, sound examples, and traceable evidence. Contributions can correct science, improve teaching, refine translations, or improve accessibility.

## Scope

Prioritize stable concepts, principles, methods, and connections to computational analysis. Explain prerequisites before advanced details. Do not turn the wiki into a stream of recent papers or product announcements.

## Edit a guide

1. Edit `content/en/<slug>.html` and its corresponding `content/zh/<slug>.html`.
2. Keep section IDs identical across the two versions. Do not place both languages in one article view.
3. Keep navigation, metadata field names, README, contribution docs, and issue/PR templates in English. Chinese text belongs in matched article translations and their title/summary metadata.
4. Add references to `content/references.json` and list their keys in the article metadata. Use local `#ref-<key>` links in the body. Citation numbers follow the metadata order.
5. Run `python3 scripts/build.py` and `python3 scripts/check.py`. For layout or behavior changes, also run the browser checks described in the README.
6. Commit source and generated output together. Submit a pull request explaining the reader-facing improvement and validation.

## Add a topic

Use `content/ARTICLE_TEMPLATE.html` as a structure, not as text to publish unchanged. Add a unique slug and matching English/Chinese content; include prerequisites, related guides, and reference keys in `content/articles.json`. Keep the metadata order appropriate to the learning path. Do not publish a translation stub as a completed translation.

## Edit terminology

Edit the paired fragments in `content/terms/en/` and `content/terms/zh/`, with matching section IDs. Use `content/terms.json` for titles, summaries, ordered references, `related_guides`, and `related_terms`. Keep terms out of the numbered Guide array. The builder generates the English `/terms/` index, separate language views, reciprocal Guide links, and search classifications.

Run the build, structural checks, all scientific fixture checks (`check_science.py`, `check_ionization.py`, `check_terms.py`, `check_analyzers.py`, `check_fragmentation.py`, and `check_acquisition.py`), and the browser checks after collection changes. Commit source and generated output together.

## Scientific standards

- Distinguish an observation, ion assignment, formula hypothesis, and structure identification.
- State charge, polarity, adducts, mass conventions, units, and assumptions in calculations.
- Describe limitations and plausible alternatives. Avoid universal claims from one instrument or method.
- Use standards, official resources, or primary papers for factual support. Verify titles, authors, years, DOI/URLs, and the claim a source supports.
- Write original explanations. Do not copy protected figures, spectra, or extended passages. Record provenance and permission for contributed data or media.
- Label constructed examples and schematic figures. Avoid implying they are experimental results.
- Keep translations aligned in meaning, examples, qualifications, section IDs, and references. Explain any temporary mismatch in the PR rather than hiding it.

## Review checklist

Check scientific accuracy, translation equivalence, readable examples, source validity, internal links, keyboard behavior, narrow-screen layout, and the effect on search. Automated tests validate structure and behavior; they do not establish scientific correctness.

## Report a problem

Use the content issue template for an incorrect claim, translation mismatch, or broken reference. Use the site issue template for layout and search defects. Include the article URL and a reproducible example where possible. Do not include private data, credentials, or identifiable sample information.
