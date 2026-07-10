---
name: case-analysis
description: >
  IRAC generalized - identify the issue, determine the governing
  rules or principles, apply them to the facts, and reach a conclusion.
  Use for applying any rule system to a specific situation, legal,
  policy, contractual, or procedural.
type: composite
category: analysis
difficulty: 3
tokens: ~800
dependencies: [question-decomposition, argument-mapping, steelmanning, analogical-reasoning]
related: [argument-mapping, analogical-reasoning, steelmanning]
---

# Case Analysis

IRAC generalized: identify the issue, determine the governing rules or principles, apply them to the facts, and reach a conclusion — a structure for any rule-governed judgment.

## Why

Judgment under a rule system fails when the issue is misidentified or the rule is applied to facts it doesn't actually govern. The four-part structure forces each link to be checked separately.

## Use when / Don't use when

- **Use when:** applying any rule system to a specific situation — legal questions, policy compliance, contractual interpretation, procedural rulings, or codified organizational policy.
- **Don't use when:** no governing rule system exists — this isn't for open-ended judgment calls.

## Inputs → Outputs

- **Inputs:** a fact pattern plus a governing rule system.
- **Outputs:** the issue framed precisely, the applicable rules stated, the application reasoned through, and a conclusion with its confidence and the strongest counter-analysis.

## Principles

- The issue must be stated precisely enough that the rule's applicability is testable.
- Rules have elements — check each one against the facts, not the rule's gist.
- Precedent applies through analogical mapping — the mapping must hold, not just the surface similarity.
- A conclusion should state its confidence and the best counter-argument.

## Procedure

1. **Issue:** state the precise question the facts raise under the rule system. Run `question-decomposition` if it bundles multiple issues.
2. **Rule:** identify the governing rule(s), stated with their actual elements or conditions, not summarized loosely.
3. **Application:** work through each element against the specific facts. Where similar prior cases are used, verify the analogy holds via `analogical-reasoning` rather than assuming surface similarity suffices.
4. Run `steelmanning` on the counter-position — the strongest argument the rule doesn't apply, or applies differently.
5. **Conclusion:** state the answer, its confidence, and what fact, if different, would flip it.
6. Map the full reasoning with `argument-mapping` if the analysis will be scrutinized or contested.

## Common mistakes

- Stating the issue too broadly, inviting rule-shopping.
- Applying the rule's "spirit" while skipping its actual elements.
- One-sided application with no counter-analysis.

## Examples

- Contract interpretation dispute.
- Whether an action violates a specific policy.
- Applying an internal engineering standard to an edge-case design.

## Related

- [[argument-mapping]] — structures the reasoning for scrutiny.
- [[analogical-reasoning]] — verifies precedent actually maps.
- [[steelmanning]] — ensures the counter-position gets a fair hearing.
