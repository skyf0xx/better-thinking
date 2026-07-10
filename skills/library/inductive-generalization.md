---
name: inductive-generalization
description: >
  Generalize from observed instances to a rule, with explicit checks on
  sample size, representativeness, and scope. Use when concluding anything
  of the form "Xs tend to Y" from a set of cases, or when evaluating
  someone else's generalization.
type: atomic
category: reasoning
difficulty: 2
tokens: ~790
dependencies: []
related: [reference-class-forecasting, statistical-audit, disconfirmation-search]
---

# Inductive Generalization

Generalize from observed instances to a rule, with explicit checks on sample size, representativeness, and scope.

## Why

Generalization is unavoidable — it's how anecdotes could ever become useful knowledge — but ungoverned generalization is exactly how anecdotes wrongly become treated as facts. The checks here turn generalization from a leap into a graded inference with an honest scope.

## Use when / Don't use when

- **Use when:** concluding anything of the form "Xs tend to Y" from a set of cases; evaluating someone else's generalization before accepting it.
- **Don't use when:** a mechanism-level causal explanation is already available — prefer a causal analysis over pattern-matching from instances.

## Inputs → Outputs

- **Inputs:** a set of observations.
- **Outputs:** a candidate generalization with explicit scope limits and a confidence grade.

## Principles

- The sample's selection process matters more than its size — a huge biased sample is worse than a small representative one.
- The generalization's scope must not exceed the sample's actual coverage.
- Seek the counterexample before publishing the rule, not after.

## Procedure

1. State the candidate rule and the specific instances supporting it.
2. Describe how the instances were selected; name the selection biases that process invites.
3. Check coverage: what sub-populations, conditions, or time periods does the sample miss entirely?
4. Actively search for counterexamples within reach, rather than only counting confirmations.
5. Narrow the rule's scope until it's genuinely supported by the actual coverage of the sample.
6. Grade confidence and state what additional evidence would strengthen or break the rule — this is the residual uncertainty to carry forward.

## Common mistakes

- Counting confirmations while never sampling for disconfirmations.
- Generalizing from survivors — the cases that didn't make it into the sample often didn't for a reason (the dead don't report).
- Scope creep: the rule quietly gets applied more broadly later than the sample ever supported.

## Examples

- Deciding whether five user complaints indicate a systemic UX issue or five unlucky edge cases.
- Judging whether a drug's trial population licenses claims about elderly patients who weren't well-represented in the trial.
- Inferring a general coding pattern from three example repositories.

## Related

- [[reference-class-forecasting]] — uses a well-scoped generalization as its base rate.
- [[statistical-audit]] — the deeper quantitative check on a generalization's numeric support.
- [[disconfirmation-search]] — the active-search discipline this skill's step 4 depends on.
