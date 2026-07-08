---
id: LL-9
title: Build interactive architecture walkthrough
status: Done
assignee:
  - '@pi'
created_date: '2026-07-08 15:17'
updated_date: '2026-07-08 15:52'
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
- [x] #1 Walkthrough is available as a static, shareable artifact requiring no backend
- [x] #2 Pipeline visually includes source corpus, source inventory, extracted claims, case cards, queryable failure memory, deterministic sweep, LLM semantic review, and readiness gaps
- [x] #3 Each stage has a clickable explanation panel covering inputs, outputs, human/expert role, failure modes, and example repo links
- [x] #4 Walkthrough states that outputs are review-readiness coaching artifacts, not certification
- [x] #5 Expert handoff packet links to the walkthrough
- [x] #6 Walkthrough is implemented as a new standalone HTML page, not as a tab inside lunar_redteam_demo.html
- [x] #7 A GitHub Actions workflow publishes or builds the static walkthrough page for reviewer access
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Complete standalone walkthrough HTML via LL-9.1.\n2. Complete GitHub Pages publishing via LL-9.2.\n3. Update expert handoff packet and README links.\n4. Verify smoke test and finalize parent task.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Completed via LL-9.1 and LL-9.2. Implemented architecture_walkthrough.html, added GitHub Pages workflow, linked from README and expert handoff packet, and verified python3 redteam.py plus content grep checks.
<!-- SECTION:NOTES:END -->

## Comments

<!-- COMMENTS:BEGIN -->
created: 2026-07-08 15:19
---
Decision: build the walkthrough first as a standalone static HTML page and add a GitHub Actions workflow to publish/build it for reviewers. Keep it separate from lunar_redteam_demo.html until the onboarding artifact stabilizes.
---
<!-- COMMENTS:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Built and wired the interactive architecture walkthrough as a standalone static page with GitHub Pages publishing. The page visualizes the full pipeline, includes clickable stage panels, Hakuto-R M1 example, guardrails, and limitations.
<!-- SECTION:FINAL_SUMMARY:END -->
