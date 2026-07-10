---
name: feedback-loop-analysis
description: >
  Identify the reinforcing and balancing loops that drive a system's
  behavior over time. Use when something is growing, shrinking, or
  oscillating and you want to know why it will continue or stop.
type: atomic
category: systems-strategy
difficulty: 3
tokens: ~810
dependencies: []
related: [systems-mapping, leverage-points, second-order-scan]
---

# Feedback Loop Analysis

Identify the reinforcing (amplifying) and balancing (self-correcting) loops that drive a system's behavior over time.

## Why

Most persistent behaviors — growth, decline, equilibrium, oscillation — are loop-driven, and the loop type predicts the shape of the behavior before you even have data. Recognizing which loop dominates tells you whether to accelerate, dampen, or redirect it.

## Use when / Don't use when

- **Use when:** something is growing, shrinking, or oscillating and you want to know why it will continue or stop; designing an intervention meant to persist.
- **Don't use when:** the behavior is a one-off event, not a pattern.

## Inputs → Outputs

- **Inputs:** a system or trend with an observable pattern over time.
- **Outputs:** the dominant loop(s) identified, their type, and the point where intervention changes the loop's behavior.

## Principles

- Reinforcing loops amplify — more begets more — and explain runaway growth or collapse.
- Balancing loops seek a target and resist change — they explain why some things "snap back."
- Every reinforcing loop is eventually capped by a balancing loop; the question is which one binds and when.
- The loop with the shortest delay dominates short-term behavior; the loop with the longest reach often dominates long-term behavior.

## Procedure

1. Describe the behavior pattern observed — growing, shrinking, oscillating, stable.
2. Trace the causal loop: does A increase B, which increases A (reinforcing), or does A increase B, which decreases A (balancing)?
3. Identify all loops touching the variable of interest; note which dominates currently and why.
4. For reinforcing loops, find the limit that will eventually cap them — it's usually already operating, just weaker.
5. For balancing loops, find the target they're defending — interventions that fight the target get absorbed; interventions that change the target work.
6. Recommend intervention at the loop level — strengthen or weaken a specific loop, or shift a balancing loop's target.

## Common mistakes

- Pushing against a balancing loop's target instead of changing the target, so the system reabsorbs the push.
- Missing that a runaway reinforcing loop is about to hit its cap.
- Treating a loop-driven pattern as caused by a single triggering event.

## Examples

- Viral growth (reinforcing) hitting market saturation (balancing cap).
- A thermostat-like pricing and demand cycle.
- Why adding process to fix quality issues sometimes worsens throughput-driven quality issues by targeting the wrong loop.

## Related

- [[systems-mapping]] — the structural substrate this analysis works within.
- [[leverage-points]] — determines where to intervene once the dominant loop is known.
- [[second-order-scan]] — the lightweight, single-step version of this same tracing instinct.
