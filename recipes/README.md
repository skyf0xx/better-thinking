# Recipes

## Index

| Recipe | Framework | Core loop |
|---|---|---|
| [design-thinking.md](design-thinking.md) | Design Thinking | empathize → define → ideate → (prototype) → test, iterated |
| [lean-startup.md](lean-startup.md) | Lean Startup / Build-Measure-Learn | hypothesize → build → measure → learn → persevere-or-pivot |

## Conventions

- A recipe is a markdown doc, never a `SKILL.md` — it has no frontmatter, declares no `dependencies`, and isn't loaded by an orchestrator's routing pass. It's addressed to a human (or an agent already mid-task) who names the framework explicitly.
- Every recipe links each stage to a real skill in [skills/](../skills/) by `[[name]]`, in the order they run.
- Every recipe ends with a **Residual gap** section — what the mapping doesn't cover, usually a "build/do" stage this collection deliberately excludes (see [README.md](../README.md)'s "Excluded by design" list), or a repurposed skill that's an imperfect fit.
- Recipes cross-link each other under **Related recipes** where their stages overlap, the same way skills cross-link via `related`.

## Adding a new recipe

A framework belongs here, not as a skill, when it names a *combination* of existing procedures rather than contributing a new one.