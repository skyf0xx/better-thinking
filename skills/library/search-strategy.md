---
name: search-strategy
description: >
  Plan queries, sources, and stop-conditions before searching, then adapt
  on evidence of coverage rather than fatigue. Use for any search beyond a
  single lookup, especially when the first page of results agrees
  suspiciously well.
type: atomic
category: research
difficulty: 2
tokens: ~850
dependencies: []
related: [evidence-triangulation, source-credibility, disconfirmation-search]
---

# Search Strategy

Plan queries, sources, and stop-conditions before searching, then adapt on evidence of coverage rather than fatigue.

## Why

Unplanned search finds whatever ranks first and stops as soon as the searcher gets tired — a recipe for availability bias dressed up as diligence. A strategy with real stop-conditions makes coverage a deliberate decision rather than an accident of when someone got bored.

## Use when / Don't use when

- **Use when:** any search beyond a single lookup; especially when the first page of results agrees suspiciously well with itself.
- **Don't use when:** a single canonical source is already known and sufficient.

## Inputs → Outputs

- **Inputs:** an answerable question, ideally already decomposed.
- **Outputs:** a source and query plan, a stop rule, and a coverage self-assessment produced after execution.

## Principles

- Vary the *kind* of source — primary versus secondary, pro versus con, practitioner versus academic — not just the wording of the query.
- Search explicitly for disconfirming material ("X doesn't work," "X criticism," "X failed") — the confirming version tends to find itself without any extra effort.
- Saturation, where new sources just repeat old ones, is the honest signal to stop.
- Track provenance carefully, so a later independence check can detect sources that share a hidden upstream origin.

## Procedure

1. State what a satisfying answer would actually look like, and what would count as enough evidence.
2. List the source types most likely to hold that answer, noting each type's characteristic bias.
3. Draft queries, deliberately including disconfirming formulations alongside the obvious ones.
4. Execute breadth-first, logging each source, its claim, and — critically — that source's own source.
5. Check saturation and coverage: is any viewpoint or source-type still unsampled?
6. Stop on the pre-set rule, and report what was searched, what wasn't, and your confidence in the coverage achieved — that confidence gap is the residual uncertainty.

## Common mistakes

- Query monoculture — rephrasing the same underlying assumption five different ways without actually varying the search.
- Stopping at apparent agreement without noticing that every source traces back to one shared origin.
- Searching until confirmation of the expected answer arrives, then declaring the search complete.

## Examples

- Due diligence on a vendor's reliability claims before signing a contract.
- Scoping prior art before committing engineering effort to a new approach.
- Checking whether a "well-known fact" actually survives tracing its own citations.

## Related

- [[evidence-triangulation]] — the next step, testing whether the gathered sources are actually independent of each other.
- [[source-credibility]] — grades each individual source once found.
- [[disconfirmation-search]] — the general discipline this skill's step 3 specializes for search specifically.
