---
name: solution-space-mapping
description: >
  Enumerate the families of possible solutions before evaluating any
  candidate, so the choice is made from the full space rather than the
  first basin found. Use before committing design, architecture, or
  strategy effort to the first plausible approach.
type: atomic
category: problem-solving
difficulty: 2
tokens: ~450
dependencies: []
related: [morphological-analysis, divergent-ideation, decision-framing]
---

# Solution Space Mapping

Enumerate the families of possible solutions before evaluating any candidate, so the choice is made from the full space rather than the first basin found.

## Why

The first workable idea recruits all subsequent effort — design fixation. Mapping families, not just instances, reveals whole regions that were never considered and makes "compared to what?" answerable.

## Use when / Don't use when

- **Use when:** about to commit design, architecture, or strategy effort to the first plausible approach; someone asks "what are our options?" and the honest answer is "the one I thought of."
- **Don't use when:** the space is genuinely known and small.

## Inputs → Outputs

- **Inputs:** a framed problem.
- **Outputs:** a taxonomy of solution approaches with at least one concrete instance each, plus the axes that distinguish them.

## Principles

- Enumerate at the level of approach, not variant — three caching strategies are one family, not three.
- The axes that generate the families matter more than the resulting list.
- Always include the null solution (do nothing) and the dissolve solution (make the problem irrelevant).

## Procedure

1. Identify 2–4 axes along which solutions can differ — where in the pipeline, who acts, prevention versus cure, buy versus build.
2. Generate the family grid from the axes; add families the grid missed.
3. Always include: do-nothing, and dissolve-the-problem.
4. Populate each family with one concrete representative.
5. Kill families that violate hard constraints; record why, since constraints change.
6. Hand the survivors to evaluation — report which families were eliminated and why, as residual uncertainty for anyone revisiting this later.

## Common mistakes

- Listing five variants of one approach and calling it a space.
- Skipping the do-nothing baseline.
- Evaluating while enumerating, which kills generation by narrowing too early.
- Losing the rejected-families record, forcing the next person to re-discover why an option was cut.

## Examples

- Reducing churn: product fixes versus pricing versus onboarding versus customer selection versus expectations-setting.
- Treating pain: remove the cause versus block the signal versus raise tolerance.
- Scaling a service: optimize versus shard versus cache versus shed load versus renegotiate the SLA.

## Related

- [[morphological-analysis]] — the systematic-combinatorial version, once axes are already well-defined.
- [[divergent-ideation]] — generates instances; this skill generates families first.
- [[decision-framing]] — frames the choice that this skill's output feeds into.
