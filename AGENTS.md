# AGENTS.md

Guidance for collaborators and AI agents working in this repository.

## Project Purpose

This repo is a prototype for turning lunar-lander incident history into a source-cited **failure memory** that can red-team future lander ConOps and design-review packages. The core output should help a startup or mission team answer:

- What historically recurring failure classes does this design resemble?
- What evidence should be ready for SRR/PDR/CDR and later readiness reviews?
- Which hazards, unsafe control actions, and review gaps deserve human attention now?

## Start Here

1. Read `README.md` for the product shape and commands.
2. Read `CONTEXT.md` for canonical domain language.
3. Read `data/failure_kb.json` for the current failure memory.
4. Read `examples/README.md` before changing match/review logic; it captures known false-positive and false-negative behavior.
5. Read `redteam.py` for the reference implementation.
6. Treat `sandbox/` as useful local research context, not committed product truth. It is ignored by git.

## Current Architecture

- `data/failure_kb.json` is the committed structured failure memory.
- `redteam.py` is the CLI, local server, provider bridge, keyword matcher, and LLM/agent review path.
- `lunar_redteam_demo.html` is a static browser demo and currently duplicates some knowledge-base and prompt logic.
- `examples/` is the public regression corpus for realistic lunar descent/design prose.

When changing design checks, prompts, schemas, or provider behavior, check whether both `redteam.py` and `lunar_redteam_demo.html` need updates. Avoid letting the HTML demo drift from the JSON-backed CLI.

## Method Backbone

Use Nancy Leveson's **STAMP** family precisely. See `docs/methods/stpa-cast.md` and ADR `docs/adr/0001-use-stpa-and-cast-as-method-backbone.md`.

Primary paper: Nancy G. Leveson, ["A New Accident Model for Engineering Safer Systems"](http://sunnyday.mit.edu/accidents/safetyscience-single.pdf), *Safety Science* 42(4), 237–270, 2004.

- **STPA** is the proactive hazard-analysis method for future designs.
- **CAST** is the retrospective accident/incident-learning method.
- The user may say "path"; interpret that as likely **STPA** unless they clarify otherwise.

A useful future database should map historical events and review findings to:

- losses, hazards, safety constraints;
- control structure elements;
- control actions and unsafe control actions;
- causal scenarios;
- derived requirements or review evidence;
- verification, validation, simulation, or red-team tests;
- residual risks, waivers, and review actions.

Use NASA lifecycle reviews as maturity gates, not merely dates. SRR/PDR/CDR content should be modeled as evidence linked to requirements, risks, interfaces, margins, V&V plans/results, waivers, and open actions.

## Source and Evidence Rules

- Keep claims source-cited and confidence-qualified.
- Do not overstate agency/company statements when a full mishap report is unavailable.
- Distinguish proximate cause from reusable failure class.
- Prefer "this resembles a known failure class" over "this will fail."
- A finding needs affirmative evidence in the design text. Do not flag solely because a mitigation is absent.
- Do not treat a word such as "lidar" or "Doppler" as redundancy unless the text shows an independent fallback path.
- Record when a risk was knowingly accepted, waived, or left unresolved.

## Review-Gate Orientation

For startup-facing review support, organize recommendations around evidence readiness:

- **SRR**: stakeholder expectations, ConOps, top-level requirements, initial risks, initial V&V approach, and requirement traceability.
- **PDR**: credible preliminary design, flowed-down requirements, defined interfaces, trade studies, technical margins, risk posture, integration approach, and baselined V&V plan.
- **CDR**: detailed product baseline, build-to data, finalized interfaces, AI&T plans/procedures, command/telemetry lists, safety analyses, single-point-failure rationale, and mature verification evidence.
- **Later reviews**: integration/test readiness, operational readiness, acceptance evidence, certification, unresolved liens, and final flight/use readiness.

Tailor NASA-style rigor to mission class and customer expectations; do not copy bureaucracy wholesale.

## Validation Expectations

After logic or data changes, run at least:

```bash
python3 redteam.py
python3 redteam.py examples/teamindus_arxiv.txt
python3 redteam.py examples/lunar_pallet_lander_NTRS.txt
python3 redteam.py examples/polito_thesis.txt
```

If LLM keys are available, also run representative `--agent` checks because agent mode is intended for real ConOps text.

Expected regression themes from `examples/README.md`:

- flag single-string ranging in Pallet Lander, NDL, Morpheus, and TeamIndus cases;
- do not treat "sun sensors were rejected" as measurement outlier rejection;
- credit TeamIndus lighting/terrain handling where supported;
- do not return LOW RISK on the Polito thesis merely because it uses unfamiliar vocabulary.

## Safety, Secrets, and Provider Handling

- Do not put API keys in files, examples, screenshots, or browser-side defaults.
- Prefer `python3 redteam.py --serve --provider parley` or another local-server flow so keys stay in environment variables.
- Supported key env vars are documented in `README.md` and `redteam.py`.

## Documentation Discipline

- Update `CONTEXT.md` when terminology is resolved or sharpened.
- Keep `CONTEXT.md` to domain language only; do not use it as a spec or implementation plan.
- Use an ADR only for hard-to-reverse, non-obvious decisions with real tradeoffs.
- If you introduce review-gate, STPA/CAST, or database-schema decisions, document why they were chosen and what alternatives were rejected.

<!-- BACKLOG.MD GUIDELINES START -->
<CRITICAL_INSTRUCTION>

## Backlog.md Workflow

This project uses Backlog.md for task and project management.

**For every user request in this project, run `backlog instructions overview` before answering or taking action.**

Use the overview to decide whether to search, read, create, or update Backlog tasks.

Use the detailed guides when needed:
- `backlog instructions task-creation` for creating or splitting tasks
- `backlog instructions task-execution` for planning and implementation workflow
- `backlog instructions task-finalization` for completion and handoff

Use `backlog <command> --help` before running unfamiliar commands. Help shows options, fields, and examples.

Do not edit Backlog task, draft, document, decision, or milestone markdown files directly. Use the `backlog` CLI so metadata, relationships, and history stay consistent.

</CRITICAL_INSTRUCTION>
<!-- BACKLOG.MD GUIDELINES END -->
