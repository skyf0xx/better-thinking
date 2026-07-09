# Cognitive Algorithms

**An operating system for cognition.** A composable, open-source collection of AI Skills that teach a model *how to think* — not what to know, and never who to pretend to be.

Each Skill is a **reusable cognitive algorithm**: a repeatable, domain-independent thinking procedure that can be invoked on its own or composed with other Skills.

## Installation

This repo is a Claude Code plugin. Install it directly from GitHub:

```
/plugin marketplace add skyf0xx/cognitive-algorithms
/plugin install cognitive-algorithms@cognitive-algorithms
```

Or from a local clone:

```
/plugin marketplace add /path/to/cognitive-algorithms
/plugin install cognitive-algorithms@cognitive-algorithms
```

This registers all 121 skills for discovery. Start any nontrivial task with `cognitive-triage` (or let it auto-route) — it reads [skills/INDEX.json](skills/INDEX.json) to select the right skill instead of guessing from a crowded name list.

## What a Skill is (and is not)

A Skill encodes a *procedure*, never a *persona*.

**Bad:** "Act like a scientist."

**Good:**
1. Form hypotheses.
2. Identify assumptions.
3. Design experiments.
4. Evaluate evidence quality.
5. Attempt falsification.
6. Update confidence.
7. Report remaining uncertainty.

Excluded by design: programming languages, framework knowledge, APIs, professional personas, static reference material. If it isn't a transferable thinking process, it doesn't belong here.

## Atomic vs. Composite

The collection is two-layered:

- **Atomic skills** implement a single cognitive algorithm — one move, done well. Examples: `bayesian-updating`, `steelmanning`, `premortem`, `active-listening`. Atomic skills have no required dependencies (they may *suggest* related skills).
- **Composite skills** orchestrate atomic skills into a larger workflow. Examples: `scientific-method`, `decision-analysis`, `competing-hypotheses`, `negotiation`. Composite skills **declare their dependencies** in frontmatter, and their procedures read like pipelines: each step either does local work or *invokes* a named atomic skill.

This keeps the ecosystem modular: improving one atomic skill upgrades every composite that uses it, and new composites can be assembled without writing new cognition from scratch.

## Repository layout

```
README.md               ← you are here
SKILL_TEMPLATE.md       ← canonical template every skill follows
TAXONOMY.md             ← hierarchical index of all skills
catalog/                ← full specification of every skill, by category
  01-reasoning.md
  02-problem-solving.md
  03-decision-making.md
  04-research.md
  05-analysis.md
  06-systems-strategy.md
  07-forecasting.md
  08-creativity.md
  09-communication.md
  10-collaboration.md
  11-learning.md
  12-metacognition.md
  13-ethics.md
skills/                 ← one directory per skill: skills/<name>/SKILL.md
  INDEX.json             ← machine-readable index; cognitive-triage reads this to route instead of relying on memorized recall
recipes/                ← named-framework mappings (design thinking, ...) onto skill sequences
```

## Design principles

1. **Algorithm, not vibe.** Every skill has a numbered procedure a model can actually execute. If a step can't fail, it isn't a step.
2. **Domain-free.** A skill must work equally well on a medical question, a legal dispute, a product decision, and a debugging session. Domain examples illustrate; they never define.
3. **Composable.** Atomic skills are single-responsibility. Composites declare dependencies and orchestrate; they never re-implement an atomic procedure inline.
4. **Explicit activation.** Every skill states *when to fire* — trigger conditions a model can pattern-match against the task at hand, and anti-triggers for when it's overkill.
5. **Honest output contracts.** Every skill states what it consumes and what it produces, so skills can be chained like functions.
6. **Failure-aware.** Every skill lists its characteristic misuses, because a thinking tool applied wrong is worse than no tool.
7. **Token-budgeted.** Every skill carries a footprint estimate so orchestrators can reason about the cost of loading it.

## Difficulty & footprint conventions

- **Difficulty (D1–D5):** how hard the skill is to execute *well*. D1 = mechanical checklist; D3 = requires judgment at each step; D5 = requires orchestrating many judgment calls under uncertainty.
- **Token footprint:** estimated size of the final SKILL.md body. Atomic skills target **300–700 tokens**; composites **800–1,500** (they lean on their dependencies for detail).

## Status

The catalog specifies **135 skills (107 atomic, 28 composite)** across 13 categories; **121 are built** as `skills/<name>/SKILL.md` (Phases 0–3). [recipes/](recipes/) (Phase 4) maps well-known named frameworks — design thinking, lean startup — onto sequences of existing skills.
