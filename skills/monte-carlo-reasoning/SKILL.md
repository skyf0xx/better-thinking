---
name: monte-carlo-reasoning
description: >
  Mentally sample many possible runs of an uncertain process instead of
  reasoning about one representative story. Use when an outcome depends
  on several compounding uncertain factors, or when tail risk matters.
type: atomic
category: forecasting
difficulty: 3
tokens: ~840
dependencies: []
related: [uncertainty-decomposition, expected-value, sensitivity-analysis]
---

# Monte Carlo Reasoning

Mentally (or computationally) sample many possible runs of an uncertain process, instead of reasoning about one representative story.

## Why

When outcomes depend on the combination of several independent uncertain factors, intuition tends to reason about one plausible scenario at a time and misses how the combination of many small uncertainties produces a wide — and often skewed — outcome distribution.

## Use when / Don't use when

- **Use when:** an outcome depends on several compounding uncertain factors; a single "expected case" story is being used to plan for a process that's actually quite variable; tail risk matters.
- **Don't use when:** one factor dominates — sensitivity analysis on that factor is simpler and sufficient.

## Inputs → Outputs

- **Inputs:** a process with multiple uncertain, roughly independent inputs.
- **Outputs:** an outcome distribution, even a rough sketch of one, rather than a single-scenario story, with the tail behavior noted.

## Principles

- Don't reason about "the" scenario — reason about the *distribution* of scenarios.
- When uncertain factors combine multiplicatively or with dependencies, the tails are often fatter than intuition expects.
- A distribution's mean and its most likely single outcome (mode) can differ substantially when skewed — planning for "the expected case" can mean planning for something individually unlikely.

## Procedure

1. Identify the independent, or roughly independent, uncertain inputs to the process.
2. Estimate a plausible range or distribution shape for each, even qualitatively.
3. Mentally sample several combinations — not just "everything average" and "everything bad," but genuinely varied combinations where some inputs are good and others bad simultaneously.
4. Sketch the resulting outcome distribution: where does it cluster, how fat are the tails, is it skewed?
5. Identify what specifically drives the worst outcomes — usually a particular combination, not any single input alone.
6. Plan against the distribution — buffer, optionality, contingency — rather than the single expected-case story.

## Common mistakes

- Planning for "the average scenario" when the distribution is skewed and the average is rarely the actual outcome.
- Assuming independence when inputs are actually correlated, which is exactly how tail risk happens.
- Doing this so informally that it collapses back into "just imagine one bad case."

## Examples

- Project timeline risk when multiple independent tasks can each slip.
- Portfolio risk from multiple correlated positions.
- Capacity planning under variable demand and variable failure rates simultaneously.

## Related

- [[uncertainty-decomposition]] — supplies the individual input ranges this skill combines.
- [[expected-value]] — the single-number summary this skill's distribution feeds into.
- [[sensitivity-analysis]] — the simpler, single-factor version of this same instinct.
