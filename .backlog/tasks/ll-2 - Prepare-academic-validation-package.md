---
id: LL-2
title: Prepare academic validation package
status: To Do
assignee: []
created_date: '2026-07-08 14:18'
updated_date: '2026-07-08 15:15'
labels:
  - research
  - validation
dependencies: []
references:
  - docs/research/expert-handoff-packet.md
documentation:
  - docs/adr/0004-start-with-academic-validation-before-startup-use.md
  - docs/methods/stpa-cast.md
priority: high
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Create the next-phase research package for academic/domain-expert evaluation before translating the tool into a startup workflow. The package should let spacecraft systems, mission assurance, GNC, and safety-analysis experts judge whether the corpus, CAST/STPA framing, hindcast logic, source quality, and review-gate evidence model are credible.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Package states the research claims and non-claims clearly
- [ ] #2 Package defines what expert reviewers should evaluate and what would falsify or weaken the method
- [ ] #3 Package includes representative CAST/STPA case cards and at least one hindcast narrative
- [ ] #4 Package separates academic validation audience from later startup engineering and technical diligence audiences
<!-- AC:END -->

## Comments

<!-- COMMENTS:BEGIN -->
created: 2026-07-08 14:20
---
Central research claim agreed: a source-cited lunar-lander failure memory, structured with CAST/STPA, can generate review-readiness questions that would have surfaced recurring failure classes before later missions repeated them. Addendum: each concern should point to past occurrences of the failure class so reviewers can see the rationale for why a ConOps feature is potentially problematic.
---

created: 2026-07-08 15:11
---
Handoff decision: propose a small 3-5 case-card domain-expert review loop as a scaffold, but do not treat it as mandatory. Domain experts should be free to change the workflow, review criteria, terminology, and acceptance process.
---

created: 2026-07-08 15:15
---
Decision: create a concise expert handoff packet instead of expecting domain experts to inspect the whole repository. Initial packet should include README, central claim, proposed review workflow, STPA/CAST method notes, Hakuto-R M1 pilot card, later draft cards, and reviewer questions.
---
<!-- COMMENTS:END -->
