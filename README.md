# Lunar Landers

Small research/demo tool for reviewing a lunar lander descent design against a structured record of past lunar landing failures.

The repository has two main pieces:

- `data/failure_kb.json`: a hand-built, cited failure-memory dataset covering robotic lunar soft-landing attempts from Chang'e 3 through Hakuto-R Mission 2.
- `redteam.py` and `lunar_redteam_demo.html`: a CLI and browser UI that compare a design text or ConOps excerpt against reusable failure patterns drawn from that dataset.

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
- `data/failure_kb.json`: mission records, reusable design checks, and built-in example design texts
- `.gitignore`: Python cache exclusions

## Quick Start

No third-party Python packages are required.

```bash
python3 redteam.py
python3 redteam.py design.txt
python3 redteam.py design.txt --agent
python3 redteam.py design.txt --llm
```

To run the local UI without exposing API keys to the browser:

```bash
MY_MIT_PARLEY_API_KEY=... python3 redteam.py --serve --provider parley
```

Then open `http://127.0.0.1:8787/`.

## Model Providers

LLM-backed modes read keys from the environment:

- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `MY_MIT_PARLEY_API_KEY`

Parley aliases are also supported:

- `MIT_PARLEY_API_KEY`
- `PARLEY_API_KEY`

The local server path exists so the browser can call a localhost JSON endpoint and keep the actual provider key in the Python process environment.

## Failure Memory Structure

`data/failure_kb.json` stores:

- mission records with dates, subsystem, proximate cause, generalizable weakness, source URL, confidence, and tags
- reusable design checks with severity, diagnostic question, keyword signals, precedent missions, and recommended mitigations
- built-in example design texts for demo and regression use

The emphasis is on reusable engineering lessons rather than generic summaries of lunar missions.

This repository is not just a landing-history dataset. It is a red-team review tool for lunar descent GNC designs, built to compare transparent rule-based matching against a more careful LLM analyst.

## Current State

This is a coherent prototype with a clear research/demo shape:

- the knowledge base is already substantial and citation-driven
- the Python script contains both the deterministic matcher and the LLM/agent pipeline
- the HTML UI is polished enough for interactive demos
- the project already contains built-in example design texts for demos and regression checks
