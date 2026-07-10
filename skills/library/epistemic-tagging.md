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
tokens: ~850
dependencies: []
related: [assumption-audit, critical-reading, confidence-calibration]
---

# Epistemic Tagging

Label every claim in a piece of reasoning as fact, inference, assumption, or speculation — making the reasoning's actual evidential structure visible.

## Why

Prose blends established fact with plausible inference with pure guesswork seamlessly, and readers — including the author, later — lose track of which is which. Explicit tagging prevents a speculation from quietly hardening into a treated-as-fact premise, one of the most common ways confident conclusions rest on nothing.

## Use when / Don't use when

- **Use when:** writing or reviewing analysis where confidence level matters; a conclusion needs its foundation audited before acting on it.
- **Don't use when:** the content is uniformly one type — tagging adds no information there.

## Inputs → Outputs

- **Inputs:** a piece of reasoning, analysis, or written conclusion.
- **Outputs:** the content with each claim tagged by epistemic status, and any status upgrades or downgrades flagged.

## Principles

- Fact = directly verified. Inference = follows from stated facts via stated reasoning. Assumption = accepted premise, unverified. Speculation = a low-confidence guess. These four stay visibly distinct throughout.
- A claim's tag can and should change as it's used elsewhere — an assumption in one paragraph must not silently become a fact by the conclusion.

## Procedure

1. Go through the claims in the reasoning one at a time.
2. Tag each: fact / inference / assumption / speculation.
3. For inferences, check the reasoning connecting them to source facts actually holds.
4. Check for status drift: does an assumption or speculation get treated as settled fact later?
5. Where drift is found, downgrade the later claim, or explicitly upgrade it with the evidence that justifies the promotion.
6. Report the conclusion's actual epistemic foundation — how much rests on fact versus assumption — as the residual uncertainty.

## Common mistakes

- Tagging once at the start and letting status silently drift through the rest of the document.
- Treating "assumption" as an embarrassing tag to avoid, rather than useful information about where risk sits.
- Tagging word-by-word instead of claim-by-claim, obscuring more than it clarifies.

## Examples

- Auditing an investment thesis for which parts are verified data versus assumed market behavior.
- A legal memo separating established fact from inference from the client's own account of events.
- A forecast report distinguishing data-backed claims from judgment calls, so a reader knows exactly where to push back.

## Related

- [[assumption-audit]] — a deeper dive specifically into the assumption-tagged claims, testing each for fragility.
- [[critical-reading]] — uses this tagging discipline when extracting claims from someone else's text.
- [[confidence-calibration]] — the natural next step once claims are tagged, for attaching actual probabilities.
