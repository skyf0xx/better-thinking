---
name: counterfactual-reasoning
description: >
  Evaluate "what would have happened if X had been different" by
  constructing the minimally-changed alternative world. Use when
  attributing success or failure to a factor, evaluating a past decision,
  or measuring the impact of anything.
type: atomic
category: reasoning
difficulty: 3
tokens: ~890
dependencies: []
related: [causal-analysis, decision-journaling, after-action-review]
---

# Counterfactual Reasoning

Evaluate "what would have happened if X had been different" by constructing the minimally-changed alternative world.

## Why

Credit assignment, regret, blame, and impact evaluation all secretly depend on counterfactuals. Done implicitly, people tend to change too much of the world at once when imagining the alternative, and reach self-serving or narratively convenient conclusions instead of disciplined ones.

## Use when / Don't use when

- **Use when:** attributing success or failure to a specific factor; evaluating a past decision; measuring the impact of anything ("did the campaign actually work?").
- **Don't use when:** you can just run the actual experiment instead — do that, since it beats any counterfactual construction.

## Inputs → Outputs

- **Inputs:** an actual outcome plus a candidate difference-maker, X.
- **Outputs:** the most plausible alternative history, and a judgment of X's actual contribution to the outcome.

## Principles

- Change only X and what X causally forces — hold everything else fixed in the alternative world.
- Evaluate a past decision by what was knowable at the time, not by the outcome that happened to follow.
- Multiple sufficient causes mean no single factor "made the difference" on its own — check for this before assigning full credit or blame.

## Procedure

1. Specify the actual world: the outcome, and the factor X under evaluation.
2. Construct the nearest alternative world where X differs — change nothing else except what X causally forces downstream.
3. Trace forward: what plausibly happens in that alternative world? Use base rates to reason about it, not a convenient narrative.
4. Check for redundant causation: would some other factor have produced the same outcome anyway, even without X?
5. State X's contribution: necessary, sufficient, merely contributory, or irrelevant.
6. Flag the counterfactual's confidence explicitly — distant alternative worlds are speculation, not analysis, and that distinction is the residual uncertainty to report.

## Common mistakes

- Rewriting many variables at once ("if I'd been smarter and earlier and richer…") instead of isolating X alone.
- Hindsight bias — importing knowledge you have now into the alternative past, making the counterfactual actor look more foolish or more prescient than they could have been.
- Confusing "X preceded Y" with "without X, no Y" — sequence alone doesn't establish necessity.

## Examples

- Would the deal have closed without the discount, or was the buyer already committed regardless?
- Would the outage have happened without the specific config change, or was a different failure waiting in the wings?
- Assessing whether a historical policy actually changed the outcome it's credited or blamed for.

## Related

- [[causal-analysis]] — the graph-building companion this skill's semantics depend on.
- [[decision-journaling]] — captures the ex-ante view this skill's step 6 needs to avoid hindsight bias.
- [[after-action-review]] — the composite review process that regularly invokes this skill to diagnose a gap's cause.
