---
id: LL-11
title: Adopt uv environment management
status: Done
assignee:
  - '@pi'
created_date: '2026-07-08 18:46'
updated_date: '2026-07-08 18:49'
labels: []
dependencies: []
ordinal: 17000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Clean up repository environment setup so collaborators use uv consistently for Python execution and dependency management.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Repository includes standard uv project metadata and lockfile where applicable
- [x] #2 README quick-start and development commands use uv
- [x] #3 Existing validation commands pass through uv-managed execution
- [x] #4 No generated caches or local virtual environments are tracked
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Inspect current Python/runtime files and validation commands.
2. Add uv project metadata/lockfile and ignore local environments/caches.
3. Update README to make uv the primary workflow.
4. Run validation commands via uv and record results.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Added uv project metadata (.python-version, pyproject.toml, uv.lock), ignored local virtualenv/cache folders, and updated README, examples README, AGENTS guidance, and redteam.py usage text to prefer uv run. Validated with uv run python -m py_compile redteam.py plus the required keyword-mode sample commands.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Adopted uv for repository environment management by adding .python-version, pyproject.toml, and uv.lock; updated README, examples, AGENTS, and script usage docs to use uv run; ignored local virtualenv/cache directories; verified with uv sync, py_compile, and required sample review commands.
<!-- SECTION:FINAL_SUMMARY:END -->
