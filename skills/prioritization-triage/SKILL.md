---
name: prioritization-triage
description: >
  Rank competing demands by value, urgency, and cost-of-delay under
  explicit capacity limits, and make the cut line real. Use whenever
  demand exceeds capacity, starting a planning cycle, or feeling busy but
  unproductive.
type: atomic
category: decision-making
difficulty: 2
tokens: ~800
dependencies: []
related: [cost-benefit, satisficing-thresholds, bottleneck-analysis]
---

# Prioritization Triage

Rank competing demands by value, urgency, and cost-of-delay under explicit capacity limits — and make the cut line real.

## Why

Without explicit triage, work gets ordered by recency, loudness, and ease rather than actual value. The scarce resource isn't effort but capacity, and every "yes" is a hidden "no" — triage makes those no's chosen deliberately instead of accidental.

## Use when / Don't use when

- **Use when:** demand exceeds capacity (nearly always); starting a planning cycle; feeling busy but unproductive.
- **Don't use when:** a single deadline dominates everything — just do that.

## Inputs → Outputs

- **Inputs:** a demand list plus a capacity estimate.
- **Outputs:** an ordered list with an explicit cut line, and the things below it named explicitly.

## Principles

- Urgency and importance are independent axes, and urgency is usually the more persuasive liar.
- Cost-of-delay distinguishes "valuable" from "valuable *now*" — some value decays if deferred, some doesn't.
- The list below the cut line is the actual decision — everything above it is comparatively easy.
- Ordering interacts with dependencies and batching — pure scoring ignores sequencing value.

## Procedure

1. List all demands, including easy-to-forget ones — maintenance, recovery time, thinking time.
2. Estimate per item: value, cost-of-delay, and required effort.
3. Kill or delegate items failing an importance floor before ranking, not after.
4. Rank by value-adjusted-for-delay per unit effort, then adjust for dependencies and batching.
5. Draw the cut line at realistic capacity — planned capacity times a historical delivery ratio.
6. Name what falls below the line and notify affected parties — this step is the actual triage.
7. Re-triage on a set cadence or material new information, not reactively on every loud request.

## Common mistakes

- Ranking without ever drawing a cut line, producing a wish list rather than a plan.
- Capacity fantasy — planning against theoretical rather than historically realistic capacity.
- Letting urgency proxy for importance without checking whether that's true.
- Re-triaging reactively so the loudest voice always wins.

## Examples

- Sprint planning with an explicit, communicated cut line.
- An emergency room's actual triage process under real capacity constraints.
- A founder deciding which fires deliberately not to fight during an ongoing incident.

## Related

- [[cost-benefit]] — supplies the value estimates this skill ranks against.
- [[satisficing-thresholds]] — a complementary approach for bounding the search cost of individual choices, not just ranking a full backlog.
- [[bottleneck-analysis]] — treats capacity itself as a constraint problem worth diagnosing directly.
