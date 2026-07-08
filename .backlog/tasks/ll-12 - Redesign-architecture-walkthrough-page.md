---
id: LL-12
title: Redesign architecture walkthrough page
status: Done
assignee:
  - '@pi'
created_date: '2026-07-08 19:28'
updated_date: '2026-07-08 19:41'
labels: []
dependencies: []
ordinal: 18000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Replace the current architecture walkthrough page styling/content structure because it reads as AI-generated visual slop, has conflicting visuals, and can overlap text. The page should be credible to a cold reader and visually clean across viewport sizes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Page has a coherent visual system with no obvious text overlap at desktop, tablet, or mobile widths
- [x] #2 Cold reader can understand the purpose, evidence flow, and limits without prior repository context
- [x] #3 Hakuto-R M1 example is used clearly without overstating source authority
- [x] #4 Playwright-based visual/layout checks are run and findings addressed
- [x] #5 Existing GitHub Pages publishing path remains compatible
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Run cold-read lint and context-denied review on the current walkthrough.
2. Use Playwright to inspect desktop/tablet/mobile screenshots and detect obvious text overlaps/overflow.
3. Rewrite architecture_walkthrough.html around a calmer evidence-first visual system and clearer cold-reader narrative.
4. Re-run Playwright checks and cold-read lint; iterate until visual/layout issues are resolved.
5. Record validation and hand off.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Replaced the neon/glassmorphism walkthrough with a calmer evidence-first page. Added a visible Hakuto-R M1 chain, source caveat, concrete design-text to precedent to review-question example, short glossary, and flow-based pipeline cards without absolute-positioned labels. Added local demo.html redirect while preserving existing GitHub Pages behavior. Validation: cold-read slop_lint clean; Playwright screenshots captured for desktop/tablet/mobile/full-page; Playwright CLI overflow checks passed at 1440, 768, 390, and 320 px, including every pipeline stage.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Redesigned the architecture walkthrough from a visually noisy card grid into a calmer evidence-first explainer. Removed overlapping pipeline labels by using normal-flow badges and button styling, added glossary and concrete example for cold readers, clarified Hakuto-R source caveats, added a local demo redirect, and verified with cold-read lint plus Playwright screenshot/overflow checks across desktop, tablet, mobile, and narrow viewports.
<!-- SECTION:FINAL_SUMMARY:END -->
