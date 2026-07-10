---
name: analogical-reasoning
description: >
  Transfer structure from a well-understood source domain to a target
  problem, then explicitly verify the mapping holds where it matters. Use
  when a problem resembles something solved elsewhere, when generating
  approaches for a novel situation, or when evaluating someone's
  persuasive analogy.
type: atomic
category: reasoning
difficulty: 3
tokens: ~890
dependencies: []
related: [explanatory-analogy, concept-blending, mental-model-extraction]
---

# Analogical Reasoning

Transfer structure from a well-understood source domain to a target problem, then explicitly verify the mapping holds where it matters.

## Why

Analogy is the fastest way to import a solved problem's machinery into a new one — and, unverified, the fastest way to import wrong conclusions when surface similarity masks a real structural difference. The verification step is what turns analogy from rhetoric into reasoning.

## Use when / Don't use when

- **Use when:** the problem resembles something solved elsewhere; generating approaches for a genuinely novel situation; evaluating someone else's persuasive analogy before accepting its conclusion.
- **Don't use when:** direct analysis of the target problem is cheap and available — analogy is a bridge to insight, not a destination in itself.

## Inputs → Outputs

- **Inputs:** a target problem plus one or more candidate source domains.
- **Outputs:** a structure mapping, the transferred insight, and a list of disanalogies with their consequences.

## Principles

- Map relations, not surface features — "both involve networks" is a surface match, not a structural one.
- An analogy is an argument only where the mapped structure is causally relevant to the conclusion being drawn.
- Every analogy breaks somewhere; find where before relying on it for anything consequential.

## Procedure

1. State the target problem's essential structure — its entities, relations, and constraints.
2. Search for source domains sharing that *relational* structure, not just surface resemblance; list 2–3 candidates.
3. For the best candidate, build the explicit mapping: what in the source corresponds to what in the target.
4. Transfer the source's solution or lesson through that mapping.
5. Hunt for disanalogies: relations present in the target with no source counterpart, and vice versa.
6. Judge whether any disanalogy touches the causal path of the transferred lesson — if so, discard or repair the transfer.
7. Report the insight plus the specific boundary where the analogy stops working as the residual uncertainty.

## Common mistakes

- Matching on surface features instead of relational structure.
- Riding the analogy past its breaking point instead of stopping at the boundary found in step 6.
- Adopting the first analogy that comes to mind instead of comparing several candidates.

## Examples

- Using epidemiology's spread models to reason about how misinformation propagates through a network.
- Treating technical debt with financial-debt intuitions, then explicitly finding where the analogy breaks (technical debt doesn't compound at a fixed, knowable rate).
- Porting immune-system self/non-self tolerance concepts to content moderation policy design.

## Related

- [[explanatory-analogy]] — the same machinery, aimed at teaching rather than problem-solving.
- [[concept-blending]] — a stronger move merging two frames into a new space rather than just transferring one.
- [[mental-model-extraction]] — often supplies the source domain's structure.
