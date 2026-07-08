---
id: LL-1.1
title: Define CAST/STPA case-card schema
status: To Do
assignee: []
created_date: '2026-07-08 14:12'
labels:
  - methods
  - schema
dependencies: []
references:
  - data/cases/hakuto_r_m1.md
  - data/cases/README.md
parent_task_id: LL-1
priority: high
ordinal: 2000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Define the reusable human-readable case-card format for historical lunar landing events. The schema should be easy for engineers to read and easy for agents to parse, using YAML frontmatter plus Markdown narrative.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Schema includes evidence layer, CAST reading, STPA-derived future review check, review-gate evidence, and human-readable lesson
- [ ] #2 Schema identifies required versus optional fields
- [ ] #3 Schema documents how cards relate to data/failure_kb.json IDs and source URLs
- [ ] #4 At least one existing card, data/cases/hakuto_r_m1.md, conforms to the schema
<!-- AC:END -->
