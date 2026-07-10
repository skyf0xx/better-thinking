---
name: after-action-review
description: >
  Compare intended outcome against actual outcome, diagnose the gap, and
  extract what to keep, drop, and change. Use after any completed effort
  worth learning from — both failures and successes — as a lightweight,
  general-purpose learning loop.
type: composite
category: metacognition
difficulty: 2
tokens: ~1110
dependencies: [counterfactual-reasoning, decision-journaling, epistemic-tagging]
related: [retrospective-facilitation, root-cause-investigation]
---

# After-Action Review

Compare intended outcome against actual outcome, diagnose the gap, and extract what to keep, drop, and change — a lightweight, general-purpose learning loop for any completed effort.

## Why

Experience alone doesn't produce learning — it requires an explicit comparison between what was intended and what happened, since memory alone tends to smooth over the gap or misattribute its cause. A short structured review captures the lesson while it's still fresh and specific, and works for both failures and successes, which most retrospection skips.

## Use when / Don't use when

- **Use when:** after any effort worth learning from — not only failures; successes deserve review too, to learn *why* they worked rather than just assuming it'll repeat. Lighter-weight than a full root-cause investigation, and suited to routine, frequent use.
- **Don't use when:** the effort was too trivial to yield a reusable lesson.

## Inputs → Outputs

- **Inputs:** a completed action, decision, or effort with an original intention.
- **Outputs:** a documented comparison of intended versus actual outcome, the diagnosed cause of any gap, and specific keep/drop/change items.

## Principles

- Compare against the *original* intention, not a retroactively adjusted version of what you meant to do — using `decision-journaling` output when it exists is what makes this comparison honest instead of self-serving.
- Review successes as rigorously as failures. A success with the wrong causal story teaches the wrong lesson for next time.
- The output must be specific and actionable — keep/drop/change items tied to a diagnosed cause, not a general mood about how it went.

## Procedure

1. State the original intention or plan, ideally from a contemporaneous source — run `decision-journaling` retrieval if an entry exists, rather than relying on memory.
2. State what actually happened, factually. Run `epistemic-tagging` to keep observed fact separated from interpretation at this stage.
3. Identify the gap, if any, between intended and actual outcome.
4. Diagnose the cause: was the plan wrong, the execution wrong, or was it an unforeseeable factor? Run `counterfactual-reasoning` — would a plausibly different choice have changed the outcome, or was this outcome likely regardless of the choice made?
5. For successes specifically, explicitly check that the causal story isn't just a comfortable narrative — did the plan actually cause the good outcome, or did it succeed despite the plan, for unrelated reasons?
6. Extract specific items: what to keep doing, what to stop doing, what to change — each tied to the diagnosed cause from step 4, not a vague impression. State clearly which parts of the diagnosis remain uncertain rather than papering over them with a tidy conclusion.

## Common mistakes

- Reviewing only failures and skipping successes, which teaches nothing about why the good outcomes actually happened.
- Comparing against a memory of the plan that's already drifted toward matching the outcome, instead of the original record.
- Producing vague takeaways ("communicate better") instead of specific, actionable changes tied to a real diagnosed cause.

## Examples

- Reviewing a completed project against its original charter to see where scope or assumptions drifted.
- A personal review of a negotiation outcome, checking whether the result came from the strategy or from the counterparty's unrelated circumstances.
- Reviewing why a successful product launch actually succeeded, specifically to know what's worth repeating next time.

## Related

- [[retrospective-facilitation]] — the group-facilitated version of this same review, with added consensus-mapping for disagreement.
- [[decision-journaling]] — the ideal contemporaneous input this review compares against.
- [[root-cause-investigation]] — a heavier, evidence-gated version suited to serious or recurring failures.
