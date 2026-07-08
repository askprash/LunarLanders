---
id: LL-6
title: Create lunar source ingestion skill
status: Done
assignee: []
created_date: '2026-07-08 14:28'
updated_date: '2026-07-08 15:06'
labels:
  - skills
  - ingestion
  - research
dependencies: []
references:
  - docs/research/central-claim.md
documentation:
  - >-
    /Users/prashanth/.nvm/versions/node/v22.19.0/lib/node_modules/@earendil-works/pi-coding-agent/docs/skills.md
  - docs/methods/stpa-cast.md
priority: high
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Create a project-local Pi skill or saved prompt that lets collaborators pass downloaded PDFs or source texts to an agent and have them converted into the project's required failure-memory format. The skill should support lunar-only corpus ingestion first and produce source-cited, confidence-qualified draft case cards or extraction records rather than directly mutating the canonical KB.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Project-local skill exists under a Pi-discoverable project skills directory
- [x] #2 Skill instructions cover PDF/source intake, source triage, extraction, CAST/STPA mapping, precedent fields, and review-gate evidence
- [x] #3 Skill requires preserving source URLs, quotes, confidence, caveats, and mission/event IDs
- [x] #4 Skill clearly scopes initial use to lunar landing/descent sources and defers adjacent corpora
- [x] #5 README or docs explain how collaborators invoke the skill
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Create a project-local Pi skill in .pi/skills/lunar-source-ingestion/SKILL.md.\n2. Include a reusable workflow for ingesting PDFs/source text into draft failure-memory artifacts without directly editing the canonical KB.\n3. Add a reference output template for draft case cards/extraction records.\n4. Document invocation in README development notes.\n5. Record lunar-only initial scope and adjacent-corpus follow-up in backlog/docs.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implemented project-local Pi skill at .pi/skills/lunar-source-ingestion/SKILL.md with draft output template at .pi/skills/lunar-source-ingestion/references/draft-case-card-template.md. Documented invocation in README. Validation: python3 redteam.py smoke test passed.

Post-completion refinement from grill session: ingestion output is staged. The skill should always produce source inventory + extracted claims first, and only produce draft case cards when evidence is strong enough. Weak or fragmented evidence should remain as extracted claims with human/domain-expert questions.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Created a project-local lunar source ingestion skill for converting lunar landing/descent PDFs and reports into draft source-cited CAST/STPA failure-memory artifacts. Added template and README invocation notes; kept initial scope lunar-only and deferred adjacent corpora.
<!-- SECTION:FINAL_SUMMARY:END -->
