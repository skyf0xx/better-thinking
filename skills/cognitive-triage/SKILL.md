---
name: cognitive-triage
description: >
  Classify an incoming task by its shape (decision, diagnosis, research,
  creative, communication, learning, negotiation) and its stakes, then select
  which skills to deploy at what depth. Use as the first move on any
  nontrivial task, before any substantive work begins.
type: atomic
category: metacognition
difficulty: 3
tokens: ~900
dependencies: []
related: [effort-calibration, reversibility-classification, bias-audit, epistemic-tagging]
---

# Cognitive Triage

Classify an incoming task by its shape and stakes, and select which skills to deploy at what depth — the dispatcher that decides how much thinking machinery a task deserves.

## Why

Applying full analytical machinery to a trivial task wastes effort; applying none to a consequential one is negligent. A fast, explicit classification step routes effort proportionally before substantive work begins.

## Use when / Don't use when

- **Use when:** at first contact with any nontrivial task — the entry point other skills get dispatched from.
- **Don't use when:** never skip it; scale its own depth down instead. Triage on a small task should take seconds.

## Inputs → Outputs

- **Inputs:** an incoming task, question, or request.
- **Outputs:** a task classification (shape + stakes + reversibility) and a selected set of skills and depth.

## Principles

- Classify by shape first — decision, diagnosis, research question, creative generation, communication, learning, negotiation, or a combination. Shape determines which skill family is even relevant.
- Classify by stakes and reversibility second. This determines depth, independent of shape.
- A task can be routine in domain but high-stakes in consequence — don't classify by surface topic or tone alone.
- Re-triage if the task's real shape differs once work is underway; the initial classification is a hypothesis, not a commitment.

## Procedure

1. Identify the task's shape: decision, diagnosis, research question, creative generation, communication, learning, negotiation, or a combination.
2. Identify stakes and reversibility — a gut check, or run [[reversibility-classification]] if unclear.
3. Match shape + stakes to the relevant skill family and depth. A quick, reversible decision needs a lightweight tool; a high-stakes, hard-to-reverse one needs a full pipeline.
4. Note cross-cutting needs — most nontrivial tasks benefit from at least [[epistemic-tagging]] and [[bias-audit]] regardless of shape.
5. Proceed with the selected skills at the selected depth.
6. Re-triage explicitly if the actual shape turns out different mid-work — adjust rather than silently continuing. Report remaining ambiguity in shape or stakes as residual uncertainty.

## Common mistakes

- Applying a heavyweight composite to a low-stakes task out of habit or thoroughness-signaling.
- Skipping triage on tasks that look routine but carry hidden stakes.
- Triaging once and never revisiting, even after the true shape becomes clear mid-work.

## Examples

- Routing "should we do X or Y" to a full decision pipeline, but "which font should I use" to no formal process at all.
- Recognizing a "quick question" about odd behavior is actually a diagnosis task needing a structured differential.
- Catching that a casually-worded request will actually feed a board decision, and escalating depth accordingly.

## Related

- [[effort-calibration]] — the depth-setting logic this skill invokes.
- [[reversibility-classification]] — the stakes input this skill consumes.
- [[bias-audit]] — a cross-cutting check routed to on most tasks.
