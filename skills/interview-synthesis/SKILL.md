---
name: interview-synthesis
description: >
  Design non-leading questions, conduct inquiry-driven interviews, and
  cluster raw responses into findings that survive scrutiny. Use when the
  knowledge you need lives in people's experience — users, experts,
  witnesses, stakeholders — and you're validating assumptions about what
  others think or do.
type: composite
category: research
difficulty: 3
tokens: ~900
dependencies: [question-decomposition, active-listening, precision-questioning, inductive-generalization, epistemic-tagging, frame-detection]
related: [delphi-aggregation, empathy-mapping]
---

# Interview Synthesis

Design non-leading questions, conduct inquiry-driven interviews, and cluster raw responses into findings that survive scrutiny — UX research's core loop, generalized.

## Why

People misreport their own behavior, and interviewers hear what they hoped to hear. Discipline at both ends of the process — question design and synthesis — is what separates evidence from a collection of flattering anecdotes.

## Use when / Don't use when

- **Use when:** the knowledge lives in people's experience — users, experts, witnesses, stakeholders; validating assumptions about what others think or do.
- **Don't use when:** the behavior is directly observable — watch instead of ask; or the question is factual and better answered by a direct source.

## Inputs → Outputs

- **Inputs:** a learning goal and access to relevant people.
- **Outputs:** clustered findings with supporting quotes, confidence grades, and an explicit line between observation and interpretation.

## Principles

- Past behavior beats hypothetical opinion — "walk me through the last time" outperforms "would you."
- The interviewer's own hypothesis must not leak into the questions.
- Synthesis clusters *observations*; interpretation is a separate, labeled step, never blended in during capture.
- A disconfirming interviewee is worth more than a confirming one — sample for them deliberately.

## Procedure

1. Define the learning goals by running `question-decomposition`: what decisions will this research actually feed?
2. Draft the interview guide with open, behavioral questions and no embedded conclusions. Audit the guide with `frame-detection` to catch leading phrasing. Plan the sample deliberately, including people likely to disconfirm the working hypothesis.
3. Conduct each interview using `active-listening` — follow the surprise, not the script — and `precision-questioning` to move from generality ("it's confusing") to a concrete instance ("show me where").
4. Record observations verbatim; tag interpretation separately at the moment of capture using `epistemic-tagging`, so the two never merge silently.
5. Cluster observations across interviews. A finding needs multiple independent instances — use `inductive-generalization`'s sample-quality checks before generalizing from a cluster.
6. For each finding, state it, grade its support (how many instances, how independent, how direct), and attach the disconfirming evidence found, if any.
7. Report findings separately from recommendations. State which learning goals remain open as residual uncertainty.

## Common mistakes

- Leading questions — "wouldn't it be easier if…" — that hand the interviewee the answer.
- Treating stated intent as a predictor of actual future behavior.
- Clustering responses by the theme you expected going in, rather than what the data actually contains.
- Sampling only the willing — the people who respond are rarely representative of the people who matter.
- Selecting quotes to decorate a conclusion that was already decided before synthesis began.

## Examples

- Discovery interviews run before committing to build a product feature.
- Expert elicitation on the likelihood and shape of an emerging risk.
- Exit interviews mined across many departures for a systemic organizational pattern.
- Witness interviews in an investigation, synthesized into a fact pattern.

## Related

- [[delphi-aggregation]] — the structured, anonymous, multi-round version for expert panels specifically.
- [[empathy-mapping]] — typically consumes this skill's output to reconstruct what users perceive, think, feel, and need.
