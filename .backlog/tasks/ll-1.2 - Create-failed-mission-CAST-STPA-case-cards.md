---
id: LL-1.2
title: Create failed-mission CAST/STPA case cards
status: To Do
assignee: []
created_date: '2026-07-08 14:12'
labels:
  - methods
  - data
dependencies:
  - LL-1.1
references:
  - data/failure_kb.json
  - data/cases/hakuto_r_m1.md
parent_task_id: LL-1
priority: high
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Create case cards for the most useful failed or partial lunar missions after the Hakuto-R M1 pilot card. Focus on cases that generate distinct review questions for future ConOps: Hakuto-R M2, Beresheet, Luna 25, IM-1 Odysseus, IM-2 Athena, and Chandrayaan-2.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Each selected mission has a data/cases/*.md card with YAML frontmatter and Markdown narrative
- [ ] #2 Each card states confidence and does not overclaim beyond public sources
- [ ] #3 Each card links to the current mission ID and primary/supporting source URLs from data/failure_kb.json
- [ ] #4 Each card maps to relevant existing design_check IDs where applicable
<!-- AC:END -->
