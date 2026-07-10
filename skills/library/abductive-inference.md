---
name: abductive-inference
description: >
  Generate multiple candidate explanations for a surprising observation and
  rank them by explanatory quality, not by which came to mind first. Use
  whenever something unexpected happened and you're about to say
  "probably because…".
type: atomic
category: reasoning
difficulty: 3
tokens: ~840
dependencies: []
related: [competing-hypotheses, bayesian-updating, causal-analysis]
---

# Abductive Inference

Generate multiple candidate explanations for an observation and rank them by explanatory quality — not by which came to mind first.

## Why

The first explanation generated becomes an anchor; left unexamined, it wins by default regardless of whether it's actually the best account. Forcing a slate of rival explanations and explicit ranking criteria breaks that anchor before it hardens into a conclusion.

## Use when / Don't use when

- **Use when:** something unexpected happened and you're about to say "probably because…" without having considered alternatives.
- **Don't use when:** the space of causes is formally enumerable and testable — use a structured differential instead of open-ended generation.

## Inputs → Outputs

- **Inputs:** a surprising observation or pattern.
- **Outputs:** a ranked slate of at least three explanations, each with the discriminating evidence it would predict.

## Principles

- The best explanation is judged jointly on scope, simplicity, and prior plausibility — not on fit alone. Anything fits if it's vague enough.
- An explanation earns its rank by predicting something the others don't; that's what makes it testable, not just plausible-sounding.

## Procedure

1. State the observation precisely, separating it clearly from any interpretation already layered onto it.
2. Generate at least three candidate explanations, deliberately including a boring one — chance, measurement error, a selection effect.
3. For each candidate, ask: what else would be true if this were the explanation?
4. Score the candidates on fit, prior plausibility, and simplicity, jointly rather than on any one dimension alone.
5. Identify the cheapest observation that would discriminate between the top two candidates.
6. Report the ranking, the discriminating test, and how easily the runner-up could overtake the leader — that instability is the residual uncertainty.

## Common mistakes

- Stopping at one hypothesis and treating it as settled.
- Omitting the boring, unglamorous explanations, which are disproportionately likely to be correct.
- Scoring on fit alone — conspiracy theories fit everything, which is exactly why fit alone is a weak criterion.
- Never actually running the discriminating test once identified.

## Examples

- Why did signups drop 20% this week — a slate including a tracking bug, a real behavioral shift, and a seasonal effect.
- Why does a patient present with three symptoms together — generating rival diagnoses before committing to one.
- Why did a rival company suddenly cut prices — competitive pressure, inventory clearance, or a cost-structure change.

## Related

- [[competing-hypotheses]] — the full composite pipeline this feeds when the stakes justify a formal matrix.
- [[bayesian-updating]] — formalizes the scoring step once evidence starts arriving.
- [[causal-analysis]] — the deeper mechanism-level follow-up once a leading explanation survives.
