# STPA and CAST Method Backbone

This project uses Nancy Leveson's STAMP family of methods as the safety-analysis backbone for turning lunar-landing history into future design-review evidence.

## Primary Reference

The foundational paper for the accident model is:

- Nancy G. Leveson, **"A New Accident Model for Engineering Safer Systems,"** *Safety Science* 42(4), 237–270, 2004. PDF: http://sunnyday.mit.edu/accidents/safetyscience-single.pdf

Useful method handbooks from Leveson's MIT group:

- **STPA Handbook**: https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf
- **CAST Handbook**: http://sunnyday.mit.edu/CAST-Handbook.pdf
- MIT PSASS books and handbooks index: https://psas.scripts.mit.edu/home/books-and-handbooks/

## What We Mean

**STAMP** is the broader systems-theoretic accident model. It treats accidents as failures of constraints and control in a socio-technical system, not merely as chains of component failures.

**CAST** is the retrospective method. We use it to structure past lunar-landing events: what control structure existed, what feedback or process-model assumptions failed, what constraints were missing or ineffective, and what recommendations follow.

**STPA** is the proactive method. We use it to red-team future ConOps and design-review packages: what unsafe control actions could occur, what causal scenarios could produce them, and what safety constraints or review evidence should be required before a review gate.

## How This Applies Here

For the failure-memory database, CAST-shaped incident records should capture:

- mission/event and loss or degraded mission value;
- control structure: ground, onboard autonomy, flight software, sensors, actuators, operators, review boards;
- flawed or missing feedback;
- incorrect process-model assumptions;
- inadequate constraints or enforcement;
- causal scenario and propagation chain;
- recommendation, confidence, and source quote.

For the red-team reviewer, STPA-shaped future checks should capture:

- loss and hazard;
- relevant ConOps phase;
- control action;
- unsafe control action type: not provided, provided when unsafe, too early/late/wrong order, stopped too soon/applied too long;
- causal scenario;
- derived safety constraint;
- required review evidence at SRR, PDR, CDR, or later readiness gates;
- linked historical precedents.

## Review-Gate Crosswalk

The product should use startup-friendly readiness gates while keeping a crosswalk to NASA lifecycle reviews:

- **Concept Readiness** -> MCR/SRR-style evidence
- **Preliminary Design Readiness** -> PDR-style evidence
- **Critical Design Readiness** -> CDR-style evidence
- **Integration/Test Readiness** -> SIR/TRR/SAR-style evidence
- **Flight/Operations Readiness** -> ORR/FRR/MRR-style evidence

This is a pragmatic product vocabulary, not a claim that startups should copy NASA process wholesale. See `docs/adr/0002-use-startup-readiness-gates-mapped-to-nasa-reviews.md`.

## Product Posture

The tool is a **review-readiness coach**, not a certification or compliance authority. It should produce readiness gaps, evidence requests, and cited red-team concerns for human review. It should not claim that a design passes PDR/CDR, is flight-ready, or is certified.

See `docs/adr/0003-position-as-review-readiness-coach-not-certification-tool.md`.

## Design Rule

The tool should avoid simplistic "root cause" language when a failure is better explained as a control-structure, feedback, timing, assumption, interface, or organizational-learning problem. A proximate bug can be recorded, but the reusable artifact is the **failure class** and the **safety constraint** it implies.
