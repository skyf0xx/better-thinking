---
name: uncertainty-decomposition
description: >
  Split uncertainty about a quantity into its reducible and irreducible
  components, and report ranges rather than false-precision points. Use
  for any forecast that will inform a decision, or when deciding whether
  more research is worth the cost.
type: atomic
category: forecasting
difficulty: 3
tokens: ~770
dependencies: []
related: [sensitivity-analysis, monte-carlo-reasoning, confidence-calibration]
---

# Uncertainty Decomposition

Split uncertainty about a quantity into its reducible and irreducible components, and report ranges rather than false-precision points.

## Why

A single-point estimate hides whether the number is a near-certainty or a coin flip, and hides whether more research would even help. Decomposing uncertainty tells you both, and where to spend effort narrowing it.

## Use when / Don't use when

- **Use when:** any forecast or estimate that will inform a decision; a point estimate is being treated as exact; deciding whether more research is worth the cost.
- **Don't use when:** the quantity is actually knowable cheaply — just go look it up.

## Inputs → Outputs

- **Inputs:** an uncertain quantity or forecast.
- **Outputs:** a range, broken into reducible uncertainty (could be narrowed with more effort) and irreducible uncertainty (genuinely stochastic at this cost).

## Principles

- Report a range with a stated confidence level, not a bare point — the range is the honest answer.
- Ask "would more information narrow this?" — if yes, it's reducible; if no, it's irreducible and no analysis will shrink it further.
- Conflating the two leads to either wasted research effort or false confidence.

## Procedure

1. State the quantity and produce an initial range via fermi-estimation or reference-class-forecasting.
2. For the width of the range, ask what's driving it: missing information, or genuine randomness in the process?
3. Sort the drivers into reducible (more data or time would narrow this) and irreducible (inherent variance).
4. For reducible uncertainty: estimate the cost of narrowing it and whether it would even change the decision.
5. For irreducible uncertainty: treat it as a distribution to plan around, not a puzzle to solve.
6. Report the range, its composition, and the recommendation — narrow further or plan around it.

## Common mistakes

- Reporting a point estimate because ranges feel weak or evasive.
- Trying to research away irreducible uncertainty.
- Treating reducible uncertainty as irreducible and never bothering to narrow it when it was cheap to do so.

## Examples

- A project timeline's confidence interval and what's driving its width.
- A revenue forecast's weather-like versus knowable components.
- Estimating a technology's maturation timeline.

## Related

- [[sensitivity-analysis]] — identifies which inputs are actually worth narrowing.
- [[monte-carlo-reasoning]] — models the combined effect of multiple uncertain inputs.
- [[confidence-calibration]] — the discipline for stating the resulting range honestly.
