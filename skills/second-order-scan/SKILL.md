---
name: second-order-scan
description: >
  Trace the consequences of consequences — asking "and then what?" through
  at least two rounds of reactions and adaptations. Use when changing
  incentives, rules, prices, metrics, or interfaces that people or systems
  will actively respond to.
type: atomic
category: decision-making
difficulty: 3
tokens: ~890
dependencies: []
related: [systems-mapping, game-theoretic-analysis, chestertons-fence]
---

# Second-Order Scan

Trace the consequences of consequences — asking "and then what?" through at least two rounds of reactions and adaptations.

## Why

First-order effects are the ones actually designed for; second-order effects are the ones that actually determine outcomes, because people, markets, and systems *adapt* to whatever intervention lands on them. Most policy and incentive failures trace to an unexamined second-order effect that was entirely predictable in advance.

## Use when / Don't use when

- **Use when:** changing incentives, rules, prices, metrics, or interfaces that people or systems will respond to.
- **Don't use when:** the affected system genuinely can't adapt — it's inanimate or the interaction is truly one-shot with no feedback loop.

## Inputs → Outputs

- **Inputs:** a proposed action or change.
- **Outputs:** a consequence tree at least two levels deep, with adaptation-driven effects flagged and the net assessment revised accordingly.

## Principles

- Ask "who reacts to this, and what do they do?" — effects on *behavior* dominate effects on *state*, and behavior is what's usually missed.
- Every metric becomes a target and stops accurately measuring once it's known to be watched (Goodhart's law) — run this scan on any new metric before trusting it.
- Delayed effects escape attention precisely because of the delay between cause and visible consequence.
- Some second-order effects actually reverse the sign of the first-order effect.

## Procedure

1. State the action and its intended, first-order effect.
2. List the parties and systems affected, including the non-obvious ones — competitors, adjacent teams, your own future self.
3. For each, ask: how do they adapt once the change lands? What's their best response to it?
4. Trace those adaptations' own effects — this is the second order. Repeat once more for the largest branches.
5. Flag effects that are delayed, compounding, or sign-reversing relative to the original intent.
6. Revise the net assessment; where uncertainty remains high, propose a reversible probe instead of a full commitment, and report that uncertainty explicitly.

## Common mistakes

- Stopping at effects-on-state and skipping effects-on-behavior entirely.
- Assuming adaptations are rare edge cases rather than the main event that actually determines the outcome.
- Scanning so exhaustively that no action ever survives the process — pair this with an explicit effort-calibration check.

## Examples

- Paying per bug fixed leading to bug farming, where more bugs get quietly introduced to be "fixed" later.
- Free returns changing buying behavior in ways that erode margin.
- Publishing team-level metrics producing both metric gaming and morale effects nobody intended.

## Related

- [[systems-mapping]] — formalizes this skill's underlying structure into an explicit stock-and-flow model.
- [[game-theoretic-analysis]] — needed when the adapters are strategic actors, not just passive responders.
- [[chestertons-fence]] — the counterpart move: understanding why an existing structure exists before changing it.
