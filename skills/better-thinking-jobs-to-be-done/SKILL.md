---
name: better-thinking-jobs-to-be-done
description: >
  Explicit entry point for the Jobs-to-be-Done framework — decompose,
  interview, triangulate, rank rival explanations, audit thesis. Use when
  the user directly invokes this recipe by name rather than describing its
  stages and waiting for auto-detection.
type: composite
category: metacognition
difficulty: 3
tokens: ~400
dependencies: [recipe-runner]
related: [recipe-runner, better-thinking-rice-prioritization, better-thinking-five-forces-strategy]
---

# Recipe: Jobs-to-be-Done

Explicit, direct invocation of the Jobs-to-be-Done recipe — the decompose/interview/triangulate/rank/audit sequence mapped onto this collection's skills.

## Why

Auto-detection from a stage description is useful but not guaranteed to fire — sometimes the user already knows exactly which named framework they want and shouldn't have to phrase a request so `recipe-runner`'s triggers happen to catch it. A direct, explicitly invocable entry point removes that uncertainty for the highest-level, most-reached-for recipes.

## Use when / Don't use when

- **Use when:** the user names "jobs-to-be-done" or "JTBD" directly, or invokes this skill explicitly, wanting the recipe run rather than explained.
- **Don't use when:** the user hasn't named this framework and is instead describing an unrelated task — let `better-thinking`'s normal routing or `recipe-runner`'s own detection handle that case instead of forcing this recipe.

## Inputs → Outputs

- **Inputs:** the task to run through the Jobs-to-be-Done recipe.
- **Outputs:** identical to `recipe-runner`'s output for this recipe — each stage executed via its mapped skill, plus residual-gap notes from `recipes/jobs-to-be-done.md`.

## Principles

- This skill holds no orchestration logic of its own — it exists only to make the recipe directly reachable by name. All procedure detail lives in `recipe-runner` and in `recipes/jobs-to-be-done.md`.
- Don't duplicate `recipe-runner`'s stage-execution steps here — if they drift out of sync, the recipe-runner copy is authoritative.

## Procedure

1. Invoke `recipe-runner` with the framework fixed to `jobs-to-be-done` (`recipes/jobs-to-be-done.md`), passing along the task at hand.
2. Follow `recipe-runner`'s own procedure exactly as written — this skill changes only how the recipe is reached, not how it runs.
3. Report whatever `recipe-runner` reports: stages executed, out-of-scope gaps, and any divergence between the task's actual shape and the recipe's assumed shape.

## Common mistakes

- Re-implementing the decompose→interview→triangulate→rank→audit sequence inline here instead of delegating to `recipe-runner` — creates two copies of the same logic that can silently drift apart.
- Forcing this recipe onto a task that doesn't actually fit its shape just because it was invoked by name — `recipe-runner`'s own fit-check still applies.

## Examples

- User types `/better-thinking-jobs-to-be-done` on a new product idea before any feature work has started — runs the full decompose→audit loop via `recipe-runner`.
- A market-research question invoked directly by name, same mechanism, different domain — proving this shim is domain-agnostic since all domain judgment lives in the delegated skills.

## Related

- [[recipe-runner]] — does all the actual work; this skill only fixes which recipe to run and makes it directly nameable.
- [[better-thinking-rice-prioritization]] — the natural next recipe once a JTBD thesis produces a backlog of candidate features to sequence.
- [[better-thinking-five-forces-strategy]] — a sibling explicit entry point operating one level up, on market structure rather than a single customer job.
