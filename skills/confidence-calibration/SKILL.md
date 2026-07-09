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
tokens: ~820
dependencies: []
related: [reference-class-forecasting, decision-journaling, structured-forecasting]
---

# Confidence Calibration

Attach probabilities to beliefs that match their actual hit rate over time, checked against base rates and scored against outcomes.

## Why

Unaided confidence is systematically miscalibrated — usually overconfident on specific predictions. Calibration is trainable, but only if predictions are stated numerically and scored against outcomes; verbal hedges can never be checked.

## Use when / Don't use when

- **Use when:** stating any forecast or belief that matters enough to act on; after a process produces a conclusion needing a confidence label; periodically, to review a track record.
- **Don't use when:** the claim is a settled fact where numeric hedging adds noise, not information.

## Inputs → Outputs

- **Inputs:** a belief or forecast.
- **Outputs:** a numeric confidence level, ideally logged for later scoring against the outcome.

## Principles

- State confidence as a number or range, not a word ("likely") — words can't be scored, and different people read the same word as wildly different probabilities.
- Calibration means: among things called "80% confident," roughly 80% should happen. It's a property of a *set* of predictions, not any single one.
- Check a gut confidence level against a base rate before trusting it.
- Track a record over time; one well-calibrated-feeling guess proves nothing.

## Procedure

1. State the belief precisely enough to be scored later — a specific, resolvable outcome.
2. Assign a numeric probability, anchored first to a base rate if one exists.
3. Sanity-check: would you take a bet at these odds? If the number and the bet diverge, revise the number.
4. Log the prediction somewhere it will be revisited for scoring.
5. Periodically score past predictions: of the "70% confident" calls, did roughly 70% happen? Report the over/under-confidence pattern as the residual uncertainty.

## Common mistakes

- Using vague verbal hedges instead of numbers, making the claim unscoreable.
- Treating one correct high-confidence call as proof of good calibration — it's the long-run hit rate that matters.
- Never closing the loop: stating confidence but never checking it against outcomes.

## Examples

- A forecaster's track record scored via a proper scoring rule (e.g. Brier score) across many predictions.
- An engineer saying "I'm 90% sure this will fix it," checked over time against how often that's actually been true.
- A physician's diagnostic confidence calibrated against patient outcomes over the course of a career.

## Related

- [[reference-class-forecasting]] — supplies the base rate this skill anchors to.
- [[decision-journaling]] — the mechanism for logging predictions so they can later be scored.
- [[structured-forecasting]] — the composite pipeline this skill's output feeds into.
