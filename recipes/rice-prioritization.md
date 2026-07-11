# Recipe: RICE Prioritization

**What it is:** the Reach/Impact/Confidence/Effort framework for deciding which feature or initiative to build next out of a backlog of candidates, by scoring each on a common basis instead of by whoever argues loudest.

## Skill sequence

1. **Decompose the backlog** — run **[[mece-decomposition]]** on the candidate list so it's a set of genuinely distinct, non-overlapping options rather than several phrasings of the same idea or a vague "and also maybe X" tacked onto a bigger item.
2. **Score Reach × Impact × Confidence** — run **[[weighted-scoring]]** with Reach, Impact, and Confidence as the weighted criteria. RICE is a named instance of weighted-scoring: Reach (how many users/period), Impact (how much per user), Confidence (how sure you are of the first two) are the criteria; the arithmetic combination is the score. Use **[[expected-value]]** explicitly for the Impact × Confidence term if the impact estimate is itself uncertain or bimodal (a feature that's huge if it lands and near-zero otherwise needs an EV treatment, not a point estimate).
3. **Price the Effort side** — run **[[cost-benefit]]** to size Effort honestly, including the opportunity cost of what else the same engineering time could produce, not just raw hours. This is the step most RICE exercises shortchange — Effort gets an eyeballed t-shirt size instead of the same rigor Reach/Impact got.
4. **Sequence the output** — run **[[prioritization-triage]]** on the resulting RICE scores to produce an actual ordered sequence, not just a scored-but-unordered list — including calling out ties, near-ties, and any items whose score is so uncertain (per step 2's confidence term) that they need more information before ranking rather than a forced score.
5. **Sanity-check reversibility** — before locking the sequence, run a quick pass of **[[reversibility-classification]]** on the top few items: an easily-reversible feature worth trying earlier than its raw score suggests, and a hard-to-reverse one (schema changes, pricing, public APIs) worth a second look even at a high score.

## What this buys you over a plain RICE spreadsheet

- The backlog itself is checked for overlap and vagueness before scoring starts, instead of scoring three different phrasings of the same feature as if they were independent options.
- Impact/Confidence gets an actual expected-value treatment when the estimate is uncertain, instead of a single confident-looking number that hides a coin flip.
- Effort is priced with real opportunity cost via `cost-benefit`, not a gut-feel t-shirt size — the step where most RICE exercises quietly lose their rigor.
- The final list is a genuine sequence with ties and low-confidence items flagged, not a spreadsheet sort that pretends every score is equally trustworthy.
- Reversibility gets a final, explicit look — RICE's math alone doesn't distinguish "safe to try and see" from "hard to walk back," and this step adds that check for free.

## Residual gap

RICE presumes a backlog of already-identified candidate features; it doesn't generate the candidates themselves. Pair with [[jobs-to-be-done]] or a divergent-ideation pass (e.g. [[ideation-sprint]]) upstream if the backlog itself needs populating, not just ranking.

## Related recipes

- [[jobs-to-be-done]] — typically feeds this recipe's backlog: JTBD identifies real needs worth building for, RICE then sequences which to build first.
- [[lean-startup]] — once a RICE-prioritized feature ships, lean-startup's measure/learn loop is how its actual impact gets checked against the Impact/Confidence estimate used to rank it.
- [[dmaic]] — if Improve surfaces multiple candidate fixes competing for the same limited engineering time across several processes at once, RICE is the natural way to sequence them.
