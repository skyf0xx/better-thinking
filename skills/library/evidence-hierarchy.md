---
name: evidence-hierarchy
description: >
  Rank the available evidence by its strength for the specific claim class,
  because evidence types have different power for different kinds of
  questions. Use when evidence conflicts, a decision leans on "studies show"
  or "experts say," or mixed material needs synthesizing.
type: atomic
category: research
difficulty: 3
tokens: ~500
dependencies: []
related: [methodology-critique, statistical-audit, bayesian-updating]
---

# Evidence Hierarchy

Rank the available evidence by its strength for the specific claim class — because evidence types have different power for different kinds of questions.

## Why

Anecdote, expert opinion, observational data, and experiment differ by orders of magnitude in reliability — but the ranking itself depends on the question (an RCT is gold for "does it work on average"; a mechanism study is better for "will it work here"). Explicit ranking stops the vivid from beating the valid.

## Use when / Don't use when

- **Use when:** evidence conflicts; a decision leans on "studies show" or "experts say"; synthesizing mixed material.
- **Don't use when:** all evidence is one type — assess quality within type instead.

## Inputs → Outputs

- **Inputs:** a claim plus a pile of heterogeneous evidence.
- **Outputs:** the evidence sorted by strength-for-this-claim, with the verdict weighted accordingly.

## Principles

- For causal claims: experiments > natural experiments > controlled observational > raw correlational > anecdote — within each tier, quality still varies hugely.
- For existence claims, one good observation suffices; for "typical case" claims, representative sampling beats any single study.
- Expert opinion is evidence about judgment under uncertainty, strong only where the expert has feedback-rich experience.
- The hierarchy ranks types — a flawed RCT loses to a strong cohort study; `methodology-critique` adjudicates within-type quality.

## Procedure

1. Classify the claim: causal, existence, frequency, predictive, or normative.
2. Sort evidence into types; note the appropriate hierarchy for this claim class.
3. Within each type, spot-check quality — sample, method, independence.
4. Weight the verdict by the top-tier evidence; use lower tiers only to fill gaps the top tier doesn't cover (external validity, mechanisms, edge cases).
5. Note the mismatches: strong evidence for a nearby claim being marketed as evidence for this claim.
6. Report the verdict, the evidence carrying it, and what missing evidence tier would settle it as residual uncertainty.

## Common mistakes

- Treating the hierarchy as absolute rather than claim-relative.
- Letting twenty anecdotes outvote one experiment.
- The bait-and-switch in step 5 — efficacy evidence sold as effectiveness evidence.
- Dismissing anecdotes entirely — they're hypothesis generators and existence proofs, just not verdict-carriers.

## Examples

- Drug efficacy: trial data outweighs clinician impressions.
- "Remote work hurts productivity" — asking what evidence type even bears on the claim before weighing any of it.
- An architecture choice supported by one blog post versus real benchmark data.

## Related

- [[methodology-critique]] — audits quality within a tier; this skill ranks across tiers.
- [[statistical-audit]] — the number-level audit once a quantitative study is chosen as evidence.
- [[bayesian-updating]] — consumes the weighted verdict to update belief.
