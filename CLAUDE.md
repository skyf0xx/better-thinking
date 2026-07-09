# CLAUDE.md

This repo is the source for the `better-thinking` Claude Code plugin: a library of composable Agent Skills encoding thinking procedures. See [README.md](README.md) for what it is and how it's structured, and [CONTRIBUTING.md](CONTRIBUTING.md) for the rules a skill must follow (template, atomic vs. composite, token budgets, no personas).

## Working in this repo

- `skills/<name>/SKILL.md` is the source of truth for a skill. `skills/INDEX.json` is a generated-by-hand mirror of every skill's frontmatter that the `/better-thinking` dispatcher reads to route — it must stay in sync with the actual `SKILL.md` files, not the other way around.
- `catalog/*.md` holds full prose specs by category. A spec living in `catalog/` is not the same as a skill existing — only a `skills/<name>/SKILL.md` file makes it real. Don't let a catalog entry imply a skill exists when it doesn't.
- After adding, editing, removing, or renaming any skill (or its `related`/`dependencies`), run:
  ```
  python3 scripts/check_consistency.py
  ```
  It checks frontmatter validity, INDEX.json↔filesystem↔frontmatter sync, dangling `[[wiki-links]]`, and catalog specs with no corresponding built skill. Fix everything it reports before considering the change done — this is exactly the class of drift that accumulates silently otherwise (see git history around 2026-07-09 for the incident that motivated writing it: a fully-specified `scientific-method` composite that several other skills depended on but that was never actually built).
- There is no other build/test step. A change to this repo is a change to markdown and JSON files.
