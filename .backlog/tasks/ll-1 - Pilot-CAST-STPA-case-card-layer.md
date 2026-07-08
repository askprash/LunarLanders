---
id: LL-1
title: Pilot CAST/STPA case-card layer
status: To Do
assignee: []
created_date: '2026-07-08 14:12'
labels:
  - methods
  - documentation
dependencies: []
documentation:
  - docs/methods/stpa-cast.md
  - docs/adr/0001-use-stpa-and-cast-as-method-backbone.md
modified_files:
  - data/cases/README.md
  - data/cases/hakuto_r_m1.md
priority: high
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Create a small, human-readable CAST/STPA layer above data/failure_kb.json before attempting a full knowledge-base migration. The pilot should prove whether YAML-frontmatter + Markdown case cards help collaborators understand past lunar failures and turn them into future design-review evidence.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Pilot covers Hakuto-R M1 plus selected failed/partial missions
- [ ] #2 Case cards link back to source URLs and current data/failure_kb.json mission IDs
- [ ] #3 Each card includes CAST incident reading, STPA-derived future review check, and review-gate evidence
- [ ] #4 README or docs explain that data/failure_kb.json remains the current source of record during the pilot
<!-- AC:END -->
