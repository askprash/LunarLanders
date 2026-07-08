# Review Pipeline Architecture

The intended review pipeline is deliberately split so that an LLM does not become the only mechanism for finding risks.

## Stage 1 — Queryable Failure Memory

Store past occurrences and review checks in a structured form that can be queried without an LLM. The storage format should start as JSON/YAML/Markdown plus deterministic Python indexes, then evolve later if the corpus becomes large enough to need vector, hybrid lexical/vector, graph, or database-backed retrieval.

For academic validation, the corpus should expand beyond the current hand-built set toward authoritative sources: accident reports, failure reports, mishap investigation materials, agency technical reports, NASA NTRS documents, company technical-cause analyses, and equivalent primary or near-primary records.

Minimum queryable fields should include:

- mission/event ID and name;
- source URL and source quote;
- confidence level and caveats;
- failure class;
- proximate cause versus generalized lesson;
- CAST/STPA fields where available;
- linked design check IDs;
- review-gate evidence expectations;
- tags for phase, subsystem, sensor/actuator, terrain/lighting, software, operations, and survivability.

## Stage 2 — Deterministic Sweep

Run a deterministic Python pass before any LLM call. This sweep should:

- retrieve candidate precedents by tags, phases, subsystem terms, and explicit check signals;
- apply basic rules for known review concerns;
- produce a traceable report containing candidate failure classes, matched evidence, source links, confidence, caveats, and review-gate evidence requests;
- avoid claiming that absence of evidence is evidence of absence.

This stage should be auditable and reproducible.

## Stage 3 — LLM Semantic Review

Pass the LLM:

- the new ConOps or design-review excerpt;
- the deterministic sweep report;
- the relevant knowledge-base excerpts and source-backed precedents;
- calibrated instructions to preserve caveats, avoid certification language, and distinguish proximate causes from reusable failure classes.

The LLM should then:

- interpret realistic prose and vocabulary variation;
- reject weak or misleading deterministic matches;
- identify supported concerns that deterministic keyword matching missed;
- explain precedent-backed rationale;
- output readiness gaps, evidence requests, and cited red-team concerns for human reviewers.

## Scaling Path

Do not adopt vector infrastructure until there is enough corpus scale and retrieval ambiguity to justify it. When that point arrives, preserve the deterministic sweep contract: retrieved chunks must remain attached to named missions/events, source URLs, confidence levels, source quotes, and caveats. A vector result without a traceable precedent is not acceptable evidence.

See `docs/adr/0006-start-with-structured-files-but-plan-scalable-retrieval.md`.

## Design Rule

The LLM may synthesize and challenge, but it should not invent precedents. Every precedent-backed rationale must point to a named event, source URL, confidence level, shared failure class, and caveat when proximate causes differ.
