# Packet QA

## Passed preparation checks

- Current main SHA independently verified; pinned inventory is 28 Guides and 60 terms
- Two Guide slugs and six term slugs absent from baseline
- Sixteen complete fragments, eight matched language pairs
- English Guides 951/963 words; English terms 174–184 words
- Balanced HTML and unique section IDs; English/Chinese section IDs match
- English/Chinese inline code, numeric sequence, citations and normalized internal-link order match
- References resolve to thirteen unique new `signal-` entries and one unchanged reused entry
- Citation numbers match each page's metadata reference order
- Internal routes point only to the pinned baseline or another addition in this packet
- Prerequisite, related-Guide and related-term references resolve
- Twelve fixtures checked; eleven numerical cases independently recomputed and one semantic boundary case reviewed
- Topic proposal stays outside the current term schema

## Scientific and bilingual review

Reviewed both languages for charge/current units, event versus electron counts, analog versus counting operation, image-current versus impact detection, the role of coherence, conditional Poisson uncertainty, intensity-height/sum/integral distinctions, spectral versus chromatographic axes, estimator dependence, smoothing-induced dependence, RMS denominator versus peak-to-peak noise, and the absence of a universal S/N threshold. All constructed examples retain their qualifications in Chinese.

The moving-average illustration assumes zero padding and a centered three-point arithmetic mean. The trapezoidal example integrates only the specified coordinate bounds. The RMS example uses divisor n = 4, not the sample standard-deviation divisor n − 1. The phase example is a mathematical superposition illustration, not an instrument calibration. The current example uses the exact SI elementary charge and explicitly assumes complete collection.

## Not run or claimed

No repository build, current scientific-checker integration, browser render, accessibility test, search test, deploy, or live-site verification was performed. Preparation checks validate the packet; they do not certify implementation or prove the experimental truth of a real dataset. Review scripts belong only to this packet.

## Required later integration checks

1. Reconcile current main, slugs, references and final taxonomy before any edit
2. Add exact fragments and narrowly merge metadata
3. Integrate the original fixture payload into an appropriate authorized checker
4. Run build, structural checks and all existing scientific fixture checks
5. Inspect generated routes, local references, language switches and reciprocal links
6. Check search/index/A–Z behavior alongside the separately authorized terminology-index work
7. Review wide/narrow displays and keyboard navigation before publishing
