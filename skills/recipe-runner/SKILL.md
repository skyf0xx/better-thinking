---
name: recipe-runner
description: >
  Look up a named external framework (design thinking, lean startup, ...) in
  recipes/, then execute its mapped skill sequence stage by stage as a real
  orchestrated run rather than a reference doc. Use when the user names a
  known framework explicitly ("run this as design thinking", "let's do a
  lean-startup loop on this") or describes a framework's stages without
  naming it, and wants it actually carried out, not just explained.
type: composite
category: metacognition
difficulty: 3
tokens: ~1770
dependencies: [interview-synthesis, empathy-mapping, problem-framing, ideation-sprint, scientific-method, decision-framing, bayesian-updating, confidence-calibration, decision-analysis, statistical-audit, premortem, second-order-scan, decision-journaling]
related: [better-thinking, scientific-method, decision-analysis, better-thinking-recipes]
---

# Recipe Runner

Given a named external framework, load its mapping from `recipes/` and run the mapped skill sequence as one continuous, orchestrated pass.

## Why

A recipe doc under `recipes/` states which skills implement each stage of a framework like Design Thinking, but a doc sitting unread doesn't run itself — without an orchestrator, the mapping is reference material a human has to manually walk. This skill is the bridge: it makes a named framework actually executable, the same way a composite skill makes its own procedure executable.

## Use when / Don't use when

- **Use when:** the user names a known external framework explicitly, describes its stages without naming it, or asks "what's the better-thinking equivalent of framework X" and wants it run, not just mapped.
- **Don't use when:** no matching recipe exists in `recipes/` — fall back to `better-thinking`'s normal routing instead of forcing an ill-fitting framework onto the task. Don't use for a task that's already better served by a single atomic or composite skill directly.

## Inputs → Outputs

- **Inputs:** a named framework (or a description matching one's stages) and the task to run it on.
- **Outputs:** the framework's stages executed in order via their mapped skills, plus the residual-gap notes from the recipe doc (what the framework covers that this collection deliberately doesn't).

## Principles

- A recipe names a *combination* of existing skills — it introduces no new cognition. If a stage seems to need a new move, that belongs in a skill, not patched into the recipe.
- Stage order in the recipe doc is load-bearing — later stages consume earlier stages' outputs, so skip-ahead isn't valid.
- The recipe's "Residual gap" section is not an implementation failure — some stages (building, prototyping) are outside this collection's scope by design and should be named as gaps, not silently dropped or faked.
- Prefer the recipe's own stage-to-skill mapping over improvising a similar-sounding skill sequence from memory — the doc encodes deliberate choices (e.g. why `problem-framing` over a plain brainstorm).

## Procedure

1. Identify the named framework (or infer it from a stage description) and confirm a matching file exists at `recipes/<name>.md`. If none matches, say so and hand back to `better-thinking`'s normal routing rather than forcing a fit.
2. Read the recipe doc's full skill sequence and its **Residual gap** section before starting. State the full stage list up front (names only, one line) so the user knows the shape of the run before committing to it — this is the one place the whole sequence is shown at once.
3. Run **one stage only**: invoke that stage's named skill(s) (e.g. `interview-synthesis` then `empathy-mapping` for Design Thinking's Empathize stage), then present that stage's output in full.
4. Stop the turn. State which stage just ran and which stage is next, then wait for the user's explicit go-ahead (approval, edit, or redirect) before touching the next stage. Do not draft, preview, or summarize a later stage while waiting — a stage that hasn't been checkpointed hasn't happened yet.
5. When the user responds, treat any correction or added detail as an amendment to the just-completed stage's output before it feeds forward — the next stage should consume the corrected version, not the original.
6. When a stage is marked as outside this collection's scope (e.g. Prototype, Build), state that explicitly as its own checkpoint and pause for the human/external work to happen, rather than skipping silently, hallucinating a substitute, or bundling it into an adjacent stage's turn.
7. On loop-shaped recipes (e.g. Lean Startup's persevere-or-pivot), treat the return to stage 1 as a genuine new pass with updated inputs, checkpointed the same way as the first pass — not a repeat run inline in the same turn as the pivot decision.
8. On the final stage, report which stages ran, which were out-of-scope gaps, and any point where the task's actual shape diverged from the recipe's assumed shape — recipes are a good fit until they aren't, and forcing one past its fit is a common failure mode.

## Common mistakes

- Improvising a plausible-sounding skill sequence instead of reading the actual recipe doc, silently drifting from its deliberate stage-to-skill choices.
- Running every stage in one turn and presenting the whole recipe as a finished report — this defeats the checkpoint model as completely as skipping it outright; a recipe is a workshop the user steps through, not a document generated at them.
- Silently skipping or faking an out-of-scope stage (Build, Prototype) instead of naming it as a residual gap and its own checkpoint.
- Running stages out of order or without waiting for go-ahead, losing the compounding effect of each stage consuming the last one's (possibly user-corrected) output.
- Forcing a task into a named framework's shape when the fit is poor, instead of falling back to plain `better-thinking` routing.

## Examples

- "Run this new feature idea through design thinking" — loads `recipes/design-thinking.md`, states the five-stage shape, then runs `interview-synthesis` + `empathy-mapping` for Empathize alone, presents that output, and stops for go-ahead before touching Define.
- "Let's do build-measure-learn on this pricing experiment" — loads `recipes/lean-startup.md`, runs the hypothesize stage via `decision-framing`, checkpoints, and only reaches the persevere-or-pivot `decision-analysis` stage (logged via `decision-journaling`) turns later, once the user has confirmed each prior stage.
- A user describes empathize/define/ideate stages without naming "design thinking" — recipe-runner recognizes the shape from `recipes/README.md`'s index, confirms the framework match, then runs and checkpoints Empathize the same as any named-framework invocation.

## Related

- [[better-thinking]] — the general dispatcher this composite is a specialized bridge for named-framework requests.
- [[scientific-method]] — a dependency invoked by multiple recipes' test/measure stages.
- [[decision-analysis]] — a dependency invoked by recipes' persevere-or-pivot / decision stages.
