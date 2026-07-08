---
id: LL-9
title: Build interactive architecture walkthrough
status: To Do
assignee: []
created_date: '2026-07-08 15:17'
updated_date: '2026-07-08 15:19'
labels:
  - ui
  - documentation
  - validation
dependencies: []
references:
  - docs/research/expert-handoff-packet.md
  - lunar_redteam_demo.html
documentation:
  - docs/product/interactive-architecture-walkthrough.md
  - docs/adr/0009-publish-architecture-walkthrough-as-standalone-html.md
priority: high
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Build a polished static interactive walkthrough for the expert handoff package. It should visually explain the pipeline from source PDFs to extracted claims, case cards, queryable failure memory, deterministic sweep, LLM semantic review, and readiness gaps. Reviewers should be able to click pipeline blocks and read short explanatory panels.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Walkthrough is available as a static, shareable artifact requiring no backend
- [ ] #2 Pipeline visually includes source corpus, source inventory, extracted claims, case cards, queryable failure memory, deterministic sweep, LLM semantic review, and readiness gaps
- [ ] #3 Each stage has a clickable explanation panel covering inputs, outputs, human/expert role, failure modes, and example repo links
- [ ] #4 Walkthrough states that outputs are review-readiness coaching artifacts, not certification
- [ ] #5 Expert handoff packet links to the walkthrough
- [ ] #6 Walkthrough is implemented as a new standalone HTML page, not as a tab inside lunar_redteam_demo.html
- [ ] #7 A GitHub Actions workflow publishes or builds the static walkthrough page for reviewer access
<!-- AC:END -->

## Comments

<!-- COMMENTS:BEGIN -->
created: 2026-07-08 15:19
---
Decision: build the walkthrough first as a standalone static HTML page and add a GitHub Actions workflow to publish/build it for reviewers. Keep it separate from lunar_redteam_demo.html until the onboarding artifact stabilizes.
---
<!-- COMMENTS:END -->
