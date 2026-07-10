---
name: competing-hypotheses
description: >
  Analysis of Competing Hypotheses - rank rival explanations by how much
  the evidence disconfirms each, rather than how much confirms any
  single favorite. Use for high-stakes explanatory questions with
  ambiguous or contested evidence.
type: composite
category: analysis
difficulty: 4
tokens: ~880
dependencies: [abductive-inference, evidence-hierarchy, disconfirmation-search, bayesian-updating]
related: [differential-diagnosis, abductive-inference, bayesian-updating]
---

# Competing Hypotheses

Analysis of Competing Hypotheses: rank rival explanations by how much the evidence *disconfirms* each, rather than how much confirms any single favorite.

## Why

Confirmation-seeking analysis lets any hypothesis with enough support "win," even when the evidence fits every rival equally well. Scoring by inconsistency exposes which evidence actually discriminates, and which hypothesis survives that scrutiny.

## Use when / Don't use when

- **Use when:** high-stakes explanatory questions with ambiguous or contested evidence — intelligence-style assessment, complex diagnosis, contested historical or organizational questions.
- **Don't use when:** one hypothesis is already overwhelmingly favored by direct evidence — this machinery is for genuine ambiguity.

## Inputs → Outputs

- **Inputs:** a question with multiple plausible explanations and a body of evidence.
- **Outputs:** an evidence-by-hypothesis matrix scored by inconsistency, the surviving hypothesis or a genuine tie, and the diagnostic evidence that would break the tie.

## Principles

- Evidence consistent with every hypothesis is worthless for discrimination, however voluminous.
- The strongest hypothesis is the one with the *fewest* strong inconsistencies, not the most confirmations.
- Disproof is more diagnostic than proof.
- Write the matrix down — it externalizes the comparison the unaided mind can't hold.

## Procedure

1. Run `abductive-inference` to generate the full hypothesis set, including ones you find unlikely or unwelcome.
2. List all relevant evidence, gathered independent of any hypothesis.
3. Build the matrix: for each evidence-by-hypothesis cell, mark consistent, inconsistent, strongly inconsistent, or not applicable. Grade each evidence item's reliability with `evidence-hierarchy`.
4. Score each hypothesis by total inconsistency, weighted by evidence reliability, not by count of confirmations.
5. The hypothesis with the least, weakest inconsistency leads. If several are close, that closeness is itself the finding.
6. Run `disconfirmation-search`: what evidence, if found, would most separate the leaders? Prioritize gathering it.
7. Report the ranking, confidence via `bayesian-updating` on the margin, and the diagnostic evidence still missing.

## Common mistakes

- Generating hypotheses then unconsciously gathering only confirming evidence.
- Scoring by confirmation count, which defeats the method's purpose.
- Treating a narrow win as certainty.
- Skipping the matrix and doing it "in your head" — it doesn't work in your head, which is the whole reason for the technique.

## Examples

- Intelligence assessment of an ambiguous geopolitical event.
- Diagnosing why a metric moved when three plausible causes coincide.
- Determining why a hire didn't work out.

## Related

- [[differential-diagnosis]] — the same logic applied to a live, ongoing case.
- [[abductive-inference]] — supplies the hypothesis set.
- [[bayesian-updating]] — formalizes the scoring.
