---
name: structured-forecasting
description: >
  The superforecaster pipeline: decompose the question, anchor on a base
  rate, adjust with named evidence, express calibrated confidence, and
  schedule updates. Use when a forecast will inform a real decision and
  is specific enough to be scored later.
type: composite
category: forecasting
difficulty: 4
tokens: ~940
dependencies: [question-decomposition, reference-class-forecasting, bayesian-updating, uncertainty-decomposition, confidence-calibration, tripwires]
related: [decision-analysis, scenario-planning, delphi-aggregation]
---

# Structured Forecasting

The superforecaster pipeline: decompose the question, anchor on a base rate, adjust with named evidence, express calibrated confidence, and schedule updates.

## Why

Forecasting accuracy research consistently shows the same disciplined process beats both raw expertise and unaided intuition. The gains come from decomposition, outside-view anchoring, and disciplined updating — not from any special genius.

## Use when / Don't use when

- **Use when:** a forecast will inform a real decision and is specific or resolvable enough to be scored later; recurring forecasting needs like planning cycles or risk assessment.
- **Don't use when:** the question can't be made resolvable — sharpen it first, or this pipeline has nothing to grip.

## Inputs → Outputs

- **Inputs:** a forecasting question with a resolvable outcome and horizon.
- **Outputs:** a probability or range with the reasoning shown, a calibration check, and a schedule for revisiting.

## Principles

- Decompose before estimating — compound questions get compound answers.
- Start from the outside view, adjust modestly with inside-view evidence, in that order.
- Express uncertainty as a probability or range, not a verbal hedge that can't be scored.
- A forecast isn't finished until it has a revisit trigger — forecasts decay as the world changes.

## Procedure

1. Sharpen the question until it's resolvable: specific outcome, specific timeframe, specific resolution criteria. Run `question-decomposition` if it's compound.
2. Establish the outside view via `reference-class-forecasting` for a base rate.
3. Gather the specific evidence for this case; weigh it via `bayesian-updating` against the base rate, resisting swinging further than the evidence's actual strength warrants.
4. Run `uncertainty-decomposition`: how wide should the confidence range genuinely be, and is more research worth it before finalizing?
5. State the forecast as a number or range, not a word. Run `confidence-calibration`: does this reflect genuine hit-rate expectations, or optimism/pessimism bias?
6. Set `tripwires` for what evidence would most shift the forecast, and schedule a revisit date.
7. After resolution, score the forecast against the outcome and feed the result back into your calibration record.

## Common mistakes

- Anchoring on inside-view story-telling before checking the base rate.
- Expressing confidence in unscoreable verbal terms.
- Treating a forecast as permanent once made instead of updating on schedule.
- Never closing the loop — skipping the post-resolution scoring that's the entire mechanism for improving calibration over time.

## Examples

- Forecasting whether a project ships on time.
- Estimating the probability a deal closes this quarter.
- Geopolitical or market forecasting; predicting whether a policy will pass.

## Related

- [[decision-analysis]] — the composite this forecast typically feeds.
- [[scenario-planning]] — used instead when the future has multiple qualitatively distinct paths rather than a single probability.
- [[delphi-aggregation]] — aggregates multiple independent forecasters' versions of this pipeline.
