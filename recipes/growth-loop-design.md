# Recipe: Growth Loop Design

**What it is:** the growth-hacking practice (Sean Ellis, Andrew Chen) of deliberately designing a product's built-in viral mechanic — generating candidate loop ideas, then vetting each on whether it actually spreads person-to-person — rather than hoping virality emerges as a side effect of the product being good.

## Skill sequence

1. **Sharpen the target vector** — if the growth target is vague ("we want more users"), use **[[multi-framework-ideation]]**'s Who×Job×Friction pre-phase to ground it in a specific audience, job-to-be-done, and evidenced friction before generating loop ideas. Skip straight to step 2 if the brief is already concrete (e.g. "a shareable mechanic for our onboarding flow").
2. **Generate candidate loops** — run **[[multi-framework-ideation]]** across its four passes (morphological, analogical, provocation, first-principles) to produce a wide, structurally diverse set of raw loop-mechanic ideas. This is the step growth teams most often skip, defaulting to whatever loop shape (referral program, invite gate) the last company they worked at used — the point of running all four passes is to surface loop shapes that aren't just that same default relabeled.
3. **Score for spread potential** — run **[[spread-potential-scoring]]** on the raw list: five multiplicative gates (Payload, Transport-Reach, Sender Payoff, Receive Conversion, Loop Closure), each scored 0-2 and multiplied, not averaged, so a single fatal gate zeroes an idea outright instead of hiding behind strong scores elsewhere.
4. **Check retention shape** — for ideas surviving step 3, confirm each one's Cadence (one-shot/periodic/habitual) and Audience Density (sparse/clustered) modifiers from that same skill; demote high-scoring one-shot ideas with no retention hook below lower-scoring ideas that have one.
5. **Sequence what to build first** — run **[[prioritization-triage]]** (or **[[weighted-scoring]]** if effort/cost estimates are already in hand) on the surviving, ranked loop ideas against build cost, to decide which loop mechanic actually gets built first.
6. **Instrument and verify** — before shipping, run **[[sanity-checking]]** on the chosen mechanic's assumed loop math (K-factor, cycle time) against realistic numbers, so the loop is validated against real usage data once live, not just against the scoring rubric's predictions.

## What this buys you over ad hoc "let's add a referral program" growth work

- Loop mechanics get generated from four genuinely different mechanisms instead of defaulting to whatever loop shape is culturally standard (referral codes, invite walls) — `multi-framework-ideation`'s whole premise is that a single brainstorm collapses toward one region of idea-space.
- Every candidate is scored on the actual mechanics of spread (a nameable artifact, a 5-second receiver action, an automatic byproduct) instead of a vague "this feels viral" judgment.
- The multiplicative scoring catches ideas that are strong everywhere except one fatal gate (e.g. huge payload, but no shareable artifact) — a failure mode averaging-based scoring hides.
- One-shot novelty loops with no re-arm mechanism get explicitly demoted, instead of getting built, spiking, and dying with no one having flagged the risk upfront.

## Residual gap

This recipe designs and vets the loop mechanic; it doesn't build or run the growth experiment itself, and it doesn't cover the broader product-market-fit question of whether the underlying product is worth spreading in the first place — pair with [[jobs-to-be-done]] or [[lean-startup]] if that's still an open question. The actual K-factor math and live experiment analysis (step 6) is deliberately light — if the growth loop is a major bet, run [[lean-startup]]'s measure/learn stages on it directly instead of this recipe's single sanity-check step.

## Related recipes

- [[lean-startup]] — the natural upstream check when it's still unclear whether the underlying product is worth building a growth loop around at all; this recipe presumes that's settled.
- [[jobs-to-be-done]] — supplies the real motivational job behind step 1's Who×Job×Friction sharpening, if that job isn't already known.
- [[rice-prioritization]] — a heavier alternative to step 5 when the surviving loop ideas need to be sequenced against a broader, non-growth backlog rather than just against each other.
