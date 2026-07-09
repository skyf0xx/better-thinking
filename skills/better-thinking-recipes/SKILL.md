---
name: better-thinking-recipes
description: >
  List every named external framework recipe (design thinking, lean
  startup, jobs-to-be-done, RICE prioritization, five forces, ...) with a
  one-line description, then run whichever one the user picks. Use when the
  user directly invokes this command, asks "what recipes are there",
  "what frameworks do you support", or wants to browse before naming one.
type: composite
category: metacognition
difficulty: 2
tokens: ~500
dependencies: [recipe-runner]
related: [recipe-runner, better-thinking]
---

# Recipes

List the named frameworks available in `recipes/`, then run the one the user picks via `recipe-runner`.

## Why

`recipe-runner` executes a recipe once you name it, but a user who doesn't already know this collection's recipe names — or the jargon of the frameworks themselves — has no way to discover them short of reading `recipes/README.md` directly. This skill is the browsable front door: show what's available in one plain-language line each (the problem it solves, not its stage names), then hand the choice straight to `recipe-runner` instead of making the user learn a second command per recipe or decode "empathize → define → ideate" themselves.

## Use when / Don't use when

- **Use when:** the user invokes this skill directly, asks what recipes/frameworks exist, or wants to browse options before committing to one.
- **Don't use when:** the user already named a specific framework — invoke `recipe-runner` directly instead of detouring through a list they don't need.

## Inputs → Outputs

- **Inputs:** none required to list; a numbered selection (or a task description) once the user responds.
- **Outputs:** a numbered menu of recipes with one-line descriptions, then — once the user picks — `recipe-runner`'s full output for that recipe run against the task they provide.

## Principles

- This skill holds no orchestration logic of its own — it only surfaces the menu and forwards the pick. All procedure detail lives in `recipe-runner` and each `recipes/<name>.md`.
- The list must come from `recipes/README.md`'s index, not from memory — that file is the source of truth and gains new rows over time.
- Don't run anything before the user picks — listing and executing are two separate turns.

## Procedure

1. Read `recipes/README.md`'s index table and render it as a numbered list: recipe name, and its "What it's for" column as the one-line description — plain-language purpose, not the stage sequence or framework jargon. A user picking from this list doesn't yet know what "empathize → define → ideate" means; they know what problem they have.
2. Ask the user which number they want, and for the task to run it against (if not already given).
3. Once picked, invoke `recipe-runner` with the framework fixed to the chosen recipe's file (`recipes/<name>.md`), passing along the task.
4. Follow `recipe-runner`'s own procedure exactly as written — this skill changes only how the recipe is found and reached, not how it runs.
5. Report whatever `recipe-runner` reports: stages executed, out-of-scope gaps, and any divergence between the task's actual shape and the recipe's assumed shape.

## Common mistakes

- Re-implementing a recipe's stage sequence inline here instead of delegating to `recipe-runner` — creates a second copy of the same logic that can silently drift apart.
- Skipping straight to execution on a guessed recipe instead of listing and confirming the user's actual pick.
- Letting the rendered list go stale relative to `recipes/README.md` — always read the file fresh rather than reusing a remembered list from earlier in the conversation.

## Examples

- User types `/better-thinking-recipes` with no further context — gets a numbered list of all five recipes and picks "2" for Lean Startup, then supplies a pricing-experiment task.
- User asks "what frameworks do you support for competitive analysis?" — gets the full list (not pre-filtered), since the list is cheap to scan and the user may not know Five Forces is the match until they see it named.

## Related

- [[recipe-runner]] — does all the actual execution work; this skill only makes the set of recipes discoverable and forwards the pick.
- [[better-thinking]] — the general dispatcher; this skill is the named-frameworks equivalent of its routing for the recipes/ directory specifically.
