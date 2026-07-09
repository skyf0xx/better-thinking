---
name: scientific-method
description: >
  The full empirical loop: hypothesize, operationalize predictions, design a
  test that could fail, run it, attempt falsification, and update. Use when
  a belief is testable and consequential, or a debate could be settled by
  looking instead of arguing.
type: composite
category: research
difficulty: 4
tokens: ~1000
dependencies: [abductive-inference, assumption-audit, bayesian-updating, disconfirmation-search, sanity-checking, confidence-calibration, causal-analysis]
related: [differential-diagnosis, structured-forecasting, decision-analysis, structured-problem-solving]
---

# Scientific Method

The full empirical loop: hypothesize, operationalize predictions, design a test that could fail, run it, attempt falsification, and update.

## Why

Beliefs that never risk contact with disconfirming reality drift toward convenience. The method's power is the pre-commitment: saying what you expect before looking, so reality can actually disagree with you.

## Use when / Don't use when

- **Use when:** a belief is testable and consequential; a debate could be settled by looking; building anything on an unvalidated assumption.
- **Don't use when:** the question is normative or definitional — no experiment bears on it.

## Inputs → Outputs

- **Inputs:** a question or tentative belief about how something works.
- **Outputs:** an updated, calibrated belief with the test record — including what would still overturn it.

## Principles

- A hypothesis that cannot fail is not knowledge, it's decoration.
- Predictions are stated before observation, with the discriminating power made explicit — what result would each rival hypothesis predict?
- One disconfirmation outweighs many confirmations, but check the instrument before the theory.
- Negative results are results — record them.

## Procedure

1. State the question; run `abductive-inference` to generate rival hypotheses (≥2 — a lone hypothesis can only be confirmed, never compared).
2. Run `assumption-audit`: what does each hypothesis assume? Which assumptions are load-bearing and untested?
3. Operationalize: for each hypothesis, a concrete prediction — what will be observed, measured how, under what conditions. Prefer predictions where the rivals diverge.
4. Design the cheapest test with real discriminating power; state in advance what result supports what (`causal-analysis` discipline if the claim is causal).
5. Run it. Record everything, including the awkward parts.
6. Compare outcome to the pre-committed predictions. Run `sanity-checking` on surprises — instrument error first, then theory.
7. Update via `bayesian-updating`; run `disconfirmation-search` on the winner — what's the next observation that could still overturn it?
8. Report belief, confidence (`confidence-calibration`), the test record, and the standing falsification conditions.

## Common mistakes

- Predictions written after the data (HARKing).
- Testing only the favorite hypothesis.
- Rescuing a failed hypothesis with unplanned auxiliary assumptions ("it works, just not on Tuesdays").
- Running the expensive definitive test before the cheap discriminating one; treating one confirmation as proof.

## Examples

- A/B testing a pricing hypothesis.
- Debugging via predicted-vs-observed behavior at each layer.
- Validating a market assumption with a smoke test before building it out.

## Related

- [[differential-diagnosis]] — the find-the-cause variant, for an active abnormal condition rather than an open question.
- [[structured-forecasting]] — when the test must wait for reality to unfold rather than being run directly.
- [[decision-analysis]] — consumes the validated beliefs this produces.
- [[structured-problem-solving]] — the sibling composite for truth-shaped problems within a larger effort.
