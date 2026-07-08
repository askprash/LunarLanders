# CAST/STPA Case Cards

These case cards are the pilot human-readable layer above `data/failure_kb.json`.

- **CAST side**: explains a past event as a control-structure and feedback failure, not just a proximate root cause.
- **STPA side**: turns that lesson into future unsafe-control-action questions, derived safety constraints, and review-gate evidence.

Primary method reference: Nancy G. Leveson, **"A New Accident Model for Engineering Safer Systems,"** *Safety Science* 42(4), 237–270, 2004. PDF: http://sunnyday.mit.edu/accidents/safetyscience-single.pdf

Method notes: `docs/methods/stpa-cast.md`.

## Pilot Cases

- `hakuto_r_m1.md` — valid terrain-induced altimeter step rejected as an outlier.
- `hakuto_r_m2.md` — loss-critical LRF under-performance with no dissimilar terminal-ranging fallback.
- `beresheet.md` — IMU recovery command propagated into flight-computer reboot and engine shutdown.
- `luna_25.md` — accelerometer liveness failure before an irreversible burn.
- `im_1_odysseus.md` — disabled primary rangefinders and incomplete backup-sensor integration.
- `im_2_athena.md` — noisy laser altimetry plus polar lighting/terrain-model mismatch and poor tip-over survivability.

## Schema Pattern

Each card uses YAML frontmatter for machine parsing and Markdown for human review. Keep both parts consistent with `data/failure_kb.json`; the JSON remains the current source of record until this pilot proves useful.
