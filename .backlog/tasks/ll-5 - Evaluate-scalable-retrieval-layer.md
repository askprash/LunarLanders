---
id: LL-5
title: Evaluate scalable retrieval layer
status: To Do
assignee: []
created_date: '2026-07-08 14:26'
labels:
  - architecture
  - retrieval
dependencies:
  - LL-3
documentation:
  - docs/architecture/review-pipeline.md
  - docs/adr/0006-start-with-structured-files-but-plan-scalable-retrieval.md
priority: medium
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Evaluate future retrieval infrastructure for a larger failure memory after the structured-file pilot. Compare vector, hybrid lexical/vector, graph/database, and generated-index approaches while preserving auditable precedent links.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Evaluation defines corpus-size or retrieval-complexity triggers for moving beyond JSON/YAML plus Python indexes
- [ ] #2 Comparison covers vector search, hybrid lexical/vector retrieval, graph/database indexing, and generated static indexes
- [ ] #3 Recommended approach preserves mission/event IDs, source URLs, source quotes, confidence levels, and caveats in every retrieved result
- [ ] #4 Prototype plan explains how retrieval output feeds the deterministic sweep and LLM semantic review
<!-- AC:END -->
