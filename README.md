# Lunar Landers

> **Prototype status:** This repository is under active development. It is a research/demo tool for exploring source-cited lunar-lander failure memory and review-readiness questions. It does **not** certify designs, determine flight readiness, or replace qualified mission-assurance review.

Small research/demo tool for reviewing a lunar lander descent design against a structured record of past lunar landing failures.

The repository has two main pieces:

- `data/failure_kb.json`: a hand-built, cited failure-memory dataset covering robotic lunar soft-landing attempts from Chang'e 3 through Hakuto-R Mission 2.
- `redteam.py` and `lunar_redteam_demo.html`: a CLI and browser UI that compare a design text or ConOps excerpt against reusable failure patterns drawn from that dataset.
- `examples/`: public lunar descent-design test cases used as a regression corpus for comparing keyword mode against semantic review.

## What It Does

You paste a descent or landing design description and the tool highlights historically recurring risk patterns such as:

- single-string terminal ranging
- outlier rejection without terrain awareness
- missing sensor-liveness checks before irreversible burns
- command/recovery paths that can disturb propulsion
- terrain database or lighting mismatch
- known open risks accepted into flight
- post-CDR changes without full re-validation
- weak survivability after tip-over
- insufficient engine-out or asymmetric-thrust tolerance

Each finding is tied back to precedent missions and an explicit mitigation recommendation.

## Method Backbone

The next architecture is organized around Nancy Leveson's STAMP family of systems-safety methods:

- **CAST** structures what we learn from past lunar-landing incidents.
- **STPA** structures how we red-team future ConOps and design-review packages.

