---
name: multi-framework-ideation
description: >
  Generate ideas by running several structurally different generation
  mechanisms — morphological, analogical, provocation, first-principles —
  as separate passes, instead of one "brainstorm broadly" prompt that
  collapses toward a single region of idea-space. Use when asked to
  brainstorm, name something, or generate many options, especially if
  prior AI-generated ideas felt samey or interchangeable.
type: atomic
category: creativity
difficulty: 3
tokens: ~1265
dependencies: []
related: [divergent-ideation, morphological-analysis, analogical-reasoning, spread-potential-scoring]
---

# Multi-Framework Ideation

Generate ideas by running several structurally different generation mechanisms as separate passes, instead of one prompt asking for "diverse, creative ideas."

## Why

A single generation prompt reliably collapses toward one region of idea-space, however hard it begs for diversity — the failure is structural. Different generation *mechanisms* (recombination, analogy, reversal, first-principles) sample genuinely different regions, so diversity comes from the mechanism, not the instruction.

## Use when / Don't use when

- **Use when:** brainstorming products, names, features, or campaigns; ideas feel generic or interchangeable; before any idea-selection step, if divergence hasn't run yet.
- **Don't use when:** direction is razor-sharp and only volume is needed — plain `divergent-ideation` is cheaper. If the brief is blank or vague, sharpen it first (step 1).

## Inputs → Outputs

- **Inputs:** a concrete brief (or a vector chosen in step 1), hard constraints, 1-2 examples of the "boring" expected answer to avoid.
- **Outputs:** a raw idea list grouped by pass — undeduped, unranked, unscored.

## Principles

- Each pass is a distinct mechanism; if an idea from one pass is just a synonym of one from another, the passes weren't actually distinct.
- Divergence only — no filtering, ranking, or favorites here; that is a separate convergence phase.
- Weird output from a provocation or reversal pass is the point, not a failure to smooth over.
- Ground assumed pain points in real evidence (search reviews/complaints) rather than inventing plausible-sounding friction.

## Procedure

1. If the brief is blank or vague, sharpen it first: list 4-5 candidate audiences, name each one's job-to-be-done, ground friction in real search evidence (reviews, complaint threads — never invented pain points, and require agreement across ≥2 sources before treating a complaint as real), cross Who×Job×Friction into 5-8 candidate vectors, and have the user pick one before generating.
2. **Morphological:** break the problem into 3-5 independent dimensions (e.g. audience/mechanism/pricing/channel); list 3-4 options each; combine across dimensions, including combinations that "shouldn't" work.
3. **Analogical:** ask how ≥3 genuinely unrelated domains (nature, other industries, other crafts, history) would solve this class of problem; import the mechanism, don't just relabel it.
4. **Provocation:** state a false/extreme/forbidden premise ("what if it cost nothing," "what if users were adversaries"); push through it; extract what survives contact with real constraints, keeping the provocation itself in the output.
5. **First-principles:** name the category's default/expected answer, reject it, then rebuild from the actual job-to-be-done, stripped of inherited convention.
6. Aim for 6-10 ideas per pass; report the full list grouped by pass, plus which convention or default each pass pushed against.
7. State residual uncertainty: which pass underperformed or leaned into another's territory, and whether any friction claims lack two-source agreement.

## Common mistakes

- Running one blended pass and labeling sections after the fact — the mechanism has to actually differ, not just the label.
- Inventing friction from general knowledge instead of sourcing it from real reviews or complaints.
- Dropping the provocation or first-principles pass because its raw output looks unusable — extraction happens after generation, not instead of it.

## Examples

- Naming a fintech product: morphological on sound/structure, analogical from an unrelated craft, provocation on "what if the name had to sound bad."
- Fitness app features: first-principles rejecting "another streak counter," analogical from ecology or coaching.
- Nonprofit campaign concepts: provocation on "what if donors were adversaries," morphological on channel × register × ask size.

## Related

- [[divergent-ideation]] — the lighter single-mechanism sibling; use this skill instead when one pass keeps collapsing to the obvious answer.
- [[morphological-analysis]] — the dimension-grid technique this skill runs as one of its passes.
- [[analogical-reasoning]] — the cross-domain transfer technique this skill runs as one of its passes.
- [[spread-potential-scoring]] — a convergence-side companion when the ideas produced are consumer products/features meant to spread person-to-person.
