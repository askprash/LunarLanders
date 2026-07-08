# Lunar Lander Failure-Memory Red Team

This context covers the language of a failure-memory and AI-assisted review workflow for lunar lander concepts of operations and design-review packages. It exists to keep collaborators precise about historical incident learning, review-gate readiness, and descent-design failure modes.

## Language

**Failure Memory**:
A curated, source-cited body of historical mission events, mishaps, partial successes, design weaknesses, and mitigations that can be reused during future design reviews.
_Avoid_: Knowledge graph, database, lessons learned archive, corpus — unless referring to a specific implementation.

**Failure Class**:
A recurring, generalizable pattern by which a mission can lose safety, mission value, or landing capability, independent of the exact proximate bug in one incident.
_Avoid_: Root cause, bug, incident, anomaly.

**Historical Precedent**:
A past lunar landing event used as evidence that a failure class is real, recurring, or review-worthy for a future ConOps.
_Avoid_: Example, anecdote.

**Precedent-Backed Rationale**:
The explanation that connects a red-team concern in a future ConOps to specific past occurrences, source evidence, confidence levels, and derived mitigations or safety constraints.
_Avoid_: Warning, intuition, generic risk statement.

**Deterministic Sweep**:
The non-LLM review pass that queries the structured failure memory and applies explicit matching rules before any semantic model is asked to interpret a ConOps.
_Avoid_: AI review, agent pass.

**Semantic Review**:
The LLM-assisted pass that receives the ConOps, the structured knowledge-base context, and the deterministic sweep report, then reasons about meaning, caveats, false positives, and precedent-backed rationale.
_Avoid_: Deterministic matching, certification.

**LLM Guardrail**:
A constraint on the semantic review stage that prevents the model from inventing precedents, upgrading confidence, claiming certification, erasing proximate-cause differences, or treating absence of mitigation as proof of risk.
_Avoid_: Prompt instruction — unless discussing implementation wording.

**Queryable Failure Memory**:
The structured storage layer for historical precedents, failure classes, source evidence, checks, and review-gate mappings that can be filtered or retrieved before LLM analysis.
_Avoid_: Vector database, knowledge graph — unless referring to a chosen implementation.

**Authoritative Source Corpus**:
A larger, higher-confidence collection of primary or near-primary records such as accident reports, failure reports, mishap investigation materials, agency technical reports, NASA NTRS documents, company technical-cause analyses, and equivalent sources.
_Avoid_: Web corpus, article dump.

**Extracted Claim**:
A source-backed atomic statement pulled from an authoritative source before it has been promoted into a case card, design check, or canonical failure-memory record.
_Avoid_: Fact, finding — unless the claim has been reviewed and accepted.

**Draft Case Card**:
A human-review artifact that assembles extracted claims into a CAST/STPA narrative for a mission or event when the source evidence is strong enough.
_Avoid_: Canonical record, final case.

**Curation Approval**:
A non-domain-expert approval that checks source traceability, quote accuracy, schema completeness, and caveat labeling before a draft is shared for expert review.
_Avoid_: Domain validation, certification.

**Domain Validation**:
A review by someone with relevant spacecraft, GNC, mission-assurance, safety-analysis, or lunar-operations expertise who can judge whether the failure-class abstraction and CAST/STPA mapping are technically credible.
_Avoid_: Owner approval, editorial review.

**Validation Status**:
The explicit maturity label attached to a source, claim, case card, or design check, such as draft, curated, domain-reviewed, or accepted.
_Avoid_: Approved — unless the approver type is stated.

**Artifact Maturity Label**:
A visible label in walkthroughs or reports that distinguishes evidence from interpretation, such as official source, extracted claim, draft case card, curated-not-domain-validated, example deterministic match, or example LLM interpretation.
_Avoid_: Status — unless the maturity dimension is clear.

**Scalable Retrieval Layer**:
A future retrieval implementation, potentially vector, hybrid lexical/vector, graph, or database-backed, that can query a much larger failure corpus while preserving source citations and auditability.
_Avoid_: Vector database — unless vector retrieval is the selected implementation.

**Lunar Landing Event**:
A mission outcome or operational episode during lunar approach, descent, landing, touchdown, or early surface safing that provides evidence about lander design risk.
_Avoid_: Case study, mishap — unless the event is specifically a failure.

**ConOps**:
The operational narrative that explains how the lander, ground team, autonomy, sensors, actuators, and mission phases are expected to work together.
_Avoid_: Requirements document, design spec.

**Red-Team Review**:
An adversarial design review that asks how a proposed lander ConOps or review package could repeat known failure classes, then returns cited concerns and mitigations.
_Avoid_: Audit, verification, certification.

**Review Gate**:
A maturity checkpoint such as SRR, PDR, CDR, SIR, TRR, ORR, or FRR where the team must show evidence that the design and project baseline are ready to proceed.
_Avoid_: Deadline, timeline, milestone — unless referring to a calendar plan.

**Review Evidence**:
The artifacts, analyses, test results, decisions, margins, waivers, and traceability records used to satisfy a review gate.
_Avoid_: Documentation, paperwork.

**Review-Gate Readiness**:
The product-facing assessment of whether a team has the right evidence, owners, traceability, margins, risks, and open actions to pass a specific review gate such as SRR, PDR, CDR, ORR, or FRR.
_Avoid_: Compliance checklist, schedule readiness.

