---
name: mece-decomposition
description: >
  Split a problem or space into parts that are mutually exclusive and
  collectively exhaustive, so nothing is double-counted or dropped. Use
  when sizing or diagnosing anything, dividing work, or structuring a
  document or investigation.
type: atomic
category: problem-solving
difficulty: 2
tokens: ~810
dependencies: []
related: [question-decomposition, fermi-estimation, bottleneck-analysis]
---

# MECE Decomposition

Split a problem or space into parts that are Mutually Exclusive and Collectively Exhaustive, so nothing is double-counted or dropped.

## Why

Overlapping parts cause double-counting and turf confusion; gaps cause the real cause, option, or risk to stay invisible. A MECE structure turns a vague "analyze this" into a checklist of smaller, independently answerable analyses.

## Use when / Don't use when

- **Use when:** sizing or diagnosing anything ("where is the revenue leak?"); dividing work among people; structuring a document or investigation.
- **Don't use when:** the space is genuinely non-decomposable, or a holistic judgment call is actually the point.

## Inputs → Outputs

- **Inputs:** a problem, question, or space to be analyzed.
- **Outputs:** a tree of parts, with the cutting principle named explicitly at each level.

## Principles

- Each split uses exactly one cutting principle at a time — by stage, by segment, by component — never mixed within a single level.
- Exhaustive means adding an explicit "other / none of the above" bucket whenever coverage is uncertain.
- The right cut is the one that isolates where the variance actually concentrates, not just any valid partition.

## Procedure

1. State the whole precisely — what's actually in scope.
2. Choose a cutting principle and state it explicitly.
3. Enumerate the parts; verify no overlap (each item lands in exactly one part) and no gap (everything has somewhere to land — add "other" if unsure).
4. Recurse into the parts that matter most; stop once a part is directly answerable on its own.
5. Audit the result: does variance concentrate in one branch? If all parts matter roughly equally, the cut probably isn't pulling its weight — try a different cutting principle.

## Common mistakes

- Mixing cutting principles within one level ("by region, plus the enterprise segment").
- Fake exhaustiveness — no "other" bucket, so items with nowhere to go get silently dropped.
- Decomposing along whatever data happens to be available instead of along the problem's actual causal structure.
- "MECE theater" — a beautiful, correctly-partitioned tree that doesn't actually isolate anything useful.

## Examples

- Profit dropped: decompose by price × volume × mix, then by segment.
- A page is slow: decompose by request phase (network, server, render, etc.).
- Enumerating risk categories for a launch, exhaustively and without overlap.

## Related

- [[question-decomposition]] — the same discipline applied specifically to research questions with evidence-type tagging on the leaves.
- [[fermi-estimation]] — uses this kind of decomposition to make an unknown quantity estimable.
- [[bottleneck-analysis]] — often the next step once decomposition reveals which branch actually binds.
