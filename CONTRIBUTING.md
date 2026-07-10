# Contributing

Better Thinking is a library of thinking *procedures*, not a library of prompts, personas, or reference docs. Every contribution — new skill, edit, or recipe — is judged against that bar. If in doubt, read [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) before opening a PR; that doc is the process and the spec.

## Before you start

- **Search first.** Check [skills/INDEX.json](skills/INDEX.json) for something that already covers your idea, atomically or as part of a composite. Near-duplicate skills fragment routing quality.
- **Ask: is this a thinking process, or is it domain knowledge?** Excluded by design: programming languages, framework/API knowledge, professional personas, static reference material. A skill must be transferable across unrelated domains — if you can't imagine it applying to both a medical question and a legal one, it's probably not a skill.
- **Decide atomic vs. composite.**
  - **Atomic** = one cognitive move, done well, executable standalone. No required dependencies.
  - **Composite** = orchestrates multiple atomic skills into a workflow, declares its `dependencies` in frontmatter, and its procedure steps invoke them by name rather than re-implementing them inline.

## Adding a new skill

1. **Follow the template exactly.** Copy the structure in [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) — frontmatter fields, section order and names, everything. Orchestrators route on the `description` field alone, so it must contain real trigger vocabulary ("when comparing options…", "when a claim seems too clean…"), not a vague summary.
2. **Create the file.** Only two names are real dispatcher entry points and get registered as slash commands by the harness: `better-thinking` and `better-thinking-recipes` — those live at `skills/<name>/SKILL.md`. Every other skill is reference content the dispatcher reads and applies inline, never independently invoked, and lives at `skills/library/<kebab-case-name>.md` (note: not named `SKILL.md`, and not in its own subdirectory — the Claude Code harness only auto-registers a slash command for a file literally named `SKILL.md` directly under `skills/<name>/`, so this shape keeps ordinary skills out of the command list by construction).
3. **Respect the rules in SKILL_TEMPLATE.md**, most importantly:
   - No personas, ever. Any "act as / you are a / think like a `<profession>`" fails review — encode what the professional *does*, stepwise, instead.
   - Every procedure ends by reporting residual uncertainty. No skill is allowed to launder confidence.
   - Examples must span **at least two unrelated domains** — this is the transferability test.
   - Composite procedures must name the atomic skill they invoke (e.g. "Run `assumption-audit` on the leading hypothesis"), never inline its logic. This is always a textual reference read and applied within the same response — no skill in this repo invokes another as a separate tool call, so "invoke"/"run" here means "read that skill's file and apply its procedure inline," not a mechanical sub-invocation.
4. **Stay in budget.** Token estimate (chars ÷ 4) is enforced: atomic skills ≤ 900 tokens, composite ≤ 1,700. If a skill keeps pushing past its ceiling, it's doing too much — split it.
   - **Exception: interactive orchestrators.** [[better-thinking-recipes]] is exempt from the 1,700 ceiling, capped instead at 2,500. Its procedure must specify checkpoint behavior (when to stop and wait for user go-ahead between stages) on top of the stage-invocation logic every composite carries, and that costs real procedure text. This exception is granted per-skill, not by category — a new composite doesn't get the higher ceiling just for being multi-stage; it has to actually orchestrate a paused, multi-turn interaction the same way.
5. **Update `skills/INDEX.json`.** Add an entry matching your `SKILL.md` frontmatter (`name`, `type`, `category`, `difficulty`, `status: "built"`, `one_line`, `triggers`, `related`, `path`). This is what the `/better-thinking` dispatcher reads to route — an undocumented skill is invisible to it.
6. **Cross-link `related` skills both directions.** If skill A lists skill B as related, B should list A back.

## Editing an existing skill

- Keep the frontmatter and body in sync — if you change `dependencies`, `difficulty`, or `related`, update `skills/INDEX.json` to match.
- Don't widen an atomic skill into a composite (adding dependencies) without renaming it clearly and re-checking every skill that lists it as `related`.
- Preserve cross-domain examples when editing — don't collapse them into a single domain for brevity.

## Recipes

Recipes (`recipes/`) map a named, well-known framework (design thinking, lean startup, etc.) onto a sequence of *existing* skills — they don't introduce new cognition. If your idea requires a new atomic move to make the recipe work, build that skill first, then reference it from the recipe.

A recipe doc alone is enough to make a framework runnable: [[better-thinking-recipes]] auto-detects a named framework or its stage description and executes the mapped sequence directly from the doc — no skill file required. It's also the single standing command for discovery: invoked with no framework named, it lists every recipe with a one-line description and runs whichever one the user picks; naming a framework directly reaches the same skill through its own detection instead. Adding a recipe to `recipes/` is enough to make it reachable both ways — do not add a new `better-thinking-<name>` shim skill per recipe.

## Categories

Every skill belongs to exactly one of the 13 categories in `catalog/`: reasoning, problem-solving, decision-making, research, analysis, systems-strategy, forecasting, creativity, communication, collaboration, learning, metacognition, ethics. If none fit, that's a signal to revisit whether the contribution is really a thinking procedure — open an issue to discuss a new category before adding one unilaterally.

## Pull request checklist

- [ ] Skill lives at `skills/<name>/SKILL.md` (entry points only: `better-thinking`, `better-thinking-recipes`) or `skills/library/<name>.md` (everything else), and follows the template structure exactly
- [ ] `description` frontmatter contains concrete trigger conditions, not a vague summary
- [ ] Atomic skill has no `dependencies`; composite skill's procedure invokes dependencies by name
- [ ] Token estimate within budget (atomic ≤ 900, composite ≤ 1,700; [[better-thinking-recipes]] is the sole exception, ≤ 2,500)
- [ ] Examples span ≥2 unrelated domains
- [ ] No personas — procedure only
- [ ] Final procedure step reports residual uncertainty
- [ ] `skills/INDEX.json` updated with a matching entry, including a `path` field pointing at the correct location
- [ ] `related` links added both directions
- [ ] `python3 scripts/build_route_index.py` re-run (regenerates `skills/ROUTE_INDEX.json`, the router's lexical index — goes stale otherwise)
- [ ] `python3 scripts/check_consistency.py` passes

## Questions

If you're unsure whether something belongs in the library at all — open an issue first rather than a PR. "Is this a persona or a procedure?" is the single most common rejection reason, and it's cheap to check before writing 900 tokens of skill body.
