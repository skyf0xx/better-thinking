---
name: better-thinking-five-forces-strategy
description: >
  Explicit entry point for Porter's Five Forces competitive strategy
  framework — map forces, analyze incentives, map system, scenario-test,
  decide posture. Use when the user directly invokes this recipe by name
  rather than describing its stages and waiting for auto-detection.
type: composite
category: metacognition
difficulty: 3
tokens: ~400
dependencies: [recipe-runner]
related: [recipe-runner, better-thinking-jobs-to-be-done, better-thinking-rice-prioritization]
---

# Recipe: Five Forces Competitive Strategy

Explicit, direct invocation of the Five Forces recipe — the map/incentives/systems/scenario/decide sequence mapped onto this collection's skills.

## Why

Auto-detection from a stage description is useful but not guaranteed to fire — sometimes the user already knows exactly which named framework they want and shouldn't have to phrase a request so `recipe-runner`'s triggers happen to catch it. A direct, explicitly invocable entry point removes that uncertainty for the highest-level, most-reached-for recipes.

## Use when / Don't use when

- **Use when:** the user names "Five Forces" or "Porter's Five Forces" directly, or invokes this skill explicitly, wanting the recipe run rather than explained.
- **Don't use when:** the user hasn't named this framework and is instead describing an unrelated task — let `better-thinking`'s normal routing or `recipe-runner`'s own detection handle that case instead of forcing this recipe.

## Inputs → Outputs

- **Inputs:** the task to run through the Five Forces recipe (typically a market-entry or market-defense decision).
- **Outputs:** identical to `recipe-runner`'s output for this recipe — each stage executed via its mapped skill, plus residual-gap notes from `recipes/five-forces-strategy.md`.

## Principles

- This skill holds no orchestration logic of its own — it exists only to make the recipe directly reachable by name. All procedure detail lives in `recipe-runner` and in `recipes/five-forces-strategy.md`.
- Don't duplicate `recipe-runner`'s stage-execution steps here — if they drift out of sync, the recipe-runner copy is authoritative.

## Procedure

1. Invoke `recipe-runner` with the framework fixed to `five-forces-strategy` (`recipes/five-forces-strategy.md`), passing along the task at hand.
2. Follow `recipe-runner`'s own procedure exactly as written — this skill changes only how the recipe is reached, not how it runs.
3. Report whatever `recipe-runner` reports: stages executed, out-of-scope gaps, and any divergence between the task's actual shape and the recipe's assumed shape.

## Common mistakes

- Re-implementing the map→incentives→systems→scenario→decide chain inline here instead of delegating to `recipe-runner` — creates two copies of the same logic that can silently drift apart.
- Forcing this recipe onto a task that doesn't actually fit its shape just because it was invoked by name — `recipe-runner`'s own fit-check still applies.

## Examples

- User types `/better-thinking-five-forces-strategy` when deciding whether to enter a new market segment — runs the full map→decide loop via `recipe-runner`.
- A market-defense question (should we harden against a new entrant) invoked directly by name, same mechanism, different domain — proving this shim is domain-agnostic since all domain judgment lives in the delegated skills.

## Related

- [[recipe-runner]] — does all the actual work; this skill only fixes which recipe to run and makes it directly nameable.
- [[better-thinking-jobs-to-be-done]] — operates one level down: JTBD asks whether a specific customer job is real; this recipe asks whether the surrounding market structure makes serving it profitable.
- [[better-thinking-rice-prioritization]] — the natural successor once a market is judged worth entering: RICE sequences the resulting feature/initiative backlog.
