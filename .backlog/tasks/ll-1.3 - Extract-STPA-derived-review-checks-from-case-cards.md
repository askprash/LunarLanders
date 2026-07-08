---
id: LL-1.3
title: Extract STPA-derived review checks from case cards
status: To Do
assignee: []
created_date: '2026-07-08 14:12'
updated_date: '2026-07-08 14:17'
labels:
  - methods
  - review-gates
dependencies:
  - LL-1.2
references:
  - docs/methods/stpa-cast.md
  - docs/adr/0003-position-as-review-readiness-coach-not-certification-tool.md
parent_task_id: LL-1
priority: medium
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Turn repeated case-card lessons into future-facing STPA review checks that can be mapped to startup review readiness. This should clarify the difference between historical incident records and reusable future review questions.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Review checks include hazard, unsafe control action, causal scenario, derived safety constraint, linked precedents, and review-gate evidence
- [ ] #2 Checks cover at least terminal altimetry, sensor liveness, command/recovery isolation, terrain/lighting validation, post-CDR change revalidation, and tip-over survivability
- [ ] #3 Output format is documented and can later be connected to redteam.py or data/failure_kb.json
<!-- AC:END -->

## Comments

<!-- COMMENTS:BEGIN -->
created: 2026-07-08 14:13
---
Decision from grill session: review-gate readiness evidence should be a first-class product concept, not just an annotation on failure-mode findings. Future STPA-derived checks should produce SRR/PDR/CDR/later-gate evidence expectations that a startup team can act on.
---

created: 2026-07-08 14:15
---
Decision logged in ADR 0002: use startup-friendly readiness gates mapped to NASA lifecycle reviews. This is provisional because stronger mission-assurance/domain experts may refine the names, mappings, and evidence requirements later.
---

created: 2026-07-08 14:17
---
Decision logged in ADR 0003: position the product as a review-readiness coach, not a certification/compliance tool. Outputs should be readiness gaps, evidence requests, and cited red-team concerns for human reviewers.
---
<!-- COMMENTS:END -->
