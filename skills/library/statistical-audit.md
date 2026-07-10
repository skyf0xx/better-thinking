---
name: statistical-audit
description: >
  Interrogate a quantitative claim's base rate, denominator, comparison
  group, significance, and effect size, plus the path the number took to
  reach you. Use on any statistic doing persuasive work — "X% more,"
  "studies show," record highs, rankings, risk figures.
type: atomic
category: research
difficulty: 4
tokens: ~780
dependencies: []
related: [bayesian-updating, methodology-critique]
---

# Statistical Audit

Interrogate quantitative claims: base rates, denominators, comparison groups, significance, effect size, and the path the number took to reach you.

## Why

Numbers borrow authority from mathematics while their meaning is set by choices — what was counted, compared to what, and which results got published. Most misleading statistics are technically true; the distortion lives in the unstated choices around the number, not in the arithmetic.

## Use when / Don't use when

- **Use when:** any statistic used to persuade — "X% more," "studies show," "record high," rankings, risk figures, anything with a percent sign in a pitch.
- **Don't use when:** the number is decorative and no decision or belief depends on it.

## Inputs → Outputs

- **Inputs:** a quantitative claim.
- **Outputs:** a verdict on what the number actually supports, with the specific distortions identified.

## Principles

- No numerator without a denominator.
- No change without a base — "doubled" from what?
- No comparison without checking the comparison group's composition.
- Statistical significance is not practical importance — always ask for the effect size, not just the p-value.
- The number you're seeing survived a selection process (of studies, timeframes, metrics) — ask what didn't survive it.

## Procedure

1. Restate the claim with its exact quantities, units, population, and timeframe. Vagueness in any of these is finding #1.
2. Denominator check: is this a rate or a raw count, and is it built on the right base population?
3. Comparison check: compared to what, and are the groups actually comparable in selection, composition, and time?
4. Effect-size check: is the difference large enough to matter, apart from being "significant"? Get the absolute change, not just the relative one.
5. Selection check: why this metric, this timeframe, this subgroup — what do adjacent choices show instead?
6. Survivorship/publication check: what's the path by which this number reached you, and what numbers along that path didn't make it?
7. State the verdict: what the number honestly supports, what it's being used to imply, and the gap between the two. Report any distortion you couldn't fully resolve as residual uncertainty.

## Common mistakes

- Reporting relative risk without absolute risk — "40% increase" sounds large when the base rate is tiny.
- Comparing raw counts across differently sized populations instead of rates.
- Percentage-of-percentage confusion (a 5-point rise from 10% to 15% reported as "50% more").
- Treating a precise number as an accurate one — precision and accuracy are independent properties.
- Auditing so aggressively that every number gets dismissed — the audit grades a claim, it doesn't nuke it.

## Examples

- "Crime doubled" turning out to be a rise from two incidents to four.
- A mutual fund's historical returns computed only over funds that survived to today.
- "Users spend 3x longer" without specifying which users, doing what, compared to when.
- A medical screening test's impressive sensitivity hiding a base-rate collapse in a low-prevalence population.

## Related

- [[bayesian-updating]] — supplies the base-rate machinery this skill's denominator check leans on.
- [[methodology-critique]] — the upstream audit of how the number was produced, versus this skill's audit of the number itself.
