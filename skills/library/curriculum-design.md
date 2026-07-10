---
name: curriculum-design
description: >
  Sequence learning objectives, instruction, and assessment coherently
  across a full learning arc, from where the learner starts to where
  they need to end up. Use when designing a training program, course,
  or structured onboarding.
type: composite
category: learning
difficulty: 4
tokens: ~890
dependencies: [learning-objectives, knowledge-gap-analysis, scaffolding, deliberate-practice-design, transfer-testing]
related: [learning-objectives, scaffolding, knowledge-gap-analysis, socratic-teaching]
---

# Curriculum Design

Sequence learning objectives, instruction, and assessment coherently across a full learning arc — from where the learner starts to where they need to end up.

## Why

Ad hoc instruction — a pile of good individual lessons with no overall sequence — leaves gaps and redundancies invisible until a learner fails downstream. Designing the full arc as one coherent system catches this before it costs a learner's time.

## Use when / Don't use when

- **Use when:** designing a training program, course, or structured onboarding — anything with multiple sequenced learning stages.
- **Don't use when:** the learning need is a single isolated skill with no real prerequisite chain — a single learning-objectives pass suffices.

## Inputs → Outputs

- **Inputs:** a target capability plus a starting population's current level.
- **Outputs:** a sequenced curriculum — ordered objectives, matched instruction methods, and assessments that verify each stage before the next depends on it.

## Principles

- Sequence by prerequisite dependency, not by topic convenience.
- Each stage needs its own objective and its own way to verify mastery before the learner proceeds, or gaps compound silently.
- Instruction method should match the objective's cognitive level at each stage.
- Build in transfer-testing, not just recall checks, at key checkpoints — passing a recall quiz can mask a transfer failure that derails later stages.

## Procedure

1. Define the terminal capability precisely via `learning-objectives` for the end-state.
2. Run `knowledge-gap-analysis` against the target learner population's actual starting point.
3. Decompose the terminal objective into a prerequisite chain of sub-objectives.
4. Sequence stages by that dependency chain, not by superficial topic grouping.
5. For each stage, set the objective's cognitive level and match instruction accordingly — direct teaching for recall stages, `scaffolding` plus `deliberate-practice-design` for application stages.
6. Insert assessment checkpoints between stages, including `transfer-testing` at key junctures, not just end-of-course.
7. Pilot with a small group; use checkpoint failures to find where the sequence assumed a prerequisite that wasn't actually built.

## Common mistakes

- Sequencing by topic or chapter convenience instead of actual prerequisite dependency.
- Skipping checkpoint assessment, letting a gap at an early stage silently sabotage a later one.
- Using recall-level assessment throughout even when later objectives require application, masking real gaps until it's too late to cheaply fix them.

## Examples

- A technical training program's module sequence.
- A university course's syllabus design.
- A company's structured onboarding curriculum.

## Related

- [[learning-objectives]] — the per-stage target this composite sequences.
- [[scaffolding]] — the support technique used within application-level stages.
- [[socratic-teaching]] — one instruction method available within the curriculum.
