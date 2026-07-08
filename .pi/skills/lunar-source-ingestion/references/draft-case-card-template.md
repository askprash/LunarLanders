# Draft Case Card Template

Use this template for draft outputs from the `lunar-source-ingestion` skill. Drafts should be reviewed before being promoted to `data/cases/` or `data/failure_kb.json`.

```markdown
---
id: <mission_or_event_id>
mission: <mission name>
organization: <agency/company/team>
date: <YYYY-MM-DD or unknown>
outcome_class: <SUCCESS | LOST | TIPPED_SURVIVED | TIPPED_LOST | NO_LANDING_ATTEMPT | other>
method_view: CAST incident card + STPA future review check
source_type: <primary | near-primary | secondary>
primary_source: <url or local path>
supporting_sources:
  - <url or local path>
confidence: <HIGH | MEDIUM-HIGH | MEDIUM | LOW-MEDIUM | LOW>
confidence_notes: <short caveat>
failure_classes:
  - <generalized failure class>
linked_design_checks:
  - <existing design_check id, if applicable>
review_gate_focus:
  - <Concept Readiness | Preliminary Design Readiness | Critical Design Readiness | Integration/Test Readiness | Flight/Operations Readiness>
extraction_status: draft
---

# <Mission/Event> — <short failure-class title>

## Source inventory

| Source | Type | Authority | Notes |
|---|---|---|---|
| <title/url/path> | <primary/near-primary/secondary> | <agency/company/etc.> | <coverage and limitations> |

## Evidence layer — what happened

<Concise source-supported event summary. Distinguish established facts from uncertain claims.>

### Key quoted evidence

> "<short quote>" — <source, page/section if available>

## CAST reading — how the control structure failed

- **Loss**: <loss or degraded mission value>
- **Controlled process**: <process>
- **Controller(s)**: <controllers>
- **Control action(s)**: <actions>
- **Feedback problem**: <missing/delayed/incorrect feedback>
- **Incorrect process model**: <assumption or mental/software model problem>
- **Inadequate constraint**: <missing/weak constraint>
- **Organizational/review factor**: <only if source-supported>
- **Reusable failure class**: <failure class>

## STPA-derived future review check

- **Hazard**: <hazard>
- **Unsafe control action**: <UCA>
- **Unsafe-control-action type**: <not provided | provided when unsafe | too early/late/wrong order | stopped too soon/applied too long>
- **Causal scenario**: <future scenario>
- **Derived safety constraint**: <constraint>

## Review evidence by gate

- **Concept Readiness**: <MCR/SRR-style evidence>
- **Preliminary Design Readiness**: <PDR-style evidence>
- **Critical Design Readiness**: <CDR-style evidence>
- **Integration/Test Readiness**: <SIR/TRR/SAR-style evidence>
- **Flight/Operations Readiness**: <ORR/FRR/MRR-style evidence>

## Precedent-backed rationale

<Explain why this past occurrence makes a similar ConOps feature review-worthy. Include caveats if proximate causes differ.>

## Open questions for domain experts

- <question>

## Promotion notes

- Existing `data/failure_kb.json` mission ID: <id or none>
- Existing `data/cases/` card: <path or none>
- Recommended action: <new card | update existing card | source inventory only | adjacent-corpus follow-up>
```
