---
name: scenario-planning
description: >
  Construct several divergent, internally consistent futures and test
  candidate strategies against all of them, rather than betting
  everything on one forecast. Use for long-horizon strategic decisions
  where the environment is genuinely uncertain.
type: composite
category: systems-strategy
difficulty: 4
tokens: ~1000
dependencies: [uncertainty-decomposition, structured-what-if, second-order-scan, sensitivity-analysis, tripwires]
related: [backcasting, wargaming, structured-forecasting, decision-analysis]
---

# Scenario Planning

Construct several divergent, internally consistent futures and test candidate strategies against all of them, rather than betting everything on one forecast.

## Why

Point forecasts are almost always wrong, and strategies optimized for one forecast are fragile when reality lands elsewhere. Building multiple plausible futures and demanding a strategy survive across them produces robustness that no single best-guess forecast can.

## Use when / Don't use when

- **Use when:** long-horizon strategic decisions where the environment — market, technology, regulation, competition — is genuinely uncertain, not just internally uncertain.
- **Don't use when:** the horizon is short enough that a single forecast is reliable, or the decision doesn't depend on how the environment unfolds.

## Inputs → Outputs

- **Inputs:** a strategic question with a meaningful time horizon and real environmental uncertainty.
- **Outputs:** 3 to 4 divergent scenarios, each internally coherent, plus a strategy assessment of what performs well across them.

## Principles

- Scenarios are not predictions and not a probability-weighted set — they're a deliberately spread set designed to bracket the plausible range.
- The two or three axes of deepest uncertainty, not the many minor ones, generate the scenario set.
- A scenario must be internally consistent — a coherent combination of driver outcomes, not a grab-bag.
- The point is testing strategy robustness, not picking the "right" scenario in advance.

## Procedure

1. Frame the strategic question and horizon.
2. Run `uncertainty-decomposition`: identify the critical uncertainties — the few drivers that are both highly uncertain and highly impactful.
3. Select the two axes of deepest uncertainty; cross them to generate 3–4 scenario quadrants, or hand-author divergent coherent narratives if the drivers aren't cleanly orthogonal.
4. Flesh out each scenario with `structured-what-if`: what does this world look like, and what does it imply for the question at hand?
5. Test each candidate strategy against every scenario: does it work, fail, or need adaptation?
6. Favor strategies robust across scenarios, using `sensitivity-analysis` on strategy performance versus scenario, over those optimal in only one.
7. Where a robust strategy doesn't exist, identify the earliest signal via `tripwires` that would indicate which scenario is unfolding, and build the option to pivot.
8. Run `second-order-scan` on the chosen strategy within its best-fit scenario, checking for adaptation effects.

## Common mistakes

- Treating one scenario as "the forecast" and just planning for it, defeating the entire method.
- Generating scenarios that are all mild variations of the present, not divergent enough to test robustness.
- Too many scenarios, diluting attention — 3–4 is the practical range.
- Skipping the tripwires step, leaving the organization blind to which future is arriving.

## Examples

- An energy company planning across divergent regulatory or price futures.
- A startup's product strategy across different competitive-response scenarios.
- National security planning; an AI-adoption strategy across capability-trajectory scenarios.

## Related

- [[backcasting]] — for a chosen future rather than uncertain ones.
- [[wargaming]] — the adversarial version of this method.
- [[structured-forecasting]] — the probabilistic single-path alternative.
