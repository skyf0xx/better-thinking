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
tokens: ~600
dependencies: []
related: [effort-calibration, reversibility-classification, bias-audit, epistemic-tagging]
---

# Cognitive Triage

Classify an incoming task by its shape and stakes, and select which skills to deploy at what depth — the dispatcher that decides how much thinking machinery a task deserves.

## Why

Applying full analytical machinery to a trivial task wastes effort and attention that later, higher-stakes tasks will need. Applying none to a consequential one is negligent. A fast, explicit classification step routes effort proportionally before any substantive work begins, and is what lets every other skill in this collection get invoked when it's actually warranted instead of by habit.

## Use when / Don't use when

- **Use when:** at first contact with any nontrivial task — this is the entry point other skills get dispatched from. It should run before you commit to an approach, not after.
- **Don't use when:** never skip it outright; instead scale its own depth down. Triage on a small task should take seconds, not a paragraph of visible reasoning.

## Inputs → Outputs

- **Inputs:** an incoming task, question, or request, however it's phrased.
- **Outputs:** a task classification (shape + stakes + reversibility) and a selected set of skills and depth to apply to the rest of the work.

## Principles

- Classify by shape first — decision, diagnosis/investigation, research/evidence question, creative generation, communication, learning, negotiation/collaboration, or some combination. Shape determines which skill family is even relevant.
- Classify by stakes and reversibility second (feed from [[reversibility-classification]] when unclear). This determines depth, independent of shape.
- A task can be routine in domain but high-stakes in consequence — a "simple" email that will be read by a board is not a simple task. Don't classify by surface topic or tone alone.
- Re-triage if the task's real shape turns out different once work is underway; the initial classification is a hypothesis, not a commitment.

## Procedure

1. Identify the task's shape: decision, diagnosis/investigation, research/evidence question, creative generation, communication, learning, negotiation/collaboration, or some combination of these.
2. Identify stakes and reversibility — a quick gut check, or run [[reversibility-classification]] explicitly if it's unclear.
3. Match shape + stakes to the relevant skill family and depth. A quick, reversible decision needs a lightweight tool (e.g. `satisficing-thresholds`); a high-stakes, hard-to-reverse one needs the full pipeline (e.g. `decision-analysis`).
4. Note any cross-cutting needs — most nontrivial tasks benefit from at least [[epistemic-tagging]] and [[bias-audit]] regardless of shape.
5. Proceed with the selected skills at the selected depth.
6. Re-triage explicitly if the task's actual shape reveals itself to be different mid-work — state the revised classification and adjust rather than silently continuing on the original one. Report any remaining ambiguity in the task's shape or stakes as residual uncertainty.

## Common mistakes

- Applying a heavyweight composite to a low-stakes task out of habit or thoroughness-signaling — the triage step exists specifically to prevent this.
- Skipping triage on tasks that look routine but carry hidden stakes (small-sounding requests that feed a big decision downstream).
- Triaging once and never revisiting, even after the task's true shape becomes clear mid-work.

## Examples

- Routing "should we do X or Y" to a full decision-analysis pipeline, but "which font should I use" to no formal process at all.
- Recognizing a "quick question" about a system's odd behavior is actually a diagnosis task needing a structured differential, not a one-line guess.
- Catching that a casually-worded request will actually feed a board decision, and escalating its depth accordingly.

## Related

- [[effort-calibration]] — the depth-setting logic this skill invokes once shape and stakes are known.
- [[reversibility-classification]] — the stakes/reversibility input this skill consumes.
- [[bias-audit]] — a cross-cutting check this skill routes to on most nontrivial tasks.
- Every composite skill in the collection — this is their common entry point.
