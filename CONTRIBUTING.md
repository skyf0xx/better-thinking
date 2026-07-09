# Contributing

Better Thinking is a library of thinking *procedures*, not a library of prompts, personas, or reference docs. Every contribution — new skill, edit, or recipe — is judged against that bar. If in doubt, read [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) and [TAXONOMY.md](TAXONOMY.md) before opening a PR; this doc is the process, those are the spec.

## Before you start

- **Search first.** Check [TAXONOMY.md](TAXONOMY.md) and [skills/INDEX.json](skills/INDEX.json) for something that already covers your idea, atomically or as part of a composite. Near-duplicate skills fragment routing quality.
- **Ask: is this a thinking process, or is it domain knowledge?** Excluded by design: programming languages, framework/API knowledge, professional personas, static reference material. A skill must be transferable across unrelated domains — if you can't imagine it applying to both a medical question and a legal one, it's probably not a skill.
- **Decide atomic vs. composite.**
  - **Atomic** = one cognitive move, done well, executable standalone. No required dependencies.
  - **Composite** = orchestrates multiple atomic skills into a workflow, declares its `dependencies` in frontmatter, and its procedure steps invoke them by name rather than re-implementing them inline.

## Adding a new skill

1. **Follow the template exactly.** Copy the structure in [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) — frontmatter fields, section order and names, everything. Orchestrators route on the `description` field alone, so it must contain real trigger vocabulary ("when comparing options…", "when a claim seems too clean…"), not a vague summary.
2. **Create the file** at `skills/<kebab-case-name>/SKILL.md`.
3. **Respect the rules in SKILL_TEMPLATE.md**, most importantly:
   - No personas, ever. Any "act as / you are a / think like a `<profession>`" fails review — encode what the professional *does*, stepwise, instead.
   - Every procedure ends by reporting residual uncertainty. No skill is allowed to launder confidence.
   - Examples must span **at least two unrelated domains** — this is the transferability test.
   - Composite procedures must name the atomic skill they invoke (e.g. "Run `assumption-audit` on the leading hypothesis"), never inline its logic.
4. **Stay in budget.** Token estimate (chars ÷ 4) is enforced: atomic skills ≤ 900 tokens, composite ≤ 1,700. If a skill keeps pushing past its ceiling, it's doing too much — split it.
5. **Update `skills/INDEX.json`.** Add an entry matching your `SKILL.md` frontmatter (`name`, `type`, `category`, `difficulty`, `status: "built"`, `one_line`, `triggers`, `related`, `path`). This file is the machine-readable companion to `TAXONOMY.md` and is what the `/better-thinking` dispatcher reads to route — an undocumented skill is invisible to it.
6. **Update `TAXONOMY.md`** under the relevant category so the human-facing index stays in sync with `INDEX.json`.
7. **Cross-link `related` skills both directions.** If skill A lists skill B as related, B should list A back.

## Editing an existing skill

- Keep the frontmatter and body in sync — if you change `dependencies`, `difficulty`, or `related`, update `skills/INDEX.json` and `TAXONOMY.md` to match.
- Don't widen an atomic skill into a composite (adding dependencies) without renaming it clearly and re-checking every skill that lists it as `related`.
- Preserve cross-domain examples when editing — don't collapse them into a single domain for brevity.

## Recipes

Recipes (`recipes/`) map a named, well-known framework (design thinking, lean startup, etc.) onto a sequence of *existing* skills — they don't introduce new cognition. If your idea requires a new atomic move to make the recipe work, build that skill first, then reference it from the recipe.

## Categories

Every skill belongs to exactly one of the 13 categories in `catalog/`: reasoning, problem-solving, decision-making, research, analysis, systems-strategy, forecasting, creativity, communication, collaboration, learning, metacognition, ethics. If none fit, that's a signal to revisit whether the contribution is really a thinking procedure — open an issue to discuss a new category before adding one unilaterally.

## Pull request checklist

- [ ] Skill lives at `skills/<name>/SKILL.md` and follows the template structure exactly
- [ ] `description` frontmatter contains concrete trigger conditions, not a vague summary
- [ ] Atomic skill has no `dependencies`; composite skill's procedure invokes dependencies by name
- [ ] Token estimate within budget (atomic ≤ 900, composite ≤ 1,700)
- [ ] Examples span ≥2 unrelated domains
- [ ] No personas — procedure only
- [ ] Final procedure step reports residual uncertainty
- [ ] `skills/INDEX.json` updated with a matching entry
- [ ] `TAXONOMY.md` updated under the correct category
- [ ] `related` links added both directions

## Questions

If you're unsure whether something belongs in the library at all — open an issue first rather than a PR. "Is this a persona or a procedure?" is the single most common rejection reason, and it's cheap to check before writing 900 tokens of skill body.
