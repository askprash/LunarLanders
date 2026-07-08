---
id: LL-4
title: Expand authoritative failure source corpus
status: To Do
assignee: []
created_date: '2026-07-08 14:26'
updated_date: '2026-07-08 14:30'
labels:
  - research
  - data
dependencies: []
references:
  - data/failure_kb.json
documentation:
  - docs/adr/0007-validate-lunar-corpus-before-adjacent-corpora.md
priority: high
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Expand the academic validation corpus beyond the current hand-built lunar landing set using more authoritative primary and near-primary sources. Prioritize accident reports, failure reports, mishap investigation materials, agency technical reports, NASA NTRS documents, company technical-cause analyses, and equivalent sources so domain experts can evaluate the method on stronger evidence.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Source inventory identifies candidate reports by mission/event, source type, URL, authority level, and access status
- [ ] #2 Corpus distinguishes primary, near-primary, and secondary sources
- [ ] #3 Each added source has citation metadata and notes on confidence, limitations, and extraction priority
- [ ] #4 Academic validation package states whether the corpus is sufficient and what important sources remain missing
<!-- AC:END -->

## Comments

<!-- COMMENTS:BEGIN -->
created: 2026-07-08 14:30
---
Scope decision: academic source-corpus expansion should remain lunar landing/descent only for the first validation pass. Adjacent domains are tracked separately in LL-7.
---
<!-- COMMENTS:END -->
