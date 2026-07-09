# CLAUDE.md

This repo is the source for the `better-thinking` Claude Code plugin: a library of composable Agent Skills encoding thinking procedures. See [README.md](README.md) for what it is and how it's structured, and [CONTRIBUTING.md](CONTRIBUTING.md) for the rules a skill must follow (template, atomic vs. composite, token budgets, no personas).

## Working in this repo

- `skills/<name>/SKILL.md` is the source of truth for a skill. `skills/INDEX.json` is a generated-by-hand mirror of every skill's frontmatter that the `/better-thinking` dispatcher reads to route — it must stay in sync with the actual `SKILL.md` files, not the other way around.
- `catalog/*.md` holds full prose specs by category. A spec living in `catalog/` is not the same as a skill existing — only a `skills/<name>/SKILL.md` file makes it real. Don't let a catalog entry imply a skill exists when it doesn't.
- `skills/ROUTE_INDEX.json` is a **generated** TF-IDF lexical index (name/one_line/triggers/category/Examples, field-weighted, stemmed) built from `skills/INDEX.json` + each `SKILL.md`'s Examples section by `scripts/build_route_index.py`. The dispatcher (`skills/better-thinking/SKILL.md` step 3) runs `scripts/route.py "<task>"` against it for a lexical shortlist before confirming against `INDEX.json` — a token-overlap aid, not a semantic/embeddings search, so it can still miss a good match phrased very differently from the skill's own vocabulary. Never hand-edit `ROUTE_INDEX.json`.
- After adding, editing, removing, or renaming any skill (or its `related`/`dependencies`, `one_line`, `triggers`, or `## Examples` section), run both:
  ```
  python3 scripts/build_route_index.py
  python3 scripts/check_consistency.py
  ```
  `check_consistency.py` checks frontmatter validity, INDEX.json↔filesystem↔frontmatter sync, dangling `[[wiki-links]]`, and catalog specs with no corresponding built skill. Fix everything it reports before considering the change done — this is exactly the class of drift that accumulates silently otherwise (see git history around 2026-07-09 for the incident that motivated writing it: a fully-specified `scientific-method` composite that several other skills depended on but that was never actually built — since resolved, the skill is built and registered). `build_route_index.py` must be re-run any time the text it's built from changes, or the router's shortlist goes stale relative to the actual skills.
- There is no other build/test step. A change to this repo is a change to markdown and JSON files (plus regenerating `ROUTE_INDEX.json` when its inputs change).
