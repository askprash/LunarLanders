---
id: hakuto_r_m1
mission: Hakuto-R Mission 1
company: ispace
date: 2023-04-25
outcome_class: LOST
method_view: CAST incident card + STPA future review check
primary_source: https://ispace-inc.com/news-en/?p=4691
supporting_source: https://ispace-inc.com/wp-content/uploads/2023/05/EN_ispace_release_20230506_Final-Results.pdf
confidence: HIGH
failure_classes:
  - terrain-unaware outlier rejection
  - single-string terminal altimetry
  - post-CDR change without full re-validation
linked_design_checks:
  - chk_single_string_ranging
  - chk_outlier_rejection
  - chk_terrain_db_validation
  - chk_post_cdr_change
review_gate_focus:
  - PDR
  - CDR
  - FRR
---

# Hakuto-R Mission 1 — Terrain step rejected as sensor failure

## Evidence layer — what happened

During terminal/vertical descent, the lander crossed the rim of Atlas crater. The laser altimeter reported a large altitude change that was consistent with the terrain, but the onboard filter classified the measurement as anomalous and rejected it. The lander continued with an internal altitude estimate near zero while true altitude was several kilometers, exhausted propellant, and impacted the Moon.

The landing site had changed after CDR, and the new terrain corridor was not adequately represented in the validation cases.

## CAST reading — how the control structure failed

- **Loss**: lander lost during terminal descent.
- **Controlled process**: vertical descent state estimation and braking/landing sequence.
- **Controller**: onboard GNC software and altitude-estimation filter.
- **Control action**: accept or reject altimeter measurements used for terminal descent state estimation.
- **Feedback problem**: valid laser-altimeter feedback was blocked as an outlier.
- **Incorrect process model**: the lander/software behaved as if the altitude estimate near zero was credible while true altitude was much higher.
- **Inadequate constraint**: outlier rejection was not constrained by a terrain-aware sanity model and did not require independent confirmation before quarantining loss-critical altitude data.
- **Organizational/review factor**: post-CDR landing-site change did not trigger sufficient re-simulation of the new route's terrain.

## STPA-derived future review check

- **Hazard**: lander conducts terminal descent with an invalid altitude state.
- **Unsafe control action**: the navigation filter rejects a valid altitude measurement when terrain produces a large but real altitude discontinuity.
- **Unsafe-control-action type**: needed feedback/control input is not provided to the estimator; rejection occurs at the wrong time/context.
- **Causal scenario**: crater-rim or local terrain step exceeds a filter threshold tuned to the planned trajectory rather than terrain reality.
- **Derived safety constraint**: terminal-descent altitude filtering must distinguish sensor faults from terrain-induced altitude changes using route-specific terrain data, sensor fusion, or independent confirmation before rejecting loss-critical measurements.

## Review evidence by gate

- **SRR**: terminal-descent hazards include terrain-induced altitude discontinuities and stale altitude-state propagation.
- **PDR**: preliminary GNC architecture shows how terrain, map uncertainty, and sensor-fusion assumptions bound altitude filtering.
- **CDR**: validated terrain-aware filter behavior against the actual landing corridor, including crater-rim discontinuities and map-error cases.
- **FRR**: any post-CDR landing-site, route, terrain-database, software, or sensor-processing change has closed regression evidence.

## Human-readable lesson

Do not only ask whether the altimeter works. Ask whether the system can recognize when a surprising altimeter reading is true.