See `docs/methods/stpa-cast.md` and ADR `docs/adr/0001-use-stpa-and-cast-as-method-backbone.md`. The foundational paper is Nancy G. Leveson, ["A New Accident Model for Engineering Safer Systems"](http://sunnyday.mit.edu/accidents/safetyscience-single.pdf), *Safety Science* 42(4), 237–270, 2004.

## Review Modes

`redteam.py` supports three review modes:

- `keyword` (default): offline, deterministic keyword matching against the checks in `data/failure_kb.json`
- `--llm`: one-pass semantic review by a language model
- `--agent`: multi-pass review that extracts supported facts, drafts findings, then audits for false positives and false mitigations

The code is explicit about the intended tradeoff:

- keyword mode is transparent and inspectable, but brittle on real prose
- agent mode is the mode intended for actual ConOps or design-review text

## Files

- `redteam.py`: CLI entrypoint, local HTTP server, provider selection, rendering, and all review logic
- `lunar_redteam_demo.html`: static browser UI with three tabs:
  - review a design
  - browse the failure record
  - inspect how the pipeline works
- `data/failure_kb.json`: mission records and reusable design checks
- `examples/`: six public ConOps/design texts used to stress the matcher on realistic prose
- `architecture_walkthrough.html`: standalone interactive architecture walkthrough for expert onboarding
- `.github/workflows/pages.yml`: GitHub Pages publishing workflow for the walkthrough and demo
- `docs/methods/stpa-cast.md`: project framing for STPA/CAST usage
- `docs/adr/0001-use-stpa-and-cast-as-method-backbone.md`: decision record for adopting STPA/CAST as the method backbone
- `pyproject.toml`, `uv.lock`, `.python-version`: `uv` environment metadata
- `.gitignore`: Python cache and local environment exclusions

## Quick Start

This repository uses [`uv`](https://docs.astral.sh/uv/) for Python environment management. No third-party Python packages are required today, but using `uv` keeps the Python version and lockfile workflow consistent for collaborators.

Install `uv` if needed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create or refresh the local environment:

```bash
uv sync
```

Run the reviewer through the managed environment:

```bash
uv run redteam.py
uv run redteam.py design.txt
uv run redteam.py examples/teamindus_arxiv.txt
uv run redteam.py design.txt --agent
uv run redteam.py design.txt --llm
```

To run the local UI without exposing API keys to the browser:

```bash
MY_MIT_PARLEY_API_KEY=... uv run redteam.py --serve --provider parley
```

Then open `http://127.0.0.1:8787/`.

## Development Notes

This repository uses [Backlog.md](https://github.com/MrLesk/Backlog.md) for task tracking. Before planning or changing non-trivial work, run:

```bash
backlog instructions overview
```

Use the `backlog` CLI to create, update, and complete tasks; do not edit Backlog task files directly. The `.backlog/` directory is intentionally part of the repository and should be committed so collaborators share the same task state.

Project-local Pi skills live under `.pi/skills/` and should also be committed when they encode reusable workflows. The first project skill is:

```text
/skill:lunar-source-ingestion
```

Use it when collaborators provide lunar landing/descent PDFs, reports, or source texts that need to be converted into draft failure-memory records or CAST/STPA case-card material.

The standalone architecture walkthrough is published by GitHub Actions / GitHub Pages. Once Pages is enabled for this repository, reviewers should be able to open:

- `https://askprash.github.io/LunarLanders/` — interactive architecture walkthrough
- `https://askprash.github.io/LunarLanders/demo.html` — original browser demo

## Model Providers

LLM-backed modes read keys from the environment:

- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `MY_MIT_PARLEY_API_KEY`

Parley aliases are also supported:

- `MIT_PARLEY_API_KEY`
- `PARLEY_API_KEY`

The local server path exists so the browser can call a localhost JSON endpoint and keep the actual provider key in the Python process environment.

### Safe local Parley key setup

Do **not** paste API keys into source files, notebooks, screenshots, committed docs, or browser-side configuration. Keep keys only in your local shell environment.

Recommended one-time setup for macOS/Linux with `zsh`:

```bash
# Replace the placeholder with your actual Parley key.
# Do not include spaces around the equals sign.
echo 'export MY_MIT_PARLEY_API_KEY="YOUR_PARLEY_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```

For a single terminal session only:

```bash
export MY_MIT_PARLEY_API_KEY="YOUR_PARLEY_KEY_HERE"
```

Then run the local server so the browser talks only to `localhost` and never sees the key directly:

```bash
uv run redteam.py --serve --provider parley
```

Open `http://127.0.0.1:8787/` and select the local-server option in the UI.

Safety checks before committing or pushing:

```bash
# Confirm the key is available locally.
uv run python - <<'PY'
import os
print('Parley key configured:', bool(os.environ.get('MY_MIT_PARLEY_API_KEY')))
PY

# Confirm no API key value was accidentally staged.
git diff --staged
```

Local `.env` files are ignored by `.gitignore`, but shell environment variables are preferred for this project. If a student does use a local `.env`, it must stay uncommitted.

## Failure Memory Structure

`data/failure_kb.json` stores:

- mission records with dates, subsystem, proximate cause, generalizable weakness, source URL, confidence, and tags
- reusable design checks with severity, diagnostic question, keyword signals, precedent missions, and recommended mitigations

The emphasis is on reusable engineering lessons rather than generic summaries of lunar missions.

This repository is not just a landing-history dataset. It is a red-team review tool for lunar descent GNC designs, built to compare transparent rule-based matching against a more careful LLM analyst.

## Audience Sequence

The next phase should start as an academic/domain-expert validation effort: test whether the corpus, CAST/STPA framing, hindcast logic, source quality, and review-gate evidence model are credible. Startup engineering teams and technical diligence reviewers are important later audiences, but the method should be validated before it is presented as an operational startup workflow.

Central claim: a source-cited lunar-lander failure memory, structured with CAST/STPA, can generate review-readiness questions that would have surfaced recurring failure classes before later missions repeated them. Those questions must be **precedent-backed**: they should point to past occurrences so reviewers can see why a particular ConOps feature is potentially problematic.

See `docs/adr/0004-start-with-academic-validation-before-startup-use.md`, `docs/research/central-claim.md`, and `docs/research/proposed-domain-expert-review-workflow.md`. The expert-review workflow is only a suggested handoff scaffold; domain experts should change it as needed.

For a concise domain-expert starting point, use `docs/research/expert-handoff-packet.md` rather than asking reviewers to inspect the whole repo. The interactive architecture walkthrough is a standalone static HTML page published by GitHub Actions; see `architecture_walkthrough.html` and `docs/adr/0009-publish-architecture-walkthrough-as-standalone-html.md`.

## Review Pipeline Direction

The review architecture should use a deterministic sweep before LLM semantic review:

1. Store past occurrences in a structured, queryable failure memory.
2. Run a deterministic Python pass that retrieves candidate precedents and applies explicit review checks.
3. Pass the ConOps, deterministic report, and relevant source-backed precedents to an LLM for semantic review, caveat handling, and precedent-backed explanation.

See `docs/architecture/review-pipeline.md` and `docs/adr/0005-use-deterministic-sweep-before-llm-semantic-review.md`.

## Examples Corpus

The `examples/` directory contains six genuinely public lunar-lander descent and landing design texts. They are useful because they are not written to match the tool's keywords; they are realistic prose inputs for regression testing.

This corpus is mainly there to expose the limitations of the offline matcher:

- false positives from literal keyword matches
- false mitigations where a sensor mention is mistaken for redundancy
- missed findings when the document uses different vocabulary than the built-in examples

For real design-review text, these files are the best demonstration of why `--agent` is the intended mode.

## Current State

This is a coherent prototype with a clear research/demo shape:

- the knowledge base is already substantial and citation-driven
- the Python script contains both the deterministic matcher and the LLM/agent pipeline
- the HTML UI is polished enough for interactive demos
- the project contains both built-in examples and a separate public regression corpus under `examples/`
