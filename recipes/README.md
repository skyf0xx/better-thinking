# Recipes

## Index

| Recipe | Framework | What it's for | What you get |
|---|---|---|---|
| [design-thinking.md](design-thinking.md) | Design Thinking | You're building something for other people and want it to solve their real problem, not the one you assumed. | A solution grounded in what users actually need, plus a plan to test it before you over-invest. |
| [lean-startup.md](lean-startup.md) | Lean Startup / Build-Measure-Learn | You have a business idea and don't yet know if anyone wants it. | A cheap, fast way to find out — and an honest answer on whether to keep going or change direction. |
| [jobs-to-be-done.md](jobs-to-be-done.md) | Jobs-to-be-Done | You want to know the real reason people buy or use something, beneath what they say. | The underlying motivation driving the behavior, checked against competing explanations before you trust it. |
| [rice-prioritization.md](rice-prioritization.md) | RICE Prioritization | You have a long list of things you could work on and limited time to do them. | A ranked order, backed by a transparent score, so you can defend why X comes before Y. |
| [five-forces-strategy.md](five-forces-strategy.md) | Five Forces Competitive Strategy | You want to understand why an industry is profitable (or brutal) and where your business stands in it. | A clear-eyed picture of the competitive pressures at play, and a stance for how to respond to them. |

## Conventions

- A recipe is a markdown doc, never a `SKILL.md` — it has no frontmatter, declares no `dependencies`, and isn't loaded by an orchestrator's routing pass. It's addressed to a human (or an agent already mid-task) who names the framework explicitly.
- Every recipe links each stage to a real skill in [skills/](../skills/) by `[[name]]`, in the order they run.
- Every recipe ends with a **Residual gap** section — what the mapping doesn't cover, usually a "build/do" stage this collection deliberately excludes (see [README.md](../README.md)'s "Excluded by design" list), or a repurposed skill that's an imperfect fit.
- Recipes cross-link each other under **Related recipes** where their stages overlap, the same way skills cross-link via `related`.
- A recipe is a multi-session workshop, not a single-turn report. Each numbered stage in **Skill sequence** is a checkpoint: [[better-thinking-recipes]] runs that stage's skill(s), presents the output, and stops — it does not run ahead into the next stage in the same turn. A recipe doc doesn't need its own checkpoint language per stage; `better-thinking-recipes`'s procedure carries that behavior generically for every recipe in this directory.

## Running a recipe

Recipe docs stay pure content — no new skill is required to make a recipe executable. [[better-thinking-recipes]] (`skills/better-thinking-recipes/SKILL.md`) is a composite skill that bridges this directory into the routable skill system: name a framework (or describe its stages) and `better-thinking-recipes` finds the matching doc here and executes its stage sequence one checkpointed stage at a time, instead of leaving the mapping as reference material a human has to walk manually, or dumping every stage at once. Adding a recipe here makes it auto-detectable for free — no per-recipe skill needed.

One command covers both discovery and direct invocation for the whole directory: [[better-thinking-recipes]] (`/better-thinking-recipes`), invoked with no framework named, lists every recipe here with a one-line description and runs whichever one the user picks; naming a framework directly (or describing its stages) reaches the same skill through its own auto-detection instead. There is no per-recipe shim skill — a new recipe added here is reachable both ways automatically, no new skill file needed.

## Adding a new recipe

A framework belongs here, not as a skill, when it names a *combination* of existing procedures rather than contributing a new one.
