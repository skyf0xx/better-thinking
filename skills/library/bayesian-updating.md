---
name: bayesian-updating
description: >
  Revise belief in a hypothesis by asking how much more likely the evidence
  is under that hypothesis than under its rivals. Use whenever new
  information arrives on an open question, a belief seems to be flipping
  on a single data point, or diagnosing from symptoms or signals.
type: atomic
category: reasoning
difficulty: 3
tokens: ~820
dependencies: []
related: [reference-class-forecasting, confidence-calibration, competing-hypotheses]
---

# Bayesian Updating

Revise belief in a hypothesis by asking how much more likely the evidence is under that hypothesis than under its rivals.

## Why

Untrained belief revision overreacts to vivid evidence and underreacts to boring evidence. The likelihood-ratio question — "how surprising is this if I'm wrong?" — is the highest-leverage correction available for reasoning under uncertainty.

## Use when / Don't use when

- **Use when:** new information arrives on an open question; a belief flips on a single data point; diagnosing from symptoms or signals.
- **Don't use when:** the question is deductive or purely definitional.

## Inputs → Outputs

- **Inputs:** a prior belief, even a rough one, plus new evidence.
- **Outputs:** an updated probability, with the reasoning shown.

## Principles

- Evidence supports H only if it's more probable under H than under not-H — evidence equally likely either way is noise, however dramatic.
- The prior should be the relevant base rate unless there's a specific reason otherwise.
- Strong claims need evidence that would be *rare* if the claim were false.
- Update incrementally — no single data point earns certainty.

## Procedure

1. State the hypothesis H and its live rivals.
2. Set a prior for H, anchored on a base rate; write the number down.
3. State the evidence E precisely.
4. Estimate P(E|H) and P(E|not-H) — the ratio is the evidence's strength.
5. Update the prior by that ratio — do the arithmetic if stakes justify it, otherwise shift qualitatively (~1 → no update, ~3 → mild, 10+ → strong).
6. Sanity-check the posterior against base rates and against what you'd actually bet.
7. State the posterior and what evidence would move it most next — the residual uncertainty worth tracking.

## Common mistakes

- Ignoring the base rate: a rare condition, a decent test, a wildly overestimated posterior after one positive result.
- Updating on evidence equally likely either way (P(E|H) ≈ P(E|not-H) is noise, not signal).
- Double-counting correlated evidence as independent confirmation.
- Choosing the prior after already seeing the evidence, laundering motivated reasoning into a "principled" update.

## Examples

- How much a positive screening test should actually raise the probability of a rare disease.
- Whether a competitor's job posting signals a strategic pivot or is just routine-hiring noise.
- How strongly one failed test implicates the most recent commit versus something else.

## Related

- [[reference-class-forecasting]] — the primary source for setting an honest prior.
- [[confidence-calibration]] — the check that audits whether these updates produce well-calibrated outputs over time.
- [[competing-hypotheses]] — a matrix-based composite applying this same logic across many hypotheses and evidence items at once.
