---
name: premortem
description: >
  Assume the plan has already failed, then work backwards to explain why —
  converting hindsight's clarity into foresight. Use before committing to
  any significant plan, when a team is uniformly optimistic, or before
  taking irreversible steps.
type: atomic
category: decision-making
difficulty: 2
tokens: ~900
dependencies: []
related: [inversion, tripwires, red-teaming]
---

# Premortem

Assume the plan has already failed, then work backwards to explain why — converting hindsight's clarity into foresight.

## Why

Prospective critique ("what could go wrong?") is socially costly to voice and cognitively weak in practice; retrospective explanation, by contrast, is fluent and safe to offer. The temporal trick — "it failed; why?" — unlocks failure modes that direct forward-looking questioning almost never surfaces.

## Use when / Don't use when

- **Use when:** before committing to any significant plan; when a team is uniformly optimistic; before taking irreversible steps.
- **Don't use when:** the plan is a cheap experiment whose failure is itself the information being sought — there, just run it.

## Inputs → Outputs

- **Inputs:** a concrete plan with a timeline.
- **Outputs:** a ranked list of failure causes with early-warning signs and mitigations, plus the resulting plan modifications.

## Principles

- Phrase everything in the past tense — "it failed" — not the hedged "it might fail." The tense shift is what unlocks fluent, honest generation.
- Generate independently before discussing as a group; open discussion collapses the diversity of failure modes people would otherwise surface.
- Prioritize failures that are both likely and preventable, not just dramatic.
- The output is concrete plan changes, not merely a worry list.

## Procedure

1. Set the scene explicitly: it's some date after the plan's horizon, and the plan failed badly.
2. Independently generate reasons it failed — both internal (our own execution, our own assumptions) and external (environment, adversaries, plain luck). Push past the first five reasons; the more interesting ones tend to surface later.
3. Consolidate the generated list and rank it by likelihood times preventability.
4. For the top items, identify the earliest observable warning sign and the corresponding mitigation or plan change.
5. Install the warning signs as tripwires, amend the plan accordingly, and record what risk was deliberately accepted rather than mitigated — that acceptance is the residual uncertainty to carry forward.

## Common mistakes

- Running it as generic risk brainstorming, which loses the specific power of the past-tense framing trick.
- Only listing external causes (comfortable) while skipping the self-inflicted ones (uncomfortable but usually more actionable).
- Generating a list of failure modes without ever changing the plan in response to it.
- Running the exercise after commitment, as pure theater with no ability to act on the findings.

## Examples

- A product launch premortem surfacing "we never actually defined success, so we declared victory and moved on."
- A migration premortem catching a missing rollback plan before it becomes a live incident.
- A research project premortem catching an unvalidated data dependency early enough to fix it cheaply.

## Related

- [[inversion]] — the general content-free version of this "imagine failure" move.
- [[tripwires]] — operationalizes this skill's early-warning signs into pre-committed actions.
- [[red-teaming]] — the fuller, adversarial sibling for higher-stakes plans.
