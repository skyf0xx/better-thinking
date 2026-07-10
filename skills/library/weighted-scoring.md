---
name: weighted-scoring
description: >
  Score options against explicitly weighted criteria, using the matrix to
  expose disagreement and sensitivity rather than to outsource the
  decision. Use for multi-attribute choices among comparable options like
  vendors, candidates, designs, or sites.
type: atomic
category: decision-making
difficulty: 2
tokens: ~870
dependencies: []
related: [decision-analysis, satisficing-thresholds, sensitivity-analysis, decision-framing]
---

# Weighted Scoring

Score options against explicitly weighted criteria, using the matrix to expose disagreement and sensitivity — not to outsource the decision.

## Why

Unstructured comparison lets one vivid attribute silently dominate the whole judgment. A weighted matrix forces every criterion into the open and shows precisely *why* one option wins — and, just as importantly, exactly where a single judgment flip would change the answer.

## Use when / Don't use when

- **Use when:** multi-attribute choices among genuinely comparable options — vendors, candidates, designs, sites.
- **Don't use when:** one criterion is truly lexicographic (a hard dealbreaker constraint — filter for it first, don't weight it), or the options differ in kind rather than in degree.

## Inputs → Outputs

- **Inputs:** two or more options, plus elicited criteria.
- **Outputs:** a scored matrix, the winner, and a sensitivity note on which weight or score changes would flip the result.

## Principles

- Hard constraints filter before scoring — weighting a dealbreaker at even 40% is exactly how dealbreakers sneak through unnoticed.
- Weights encode values and belong to the decider, not to whoever built the matrix.
- The matrix's real job is to localize disagreement to a specific cell, not to produce a falsely definitive-looking number.

## Procedure

1. Filter the options through any hard constraints first, before scoring begins.
2. List the criteria; merge any overlapping ones, since double-listing them is quietly double-weighting them.
3. Set weights before scoring any option, and have the actual decider own that weighting.
4. Score each option against each criterion using a defined scale, noting evidence quality per cell.
5. Compute the totals, then immediately run a sensitivity check: which single cell or weight change would flip the winner?
6. If the result offends intuition, locate the disagreement in a specific cell rather than dismissing either the matrix or the intuition wholesale — one of them is missing something real.
7. Report the winner, the margin, and the flip conditions as the residual uncertainty worth watching.

## Common mistakes

- Reverse-engineering the weights after the fact to crown an already-favored option.
- Correlated criteria that quietly double-count the same underlying theme.
- False precision — scoring options 7.5 versus 8 on what is really just gut feel.
- Ignoring an intuition mismatch instead of mining it for a missing criterion.

## Examples

- Vendor selection among several credible candidates.
- Choosing between job offers with different, hard-to-compare tradeoffs.
- Prioritizing which market to enter first; comparing apartments during a search.

## Related

- [[decision-analysis]] — the fuller pipeline this scoring step sits inside for high-stakes choices.
- [[satisficing-thresholds]] — the cheaper alternative when precise optimizing isn't worth it.
- [[decision-framing]] — should run before this, to establish options and criteria.
