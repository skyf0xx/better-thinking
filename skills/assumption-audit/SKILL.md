---
name: assumption-audit
description: >
  Surface the load-bearing assumptions beneath a claim or plan and test each
  for fragility. Use before committing to a plan, when a conclusion feels
  solid but stakes are high, or whenever someone says "obviously" about
  something that hasn't actually been checked.
type: atomic
category: analysis
difficulty: 2
tokens: ~870
dependencies: []
related: [first-principles, premortem, disconfirmation-search, epistemic-tagging]
---

# Assumption Audit

Surface the load-bearing assumptions beneath a claim or plan, and test each for fragility.

## Why

Conclusions are only as strong as their weakest unexamined assumption, and assumptions are invisible by default — that's what makes them assumptions. Naming them out loud converts a hidden risk into a checklist that can actually be worked through, and is the single most-depended-upon move in this entire collection: more composite skills call this one than any other.

## Use when / Don't use when

- **Use when:** before committing to a plan; a conclusion feels solid but stakes are high; someone says "obviously" about a claim that hasn't actually been checked.
- **Don't use when:** the claim is definitional or already fully specified, with nothing left implicit.

## Inputs → Outputs

- **Inputs:** a claim, plan, or forecast.
- **Outputs:** a list of assumptions tagged load-bearing or cosmetic, each with a fragility note and a way it could be tested.

## Principles

- Ask "what has to be true for this to hold?" — not "what do I believe?" The audit targets the plan's dependencies, not the author's confidence.
- Not all assumptions matter equally; rank by what breaks if the assumption turns out false.
- The cheapest assumptions to test should be tested first, so the audit produces action, not just a list.
- An assumption stated out loud can be disagreed with — surfacing it is the point, even if it turns out to hold.

## Procedure

1. State the claim or plan precisely.
2. List everything that must be true for it to work — inputs, behaviors, environment, timing.
3. Classify each: load-bearing (the claim collapses without it) versus cosmetic (the claim survives even if this is wrong).
4. For load-bearing assumptions, rate confidence and cost-to-test.
5. Test or validate the cheapest, highest-doubt assumptions first.
6. Report the surviving plan plus the assumptions still untested and their risk — this untested set is the explicit residual uncertainty.

## Common mistakes

- Listing assumptions without ranking them — a wall of text nobody actually acts on.
- Treating "obvious" as a reason to skip listing something, when "obvious" is often exactly where the risk hides.
- Auditing once and never re-auditing as conditions change and old assumptions quietly stop holding.

## Examples

- A growth forecast that assumes current conversion rates hold steady into next quarter.
- A migration plan that assumes zero data drift between source and destination.
- A negotiation position that assumes the counterparty's stated priority is actually their real one.

## Related

- [[first-principles]] — a deeper rebuild once cosmetic assumptions have been stripped away.
- [[premortem]] — a complementary technique that surfaces failure modes rather than assumptions directly.
- [[disconfirmation-search]] — the natural next step for testing a load-bearing assumption.
- [[epistemic-tagging]] — the general-purpose tagging discipline this skill applies specifically to assumptions.
