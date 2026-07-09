---
name: negotiation
description: >
  The full pipeline - prepare BATNAs, probe for underlying interests,
  generate joint options, and converge on an agreement that survives
  both sides' scrutiny. Use for any negotiation with meaningful stakes.
type: composite
category: collaboration
difficulty: 4
tokens: ~890
dependencies: [batna-analysis, empathy-mapping, interest-based-bargaining, active-listening, game-theoretic-analysis]
related: [batna-analysis, interest-based-bargaining, conflict-mediation, game-theoretic-analysis]
---

# Negotiation

The full pipeline: prepare BATNAs, probe for underlying interests, generate joint options, and converge on an agreement that survives both sides' scrutiny.

## Why

Negotiations conducted without preparation default to positional bargaining and leave value on the table, or collapse into a bad deal driven by fear of walking away. The full pipeline systematically captures the value interest-based approaches can find while keeping leverage realities in view.

## Use when / Don't use when

- **Use when:** any negotiation with meaningful stakes — commercial, employment, interpersonal, diplomatic.
- **Don't use when:** the terms are truly fixed and non-negotiable — negotiation effort there is wasted.

## Inputs → Outputs

- **Inputs:** an upcoming negotiation with a counterparty.
- **Outputs:** an agreement, or a deliberate no-deal, that reflects both sides' actual interests and each side's real leverage.

## Principles

- Preparation determines most of the outcome, before either side says a word.
- Interests unlock value positions can't reach, but BATNA still sets the floor beneath which no interest-based creativity should push you.
- Understanding is not concession — fully grasping their position costs nothing and reveals options.
- Walking away is a legitimate, sometimes correct, outcome.

## Procedure

1. **Prepare:** run `batna-analysis` — your alternative, your reservation point, their estimated BATNA, the resulting ZOPA if any.
2. Run `empathy-mapping` on the counterparty: their likely interests, constraints, and pressures beyond what they'll state.
3. **Open:** state your position, then genuinely elicit theirs; use `active-listening` to verify you understand their actual position before responding.
4. **Probe interests:** run `interest-based-bargaining` — ask why behind stated positions on both sides.
5. **Invent options:** generate multiple ways to satisfy both sides' interests before committing to any.
6. For complex or repeated negotiations, run `game-theoretic-analysis` on how each proposed structure incentivizes future behavior, not just this deal.
7. **Converge:** select the option best satisfying both sides' interests within each side's reservation point; use objective criteria to justify terms where possible.
8. If no option clears both reservation points, recognize and accept no-deal rather than forcing a bad agreement.

## Common mistakes

- Skipping BATNA preparation and negotiating from fear or hope instead of a known floor.
- Treating interest-based bargaining as a soft alternative to leverage rather than a complement to it.
- Anchoring immediately on positions and never reaching the interest layer.

## Examples

- A job offer negotiation.
- A vendor contract.
- A business partnership dissolution; an international trade negotiation.

## Related

- [[batna-analysis]] — the preparation step this pipeline runs first.
- [[interest-based-bargaining]] — the probing technique at this pipeline's core.
- [[conflict-mediation]] — the third-party facilitated version.
