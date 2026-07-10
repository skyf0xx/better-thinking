---
name: better-thinking-recipes
description: >
  Look up a named external framework (design thinking, lean startup, ...) in
  recipes/, then execute its mapped skill sequence stage by stage as a real
  orchestrated run rather than a reference doc. If no framework is named,
  list every recipe in recipes/README.md with a one-line description and run
  whichever one the user picks. Use when the user names a known framework
  explicitly ("run this as design thinking", "let's do a lean-startup loop
  on this"), describes a framework's stages without naming it, or asks what
  recipes/frameworks are available and wants to browse before choosing one.
type: composite
category: metacognition
difficulty: 3
tokens: ~2350
dependencies: [interview-synthesis, empathy-mapping, problem-framing, ideation-sprint, scientific-method, decision-framing, bayesian-updating, confidence-calibration, decision-analysis, statistical-audit, premortem, second-order-scan, decision-journaling]
related: [better-thinking, scientific-method, decision-analysis]
---

# Recipes

Given a named external framework — or a request to browse what's available — load its mapping from `recipes/` and run the mapped skill sequence as one continuous, orchestrated pass.

## Why

A recipe doc under `recipes/` states which skills implement each stage of a framework like Design Thinking, but a doc sitting unread doesn't run itself — without an orchestrator, the mapping is reference material a human has to manually walk. This skill is the bridge: it makes a named framework actually executable, the same way a composite skill makes its own procedure executable. And a user who doesn't yet know this collection's recipe names — or the jargon of the frameworks themselves — needs a way to discover them without reading `recipes/README.md` directly, so browsing and running live in one place rather than forcing a second command per recipe.

## Use when / Don't use when

- **Use when:** the user names a known external framework explicitly, describes its stages without naming it, asks what recipes/frameworks exist, or wants to browse options before committing to one.
- **Don't use when:** no matching recipe exists in `recipes/` — fall back to `better-thinking`'s normal routing instead of forcing an ill-fitting framework onto the task. Don't use for a task that's already better served by a single atomic or composite skill directly.

## Inputs → Outputs

- **Inputs:** either a named framework (or a description matching one's stages) and the task to run it on, or no framework at all — just a request to see what's available.
- **Outputs:** if browsing, a numbered menu of recipes with one-line descriptions and a prompt for a pick; either way, the framework's stages executed in order via their mapped skills, plus the residual-gap notes from the recipe doc (what the framework covers that this collection deliberately doesn't).

## Principles

- A recipe names a *combination* of existing skills — it introduces no new cognition. If a stage seems to need a new move, that belongs in a skill, not patched into the recipe.
- The recipe list must come from `recipes/README.md`'s index, not from memory — that file is the source of truth and gains new rows over time.
- Stage order in the recipe doc is load-bearing — later stages consume earlier stages' outputs, so skip-ahead isn't valid.
- The recipe's "Residual gap" section is not an implementation failure — some stages (building, prototyping) are outside this collection's scope by design and should be named as gaps, not silently dropped or faked.
- Prefer the recipe's own stage-to-skill mapping over improvising a similar-sounding skill sequence from memory — the doc encodes deliberate choices (e.g. why `problem-framing` over a plain brainstorm).

## Procedure

1. If a framework is already named or its stages already described, skip to step 2. Otherwise — the user invoked this skill directly with no framework in mind, or asked what's available — read `recipes/README.md`'s index table and render it as a numbered list: recipe name, and its "What it's for" column as the one-line description, plain-language purpose rather than stage sequence or framework jargon. Resolve `recipes/README.md` relative to this skill's own base directory, not the user's project: take the `Base directory for this skill:` value supplied with this invocation (a path ending in `.../skills/better-thinking-recipes`), go up one level to its parent, and read `recipes/README.md` there (a sibling of `skills/`) — don't search the current working directory for it. Ask which number the user wants, and for the task to run it against if not already given, then stop the turn and wait for their pick — listing and executing are two separate turns.
2. Identify the named framework (from step 1's pick, or as directly named) and confirm a matching file exists at `recipes/<name>.md`, resolved the same way (sibling of `skills/`, not the user's project). Do not search the current working directory or project root for a `recipes/` folder — it lives in the plugin's own install location. If none matches, say so and hand back to `better-thinking`'s normal routing rather than forcing a fit.
3. Read the recipe doc's full skill sequence and its **Residual gap** section before starting. State the full stage list up front (names only, one line) so the user knows the shape of the run before committing to it — this is the one place the whole sequence is shown at once.
4. Run **one stage only**: invoke that stage's named skill(s) (e.g. `interview-synthesis` then `empathy-mapping` for Design Thinking's Empathize stage), then present that stage's output in full.
5. Stop the turn. State which stage just ran and which stage is next, then wait for the user's explicit go-ahead (approval, edit, or redirect) before touching the next stage. Do not draft, preview, or summarize a later stage while waiting — a stage that hasn't been checkpointed hasn't happened yet.
6. When the user responds, treat any correction or added detail as an amendment to the just-completed stage's output before it feeds forward — the next stage should consume the corrected version, not the original.
7. When a stage is marked as outside this collection's scope (e.g. Prototype, Build), state that explicitly as its own checkpoint and pause for the human/external work to happen, rather than skipping silently, hallucinating a substitute, or bundling it into an adjacent stage's turn.
8. On loop-shaped recipes (e.g. Lean Startup's persevere-or-pivot), treat the return to stage 1 as a genuine new pass with updated inputs, checkpointed the same way as the first pass — not a repeat run inline in the same turn as the pivot decision.
9. On the final stage, report which stages ran, which were out-of-scope gaps, and any point where the task's actual shape diverged from the recipe's assumed shape — recipes are a good fit until they aren't, and forcing one past its fit is a common failure mode.

## Common mistakes

- Running every stage in one turn and presenting the whole recipe as a finished report — this defeats the checkpoint model as completely as skipping it outright; a recipe is a workshop the user steps through, not a document generated at them.
- Improvising a plausible-sounding skill sequence instead of reading the actual recipe doc, silently drifting from its deliberate stage-to-skill choices.
- Silently skipping or faking an out-of-scope stage (Build, Prototype) instead of naming it as a residual gap and its own checkpoint.
- Running stages out of order or without waiting for go-ahead, losing the compounding effect of each stage consuming the last one's (possibly user-corrected) output.
- Skipping straight to execution on a guessed recipe instead of listing and confirming the user's actual pick, when no framework was named.
- Letting the rendered list go stale relative to `recipes/README.md` — always read the file fresh rather than reusing a remembered list from earlier in the conversation.
- Forcing a task into a named framework's shape when the fit is poor, instead of falling back to plain `better-thinking` routing.

## Examples

- User types `/better-thinking-recipes` with no further context — gets a numbered list of all five recipes, picks "2" for Lean Startup, supplies a pricing-experiment task, and the run begins at the next turn.
- "Run this new feature idea through design thinking" — loads `recipes/design-thinking.md`, states the five-stage shape, then runs `interview-synthesis` + `empathy-mapping` for Empathize alone, presents that output, and stops for go-ahead before touching Define.
- "Let's do build-measure-learn on this pricing experiment" — loads `recipes/lean-startup.md`, runs the hypothesize stage via `decision-framing`, checkpoints, and only reaches the persevere-or-pivot `decision-analysis` stage (logged via `decision-journaling`) turns later, once the user has confirmed each prior stage.
- A user describes empathize/define/ideate stages without naming "design thinking" — recognizes the shape from `recipes/README.md`'s index, confirms the framework match, then runs and checkpoints Empathize the same as any named-framework invocation.

## Related

- [[better-thinking]] — the general dispatcher this composite is a specialized bridge for named-framework (and recipe-browsing) requests.
- [[scientific-method]] — a dependency invoked by multiple recipes' test/measure stages.
- [[decision-analysis]] — a dependency invoked by recipes' persevere-or-pivot / decision stages.
