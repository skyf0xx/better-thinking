---
name: decision-analysis
description: >
  The full pipeline for consequential choices: frame, generate options,
  model uncertainty, score, stress-test, decide, and record. Use when
  reversibility-classification grades a decision costly-reversible or
  worse and options are genuinely open.
type: composite
category: decision-making
difficulty: 4
tokens: ~1050
dependencies: [decision-framing, reversibility-classification, solution-space-mapping, weighted-scoring, expected-value, premortem, second-order-scan, tripwires, decision-journaling, confidence-calibration]
related: [structured-problem-solving, scenario-planning, negotiation]
---

# Decision Analysis

The full pipeline for consequential choices: frame, generate options, model uncertainty, score, stress-test, decide, and record.

## Why

High-stakes decisions fail at whichever stage was skipped — usually option generation or stress-testing. The pipeline guarantees every stage runs at a depth proportional to stakes, so a decision that matters gets the full sequence rather than whichever piece felt most comfortable to the decider.

## Use when / Don't use when

- **Use when:** [[reversibility-classification]] grades the decision costly-reversible or worse, and the options are genuinely open rather than pre-determined.
- **Don't use when:** the door is two-way — decide fast and review later — or one option already dominates on every criterion.

## Inputs → Outputs

- **Inputs:** a consequential, non-obvious choice.
- **Outputs:** a decision with documented rationale, the losing options and why they lost, sensitivity flags, tripwires, and a journal entry for later scoring.

## Principles

- Process weight scales with irreversibility — this pipeline is not owed to every decision, only the ones that earn it.
- Option generation is where decisions are actually won; evaluation just confirms what generation already made possible.
- Uncertainty gets modeled explicitly, not smoothed into adjectives like "likely."
- The decision isn't done until its revisit conditions are installed — a decision with no way to be reopened silently becomes dogma.

## Procedure

1. Run `reversibility-classification`; confirm this pipeline is warranted and set the process budget accordingly.
2. Run `decision-framing`: the question, decider, criteria, deadline, and default path if no decision is made.
3. Run `solution-space-mapping`; ensure at least three genuinely distinct options exist, plus the default.
4. Model uncertainty: for each option, identify the key uncertain outcomes with probabilities, using `expected-value` where payoffs are commensurable.
5. Evaluate via `weighted-scoring` across criteria; run its sensitivity step hard — which single judgment flips the result?
6. Stress-test the leading option: run `premortem` and `second-order-scan`. Amend the option or switch to the runner-up if the wounds found are fatal.
7. Decide. Write the rationale, name the runner-up, and state *why the runner-up lost* — that's what gets revisited if conditions change.
8. Install `tripwires`: the specific observations that would reopen the decision.
9. Log via `decision-journaling` with calibrated confidence from `confidence-calibration`, for later scoring against the outcome.

## Common mistakes

- Running the full pipeline on two-way doors, turning process into procrastination.
- Skipping step 6 because the leading option "feels solid" — that feeling is precisely the reason to run it.
- Writing the rationale after the fact so it sounds inevitable, rather than during the actual reasoning.
- Installing no tripwires, so the decision silently becomes unquestionable dogma.

## Examples

- A build-versus-buy decision on a core system.
- A market-entry decision under genuine uncertainty.
- Choosing a therapy path from mixed clinical evidence.
- A family's decision to relocate.

## Related

- [[structured-problem-solving]] — the sibling composite for when the task isn't a choice among options.
- [[scenario-planning]] — used instead when the uncertainty is about the world, not the options themselves.
- [[negotiation]] — used instead when the options are held by a counterparty, not chosen unilaterally.
