---
name: game-theoretic-analysis
description: >
  Model a strategic interaction's players, moves, payoffs, and
  information to identify likely equilibria and exploitable asymmetries.
  Use when negotiating, competing, or designing mechanisms where others
  will respond strategically.
type: atomic
category: systems-strategy
difficulty: 4
tokens: ~850
dependencies: []
related: [incentive-analysis, negotiation, wargaming, second-order-scan]
---

# Game-Theoretic Analysis

Model a strategic interaction's players, available moves, payoffs, and information to identify likely equilibria and exploitable asymmetries.

## Why

When outcomes depend on others' choices that depend on yours, single-actor optimization gives wrong answers. Modeling the interaction explicitly reveals what a rational counterpart will actually do, often counter to what they say.

## Use when / Don't use when

- **Use when:** negotiating, competing, or designing mechanisms and incentives where others will respond strategically; predicting a rival's move; auditing whether a policy is game-able.
- **Don't use when:** the other party's behavior is fixed or non-strategic — overkill for non-interactive decisions.

## Inputs → Outputs

- **Inputs:** a strategic situation with two or more interacting parties whose outcomes are interdependent.
- **Outputs:** the game's structure (players, moves, payoffs, information), likely equilibrium behavior, and the point of maximum leverage.

## Principles

- Payoffs must be modeled from each player's perspective, not yours — their rational move depends on their incentives.
- Check what's common knowledge versus private information — information asymmetry changes the game entirely.
- A stated threat or promise is only credible if it's rational for them to follow through when the moment comes.
- Repeated interaction changes the game — cooperation can be rational repeated where it isn't one-shot.

## Procedure

1. Identify the players and their available moves.
2. Estimate each player's payoff for each outcome combination, from their perspective and incentives, not yours.
3. Identify what's common knowledge versus privately known by each side.
4. Determine if it's one-shot or repeated — this changes whether cooperation and reputation effects are rational.
5. Find the likely equilibrium: what does each player do assuming the others act rationally in their own interest?
6. Check credibility of any threats or promises in the model — would the player actually want to follow through?
7. Identify your highest-leverage move: where can you change the *other* player's payoffs or information, not just react to them?

## Common mistakes

- Modeling the other side's payoffs as if they shared your values.
- Assuming a stated threat is credible without checking if carrying it out would be rational for them.
- Treating a repeated interaction as one-shot, or vice versa, destroying or manufacturing cooperation incorrectly.

## Examples

- Pricing decisions anticipating a competitor's response.
- A negotiation's opening-offer strategy.
- Designing an auction or incentive mechanism resistant to gaming.

## Related

- [[incentive-analysis]] — sharpens the payoff estimation this analysis depends on.
- [[negotiation]] — the composite this analysis often feeds for complex or repeated deals.
- [[wargaming]] — the multi-turn extension of this same modeling.
