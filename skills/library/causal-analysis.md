---
name: causal-analysis
description: >
  Build an explicit causal model of a phenomenon, distinguishing causation
  from correlation, confounding, and selection. Use for any claim of the
  form "X causes/drives/leads to Y," and always before intervening on X to
  try to change Y.
type: atomic
category: reasoning
difficulty: 4
tokens: ~840
dependencies: []
related: [counterfactual-reasoning, statistical-audit, root-cause-investigation, sanity-checking]
---

# Causal Analysis

Build an explicit causal model of a phenomenon, distinguishing causation from correlation, confounding, and selection.

## Why

Almost every intervention decision assumes a causal claim, and correlational data always offers rival stories for the same pattern (X causes Y, Y causes X, or some Z causes both). Making the graph explicit exposes which story is being silently assumed.

## Use when / Don't use when

- **Use when:** any claim of the form "X causes, drives, or leads to Y"; before intervening on X to change Y.
- **Don't use when:** only prediction is needed, not intervention — correlation alone suffices for forecasting.

## Inputs → Outputs

- **Inputs:** an observed relationship or a proposed intervention.
- **Outputs:** a causal graph (even informal), the rival explanations for the data, and what evidence would distinguish them.

## Principles

- Correlation licenses prediction, not intervention. Draw the confounder before believing the arrow.
- Conditioning on a common effect *creates* fake correlation between its causes (collider bias).
- Temporal order is necessary for causation but not sufficient.

## Procedure

1. State the causal claim as an arrow, X → Y, with population and timescale.
2. Draw rival graphs: reverse causation, a common cause Z, selection effects in how the data was gathered.
3. For each rival, name a concrete candidate — an actual plausible Z, an actual selection mechanism.
4. Ask what the mechanism would have to be for the claimed arrow — trace it step by step.
5. Identify discriminating evidence: natural experiments, dose-response, timing, what happens when X is removed.
6. If intervention data exists, weight it far above observational data.
7. Report the graph you believe, confidence, and the single most likely alternative as the residual uncertainty.

## Common mistakes

- Accepting mechanism-free correlations because the narrative feels intuitive.
- Ignoring selection effects in how the data reached you.
- Assuming the arrow's direction from narrative convention rather than evidence.
- Treating "we controlled for X" as if it resolves confounding automatically.

## Examples

- Does a new onboarding flow cause retention, or do already-motivated users just complete both?
- Does a medication help, or do healthier patients get prescribed it in the first place?
- Did a reorg improve velocity, or were weak projects cancelled at the same time for unrelated reasons?

## Related

- [[counterfactual-reasoning]] — supplies the formal semantics behind what a causal arrow actually claims.
- [[statistical-audit]] — the numeric companion check on the data supporting the claim.
- [[root-cause-investigation]] — applies this same discipline backwards, from an observed effect to its cause.
- [[sanity-checking]] — a lightweight companion check worth running on any causal graph before trusting it.
