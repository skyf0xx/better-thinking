---
name: wargaming
description: >
  Simulate an adversary's moves and countermoves across multiple turns to
  stress-test a strategy against active opposition, not a static
  environment. Use for competitive strategy against a specific capable
  rival.
type: composite
category: systems-strategy
difficulty: 4
tokens: ~880
dependencies: [game-theoretic-analysis, incentive-analysis, red-teaming, second-order-scan]
related: [game-theoretic-analysis, red-teaming, scenario-planning]
---

# Wargaming

Simulate an adversary's moves and countermoves across multiple turns to stress-test a strategy against active opposition, not a static environment.

## Why

Strategies evaluated against a passive environment miss the fact that a capable adversary adapts to whatever you do. Turn-based simulation with a genuinely adversarial opposing side surfaces the counter-moves a static plan can't see coming.

## Use when / Don't use when

- **Use when:** competitive strategy against a specific capable rival; military, security, or high-stakes competitive planning; testing a negotiating strategy against a sophisticated counterpart.
- **Don't use when:** there's no real adversary — the challenge is environmental, not strategic; use scenario-planning instead.

## Inputs → Outputs

- **Inputs:** a strategy or plan plus a capable, motivated adversary.
- **Outputs:** a multi-turn simulation record, the adversary's most damaging counter-strategy found, and plan revisions that survive it.

## Principles

- The opposing side must be played to genuinely win, not to lose gracefully — a compliant adversary tests nothing.
- Play multiple turns — single-turn exercises miss the adaptation dynamics that define real strategic interaction.
- The most valuable output is usually the adversary's move nobody on the planning side considered.
- Separate the blue (planning) and red (adversary) teams so red isn't anchored on blue's assumptions.

## Procedure

1. Define the objective, the players, the turn structure, and what "winning" means for each side.
2. Model the adversary's actual incentives and constraints via `incentive-analysis` and `game-theoretic-analysis` — not a strawman opponent.
3. Assign a red team empowered and motivated to find the plan's most damaging exploit, via `red-teaming` posture.
4. Play turn 1: blue commits to a move; red responds with their best countermove given blue's action and their own incentives.
5. Run `second-order-scan` after each exchange — what does this move open up for subsequent turns?
6. Continue for multiple turns; log every red counter-move that damaged blue's position.
7. Debrief: which red moves were most damaging and least anticipated? Revise blue's strategy specifically against those.
8. Re-run the revised strategy against the same or a fresh red team to confirm the fix holds.

## Common mistakes

- A red team that plays weakly, unconsciously protecting blue's plan.
- Stopping after one turn, missing adaptation dynamics entirely.
- Blue team also serving as red, unable to escape their own blind spots.

## Examples

- Competitive response simulation before a major product launch.
- A negotiation rehearsal against a sophisticated counterparty.
- Military course-of-action wargaming; regulatory-response simulation.

## Related

- [[game-theoretic-analysis]] — the modeling substrate this composite runs on.
- [[red-teaming]] — the single-round adversarial sibling.
- [[scenario-planning]] — used instead when the uncertainty is environmental, not adversarial.
