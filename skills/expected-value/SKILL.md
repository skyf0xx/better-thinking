---
name: expected-value
description: >
  Evaluate an uncertain option by weighing each outcome's payoff by its
  probability, including the unlikely tails. Use when comparing gambles,
  bets, investments of time or money, or insurance-shaped choices.
type: atomic
category: reasoning
difficulty: 2
tokens: ~830
dependencies: []
related: [risk-matrix, monte-carlo-reasoning, cost-benefit]
---

# Expected Value

Evaluate an uncertain option by weighing each outcome's payoff by its probability — including the unlikely tails.

## Why

Unaided judgment tends to evaluate gambles by their single most vivid outcome. Expected-value thinking forces the full distribution into view, which is exactly where asymmetric bets — small cost with huge upside, or the reverse — otherwise hide undetected.

## Use when / Don't use when

- **Use when:** comparing gambles, bets, investments of time or money, or insurance-shaped choices.
- **Don't use when:** outcomes are certain, or a single catastrophic branch dominates — ruin isn't something that averages away, and should be flagged separately rather than blended into an EV number.

## Inputs → Outputs

- **Inputs:** an option with uncertain outcomes.
- **Outputs:** an expected-value estimate, the outcome distribution behind it, and flags for where EV alone is a bad guide to the decision.

## Principles

- Value equals the sum of probability times payoff, over *all* branches, including the ones easy to forget.
- A 1% chance of a large loss can outweigh a 90% chance of a small gain — the tails matter, not just the modal outcome.
- EV is a long-run guide; for unrepeatable, ruin-risking choices, the variance around the mean matters as much as the mean itself.

## Procedure

1. Enumerate the outcome branches, including "nothing happens" and the tail cases that are easy to skip.
2. Assign probabilities, anchored to base rates first; check that they sum to roughly 1.
3. Assign payoffs in a common unit, counting second-order costs, not just the obvious first-order ones.
4. Compute or estimate the expected value.
5. Check the distribution: is the EV being driven by a tiny-probability branch? Is any branch ruinous or irreversible?
6. Report the EV, the distribution shape behind it, and whether EV is even the right criterion for this decision — that judgment is the final, explicit output.

## Common mistakes

- Truncating the tails ("that won't happen") instead of including them in the calculation.
- Using EV as the sole criterion on a one-shot, ruin-risking choice where variance matters more than the mean.
- Precision theater — reporting fake decimal places on probabilities that were really just guesses.
- Ignoring the cost of the option not taken, which is itself part of the comparison.

## Examples

- Whether to settle a legal dispute or take it to litigation.
- Whether a startup should accept an acquisition offer versus continue independently.
- Whether to buy an extended warranty, and triaging which incident risks are worth mitigating first.

## Related

- [[risk-matrix]] — the categorical, non-numeric sibling for when precise probabilities aren't available.
- [[monte-carlo-reasoning]] — the extension for when branches are too numerous to enumerate by hand.
- [[cost-benefit]] — the broader ledger this skill's probabilistic entries often feed into.
