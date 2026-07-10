---
name: sensitivity-analysis
description: >
  Vary each input assumption to find which ones actually move the
  conclusion, separating load-bearing assumptions from decorative ones.
  Use when a model or estimate has several assumptions of uneven
  confidence, or when deciding where to spend validation effort.
type: atomic
category: forecasting
difficulty: 3
tokens: ~810
dependencies: []
related: [uncertainty-decomposition, weighted-scoring, monte-carlo-reasoning]
---

# Sensitivity Analysis

Vary each input assumption to find which ones actually move the conclusion — separating load-bearing assumptions from decorative ones.

## Why

Complex estimates rest on many assumptions, but usually only one or two actually determine the answer. Testing each in turn finds those, telling you where to focus scrutiny and where precision is wasted effort.

## Use when / Don't use when

- **Use when:** a model or estimate has several assumptions of uneven confidence; deciding where to spend validation effort; presenting a number that needs to survive scrutiny.
- **Don't use when:** the estimate has one obviously dominant input already — the ranking would be trivial.

## Inputs → Outputs

- **Inputs:** an estimate or model with multiple input assumptions.
- **Outputs:** a ranked list of which inputs move the conclusion most, and the conclusion's stability across plausible input ranges.

## Principles

- Vary one input at a time, holding others fixed, to isolate its individual effect.
- Vary each across its *plausible* range, not an arbitrary percentage — a wide-uncertainty input deserves a wide test range.
- An input that barely moves the conclusion doesn't need more precision, however uncertain it is.
- If the conclusion flips within an input's plausible range, that's the finding — report it as a conditional, not a point.

## Procedure

1. List all input assumptions and their plausible ranges, not just point values.
2. For each input, hold all others at their central estimate and vary this one across its range; record the conclusion's change.
3. Rank inputs by how much they move the conclusion per unit of their own uncertainty.
4. For the top one or two inputs, consider joint variation — do they interact, amplifying or offsetting each other?
5. Identify any input whose plausible range flips the decision; name it explicitly as the crux.
6. Report the conclusion's stability, the dominant input(s), and where further precision would and wouldn't help.

## Common mistakes

- Varying all inputs at once, making it impossible to isolate which one matters.
- Testing implausibly narrow or wide ranges.
- Polishing precision on a non-dominant input while the crux input stays a guess.

## Examples

- A financial model's dependence on churn rate versus customer acquisition cost.
- An engineering estimate's dependence on one uncertain integration.
- A policy's cost-benefit case under different discount rates.

## Related

- [[uncertainty-decomposition]] — the complementary decomposition of where the uncertainty comes from.
- [[weighted-scoring]] — runs this same sensitivity step as its own final check.
- [[monte-carlo-reasoning]] — the extension for when inputs interact across many combinations.
