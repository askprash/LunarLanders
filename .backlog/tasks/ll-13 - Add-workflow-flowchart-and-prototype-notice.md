---
id: LL-13
title: Add workflow flowchart and prototype notice
status: Done
assignee:
  - '@pi'
created_date: '2026-07-08 19:51'
updated_date: '2026-07-08 19:56'
labels: []
dependencies: []
ordinal: 19000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Add a simple visual workflow flow chart to the architecture walkthrough and make the README clearly state that the project is a prototype under active development.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Architecture walkthrough includes a simple readable workflow flow chart
- [x] #2 Flow chart renders without overlap or horizontal overflow on desktop and mobile
- [x] #3 README includes a prominent prototype/under-development notice near the top
- [x] #4 Changes are committed atomically by concern
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Add a compact workflow flow chart to architecture_walkthrough.html near the short-version/pipeline intro.
2. Validate the flow chart with cold-read lint and Playwright desktop/mobile overflow checks.
3. Commit the flow chart independently.
4. Add a prominent prototype/under-development notice to README.md.
5. Commit the README notice independently and finalize the Backlog task.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Added workflow-at-a-glance flow chart to architecture_walkthrough.html and validated with cold-read lint plus Playwright screenshots/overflow checks at desktop and mobile/narrow widths. Added README prototype-status notice near the top. Cleaned README wording so cold-read lint passes. Commits: 708e5a4 flow chart, bf91841 prototype notice, adea7d6 README wording cleanup.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Added a workflow-at-a-glance flow chart to the walkthrough, added a prominent README prototype notice, validated the walkthrough with Playwright and cold-read lint, and kept changes split into atomic commits by concern.
<!-- SECTION:FINAL_SUMMARY:END -->
