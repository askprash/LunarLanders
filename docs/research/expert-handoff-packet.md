# Expert Handoff Packet

This is the concise starting packet for spacecraft systems, GNC, mission-assurance, safety-analysis, or lunar-operations experts. It is meant to let reviewers evaluate the method without inspecting the entire repository.

## Start Here

1. `README.md` — project overview and current prototype behavior.
2. `docs/research/central-claim.md` — the research claim, non-claims, and validation questions.
3. `docs/research/proposed-domain-expert-review-workflow.md` — optional review scaffold; experts should change it as needed.
4. `docs/methods/stpa-cast.md` — how this project uses STPA/CAST.
5. `data/cases/hakuto_r_m1.md` — first pilot CAST/STPA case card.
6. `docs/product/interactive-architecture-walkthrough.md` — planned interactive walkthrough of the pipeline.

## Add When Ready

- 2–4 additional draft case cards from `data/cases/` or `data/drafts/`.
- A source inventory from the lunar-only authoritative corpus expansion.
- A hindcast narrative showing how a past failure class could have been surfaced before a later mission repeated it.
- A rendered interactive walkthrough where reviewers can click through each pipeline stage and read concise explanations.

## Questions for Reviewers

Please focus on whether the method is technically credible, not just whether the prose is clear.

1. Is the central research claim appropriately scoped?
2. Is the corpus source quality sufficient for an academic validation pass?
3. Does CAST/STPA add useful structure, or does it merely rename ordinary mishap summaries?
4. Does the Hakuto-R M1 case card separate proximate cause from reusable failure class correctly?
5. Are the derived safety constraints and review-readiness evidence requests technically useful?
6. What terminology should be changed to match spacecraft systems / mission-assurance practice?
7. What authoritative sources are missing?
8. What would make the method invalid, misleading, or not worth continuing?

## Reviewer Freedom

This packet is a scaffold, not a protocol. Domain experts should revise the workflow, case-card schema, validation statuses, corpus boundary, and acceptance criteria if they see a better path.
