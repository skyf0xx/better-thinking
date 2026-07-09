# Recipes

## Index

| Recipe | Framework | Core loop |
|---|---|---|
| [design-thinking.md](design-thinking.md) | Design Thinking | empathize → define → ideate → (prototype) → test, iterated |
| [lean-startup.md](lean-startup.md) | Lean Startup / Build-Measure-Learn | hypothesize → build → measure → learn → persevere-or-pivot |
| [jobs-to-be-done.md](jobs-to-be-done.md) | Jobs-to-be-Done | decompose → interview → triangulate → rank rival explanations → audit thesis |
| [rice-prioritization.md](rice-prioritization.md) | RICE Prioritization | decompose backlog → score reach/impact/confidence → price effort → sequence |
| [five-forces-strategy.md](five-forces-strategy.md) | Five Forces Competitive Strategy | map forces → analyze incentives → map system → scenario-test → decide posture |

## Conventions

- A recipe is a markdown doc, never a `SKILL.md` — it has no frontmatter, declares no `dependencies`, and isn't loaded by an orchestrator's routing pass. It's addressed to a human (or an agent already mid-task) who names the framework explicitly.
- Every recipe links each stage to a real skill in [skills/](../skills/) by `[[name]]`, in the order they run.
- Every recipe ends with a **Residual gap** section — what the mapping doesn't cover, usually a "build/do" stage this collection deliberately excludes (see [README.md](../README.md)'s "Excluded by design" list), or a repurposed skill that's an imperfect fit.
- Recipes cross-link each other under **Related recipes** where their stages overlap, the same way skills cross-link via `related`.

## Running a recipe

Recipe docs stay pure content — no new skill is required to make a recipe executable. [[recipe-runner]] (`skills/recipe-runner/SKILL.md`) is a composite skill that bridges this directory into the routable skill system: name a framework (or describe its stages) and `recipe-runner` finds the matching doc here and executes its stage sequence as one orchestrated pass, instead of leaving the mapping as reference material a human has to walk manually. Adding a recipe here makes it auto-detectable for free — no per-recipe skill needed.

Two commands cover discovery and direct invocation for the whole directory: [[better-thinking-recipes]] (`/better-thinking-recipes`) lists every recipe here with a one-line description and runs whichever one the user picks; naming a framework directly (or describing its stages) also reaches it through `recipe-runner`'s own auto-detection. There is no per-recipe shim skill — a new recipe added here is reachable through both commands automatically, no new skill file needed.

## Adding a new recipe

A framework belongs here, not as a skill, when it names a *combination* of existing procedures rather than contributing a new one.
