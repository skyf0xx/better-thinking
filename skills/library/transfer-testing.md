---
name: transfer-testing
description: >
  Verify real understanding by applying it in a structurally novel
  context, one that shares the underlying principle but not the surface
  features of how it was learned. Use to confirm a learner actually
  understands a principle, not just recognizes familiar problems.
type: atomic
category: learning
difficulty: 3
tokens: ~810
dependencies: []
related: [self-explanation, error-analysis, analogical-reasoning]
---

# Transfer Testing

Verify real understanding by applying it in a structurally novel context — one that shares the underlying principle but not the surface features of how it was learned.

## Why

Performance on problems structurally identical to the training examples can reflect pattern-matching to surface features rather than genuine understanding of the underlying principle. A structurally novel test is what actually distinguishes the two.

## Use when / Don't use when

- **Use when:** confirming a learner, including yourself, actually understands a principle, not just recognizes familiar problems; before relying on a skill in a new context.
- **Don't use when:** near-transfer within the same context is all that's actually needed.

## Inputs → Outputs

- **Inputs:** a claimed understanding of a concept or skill.
- **Outputs:** a verdict on whether the understanding transfers, tested via a novel-surface, same-principle application.

## Principles

- The test problem must share the deep structure while differing in surface features from how it was learned.
- Failure on a transfer test is diagnostic, not just disappointing — it locates exactly which part of the "understanding" was actually surface pattern-matching.
- Near-transfer (same domain, new instance) is weaker evidence than far-transfer (different domain, same principle).

## Procedure

1. Identify the underlying principle the learner is meant to have grasped.
2. Construct a test scenario with different surface features but the same underlying principle.
3. Present it without signaling "this is the same as what you learned."
4. Observe whether they apply the principle correctly, or fail to recognize its relevance under the new surface.
5. On failure, diagnose via error-analysis whether the gap is the principle itself or just the transfer step.
6. Prefer far-transfer tests over near-transfer for a stronger verdict.

## Common mistakes

- Testing with a superficially different but structurally identical problem — still surface pattern-matching, not real transfer.
- Interpreting a failed transfer test as "they don't understand at all" rather than diagnosing which piece broke.
- Only ever testing near-transfer, overestimating how robust the understanding is.

## Examples

- Testing a math principle in a word-problem context different from how it was taught.
- Testing whether a negotiation principle learned in one domain applies in an unrelated one.
- A hiring interview's case study designed to differ from the candidate's past work.

## Related

- [[self-explanation]] — the lighter-weight check this deeper test follows.
- [[error-analysis]] — diagnoses the cause of a transfer-test failure.
- [[analogical-reasoning]] — the underlying mechanism transfer depends on.
