# SKILL.md Template

Every skill follows this exact structure — frontmatter is machine-readable (orchestrators route on it); the body is the algorithm. Only the three dispatcher entry points (`better-thinking`, `better-thinking-recipes`, `recipe-runner`) live at `skills/<skill-name>/SKILL.md` and are independently invocable as slash commands. Every other skill lives at `skills/library/<skill-name>.md` — same structure, same frontmatter, but read by the dispatcher as reference content rather than registered as its own command (the harness only auto-registers a slash command for a file literally named `SKILL.md` directly under `skills/<name>/`).

```markdown
---
name: <kebab-case-slug>                # unique across the collection
description: >
  <One sentence: what the skill does + the trigger conditions, written so a
  router can match it against a task. This is the ONLY text loaded at
  routing time — make it earn its keep.>
type: atomic | composite
category: reasoning | problem-solving | decision-making | research | analysis
        | systems-strategy | forecasting | creativity | communication
        | collaboration | learning | metacognition | ethics
difficulty: 1-5
tokens: <estimated body size, e.g. ~500>
dependencies: []                       # composite only: atomic skills it invokes
related: []                            # see-also links, both directions
---

# <Skill Name>

<One-sentence description (may repeat frontmatter, human-facing phrasing).>

## Why

<2–3 sentences: the failure mode this skill prevents, or the capability it
unlocks. Why a model without this skill does worse.>

## Use when / Don't use when

- **Use when:** <concrete trigger conditions — task shapes, not topics>
- **Don't use when:** <anti-triggers: when the skill is overkill or misleading>

## Inputs → Outputs

- **Inputs:** <what must exist before running: a question, a claim, a set of
  options, a draft, a disagreement…>
- **Outputs:** <the artifact the skill produces: a ranked list, a causal graph,
  a calibrated probability, a revised draft, a decision record…>

## Principles

<3–5 bullets. The invariants that make the procedure work — the "why" behind
the steps, stated as rules. Someone who forgets the steps but remembers the
principles should be able to reconstruct the procedure.>

## Procedure

1. <Imperative step. Each step must be checkable — it either happened or it
   didn't. Include stop conditions and iteration points.>
2. …
N. <Final step is always: state the output artifact + residual uncertainty.>

<For COMPOSITE skills, steps that delegate must name the dependency:
"3. Run `assumption-audit` on the leading hypothesis.">

## Common mistakes

- <Characteristic misuse #1 — and the symptom that reveals it>
- <#2…>

## Examples

- <2–3 one-line applications in *different domains*, proving transferability.>

## Related

- <[[skill-name]] — one clause on the relationship (feeds into / contrast with
  / stronger version of…)>
```

## Rules

1. **The `description` frontmatter is the routing contract.** Orchestrators load only descriptions when deciding which skills to activate; the body loads on demand. Descriptions must contain trigger vocabulary ("when comparing options…", "when a claim seems too clean…").
2. **Atomic skills: no `dependencies`.** They may list `related` skills but must be executable standalone.
3. **Composite skills: procedure steps invoke dependencies by name.** A composite that inlines an atomic procedure is a bug — extract or reference it.
4. **Every procedure ends by reporting residual uncertainty.** No skill is allowed to launder confidence.
5. **Examples must span ≥2 unrelated domains.** This is the transferability test — if you can't write cross-domain examples, the skill is domain knowledge in disguise and doesn't belong.
6. **No personas, ever.** Any sentence of the form "act as / you are a / think like a <profession>" fails review. Encode what the professional *does*, stepwise.
7. **Token budget is enforced:** atomic ≤ 900, composite ≤ 1,700 (measured on the full file including frontmatter, via a chars/4 estimate). The template's eight mandatory sections have an inherent floor around 750–800 tokens once populated at real quality — a 2–3 sentence Why, 3–5 Principles, a numbered Procedure with real steps, 3 Common mistakes, 2–3 cross-domain Examples, and Related links. The original 500/1,500 figures in the catalog were estimates for compressed one-paragraph catalog prose, not the fuller SKILL.md body; these are the calibrated numbers, set after measuring the first 41 built skills. If a skill is still pushing past its ceiling, it's doing too much — split it.
