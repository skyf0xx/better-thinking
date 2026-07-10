---
name: chestertons-fence
description: >
  Before removing or changing something that seems useless, reconstruct
  why it was put there in the first place. Use when about to remove,
  simplify, or bypass something inherited whose purpose isn't obvious.
type: atomic
category: systems-strategy
difficulty: 1
tokens: ~710
dependencies: []
related: [first-principles, assumption-audit]
---

# Chesterton's Fence

Before removing or changing something that seems useless, reconstruct why it was put there in the first place.

## Why

Things that look pointless from the outside often encode hard-won knowledge about a failure mode you haven't personally experienced yet. Removing them without understanding them is how the failure mode returns.

## Use when / Don't use when

- **Use when:** about to remove, simplify, or bypass something inherited whose purpose isn't obvious; "why do we even do this?" moments.
- **Don't use when:** the origin is already fully known and documented — go straight to the verdict.

## Inputs → Outputs

- **Inputs:** an existing rule, process, structure, or artifact that seems unnecessary.
- **Outputs:** the reconstructed original rationale, a verdict on whether it still applies, and a removal plan if it doesn't.

## Principles

- "I don't see the point of this" is a report about your knowledge, not about the fence's uselessness.
- Find the person or failure that motivated it before deciding.
- Some fences really are obsolete — the goal is an informed removal, not permanent deference.

## Procedure

1. Identify the fence: the specific rule, step, or structure in question.
2. Ask who put this here and what problem they were solving; investigate, don't guess.
3. If the origin can't be reconstructed, treat that as a yellow flag, not a green light — proceed cautiously, perhaps with a reversible trial removal.
4. Determine whether the original condition that motivated the fence still holds.
5. If it doesn't hold, remove it, but note what monitoring would catch the failure mode returning.
6. If it does hold, or is unclear, keep it, and document the rationale for the next person who asks this question.

## Common mistakes

- Removing first and discovering the reason the hard way.
- Treating every inherited rule as sacred regardless of changed conditions.
- Accepting "we've always done it this way" as the reconstructed rationale — that's an absence of one.

## Examples

- A deployment step that looks redundant until you learn it prevents a specific data-corruption class.
- A legal boilerplate clause.
- An org policy from a past incident nobody remembers.

## Related

- [[first-principles]] — the counterweight, a willingness to discard once the rationale is understood.
- [[assumption-audit]] — the complementary forward-looking version of this backward-looking check.
