---
id: LL-7
title: Define adjacent corpus expansion path
status: To Do
assignee: []
created_date: '2026-07-08 14:29'
labels:
  - research
  - data
dependencies: []
documentation:
  - docs/adr/0007-validate-lunar-corpus-before-adjacent-corpora.md
  - docs/research/central-claim.md
priority: low
ordinal: 11000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Define how and when to expand beyond the lunar-only validation corpus into adjacent sources such as Mars EDL, launch-vehicle GNC failures, aviation/autonomy safety cases, or terrestrial STPA/CAST examples. This should happen after the lunar corpus and method have been academically evaluated.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Adjacent-corpus candidates are grouped by domain and expected transfer value
- [ ] #2 Task defines criteria for when adjacent sources can be introduced without weakening the lunar-specific research claim
- [ ] #3 Expansion plan preserves separate labels or collections so lunar-only validation remains reproducible
- [ ] #4 Plan identifies likely authoritative source types for each adjacent domain
<!-- AC:END -->
