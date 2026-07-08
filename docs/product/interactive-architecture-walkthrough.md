# Interactive Architecture Walkthrough

The expert handoff should eventually include a polished, preferably interactive walkthrough of the review pipeline. This should make the system understandable before a reviewer reads the detailed method documents.

## Intended Flow

Use **Hakuto-R Mission 1** as the running example, but only after verifying the highest-authority public source material. Prefer official ispace/company technical-cause materials or exchange disclosures over magazine-style summaries; document caveats if no independent accident report exists.

Show real artifacts where possible, but label maturity explicitly so reviewers can distinguish evidence from interpretation:

```text
Hakuto-R M1 official source material          [official source]
  -> source inventory                         [curation artifact]
  -> extracted altitude-filter / terrain claims [extracted claims]
  -> draft/curated/domain-reviewed case card  [draft or curated-not-domain-validated]
  -> queryable failure memory                 [structured retrieval layer]
  -> deterministic sweep for terrain-aware altimetry risk [example deterministic match]
  -> LLM semantic review of a future ConOps    [example LLM interpretation]
  -> CDR/readiness evidence gaps + cited concerns [review-readiness coaching]
```

## Interaction Concept

Each pipeline block should be clickable. Clicking opens a short explanation panel with:

- what the stage does;
- what artifact it consumes;
- what artifact it produces;
- what human or expert review is required;
- what can go wrong at that stage;
- links to example files in the repo.

## Example Panels

The page should be encouraging and visually clear: the main story is how AI can help convert historical failure evidence into better review questions. Limitations should be transparent but not dominate the first impression.

### Source Corpus

Explains that the first validation corpus is lunar landing/descent only and should prioritize authoritative sources such as accident reports, failure reports, NASA/NTRS documents, agency technical reports, and company technical-cause analyses.

### Extracted Claims

Explains that claims are atomic source-backed statements, not yet accepted facts. They preserve quotes, source URLs, confidence, and caveats.

### Case Cards

Explains the promotion path from draft case cards to curated and domain-reviewed cards, using CAST for past events and STPA for future review questions.

### Deterministic Sweep

Explains the auditable Python/rules pass that retrieves candidate precedents and review checks before the LLM reasons about the ConOps.

### LLM Semantic Review

Explains that the LLM reads realistic ConOps prose, the deterministic report, and retrieved precedents.

The panel should explicitly show what the LLM is allowed to do:

- interpret realistic ConOps prose and vocabulary variation;
- compare the ConOps to retrieved precedents;
- explain caveats and proximate-cause differences;
- reject weak deterministic matches;
- turn supported concerns into readiness gaps and evidence requests.

It should also show what the LLM is not allowed to do:

- invent precedents, sources, quotes, or mission facts;
- silently upgrade confidence;
- claim certification, compliance, or flight readiness;
- erase important differences in proximate cause;
- treat absence of a mitigation in the provided text as proof of risk.

### Readiness Gaps

Explains that the output is not certification. It is a review-readiness coaching artifact: evidence requests, cited red-team concerns, caveats, and questions for human reviewers.

## Subtle Limitations Footer

Add a small, transparent limitations section near the bottom of the page. Keep it concise and visually secondary. It should say that the pipeline can fail when:

- the source corpus is weak, secondary, incomplete, or not authoritative;
- extraction quotes or page references are wrong;
- a failure class is overgeneralized across missions with different proximate causes;
- deterministic matching misses paraphrases or creates brittle keyword matches;
- the LLM overstates confidence or interprets beyond retrieved evidence;
- a reader mistakes review-readiness coaching for certification.

The footer should end with the intended posture: these limitations are why the system preserves sources, caveats, maturity labels, deterministic retrieval, and human/domain-expert review.

## Implementation Notes

The first implementation should be a **new standalone static HTML page**, separate from `lunar_redteam_demo.html`. The demo page can link to it later, but the expert walkthrough should be independently shareable and easier to iterate.

A GitHub Actions workflow should publish the page, preferably via GitHub Pages or a generated static artifact, so academic/domain reviewers can open a stable URL without local setup.

See `docs/adr/0009-publish-architecture-walkthrough-as-standalone-html.md`.
