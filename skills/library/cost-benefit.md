---
name: cost-benefit
description: >
  Tally the full costs and benefits of an action, including opportunity
  cost, hidden costs, and who they accrue to, before judging it
  worthwhile. Use when justifying or challenging any investment of money,
  time, or attention.
type: atomic
category: decision-making
difficulty: 2
tokens: ~830
dependencies: []
related: [expected-value, second-order-scan, prioritization-triage]
---

# Cost-Benefit

Tally the full costs and benefits of an action — including opportunity cost, hidden costs, and to-whom-they-accrue — before judging it worthwhile.

## Why

Untrained tallies count visible, near-term, own-side effects and systematically miss opportunity cost, ongoing maintenance burden, and externalities — which flatters taking action over not taking it, every time.

## Use when / Don't use when

- **Use when:** justifying or challenging any investment of money, time, or attention.
- **Don't use when:** stakes are genuinely trivial, or the decision is so dominated by a single factor that a full ledger adds nothing.

## Inputs → Outputs

- **Inputs:** a proposed action.
- **Outputs:** a ledger of costs and benefits with timing, bearer, and confidence per entry, plus a net judgment flagging the dominant uncertainties.

## Principles

- The opportunity cost — the best foregone alternative — is a real cost, and it's almost always missing from the first draft of any ledger.
- Count ongoing costs (maintenance, attention, added complexity), not just the upfront acquisition cost.
- Note who bears each cost specifically — a net-positive action can still be a transfer of cost onto someone who was never consulted.
- Sunk costs are not costs, and shouldn't appear in the ledger at all.

## Procedure

1. State the action and the actual comparison baseline — usually the best alternative use of the same resources, not simply "do nothing."
2. List benefits with their timing and confidence.
3. List costs: direct, ongoing, attention/complexity, and risk-bearing.
4. Add the opportunity cost explicitly as its own line item.
5. Mark who bears each entry, and flag any asymmetries — benefits accruing to one party, costs to another.
6. Net it out, and state which one or two uncertain entries actually dominate the conclusion — that's the residual uncertainty worth resolving further.

## Common mistakes

- Using "do nothing" as the baseline when a live, better alternative actually exists.
- Ignoring the long tail of maintenance costs that follow an initial investment.
- Counting sunk costs as if they belonged in the ledger.
- Treating hard-to-quantify entries as if they were zero, rather than estimating them explicitly.

## Examples

- Whether to build an internal tool versus buying or doing without.
- Whether a recurring meeting series earns back its collective hours across attendees.
- Whether a regulation's compliance burden is proportionate to the protection it provides; whether to adopt a new dependency.

## Related

- [[expected-value]] — the probabilistic version, used when entries are genuinely uncertain rather than point estimates.
- [[second-order-scan]] — often surfaces the hidden entries this ledger would otherwise miss.
- [[prioritization-triage]] — the natural next step once several cost-benefit ledgers need to be compared against each other.
