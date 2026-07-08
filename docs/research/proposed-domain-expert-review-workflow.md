# Proposed Domain-Expert Review Workflow

This is a suggested workflow for handing the project to spacecraft, GNC, mission-assurance, safety-analysis, or lunar-operations experts. It is **not** a required process. Domain experts should change the workflow, review depth, terminology, and acceptance criteria as they see fit.

## Suggested First Pass

Start with a small sample before scaling the corpus:

1. Select 3–5 representative case cards or draft case cards.
2. Ask reviewers to judge the method, not just the wording.
3. Capture disagreements, missing evidence, and terminology corrections.
4. Revise the schema and extraction workflow before expanding the corpus.

Good initial candidates:

- Hakuto-R M1 — terrain-induced altimeter step rejected as anomalous.
- Hakuto-R M2 — single-string loss-critical LRF under-performance.
- Beresheet — sensor recovery / reboot / propulsion-control cascade.
- Luna 25 — sensor-liveness failure before an irreversible burn.
- IM-1 or IM-2 — commercial-lander altimetry, integration, and survivability issues.

## Review Questions for Experts

For each case, ask:

- Is the source evidence sufficient and accurately represented?
- Is the confidence level appropriate?
- Is the proximate cause separated from the reusable failure class?
- Is the CAST reading technically credible?
- Is the STPA-derived future review check useful or misleading?
- Are the review-gate evidence requests realistic for a mission team?
- What would you rename, split, merge, or remove?
- What sources are missing?

## Expected Output

Experts may return any format they prefer. A useful minimum is:

- accept / revise / reject for each case;
- comments on failure-class abstraction;
- comments on CAST/STPA mapping;
- source-quality concerns;
- recommended schema changes;
- missing authoritative sources;
- whether the project should continue with the current framing.

## Principle

The project should adapt to expert review. The workflow exists to make handoff easier, not to constrain reviewers.
