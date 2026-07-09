---
name: error-analysis
description: >
  Classify mistakes by type and root cause, and target instruction or
  practice at the pattern behind them, not at the individual instance.
  Use when reviewing test results or any recurring-mistake pattern.
type: atomic
category: learning
difficulty: 2
tokens: ~780
dependencies: []
related: [deliberate-practice-design, self-explanation, root-cause-investigation]
---

# Error Analysis

Classify mistakes by type and root cause, and target instruction or practice at the pattern behind them — not at the individual instance.

## Why

Correcting each mistake as a one-off instance misses the underlying pattern generating a whole class of errors. Classifying errors by cause — a missing concept, a misapplied rule, a careless slip — determines what kind of intervention will actually fix it.

## Use when / Don't use when

- **Use when:** reviewing test results, code review feedback, or any recurring-mistake pattern; designing a targeted intervention rather than generic "be more careful" feedback.
- **Don't use when:** there's only one isolated mistake with no pattern to extract.

## Inputs → Outputs

- **Inputs:** a set of mistakes or errors from performance.
- **Outputs:** an error taxonomy with root causes, and the specific pattern(s) worth targeting.

## Principles

- Distinguish a slip (knew the right answer, executed carelessly) from a misconception (systematically wrong mental model) from a gap (never learned this) — each needs a different fix.
- Look across multiple errors for the repeated pattern rather than treating each as independent.
- The same surface mistake can stem from different root causes in different people — diagnose, don't assume.

## Procedure

1. Collect a representative set of errors, not just the most recent one.
2. For each, classify: slip, misconception, or gap.
3. Look for the repeated pattern across errors — often several surface mistakes trace to one underlying misconception.
4. For misconceptions, identify specifically what the wrong model is, not just that it's wrong.
5. Target the intervention to the cause: slips need attention/process fixes, misconceptions need direct confrontation, gaps need instruction.
6. Re-test after intervention to confirm the pattern, not just the instance, is resolved.

## Common mistakes

- Treating every error as a slip when it's actually a misconception requiring real correction.
- Correcting instances one by one without ever extracting the pattern.
- Assuming the same error type has the same cause across different learners.

## Examples

- Grading a batch of exams for the recurring misconception, not just marking each wrong answer.
- Code review patterns revealing a systematic misunderstanding of a language feature.
- A coach identifying a repeated technical flaw across multiple performances.

## Related

- [[deliberate-practice-design]] — targets the specific pattern this analysis identifies.
- [[self-explanation]] — a source of self-diagnosed errors this analysis can classify.
- [[root-cause-investigation]] — the same logic applied to systems instead of learners.
