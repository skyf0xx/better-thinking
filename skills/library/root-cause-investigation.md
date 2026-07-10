---
name: root-cause-investigation
description: >
  Evidence-driven investigation of a failure: establish the timeline,
  generate causal hypotheses, test against evidence, and verify the fix
  prevents recurrence. Use when a failure matters enough to prevent, not
  just patch, or when the same problem has recurred.
type: composite
category: problem-solving
difficulty: 3
tokens: ~860
dependencies: [five-whys, causal-analysis, abductive-inference, evidence-triangulation, assumption-audit, tripwires]
related: [differential-diagnosis, after-action-review]
---

# Root Cause Investigation

Evidence-driven investigation of a failure: establish the timeline, generate causal hypotheses, test against evidence, and verify the fix prevents recurrence.

## Why

Post-incident narratives converge on the first plausible story, and fixes applied to the wrong cause create false confidence plus eventual recurrence. This pipeline forces evidence to lead and story to follow, rather than the reverse.

## Use when / Don't use when

- **Use when:** the failure matters enough to prevent, not just patch; the same problem has recurred; multiple factors seem entangled.
- **Don't use when:** the cause is obvious and singular — plain `five-whys` suffices there.

## Inputs → Outputs

- **Inputs:** a failure, incident, or defect.
- **Outputs:** a verified causal chain, contributing factors, a fix at the preventive level, and recurrence indicators.

## Principles

- Timeline before theory — establish what actually happened before generating explanations for it.
- Every causal link needs evidence, not plausibility.
- Hunt for *contributing conditions*, not just the trigger — triggers are unpredictable, conditions are fixable.
- The investigation isn't done until "how will we know if it recurs?" has an answer.

## Procedure

1. Freeze the facts: build a timeline of events with evidence for each entry, separating observation from inference throughout.
2. Run `abductive-inference` to generate at least three causal stories, including the boring ones.
3. Test each story against the timeline; discard those the evidence contradicts. Use `evidence-triangulation` on any load-bearing fact.
4. For the surviving story, run `five-whys` down to process or design level; run `causal-analysis` to separate the trigger from standing conditions.
5. Run `assumption-audit` on the conclusion: what would have to be true for this story to be wrong?
6. Design the fix at the preventive level, not the trigger level; set `tripwires` for recurrence.
7. Report: the chain, its evidence, the fix's level, and the residual risk that remains.

## Common mistakes

- Narrative lock-in after step 2, abandoning genuine testing of rival stories.
- Fixing the trigger while leaving the standing conditions untouched, guaranteeing eventual recurrence.
- Skipping step 6, so recurrence goes undetected until it's a crisis again.
- Letting the analysis terminate at "human error," which is a symptom, not a cause.

## Examples

- A production outage postmortem.
- A clinical adverse event review.
- Diagnosing why a strong candidate declined an offer.
- Diagnosing why a quarterly forecast missed by 30%.

## Related

- [[differential-diagnosis]] — the sibling composite for an *ongoing* failure where the cause must be found to stop it, not just explained after the fact.
- [[after-action-review]] — the lighter-weight composite for non-failure learning.
