---
name: ooda-loop
description: >
  Observe, orient, decide, act, iterated fast enough that your tempo
  outpaces the environment's rate of change or an adversary's own loop.
  Use in fast-moving or adversarial situations requiring repeated action
  under incomplete information.
type: composite
category: systems-strategy
difficulty: 3
tokens: ~850
dependencies: [sanity-checking, bayesian-updating, progress-monitoring, effort-calibration]
related: [wargaming, progress-monitoring, scenario-planning]
---

# OODA Loop

Observe, orient, decide, act — iterated fast enough that your tempo outpaces the environment's rate of change or an adversary's own loop.

## Why

In fast-changing or adversarial situations, being approximately right, quickly, repeatedly beats being precisely right once, slowly, because the situation moves before a slow analysis finishes. The loop's power is in the iteration rate, not any single pass's rigor.

## Use when / Don't use when

- **Use when:** conditions change faster than a full analysis cycle; competitive or adversarial dynamics where tempo itself is an advantage; incident response.
- **Don't use when:** conditions are stable and getting it right once matters more than getting it fast repeatedly — use decision-analysis instead.

## Inputs → Outputs

- **Inputs:** a fast-moving or adversarial situation requiring repeated action under incomplete information.
- **Outputs:** a sequence of fast decision cycles, each updating on the last cycle's results.

## Principles

- Orientation — your mental model, shaped by experience and prior information — is the crux; most OODA failures are orientation failures, not observation or decision failures.
- The loop is disrupted, not completed, when the situation changes mid-cycle; that's normal, restart the loop rather than forcing the old plan.
- Speed of the whole loop, not any one stage, is the target metric.
- Act to gather better information, not only to finish — the action itself can be a probe.

## Procedure

1. **Observe:** gather current, direct information, not last cycle's stale picture. Note what's actually changed.
2. **Orient:** update your mental model against the new observation; explicitly check whether your orienting assumptions still hold — this is where most loops break down unnoticed.
3. **Decide:** commit to the best action given current orientation, sized appropriately for the uncertainty.
4. **Act:** execute; treat the action partly as a probe that will generate the next cycle's observation.
5. Immediately re-enter Observe with the results, running progress-monitoring across cycles to catch drift or a stuck loop.
6. If the situation outpaces your loop, the priority becomes shrinking cycle time, even at the cost of rigor per cycle.

## Common mistakes

- Treating it as a one-time sequential process instead of a tight repeating loop.
- Over-investing in the Decide stage's rigor while Observe/Orient go stale.
- Failing to update Orient, fighting the last cycle's situation instead of the current one.

## Examples

- Incident response.
- A startup responding to a fast-moving competitive threat.
- Live negotiation adjustment.

## Related

- [[wargaming]] — models the adversary's own loop explicitly, multi-turn.
- [[progress-monitoring]] — the slower-cadence sibling for less time-critical plans.
- [[scenario-planning]] — the slower-tempo cousin for longer-horizon uncertainty.
