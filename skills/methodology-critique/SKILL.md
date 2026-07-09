---
name: methodology-critique
description: >
  Find the design flaws that break a study's claimed inference, auditing
  how the knowledge was manufactured rather than just what it concludes.
  Use when a study anchors a decision, findings conflict across studies, or
  results are surprising or suspiciously aligned with the funder.
type: atomic
category: research
difficulty: 4
tokens: ~550
dependencies: []
related: [evidence-hierarchy, statistical-audit, peer-review]
---

# Methodology Critique

Find the design flaws that break a study's claimed inference — auditing how the knowledge was manufactured, not just what it concludes.

## Why

A study's conclusions inherit the validity of its design, and design flaws are invisible in the abstract. Most contested empirical questions turn on methodology, so the critique skill is the evaluation skill.

## Use when / Don't use when

- **Use when:** a study anchors a decision; findings conflict across studies; results are surprising or suspiciously aligned with the funder.
- **Don't use when:** methods aren't available to inspect — that absence is itself the finding, not a reason to skip critique entirely.

## Inputs → Outputs

- **Inputs:** a study or analysis with its methods available.
- **Outputs:** a validity assessment: which claimed inferences survive, which break, and on what specific design choice.

## Principles

- Match the critique to the inference — a design fine for correlation breaks for causation.
- Four validity questions: measurement (does the instrument measure the construct?), internal (does the design support the causal claim?), statistical (is the analysis sound and adequately powered?), external (does it generalize to the population you care about?).
- Researcher degrees of freedom — many analyses run, one reported — inflate everything.
- A flaw must connect to a conclusion; flaw-listing without consequence is pedantry.

## Procedure

1. State the claimed inference precisely — what does the study say it showed?
2. Measurement validity: what was actually measured, and how far is it from the construct in the claim?
3. Internal validity: comparison group, assignment mechanism, confounders, attrition, blinding where relevant.
4. Statistical validity: power, multiple comparisons, outcome switching, subgroup fishing.
5. External validity: study population and conditions versus the target of the claim.
6. For each flaw found, state which conclusion it breaks and how badly — some flaws are cosmetic.
7. Report a verdict: what this study establishes, at what strength, for whom, and what remains uncertain.

## Common mistakes

- Perfectionism — no study is flawless; the question is whether the flaws touch the conclusion.
- Asymmetric rigor, auditing only studies you dislike.
- Missing outcome-switching because the pre-registration was never checked.
- Critiquing statistics when the fatal wound is actually measurement.

## Examples

- A hiring-tool vendor study built on a survivorship-selected sample.
- A nutrition finding built on food-frequency recall.
- An A/B test analyzed with peeking; an education intervention evaluated by its own designers.

## Related

- [[evidence-hierarchy]] — ranks evidence types across a claim; this skill audits quality within one study.
- [[statistical-audit]] — the number-level audit that complements this design-level one.
- [[peer-review]] — the composite that invokes this as its correctness-checking engine.