**Startup Readiness Gate**:
A startup-friendly maturity gate that asks for NASA-style evidence without requiring the team to adopt NASA's exact lifecycle bureaucracy; examples include Concept Readiness, Preliminary Design Readiness, Critical Design Readiness, Integration/Test Readiness, and Flight/Operations Readiness.
_Avoid_: NASA review, informal milestone.

**Readiness Gap**:
A missing, weak, or untraceable piece of evidence that a serious reviewer would expect before accepting a design's maturity for a review gate.
_Avoid_: Noncompliance, failure, certification issue.

**Review-Readiness Coach**:
The intended product role: a tool that surfaces readiness gaps, evidence requests, and cited red-team concerns for human review, without claiming to certify or approve a space system.
_Avoid_: Certification tool, compliance authority, flight-readiness approver.

**Interactive Architecture Walkthrough**:
A visual, clickable explanation of the pipeline from source corpus to extracted claims, case cards, deterministic sweep, LLM semantic review, and readiness gaps.
_Avoid_: Static diagram, slide — unless no interactivity is intended.

**Academic Validation Audience**:
The first target audience for evaluating whether the method, corpus, hindcasts, and STPA/CAST framing are credible before the tool is positioned for startup use.
_Avoid_: Customer, user, buyer.

**Startup Engineering Team**:
A later primary practitioner audience that would use the validated method to prepare ConOps and review evidence for internal, customer, investor, or mission-assurance reviews.
_Avoid_: First validation audience.

**Technical Diligence Reviewer**:
A secondary audience that uses the tool's cited concerns and readiness gaps to evaluate whether a startup's design story is mature, traceable, and evidence-backed.
_Avoid_: Certifier, regulator.

**STAMP**:
Nancy Leveson's systems-theoretic accident model that treats safety as a control problem across technical, human, organizational, and operational layers.
_Avoid_: STPA, CAST — those are methods within the STAMP family.

**STPA**:
Nancy Leveson's System-Theoretic Process Analysis method for identifying hazards, unsafe control actions, causal scenarios, and derived safety constraints before an accident occurs.
_Avoid_: PATH, STAMP — STAMP is the broader accident model; STPA is the proactive analysis method.

**CAST**:
Nancy Leveson's Causal Analysis based on STAMP method for learning from an incident or accident without reducing it to a single root cause.
_Avoid_: Root-cause analysis, postmortem.

**Control Structure**:
The system model of controllers, controlled processes, feedback paths, control actions, and process models used to reason about unsafe control in STPA or CAST.
_Avoid_: Architecture diagram, org chart.

**Unsafe Control Action**:
A control action that can create a hazard because it is provided, not provided, provided too early or too late, or stopped too soon or applied too long.
_Avoid_: Failure mode, operator error.

**Causal Scenario**:
A plausible chain of conditions, assumptions, feedback problems, model flaws, timing errors, or coordination gaps that can lead to an unsafe control action or hazard.
_Avoid_: Prompt, test case, story.

**Derived Safety Constraint**:
A design or operational constraint produced by hazard analysis that must hold to prevent or control a hazardous scenario.
_Avoid_: Recommendation, mitigation, checklist item.

**Terminal Descent**:
The late powered-descent phase in which altitude, velocity, attitude, hazard avoidance, touchdown sensing, and abort or safing options are most tightly coupled.
_Avoid_: Landing, final approach — unless the broader phase is intended.

**GNC**:
Guidance, navigation, and control functions that estimate lander state, choose the descent path, and command attitude, thrust, or divert behavior.
_Avoid_: Autonomy, flight software — unless discussing those narrower responsibilities.

**Single-String Sensor**:
A sensor chain whose loss, invalid output, or late data can become loss-critical because no independent fallback can provide the same needed state estimate in time.
_Avoid_: Single sensor, primary sensor.

**Dissimilar Redundancy**:
An independent backup capability that uses a meaningfully different sensing or control path, so it is less likely to share the same failure mechanism as the primary path.
_Avoid_: Redundancy, spare, second unit.

**Graceful Degradation**:
The ability to continue delivering mission value or reach a safer state after a fault by reducing capability rather than cascading to total loss.
_Avoid_: Fault tolerance, backup mode.

**Sensor Liveness**:
Evidence that a sensor chain is powered, enabled, producing fresh data, and accepted by downstream logic before it is relied on for an irreversible burn, divert, or landing decision.
_Avoid_: Health check, validity flag — unless referring to a specific mechanism.

**Terrain-Aware Sanity Model**:
Logic that judges sensor measurements against possible terrain, trajectory, and map variation rather than rejecting unexpected values solely because they differ from a propagated estimate.
_Avoid_: Outlier rejection, measurement gating.

**Known Risk Acceptance**:
A deliberate decision to fly with an unresolved or not-flight-proven weakness, with explicit rationale, ownership, evidence, and residual-risk posture.
_Avoid_: Open issue, assumption, waiver — unless the risk has been formally accepted.

**Post-CDR Change**:
A design, landing-site, ConOps, software, hardware, or operations change after Critical Design Review that can invalidate earlier analysis and therefore requires targeted re-validation.
_Avoid_: Late change, design update.

**Survivability**:
The ability to limit the loss of mission value after a finite-duration disturbance, such as a tip-over, transient sensor loss, or reboot cascade.
_Avoid_: Robustness.

**Robustness**:
The ability to maintain specified performance across expected variation in terrain, lighting, sensor behavior, propulsion behavior, software timing, and operations.
_Avoid_: Survivability.
