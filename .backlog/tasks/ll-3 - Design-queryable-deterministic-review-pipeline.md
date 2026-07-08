---
id: LL-3
title: Design queryable deterministic review pipeline
status: To Do
assignee: []
created_date: '2026-07-08 14:23'
labels:
  - architecture
  - retrieval
dependencies: []
references:
  - data/failure_kb.json
documentation:
  - docs/architecture/review-pipeline.md
  - docs/adr/0005-use-deterministic-sweep-before-llm-semantic-review.md
priority: high
ordinal: 7000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Design the next review architecture as a deterministic sweep over a structured, queryable failure memory followed by LLM semantic review. The goal is to make risk retrieval auditable before the LLM interprets realistic ConOps prose.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Storage options compare JSON/YAML plus Python indexes, lightweight SQLite, graph storage, and vector retrieval without prematurely over-engineering
- [ ] #2 Deterministic sweep output schema includes candidate failure classes, named precedents, source URLs, confidence, caveats, matched evidence, and review-gate evidence requests
- [ ] #3 LLM prompt contract requires using the deterministic report and retrieved precedents, preserving caveats, and not inventing precedents
- [ ] #4 Architecture doc explains how this differs from certification or pure LLM risk prediction
<!-- AC:END -->
