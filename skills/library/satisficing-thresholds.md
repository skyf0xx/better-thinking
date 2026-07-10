---
name: satisficing-thresholds
description: >
  Define "good enough" criteria in advance, then take the first option
  clearing them, bounding search cost on decisions that don't reward
  optimization. Use when many adequate options exist and differences among
  them are small or unknowable, or when analysis becomes procrastination.
type: atomic
category: decision-making
difficulty: 2
tokens: ~900
dependencies: []
related: [effort-calibration, weighted-scoring, prioritization-triage]
---

# Satisficing Thresholds

Define "good enough" criteria in advance, then take the first option that clears them — bounding search cost on decisions that don't reward optimization.

## Why

Optimization has real costs — time, option paralysis, post-choice regret — that routinely exceed the actual value gap between "the best" and "clearly sufficient." Pre-committed thresholds convert an otherwise unbounded search into a bounded, efficient one.

## Use when / Don't use when

- **Use when:** many adequate options exist and differences among the acceptable ones are small or genuinely unknowable in advance — most purchases, tool choices, venue selection; when analysis has visibly become procrastination.
- **Don't use when:** outcomes are heavy-tailed and choice quality compounds over time — hires, partners, core architecture decisions — where real optimization actually pays off.

## Inputs → Outputs

- **Inputs:** a choice with a stream or pool of options and a nontrivial search cost.
- **Outputs:** explicit threshold criteria, a search budget, and a stopping rule.

## Principles

- Set thresholds *before* seeing the options, or the eventual favorite will quietly set them retroactively.
- The threshold encodes the real requirements — everything above it is treated as noise by deliberate declaration.
- A search budget, in time or option-count, belongs in the rule itself.
- Classify the decision's tail-weight first — satisficing a heavy-tailed decision is the actual failure mode to avoid.

## Procedure

1. Confirm this decision is satisfice-appropriate: are differences among the acceptable options actually consequential? If yes, optimize instead of satisficing.
2. Write threshold criteria — the must-haves, with measurable levels attached.
3. Set a search budget: a maximum number of options to examine, or a maximum time to spend.
4. Search, and take the first option that clears every threshold.
5. If the budget is exhausted with nothing clearing all thresholds, either lower the *least load-bearing* threshold explicitly, or consciously extend the search — a deliberate renegotiation, not silent drift.
6. Stop evaluating once a choice is made — no retrospective shopping, which is what erases the entire benefit of satisficing.

## Common mistakes

- Satisficing a heavy-tailed decision that actually deserved full optimization.
- Thresholds quietly rewritten mid-search to retroactively justify an emerging favorite.
- Continuing to compare options after already committing, reintroducing the very cost this technique was meant to bound.

## Examples

- Choosing a library for a non-core function of a project.
- Picking a venue for an event under a reasonable time budget.
- Selecting "a good enough" analysis method under a hard deadline; most routine procurement decisions.

## Related

- [[effort-calibration]] — the general framework this is one cheap-end tactic within.
- [[weighted-scoring]] — the optimizing sibling for decisions where satisficing is wrong.
- [[prioritization-triage]] — determines which backlog items deserve satisficing versus full optimization.
