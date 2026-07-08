---
name: lunar-source-ingestion
description: Convert downloaded lunar landing/descent PDFs, reports, and source texts into source-cited draft failure-memory records, CAST/STPA case-card material, and review-gate evidence without directly mutating the canonical KB. Use when collaborators provide accident reports, failure reports, NASA/NTRS documents, company technical-cause analyses, or equivalent lunar landing sources.
---

# Lunar Source Ingestion

Use this skill when a collaborator provides one or more lunar landing/descent source documents and asks to convert them into this repository's failure-memory format.

The initial scope is **lunar landing/descent only**. Adjacent corpora such as Mars EDL, launch-vehicle GNC, aviation, terrestrial autonomy, or generic safety cases should be recorded as follow-up candidates, not mixed into the first academic validation corpus.

## Required Project Context

Before extracting, read:

- `CONTEXT.md`
- `docs/research/central-claim.md`
- `docs/methods/stpa-cast.md`
- `docs/architecture/review-pipeline.md`
- `data/cases/README.md`
- `data/failure_kb.json` for existing mission IDs, design checks, and source conventions

If the task involves PDFs, use the available PDF-processing skill/tooling first to extract text and tables. Preserve page numbers or section labels when available.

## Output Contract

Do **not** directly modify `data/failure_kb.json` unless explicitly asked. Produce draft artifacts first, usually under `data/drafts/` or as a response for human review.

Use a staged output rule:

1. Always produce a source inventory and extracted claims first.
2. Produce draft case cards only when the source evidence is strong enough to support a named event, source-backed facts, confidence, and caveats.
3. If evidence is weak or fragmented, stop at extracted claims and list what a human/domain expert must resolve before promotion.

Every extracted precedent or case must include:

1. named mission/event;
2. source URL or local source path;
3. source type and authority level: primary, near-primary, or secondary;
4. quoted evidence with page/section when available;
5. confidence level;
6. caveats and unsupported claims;
7. proximate cause versus reusable failure class;
8. CAST reading for past events;
9. STPA-derived future review check;
10. review-gate evidence expectations;
11. links to existing `design_check` IDs when applicable.

Never invent a source quote, source URL, mission ID, or technical detail. If evidence is missing, write `not established from provided sources`.

## Workflow

### 1. Source inventory

For each provided PDF/report/source text, record:

- filename or URL;
- title;
- publisher/author;
- date;
- mission/event;
- source type: primary, near-primary, secondary;
- why it is relevant;
- extraction quality and missing pages/figures/tables.

### 2. Triage against scope

Classify each source:

- **In scope now**: lunar landing, descent, terminal GNC, touchdown, safing, surface survival after landing, review evidence for lunar missions.
- **Adjacent later**: Mars/Venus/asteroid EDL, launch failures, aviation/autonomy safety cases, general STPA/CAST examples.
- **Out of scope**: generic space news without technical evidence, unsourced blog summaries, speculation.

For adjacent sources, create or recommend a Backlog follow-up rather than mixing them into lunar validation outputs.

### 3. Extract evidence

Extract only source-supported claims:

- mission and event timeline;
- outcome and loss/degraded value;
- flight phase;
- subsystem, sensor, actuator, software, operation, or organization involved;
- proximate cause;
- contributing logic;
- propagation chain;
- good practices or mitigations;
- uncertainty, disagreement, or missing evidence.

Quote the strongest source sentences. Keep quotes short and traceable.

### 4. Map to CAST

For each incident or event, draft:

- loss;
- controlled process;
- controller(s);
- control action(s);
- feedback problem;
- incorrect process model or assumption;
- inadequate constraint;
- organizational/review factor when supported;
- reusable failure class.

Avoid simplistic root-cause framing.

### 5. Map to STPA future checks

Draft future-facing review material:

- hazard;
- unsafe control action;
- unsafe-control-action type;
- causal scenario;
- derived safety constraint;
- review-gate evidence by Concept Readiness, Preliminary Design Readiness, Critical Design Readiness, Integration/Test Readiness, and Flight/Operations Readiness;
- NASA crosswalk when useful: MCR/SRR, PDR, CDR, SIR/TRR/SAR, ORR/FRR/MRR.

### 6. Produce draft artifacts

Use the template in `references/draft-case-card-template.md`.

Recommended filenames:

- `data/drafts/<mission_or_event>_source_inventory.md`
- `data/drafts/<mission_or_event>_extracted_claims.md`
- `data/drafts/<mission_or_event>_draft_case_card.md` only when evidence is strong enough
- `data/drafts/<mission_or_event>_extraction_notes.md`

If the mission already has a committed case card under `data/cases/`, do not overwrite it. Produce a draft update and list diffs for human review.

## Quality Bar

A valid precedent-backed rationale must have:

- a named mission/event;
- a source URL or path;
- a confidence level;
- a short explanation of the shared failure class;
- a caveat if the proximate cause differs.

If the source corpus is too weak, say so. The academic validation package should prefer accident reports, failure reports, mishap investigation materials, NASA/NTRS or equivalent agency technical reports, company technical-cause analyses, and other primary or near-primary sources.

## Final Response Shape

Return:

1. sources processed;
2. draft artifacts created or proposed;
3. strongest extracted precedents;
4. confidence and caveats;
5. unresolved questions for domain experts;
6. recommended Backlog updates if the work should continue.
