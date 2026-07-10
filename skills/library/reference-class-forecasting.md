---
name: reference-class-forecasting
description: >
  Forecast by starting from the base rate of similar past cases, then
  adjusting for what's genuinely different about this case, in that
  order. Use when estimating duration, cost, or success probability for
  any project, launch, or plan.
type: atomic
category: forecasting
difficulty: 3
tokens: ~820
dependencies: []
related: [inductive-generalization, fermi-estimation, structured-forecasting]
---

# Reference Class Forecasting

Forecast by starting from the base rate of similar past cases (the outside view), then adjusting for what's genuinely different about this case — in that order.

## Why

Inside-view forecasting — reasoning from this case's specific plan and details — is systematically optimistic because it only models how things go right. Anchoring on how similar efforts actually turned out corrects the bias before adjustment even begins.

## Use when / Don't use when

- **Use when:** estimating duration, cost, or success probability for any project, launch, or plan; whenever an inside-view estimate feels notably better than how "these things" usually go.
- **Don't use when:** truly no reference class exists — fall back to fermi-estimation instead.

## Inputs → Outputs

- **Inputs:** a forecasting question about a specific case.
- **Outputs:** a base-rate anchored estimate, adjusted for named differences, with the adjustment's direction and size justified separately from the anchor.

## Principles

- Find the reference class *before* looking at this case's specifics, or the class gets gerrymandered to fit the desired answer.
- The base rate is the anchor — adjustments should be modest and individually justified, not a wholesale override.
- "This time is different" is sometimes true, but needs a specific, checkable reason, not a feeling.

## Procedure

1. Define the reference class: what set of past cases is genuinely comparable to this one? Choose the class before considering this case's specifics.
2. Gather the base rate from that class: typical outcome, typical variance, typical failure modes.
3. Only now, examine what's specifically different about this case.
4. For each named difference, adjust the estimate — state the direction and rough magnitude, and why.
5. Check the total adjustment size against the base rate's variance — a small number of modest adjustments is more credible than one that moves the estimate outside the observed range.
6. Report the base rate, the adjustments, and the final estimate, so each step is auditable.

## Common mistakes

- Choosing the reference class after seeing the desired answer.
- Skipping straight to inside-view reasoning ("but our team is different").
- Adjustment creep — enough small justified-sounding adjustments to arrive wherever you wanted anyway.

## Examples

- Software project timeline estimation, anchored on similar past projects rather than this team's plan.
- Startup success-rate estimation.
- Forecasting how long a negotiation will take, or a renovation's cost.

## Related

- [[inductive-generalization]] — the general mechanism this skill applies to forecasting specifically.
- [[fermi-estimation]] — the fallback when no reference class exists.
- [[structured-forecasting]] — the composite pipeline this skill anchors.
