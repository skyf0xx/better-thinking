---
name: bias-audit
description: >
  Run a targeted checklist of the specific cognitive biases a given task
  shape invites, with a concrete checkable symptom for each, rather than a
  generic "watch out for bias" gesture. Use when a conclusion arrived too
  easily, for high-stakes judgments, or whenever cognitive-triage flags a
  task shape with known bias risk.
type: atomic
category: metacognition
difficulty: 3
tokens: ~550
dependencies: []
related: [disconfirmation-search, devils-advocacy, confidence-calibration, cognitive-triage]
---

# Bias Audit

Run a targeted checklist of the specific cognitive biases a given task shape invites, rather than a generic "watch out for bias" gesture.

## Why

Generic bias-awareness rarely changes behavior because it isn't targeted — different task shapes invite different specific biases, and naming the right one for the situation is what actually catches it. A targeted checklist with a concrete symptom to test for beats a vague caution every time.

## Use when / Don't use when

- **Use when:** a conclusion arrived too easily or too quickly; high-stakes judgments; whenever the task shape is known to carry a specific bias risk (forecasting → overconfidence; evaluating your own plan → optimism bias; hiring → affinity bias).
- **Don't use when:** the task is too low-stakes to warrant the check — running this on every trivial judgment dilutes its use where it matters.

## Inputs → Outputs

- **Inputs:** a task, judgment, or conclusion, plus its shape (a decision, forecast, evaluation, judgment-of-a-person, etc.).
- **Outputs:** the specific biases most likely to be operating, each flagged with the concrete symptom to check for, and what was corrected if anything was found.

## Principles

- Match the bias to the task shape: forecasting invites overconfidence and planning fallacy; evaluating evidence for a preferred conclusion invites confirmation bias; judging people invites halo effects and affinity bias; recent, vivid events invite availability bias in probability judgments.
- A bias check needs a concrete behavioral symptom to test for, not just the bias's name — "am I anchoring?" is unfalsifiable, "did I generate an independent estimate before seeing theirs?" is checkable.

## Procedure

1. Identify the task shape (forecast, evaluation, decision, judgment-of-person, negotiation, etc.).
2. Select the 2–3 biases most characteristic of that shape — not a generic full list run every time.
3. For each, state the concrete, checkable symptom: what would this specific bias look like happening right now, in this conclusion?
4. Check the actual reasoning against that symptom.
5. Where a bias is plausibly present, apply the specific counter — a disconfirmation search for confirmation bias, a reference-class check for planning fallacy or overconfidence, a steelman for motivated reasoning.
6. Report what was checked, what — if anything — was found and corrected, and name any bias risk that remains unaddressed as residual uncertainty.

## Common mistakes

- Running a generic, unfocused "am I biased?" check that doesn't target anything specific and therefore catches nothing.
- Checking for bias only in conclusions you already doubt, not ones that feel comfortable — comfortable conclusions are exactly where bias hides best.
- Treating a bias-audit as a formality without applying an actual counter-technique when something is genuinely found.

## Examples

- Checking a project timeline for planning fallacy before committing to it publicly.
- Checking a hiring decision for affinity bias when the leading candidate reminds the interviewer of themselves.
- Checking a "the data clearly shows" claim for confirmation bias before it anchors a strategy document.

## Related

- [[disconfirmation-search]] — the primary counter this skill routes to for confirmation bias.
- [[devils-advocacy]] — a structural counter for group-level motivated reasoning.
- [[confidence-calibration]] — the check this skill's overconfidence findings feed into.
- [[cognitive-triage]] — typically the skill that flags when a bias-audit is warranted.
