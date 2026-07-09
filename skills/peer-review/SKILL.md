---
name: peer-review
description: >
  Structured evaluation of another's work for correctness, rigor, and
  significance - feedback that a capable stranger could act on. Use when
  evaluating work before it ships, publishes, or gets relied upon.
type: composite
category: analysis
difficulty: 3
tokens: ~710
dependencies: [critical-reading, methodology-critique, assumption-audit, steelmanning]
related: [methodology-critique, feedback-delivery, revision-pass]
---

# Peer Review

Structured evaluation of another's work for correctness, rigor, and significance — feedback that a capable stranger could act on.

## Why

Unstructured review drifts to style nitpicks or vague praise, missing the load-bearing question: does this work actually establish what it claims? A repeatable structure catches that and produces actionable feedback either way.

## Use when / Don't use when

- **Use when:** evaluating work before it ships, publishes, or gets relied upon; giving feedback that needs to be actionable, not just reactive.
- **Don't use when:** a quick sanity pass suffices — full peer review has real overhead.

## Inputs → Outputs

- **Inputs:** a piece of work plus its claimed contribution.
- **Outputs:** a structured verdict — significance, correctness, and specific actionable revisions — separated from stylistic preference.

## Principles

- Evaluate the claim actually made, not a stronger or weaker one you'd have preferred.
- Separate "this is wrong" from "this is not how I'd have done it" — only the former is a correctness finding.
- Every criticism should be actionable, or it's not feedback, it's a mood.
- Significance and correctness are independent axes.

## Procedure

1. Run `critical-reading`: extract the claimed contribution and its support.
2. Assess significance: if true, does this matter? To whom, how much?
3. Assess correctness: run `methodology-critique` and `assumption-audit` on the support. Does the evidence establish the claim at the strength claimed?
4. Steelman weak points before flagging them — is there a reading where this concern doesn't apply?
5. Separate findings into must-fix, should-fix, and stylistic.
6. Write the review: verdict, top findings ranked by severity, and for each, what specifically would resolve it.

## Common mistakes

- Style creep dominating the review.
- Vague verdicts ("needs work") without the specific fix.
- Reviewing the work you wish they'd done instead of the one they did.

## Examples

- Reviewing a research paper or grant proposal.
- A technical design review.
- Assessing a junior's analysis before it goes to a client.

## Related

- [[methodology-critique]] — the correctness engine this composite invokes.
- [[feedback-delivery]] — the mechanism for delivering the verdict.
- [[revision-pass]] — the natural next step for the author.
