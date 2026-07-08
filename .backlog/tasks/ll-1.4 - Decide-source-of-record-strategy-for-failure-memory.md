---
id: LL-1.4
title: Decide source-of-record strategy for failure memory
status: To Do
assignee: []
created_date: '2026-07-08 14:12'
labels:
  - architecture
  - decision
dependencies:
  - LL-1.3
references:
  - data/failure_kb.json
  - data/cases/README.md
parent_task_id: LL-1
priority: medium
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
After the pilot case cards exist, decide whether data/failure_kb.json remains the source of record, evolves to include CAST/STPA fields, or is generated from human-readable case cards. This decision affects future contributors and tool architecture.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Decision compares keeping JSON primary, making Markdown cards primary, and maintaining both with generation/validation
- [ ] #2 Decision records tradeoffs for human readability, agent parsing, drift risk, and tool simplicity
- [ ] #3 If hard to reverse and non-obvious, record the outcome as an ADR
<!-- AC:END -->
