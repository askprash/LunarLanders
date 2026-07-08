---
id: LL-9.1
title: Create standalone walkthrough HTML page
status: To Do
assignee: []
created_date: '2026-07-08 15:19'
updated_date: '2026-07-08 15:47'
labels:
  - ui
  - documentation
dependencies:
  - LL-10
documentation:
  - docs/product/interactive-architecture-walkthrough.md
parent_task_id: LL-9
priority: high
ordinal: 14000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Implement the interactive architecture walkthrough as a standalone static HTML page, separate from lunar_redteam_demo.html, for academic/domain-expert onboarding.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Standalone HTML page renders without a backend or build step
- [ ] #2 Clickable pipeline blocks open explanation panels
- [ ] #3 Content covers inputs, outputs, human/expert role, failure modes, and example repo links for each stage
- [ ] #4 Page clearly states the tool is a review-readiness coach, not a certification authority
- [ ] #5 Hakuto-R M1 running example uses real artifacts where available and displays maturity labels such as official source, extracted claim, draft/curated-not-domain-validated card, example deterministic match, and example LLM interpretation
- [ ] #6 LLM semantic review panel states allowed actions and prohibited actions, including no invented precedents, no silent confidence upgrades, no certification claims, no erasing proximate-cause differences, and no treating absent mitigations as proof of risk
- [ ] #7 Walkthrough includes a subtle, visually secondary limitations footer covering weak sources, extraction errors, overgeneralized failure classes, deterministic misses, LLM overconfidence, and certification confusion
<!-- AC:END -->

## Comments

<!-- COMMENTS:BEGIN -->
created: 2026-07-08 15:21
---
Decision: use Hakuto-R M1 as the running example throughout the standalone walkthrough. Before implementation, depend on/source from LL-10 so the walkthrough cites the strongest available official source rather than magazine-style summaries.
---

created: 2026-07-08 15:23
---
Decision: the walkthrough should show the Hakuto-R M1 pipeline with real artifacts where possible, but every stage must display artifact maturity labels so reviewers can distinguish evidence from interpretation and validation status.
---

created: 2026-07-08 15:46
---
Decision: the walkthrough must show both what the LLM stage is allowed to do and what it is not allowed to do, so reviewers can audit the human/LLM boundary.
---

created: 2026-07-08 15:47
---
Decision: include pipeline failure modes transparently but subtly near the bottom of the page. The main walkthrough should encourage domain experts to see how AI can help, while the footer explains limitations and why sources, caveats, maturity labels, deterministic retrieval, and expert review remain necessary.
---
<!-- COMMENTS:END -->
