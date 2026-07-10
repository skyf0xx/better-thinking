---
name: fermi-estimation
description: >
  Bound an unknown quantity by decomposing it into factors you can
  estimate, then checking the result against an independent anchor. Use
  when sizing anything without direct data, or sanity-checking someone
  else's number.
type: atomic
category: reasoning
difficulty: 2
tokens: ~850
dependencies: []
related: [sanity-checking, uncertainty-decomposition, reference-class-forecasting]
---

# Fermi Estimation

Bound an unknown quantity by decomposing it into factors you can estimate, then checking the result against independent anchors.

## Why

"No idea" is rarely actually true — most people know enough to get within a factor of 3 to 10, which is more than enough to inform most decisions. Decomposition converts one impossible-feeling estimate into several easy ones whose individual errors partially cancel out.

## Use when / Don't use when

- **Use when:** sizing anything — a market, a cost, a load, a time budget, a risk exposure — without direct data; sanity-checking someone else's reported number.
- **Don't use when:** real data is a quick lookup away — go get the real number instead of estimating it.

## Inputs → Outputs

- **Inputs:** a quantitative question with no direct data available.
- **Outputs:** a point estimate with an explicit range, and the decomposition shown so it can be audited.

## Principles

- Decompose into factors you actually have anchors for, not ones you know even less about than the original question.
- Estimate in orders of magnitude first, refine second.
- Use the geometric mean of your plausible bounds rather than the arithmetic mean.
- Two independent decomposition paths that agree are worth far more than one careful path alone.

## Procedure

1. Restate the question with units and scope pinned down precisely.
2. Decompose it into a product or sum of factors that are each individually estimable.
3. Estimate each factor with an explicit range — a lower and upper bound you'd actually bet on — and take their geometric mean.
4. Combine the factors, propagating the ranges through the calculation, not just the point estimates.
5. Cross-check the result via a second, genuinely independent decomposition or a known anchor.
6. Report the estimate, its range, and which single factor contributes the most uncertainty — that's the residual uncertainty worth flagging.

## Common mistakes

- False precision — reporting four significant figures from inputs that were only good to one.
- Decomposing into factors you actually know *less* about than the original question, which adds noise instead of removing it.
- Skipping the cross-check step entirely.
- Letting two supposedly "independent" decomposition paths secretly anchor on the same hidden assumption.

## Examples

- How many support tickets a new feature will generate.
- What the annual cost of a recurring meeting actually is, once every attendee's time is counted.
- How much training data plausibly exists for a given language, or the classic piano-tuners-in-Chicago estimate.

## Related

- [[sanity-checking]] — often supplies or consumes the independent estimate used in this skill's cross-check step.
- [[uncertainty-decomposition]] — the deeper follow-up for separating reducible from irreducible uncertainty in the range.
- [[reference-class-forecasting]] — an alternative or complementary anchor when a relevant base rate exists.
