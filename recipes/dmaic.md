# Recipe: DMAIC (Six Sigma)

**What it is:** the Define-Measure-Analyze-Improve-Control cycle for improving an existing process — pin down the problem and its goal, find out what's actually happening, isolate the real cause, fix it, then lock the fix in so the process doesn't drift back.

## Skill sequence

1. **Define** — run **[[problem-framing]]** to state the process problem precisely and generate multiple candidate framings before picking one, then **[[mece-decomposition]]** to break the process into genuinely distinct stages or components so "the process" isn't treated as one opaque blob. Output: a chosen problem framing plus a structural map of the process it lives in.
2. **Measure** — run **[[knowledge-gap-analysis]]** against the framed problem: what's already known about how the process performs, what's a known-unknown worth instrumenting, and a prioritized plan to close the gap. This stage deliberately doesn't assume the user already has data — its job is to say what to go measure, not to audit numbers that may not exist yet. If the user already has quantitative claims about performance ("defect rate is 4%," "this step takes 3 days on average"), run **[[statistical-audit]]** on those specific claims before trusting them as the Analyze stage's input.
3. **Analyze** — run **[[causal-analysis]]** to build a causal graph of the process and the rival explanations for the observed problem, then **[[root-cause-investigation]]** to drive from correlated factors to a verified causal chain with a fix pitched at the preventive level, not just the proximate one.
4. **Improve** — run **[[solution-space-mapping]]** on the verified root cause to lay out the taxonomy of fixes available (not just the first one that comes to mind), **[[weighted-scoring]]** to rank candidate fixes against real criteria, and **[[cost-benefit]]** to price the leading candidate honestly, including the cost of the change itself, not just its expected payoff.
5. **Control** — run **[[tripwires]]** to set specific, observable indicators that fire if the process drifts back toward the old failure mode, **[[progress-monitoring]]** to check the fix against plan at defined checkpoints, and **[[feedback-loop-analysis]]** to identify whether the process has a reinforcing loop that could undo the fix over time (e.g. incentives that quietly reward the old behavior) and where to intervene if so.

## What this buys you over a plain DMAIC checklist

- "Define" gets `problem-framing`'s discipline of generating rival framings instead of accepting the first plausible statement of what's wrong, plus an explicit structural decomposition instead of treating "the process" as a single unit.
- "Measure" doesn't presume a dataset already exists — `knowledge-gap-analysis` produces a measurement plan when there's nothing to measure yet, and only invokes `statistical-audit` conditionally, when the user already has numbers worth stress-testing.
- "Analyze" separates correlation from verified cause via `causal-analysis` before `root-cause-investigation` commits to a fix, instead of jumping from "these two things move together" straight to "this is the cause."
- "Improve" forces a real option set (`solution-space-mapping`) and honest pricing (`cost-benefit`) before locking in a fix, instead of implementing the first idea that plausibly addresses the root cause.
- "Control" is genuinely closed-loop: `tripwires` plus `feedback-loop-analysis` catch the classic Six Sigma failure mode where a process improves temporarily and then reverts once attention moves elsewhere.

## Residual gap

DMAIC assumes an existing process to improve — it has no stage for standing up a process from nothing. If there's no process yet, this recipe doesn't apply; consider [[design-thinking]] or a first-principles build instead, then bring DMAIC in once the process exists and needs tightening. Physically implementing the Improve-stage fix (new equipment, a rewritten SOP, a code change) is also outside this collection's scope, same as the Prototype/Build gaps in [[design-thinking]] and [[lean-startup]] — this collection determines what to fix and why, not how to execute the change.

## Related recipes

- [[lean-startup]] — DMAIC tightens an existing, known process; lean-startup de-risks a new, unproven one. Different problem shape, similar discipline of measure-then-decide.
- [[rice-prioritization]] — if Improve surfaces multiple candidate fixes competing for the same limited engineering time across several processes at once, RICE is the natural way to sequence them.
