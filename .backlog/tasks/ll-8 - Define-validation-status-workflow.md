---
id: LL-8
title: Define validation-status workflow
status: To Do
assignee: []
created_date: '2026-07-08 15:09'
updated_date: '2026-07-08 15:11'
labels:
  - research
  - process
dependencies: []
references:
  - docs/research/proposed-domain-expert-review-workflow.md
documentation:
  - docs/adr/0008-separate-curation-approval-from-domain-validation.md
priority: high
ordinal: 12000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Define a practical promotion workflow for extracted claims, draft case cards, curated case cards, and domain-validated artifacts. The workflow must let non-domain maintainers perform curation approval while clearly separating that from domain validation by spacecraft/GNC/mission-assurance/safety experts.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Workflow defines statuses such as draft, curated, domain-reviewed, accepted, and rejected/deferred
- [ ] #2 Workflow states what non-domain maintainers can approve versus what requires domain expertise
- [ ] #3 Case-card and ingestion-skill templates include validation_status or equivalent metadata
- [ ] #4 Academic validation package reports which artifacts are curated versus domain-reviewed
<!-- AC:END -->

## Comments

<!-- COMMENTS:BEGIN -->
created: 2026-07-08 15:11
---
Validation workflow should be presented as proposed scaffolding for domain experts, not a required process. Non-domain maintainers can prepare curated artifacts and suggested review questions; domain experts own how they validate or revise them.
---
<!-- COMMENTS:END -->
