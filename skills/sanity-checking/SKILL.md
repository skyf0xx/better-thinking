---
name: sanity-checking
description: >
  Rapidly verify any result via units, magnitude, boundary conditions, and
  an independent approximation before trusting or presenting it. Use after
  any computation, estimate, or conclusion, and always before presenting
  anything — this is the cheapest, highest-frequency error catch available.
type: atomic
category: reasoning
difficulty: 1
tokens: ~840
dependencies: []
related: [fermi-estimation, epistemic-tagging]
---

# Sanity Checking

Rapidly verify a result via units, magnitudes, boundary conditions, and independent approximations before trusting or shipping it.

## Why

Most gross errors are catchable in seconds by tests that don't require redoing the work. The habit of running them is worth more than most sophisticated methods, precisely because it's cheap enough to run on *everything* — every number, every conclusion, every plan — and most errors it catches would otherwise have shipped.

## Use when / Don't use when

- **Use when:** always — after any computation, estimate, or conclusion, and before presenting anything to anyone else.
- **Don't use when:** never skip it; scale the depth of the check to the stakes instead of omitting it.

## Inputs → Outputs

- **Inputs:** any result — a number, a conclusion, a plan, a piece of writing.
- **Outputs:** a pass, or a specific detected anomaly with enough detail to locate and fix it.

## Principles

- Check with methods *independent* of how the result was produced — re-deriving the same way you got it the first time won't catch the same error.
- Extremes are where errors are loudest — zero, one, the maximum, and the empty case surface bugs that the typical case hides.
- An unexplained anomaly means stop and investigate, not shrug and continue.

## Procedure

1. Units/type check: is the result even the right kind of thing?
2. Magnitude check: is it within roughly 10× of what a crude independent estimate gives?
3. Boundary check: does the logic hold at zero, one, the maximum, and the empty case?
4. Consistency check: does it contradict anything else already established?
5. Smell check: is it suspiciously round, suspiciously precise, or suspiciously convenient given what you wanted to find?
6. If any check fails: locate the discrepancy before proceeding — never annotate-and-continue. If all checks pass, state that explicitly rather than silently assuming it; note any check that couldn't be run as the residual uncertainty.

## Common mistakes

- Re-checking with the same method that produced the error in the first place, which reproduces the same mistake.
- Explaining anomalies away with a plausible-sounding story instead of chasing down the actual cause.
- Skipping checks specifically when confident — confidence is exactly when a check is most needed, because it's when scrutiny naturally relaxes.

## Examples

- A revenue projection that implies capturing 140% of the addressable market.
- A model output in the wrong unit (seconds vs. milliseconds, dollars vs. thousands of dollars).
- A plan whose timeline implicitly assumes zero rework, or a percentage reported over 100.

## Related

- [[fermi-estimation]] — often supplies the independent estimate used in the magnitude check.
- [[epistemic-tagging]] — a complementary check on the conclusion's actual evidential basis, not just its arithmetic.
