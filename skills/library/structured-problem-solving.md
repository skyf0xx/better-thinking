---
name: structured-problem-solving
description: >
  Polya's loop industrialized: understand the problem, plan an approach,
  execute with monitoring, and review, with explicit gates between
  phases. Use as the general-purpose composite for any nontrivial problem
  that doesn't fit a more specific pipeline.
type: composite
category: problem-solving
difficulty: 3
tokens: ~820
dependencies: [problem-framing, mece-decomposition, solution-space-mapping, working-backwards, sanity-checking, progress-monitoring, after-action-review]
related: [decision-analysis, root-cause-investigation, scientific-method]
---

# Structured Problem Solving

Polya's loop industrialized: understand the problem, plan an approach, execute with monitoring, and review — with explicit gates between phases.

## Why

Most failed problem-solving fails at phase discipline: executing before understanding, or never reviewing afterward. The gates catch this. This is the general-purpose composite for any nontrivial problem that doesn't fit a more specific pipeline like diagnosis, decision, or research.

## Use when / Don't use when

- **Use when:** the problem is nontrivial, unfamiliar, and no specialized composite fits better.
- **Don't use when:** a specialized pipeline already exists for this problem shape — route there instead.

## Inputs → Outputs

- **Inputs:** any nontrivial problem.
- **Outputs:** a solution, plus a record of the approach, its verification, and the lessons extracted.

## Principles

- Don't plan until the problem and its constraints can be restated from scratch, unaided.
- Don't execute until the plan has a first falsifiable checkpoint.
- A solved problem isn't finished until it's been verified and mined for reusable structure.

## Procedure

1. **Understand:** run `problem-framing`; state the givens, constraints, and acceptance test explicitly. *Gate: can the problem be restated cold, without notes?*
2. **Plan:** run `solution-space-mapping`; pick an approach; decompose it via `mece-decomposition` or `working-backwards`; define checkpoints. *Gate: does the plan have a first falsifiable milestone?*
3. **Execute:** work the plan under `progress-monitoring`; on divergence, diagnose whether the plan or the original framing was wrong before simply pushing harder.
4. **Verify:** run `sanity-checking` against the acceptance test from step 1 — the original test, not a quietly weakened version of it.
5. **Review:** run a lightweight `after-action-review`; extract the reusable pattern for next time.

## Common mistakes

- Gate-skipping under time pressure — the gates exist specifically *for* time pressure, not despite it.
- Silently redefining success at step 4 so the original acceptance test is never actually met.
- Treating step 5 as optional — it's where the compounding value of the whole exercise actually accrues.

## Examples

- An ambiguous client engagement with no obvious starting method.
- A research question with no established method to lean on.
- A gnarly operations problem spanning several teams.

## Related

- [[decision-analysis]] — the sibling composite for choice-shaped problems.
- [[root-cause-investigation]] — the sibling composite for failure-shaped problems.
- [[scientific-method]] — the sibling composite for truth-shaped problems.
