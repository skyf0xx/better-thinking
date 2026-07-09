---
name: epistemic-tagging
description: >
  Label every claim in a piece of reasoning as fact, inference, assumption,
  or speculation, making the reasoning's actual evidential structure
  visible. Use when writing or reviewing any analysis where the confidence
  level of different claims matters, or when a conclusion needs its
  foundation audited.
type: atomic
category: metacognition
difficulty: 1
tokens: ~450
dependencies: []
related: [assumption-audit, critical-reading, confidence-calibration]
---

# Epistemic Tagging

Label every claim in a piece of reasoning as fact, inference, assumption, or speculation — making the reasoning's actual evidential structure visible.

## Why

Prose blends established fact with plausible inference with pure guesswork seamlessly, and readers — including the author, later — lose track of which is which. Explicit tagging prevents a speculation from quietly hardening into a treated-as-fact premise three steps later, which is one of the most common ways confident-sounding conclusions turn out to rest on nothing.

## Use when / Don't use when

- **Use when:** writing or reviewing any analysis where the confidence level of different claims matters; a conclusion needs its foundation audited before being acted on.
- **Don't use when:** the content is uniformly one type (e.g., all directly observed fact) — tagging adds no information there.

## Inputs → Outputs

- **Inputs:** a piece of reasoning, analysis, or written conclusion.
- **Outputs:** the same content with each claim tagged by its epistemic status, and any status upgrades or downgrades flagged explicitly.

## Principles

- Fact = directly verified or verifiable. Inference = follows from facts via reasoning that's been stated. Assumption = accepted as a premise but not independently verified. Speculation = a guess offered with low confidence. These four should stay visibly distinct throughout a chain of reasoning.
- A claim's tag can and should change as it's used elsewhere in the same piece — an assumption in one paragraph must not silently become a fact by the conclusion.

## Procedure

1. Go through the claims in the reasoning one at a time.
2. Tag each: fact / inference / assumption / speculation.
3. For inferences, check that the reasoning connecting them to their source facts actually holds — run a validity check if the inference is doing real work.
4. Check for status drift: does an assumption or speculation get treated as settled fact later in the same piece?
5. Where drift is found, either downgrade the later claim back to its honest status, or explicitly upgrade it with the evidence that would justify the promotion.
6. Report the conclusion's actual epistemic foundation — how much of it rests on verified fact versus assumption or speculation — as the final, explicit statement of residual uncertainty.

## Common mistakes

- Tagging once at the start and letting status silently drift through the rest of the document.
- Treating "assumption" as a lesser or embarrassing tag to avoid using, rather than useful information about where the real risk sits.
- Tagging so granularly (word-by-word rather than claim-by-claim) that the exercise obscures more than it clarifies.

## Examples

- Auditing an investment thesis for which parts are verified data versus assumed market behavior.
- A legal memo separating established fact from inference from the client's own account of events.
- A forecast report distinguishing data-backed claims from judgment calls, so a reader knows exactly where to push back.

## Related

- [[assumption-audit]] — a deeper dive specifically into the assumption-tagged claims, testing each for fragility.
- [[critical-reading]] — uses this tagging discipline when extracting claims from someone else's text.
- [[confidence-calibration]] — the natural next step once claims are tagged, for attaching actual probabilities.
