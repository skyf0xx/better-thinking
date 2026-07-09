---
name: confidence-calibration
description: >
  Attach numeric probabilities to beliefs and forecasts that match their
  actual hit rate over time, checked against base rates and scored against
  outcomes. Use when stating any forecast or belief that matters enough to
  act on, or when reviewing a past track record of predictions.
type: atomic
category: metacognition
difficulty: 3
tokens: ~550
dependencies: []
related: [reference-class-forecasting, decision-journaling, structured-forecasting]
---

# Confidence Calibration

Attach probabilities to beliefs that match their actual hit rate over time, checked against base rates and scored against outcomes.

## Why

Unaided confidence is systematically miscalibrated — usually overconfident on specific predictions, sometimes underconfident in well-understood domains. Calibration is a trainable skill, but only if predictions are stated numerically and scored against what actually happens; vague verbal hedges can never be checked and so never improve.

## Use when / Don't use when

- **Use when:** stating any forecast or belief that matters enough to act on; after a forecasting or decision process produces a conclusion needing a confidence label; periodically, to review past calibration as a track record.
- **Don't use when:** the claim is a certainty or near-certainty where numeric hedging adds noise rather than information (a settled fact).

## Inputs → Outputs

- **Inputs:** a belief or forecast.
- **Outputs:** a numeric confidence level (not a verbal hedge), ideally logged for future scoring against the actual outcome.

## Principles

- State confidence as a number or range, not a word ("likely," "probably") — words can't be scored later, and different people read the same word as wildly different probabilities.
- Calibration means: among all the things you said "80% confident" about, roughly 80% should actually happen. It is not that any single 80% call felt right in hindsight — calibration is a property of a *set* of predictions.
- Check a gut confidence level against a base rate before trusting it.
- Track a record over time; a single well-calibrated-feeling guess proves nothing on its own.

## Procedure

1. State the belief or forecast precisely enough to be scored later — a specific, resolvable outcome, not a vague impression.
2. Assign a numeric probability, anchored first to a base rate if one exists for this class of question.
3. Sanity-check: would you actually take a bet at these odds? If the stated number and the bet you'd take diverge, the stated number is performative, not calibrated — revise it until they agree.
4. Log the prediction somewhere it will be revisited for later scoring.
5. Periodically, score past predictions: of the ones called "70% confident," did roughly 70% happen? Adjust future confidence-setting habits based on the pattern — are you systematically over- or under-confident? — and report that pattern as the standing residual uncertainty in your own calibration.

## Common mistakes

- Using vague verbal hedges instead of numbers, making the claim unfalsifiable and unscoreable.
- Treating one correct high-confidence call as proof of good calibration — it's the long-run hit rate across many calls that matters, not any single one.
- Never closing the loop: stating confidence but never checking it against outcomes, so no actual calibration learning occurs.

## Examples

- A forecaster's track record scored via a proper scoring rule (e.g. Brier score) across many predictions.
- An engineer saying "I'm 90% sure this will fix it," checked over time against how often that's actually been true.
- A physician's diagnostic confidence calibrated against patient outcomes over the course of a career.

## Related

- [[reference-class-forecasting]] — supplies the base rate this skill anchors to.
- [[decision-journaling]] — the mechanism for logging predictions so they can later be scored.
- [[structured-forecasting]] — the composite pipeline this skill's output feeds into.
