# Central Research Claim

A source-cited lunar-lander failure memory, structured with CAST/STPA, can generate review-readiness questions that would have surfaced recurring failure classes before later missions repeated them.

The review questions must also point to **past occurrences** of the same or similar failure class. The point is not merely to say that a ConOps feature is suspicious; the tool should explain why it is worth reviewer attention by linking the concern to concrete historical precedents, source quotes, confidence levels, and the mitigation or safety constraint implied by those precedents.

## What Experts Should Evaluate

Academic and domain-expert reviewers should evaluate whether:

- the historical cases are source-cited and confidence-qualified;
- the source corpus is large and authoritative enough, prioritizing accident reports, failure reports, mishap investigation materials, NASA or equivalent technical reports, and company technical-cause analyses over secondary summaries;
- CAST/STPA adds useful structure rather than merely renaming ordinary mishap summaries;
- the failure classes are general enough to transfer across missions without erasing important differences in proximate cause;
- the generated review-readiness questions are specific enough to guide SRR/PDR/CDR-style evidence requests;
- the precedent links provide a persuasive rationale for why a ConOps feature deserves concern;
- hindcast examples avoid hindsight bias and do not claim prediction beyond the evidence.

## Non-Claims

This project does not claim that AI can certify a design, predict mission failure, replace domain experts, or prove that a ConOps is safe. The intended claim is narrower: cited precedent plus CAST/STPA structure can make foreseeable failure classes easier for human reviewers to notice and interrogate. The claim also depends on corpus quality; scaling to a larger authoritative lunar source corpus is part of the validation path, not an implementation detail.

## Corpus Boundary

The first validation corpus should remain lunar landing/descent focused. Adjacent corpora such as Mars EDL, launch-vehicle GNC, aviation/autonomy safety cases, or terrestrial STPA examples should be tracked for later expansion rather than mixed into the initial claim.
