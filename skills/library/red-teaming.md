---
name: red-teaming
description: >
  A structured adversarial exercise - assign a team or role to attack a
  plan, argument, or system as a genuine opponent would, then feed
  findings back before commitment. Use when the cost of being wrong in
  production exceeds the cost of a dedicated attack exercise.
type: composite
category: analysis
difficulty: 4
tokens: ~760
dependencies: [premortem, devils-advocacy, assumption-audit, incentive-analysis, second-order-scan]
related: [wargaming, devils-advocacy, premortem]
---

# Red Teaming

A structured adversarial exercise: assign a team, or role, to attack a plan, argument, or system as a genuine opponent would, then feed findings back before commitment.

## Why

Self-critique is capped by the fact that the builder can't fully escape their own blind spots and investment. An adversary optimizing purely to break the thing finds what the builder structurally cannot.

## Use when / Don't use when

- **Use when:** the cost of being wrong in production or live exceeds the cost of a dedicated attack exercise; security-, safety-, or reputation-critical work; before major public commitments.
- **Don't use when:** stakes don't justify the overhead — use premortem alone.

## Inputs → Outputs

- **Inputs:** a plan, system, argument, or product nearing commitment.
- **Outputs:** a findings report of exploitable weaknesses ranked by severity, and the plan's response to each.

## Principles

- The red team must be resourced and empowered to actually think like an adversary — real incentive to "win," not politeness.
- Success is finding real weaknesses, not validating the plan.
- Findings need a forced response — accept, mitigate, or redesign — not just a list.

## Procedure

1. Define scope and rules of engagement: what's in bounds to attack, what "winning" looks like for the red team.
2. Assign the adversarial role explicitly, separate from the builders.
3. Red team runs `assumption-audit` and `incentive-analysis` on the target to find exploitable weak points, then applies `premortem` framing.
4. Actively attempt exploits or counterarguments, not just list concerns.
5. Run `second-order-scan` on any successful attack: what does exploiting this enable next?
6. Report findings ranked by severity times exploitability.
7. Builders respond to each: fix, mitigate, accept-with-owner, or dispute-with-evidence. No silent drops.

## Common mistakes

- Red team drawn from the same team with the same blind spots and incentives.
- Findings collected but not force-ranked or force-responded-to.
- Running it too late to change anything.
- Scope so narrow the real risks are out of bounds.

## Examples

- Penetration testing before launch.
- A legal team stress-testing their own case.
- Adversarial review of an AI system's safety properties.

## Related

- [[wargaming]] — the multi-turn strategic extension of this same exercise.
- [[devils-advocacy]] — a lighter, single-person version.
- [[premortem]] — the entry-level version this composite builds on.
