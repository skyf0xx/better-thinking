# Recipe: Lean Startup (Build-Measure-Learn)

**What it is:** Eric Ries's loop for de-risking a new product or business bet — form a hypothesis about what customers want, build the smallest thing that tests it, measure real behavior, and decide whether to persevere or pivot.

## Skill sequence

1. **Frame the bet** — run **[[decision-framing]]** to state precisely what's being tested, who decides, and what the deadline for a verdict is. Lean-startup cycles fail most often from a vague hypothesis ("people will like this"), which this step forces into something falsifiable.
2. **Build (hypothesize + predict)** — run the first two stages of **[[scientific-method]]**: state the hypothesis explicitly and the specific, falsifiable prediction the minimum-viable build is meant to test. The "build" itself (the MVP) is outside this collection's scope — a construction step, not a reasoning step — but what to build is fully determined by what prediction needs testing.
3. **Measure (test + attempt falsification)** — run the corresponding stages of **[[scientific-method]]**: gather real usage data, and actively hunt for the way the data would prove the hypothesis wrong rather than only checking for confirming signal. Pair with **[[statistical-audit]]** if the metrics involve small samples, unclear denominators, or early-stage vanity metrics — a common lean-startup failure mode is reading noise as signal.
4. **Learn (update)** — run **[[bayesian-updating]]** on the original hypothesis given the measured evidence, and **[[confidence-calibration]]** to attach an honest probability to "this is working" rather than a vibe.
5. **Persevere or pivot** — treat this as its own decision and run **[[decision-analysis]]** (or its lighter-weight components — `decision-framing` is already done from step 1, so this mainly means `premortem` on the chosen path and `second-order-scan` on what a pivot would cost) before committing to another loop.
6. **Loop** — return to step 1 with the updated hypothesis. Log each cycle via **[[decision-journaling]]** so the sequence of pivots and their reasoning is auditable in hindsight, not reconstructed from memory.

## What this buys you over a plain build-measure-learn loop

- "Build" is anchored to a specific falsifiable prediction (via `scientific-method`'s framing) instead of "build an MVP and see."
- "Measure" gets an explicit falsification-hunting step and an optional statistical-rigor check, instead of counting whatever numbers happened to be easy to collect.
- "Learn" produces a calibrated probability via `bayesian-updating` + `confidence-calibration`, not just a narrative ("I think it's working").
- Persevere/pivot is treated as the consequential decision it is, with `premortem` run on the chosen path before committing the next cycle's resources.
- The journal (step 6) makes the whole sequence of pivots reconstructable later, which is exactly the input `after-action-review` needs once the venture succeeds, fails, or gets shelved.

## Residual gap

The "Build" step's actual construction work has no cognitive-algorithm equivalent, same as Prototype in [[design-thinking]] — this collection determines *what* to build and *why*, not how to build it.

## Related recipes

- [[design-thinking]] — the general-purpose ancestor of this loop; lean startup is design thinking's empathize/test cycle specialized to a business hypothesis with an explicit persevere/pivot decision gate.
- [[jobs-to-be-done]] — the natural predecessor: JTBD establishes whether a falsifiable hypothesis about a real customer job exists at all; this recipe takes that hypothesis and runs build-measure-learn on it.
- [[rice-prioritization]] — the natural successor: once a feature built under this loop ships, its measured impact is exactly the input RICE's Impact/Confidence terms need for the next round of prioritization.
- [[growth-loop-design]] — the natural downstream recipe once persevere/pivot lands on "persevere": designing the mechanic that gets the validated product to spread.
