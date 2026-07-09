---
name: claim-verification
description: >
  Journalism-grade fact-checking of a specific claim: decompose it, trace
  to origin, triangulate independently, and grade the verdict. Use when a
  claim is load-bearing for a decision or about to be repeated onward.
type: composite
category: research
difficulty: 3
tokens: ~850
dependencies: [question-decomposition, search-strategy, source-credibility, evidence-triangulation, statistical-audit, epistemic-tagging]
related: [critical-reading]
---

# Claim Verification

Journalism-grade fact-checking of a specific claim: decompose it, trace to origin, triangulate independently, and grade the verdict.

## Why

Claims travel farther than their evidence. A repeatable verification pipeline replaces "sounds right" with a graded verdict, and does it fast enough to run routinely rather than only on the rare claim that triggers suspicion.

## Use when / Don't use when

- **Use when:** a claim is load-bearing for a decision or about to be repeated onward; a statistic is doing heavy rhetorical work.
- **Don't use when:** nothing actually depends on the claim's truth.

## Inputs → Outputs

- **Inputs:** a specific factual claim.
- **Outputs:** a verdict — verified, partly verified, unsupported, false, or unverifiable — with the evidence trail behind it.

## Principles

- Verify the claim *as stated* — verifying a nearby, adjacent claim is how misinformation launders itself into credibility.
- The origin is the actual unit of verification, not the repetitions of it.
- Absence of confirmation is not refutation — "unverifiable" is an honest, legitimate verdict.
- Time-box the effort; verification depth should scale with the claim's load, not run to exhaustion on trivia.

## Procedure

1. Fix the claim verbatim; run `question-decomposition` if it bundles several assertions — verify each separately, since the bundle's truth is their conjunction.
2. Trace to origin: follow the citation chain to the primary source. Note precisely where the chain breaks or mutates — mutation is itself a finding.
3. Audit the origin with `source-credibility`; if the claim is quantitative, run `statistical-audit` on the original number, not the retelling.
4. Run `evidence-triangulation`: count independent confirmations by origin-cluster, not by raw repetition count.
5. Search for the rebuttal using `search-strategy`'s disconfirming queries: has this been debunked, corrected, or retracted?
6. Grade: verified, verified-with-distortion (true origin, mutated in transit), unsupported, false, or unverifiable. Tag residual uncertainty with `epistemic-tagging`.

## Common mistakes

- Verifying the paraphrase instead of the claim as actually stated.
- Stopping at a "reputable" repeater instead of tracing to the actual origin.
- Treating the origin's mere existence as proof of its correctness.
- Over-verifying trivia while a genuinely load-bearing claim skates through unchecked.

## Examples

- A statistic in a strategy memo before it goes to a board presentation.
- A historical "quote" attributed to a well-known figure.
- A rival's benchmark claim; a viral study result circulating without scrutiny.

## Related

- [[critical-reading]] — the upstream extraction step that identifies which claims are actually worth verifying.
