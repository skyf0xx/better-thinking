---
name: delphi-aggregation
description: >
  Aggregate independent expert estimates through anonymous, iterative
  rounds with feedback, avoiding the groupthink and status-anchoring
  that live group discussion produces. Use when a question needs expert
  judgment but live discussion would risk anchoring.
type: composite
category: collaboration
difficulty: 3
tokens: ~830
dependencies: [question-decomposition, reference-class-forecasting, confidence-calibration]
related: [structured-forecasting, interview-synthesis, consensus-mapping]
---

# Delphi Aggregation

Aggregate independent expert estimates through anonymous, iterative rounds with feedback — avoiding the groupthink and status-anchoring that live group discussion produces.

## Why

Bringing experts into a room to reach consensus is vulnerable to the loudest voice, the highest-status participant, and premature anchoring on the first number spoken. Anonymous iteration lets each expert's independent judgment register, then converges through evidence exchange rather than social pressure.

## Use when / Don't use when

- **Use when:** a question needs expert judgment but live group discussion would risk anchoring or status effects; forecasting under genuine expert disagreement.
- **Don't use when:** the question is empirically resolvable directly — don't substitute elicitation for available data.

## Inputs → Outputs

- **Inputs:** a forecasting or estimation question plus a panel of relevant experts.
- **Outputs:** a converged, or explicitly still-divergent, estimate, with the reasoning behind outlying views surfaced.

## Principles

- The first round must be genuinely independent and anonymous.
- Between rounds, share the distribution of estimates and the *reasoning* behind outliers, not just the numbers.
- Convergence isn't the goal in itself — a persistent, well-reasoned outlier is valuable information, not noise to smooth away.

## Procedure

1. Frame the question precisely with `question-decomposition` if compound; ensure it's resolvable or estimable.
2. Round 1: each expert independently submits an estimate with reasoning, anonymously.
3. Aggregate: show the panel the distribution of estimates and the anonymized reasoning behind outliers, especially the extremes.
4. Round 2: each expert revises their estimate independently, having seen the distribution and reasoning.
5. Repeat for 2–3 rounds or until movement stabilizes.
6. Report the final distribution; explicitly surface any persistent, well-reasoned disagreement rather than papering over it with an average.

## Common mistakes

- Running it as a live discussion with names attached, defeating the anonymity that prevents status anchoring.
- Sharing only the numeric distribution between rounds without the reasoning.
- Forcing consensus by stopping only when everyone agrees, discarding a legitimately informative holdout.

## Examples

- Technology forecasting panels.
- Expert elicitation for a risk assessment.
- Estimating an uncertain project cost across senior engineers.

## Related

- [[structured-forecasting]] — the individual-forecaster version of this same discipline.
- [[interview-synthesis]] — a related technique for gathering non-numeric expert input.
- [[consensus-mapping]] — the group-agreement counterpart for decisions rather than estimates.
