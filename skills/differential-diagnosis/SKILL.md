---
name: differential-diagnosis
description: >
  Enumerate the possible causes of an observed condition, order them by
  probability and severity, and run the tests that discriminate fastest
  - medicine's algorithm, generalized. Use when something is actively
  wrong, multiple causes are possible, and testing is costly.
type: composite
category: problem-solving
difficulty: 4
tokens: ~900
dependencies: [abductive-inference, bayesian-updating, reference-class-forecasting, sanity-checking, disconfirmation-search]
related: [root-cause-investigation, competing-hypotheses]
---

# Differential Diagnosis

Enumerate the possible causes of an observed condition, order them by probability and severity, and run the tests that discriminate fastest — medicine's algorithm, generalized.

## Why

Debugging-by-hunch tests hypotheses in the order they came to mind. Ordering by prior times severity times test-cost, and choosing tests for discrimination power, finds the cause faster and never silently drops the dangerous possibility.

## Use when / Don't use when

- **Use when:** something is actively wrong, multiple causes are possible, and testing is costly — debugging, medical-style triage, churn spikes, machine faults.
- **Don't use when:** one cause is near-certain, or the condition is historical — use root-cause-investigation instead.

## Inputs → Outputs

- **Inputs:** an ongoing abnormal condition in a system, organism, or organization.
- **Outputs:** a ranked differential, test results, the confirmed cause or narrowed set, and explicitly ruled-out dangerous causes.

## Principles

- Common things are common — priors come from base rates, not memorability.
- "Can't-miss" causes get tested early even when improbable, because the cost of missing them dominates.
- The best next test is the one whose result most reshapes the ranking per unit cost.
- Diagnosis is iterative — each result re-ranks the list.

## Procedure

1. Characterize the condition precisely: what's abnormal, since when, what changed around onset, what's normal — the pertinent negatives.
2. Generate the differential via `abductive-inference`: plausible causes plus the dangerous ones regardless of plausibility.
3. Assign priors from base rates via `reference-class-forecasting`; tag each cause with severity-if-missed.
4. Order the worklist by prior, promoted by severity and demoted by test cost.
5. Choose the test with the best discrimination-per-cost, preferring tests that split the list over tests that confirm the favorite.
6. Update the ranking on each result via `bayesian-updating`. Prune what's ruled out; add what new evidence suggests.
7. Stop when one cause explains all findings and the can't-miss causes are affirmatively excluded. Run `disconfirmation-search` on the final answer, and `sanity-checking` on the conclusion.
8. Report: cause, confidence, what was ruled out, and what re-presentation would reopen the case.

## Common mistakes

- Anchoring on the first hypothesis and ordering tests to confirm it.
- Satisfaction-of-search — stopping at one cause when two are present.
- Never writing the differential down; the unlisted cause can't be found.
- Ignoring pertinent negatives.

## Examples

- Intermittent API latency: GC, noisy neighbor, connection pool, DNS, retry storm.
- A patient fatigue workup.
- Sudden CAC increase: tracking bug, mix shift, competitor, seasonality.

## Related

- [[root-cause-investigation]] — the post-hoc sibling for historical, resolved failures.
- [[competing-hypotheses]] — the same logic applied to beliefs instead of live systems.
