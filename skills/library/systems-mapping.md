---
name: systems-mapping
description: >
  Model a system's stocks, flows, delays, and boundaries explicitly, so
  its behavior can be reasoned about structurally rather than
  narratively. Use when behavior seems to have no single cause, or when
  a system resists an obvious-seeming fix.
type: atomic
category: systems-strategy
difficulty: 4
tokens: ~770
dependencies: []
related: [feedback-loop-analysis, leverage-points, bottleneck-analysis]
---

# Systems Mapping

Model a system's stocks, flows, delays, and boundaries explicitly, so its behavior can be reasoned about structurally rather than narratively.

## Why

Complex behavior — oscillation, overshoot, collapse — usually comes from structure, delays and feedback, not from any single villain or event. A narrative explanation misses this; a stock-flow map exposes it.

## Use when / Don't use when

- **Use when:** behavior seems to have no single cause; oscillation, lag, or overshoot is observed; a system resists an obvious-seeming fix.
- **Don't use when:** the system is simple and linear — a direct cause suffices.

## Inputs → Outputs

- **Inputs:** a system exhibiting some behavior of interest.
- **Outputs:** a stock-and-flow map with delays marked, plus the structural explanation for the observed behavior.

## Principles

- Stocks are accumulations, things you could photograph; flows change them over time.
- Delays between action and visible effect are the single biggest cause of oscillation and overshoot.
- System boundaries are chosen, not given — what's "outside the system" is often where the real leverage or the real cost hides.
- Behavior emerges from structure — the same structure produces the same class of behavior regardless of the specific actors.

## Procedure

1. Identify the stocks — accumulated quantities such as inventory, trust, backlog, headcount, debt.
2. Identify the flows in and out of each stock, and what controls their rate.
3. Mark delays between a control action and its visible effect on the stock.
4. Draw feedback: does a stock's level influence its own flows, directly or indirectly?
5. Set the boundary explicitly — what's inside the model, what's treated as external — and note what that choice hides.
6. Explain the observed behavior structurally: which stock, flow, or delay produces it?
7. Identify where an intervention would act on structure rather than just pushing on a symptom.

## Common mistakes

- Confusing a flow (rate) with a stock (level) — "hiring is high" versus "we're understaffed."
- Ignoring delays and expecting immediate feedback from an action.
- Drawing the boundary to exclude the actual cause.

## Examples

- Why a hiring surge doesn't fix understaffing for months.
- Inventory bullwhip in a supply chain.
- Why a popular feature's support burden shows up a quarter later.

## Related

- [[feedback-loop-analysis]] — identifies which loops in this map dominate the behavior.
- [[leverage-points]] — ranks where to intervene once the structure is mapped.
- [[bottleneck-analysis]] — finds which stock or flow actually binds throughput.
