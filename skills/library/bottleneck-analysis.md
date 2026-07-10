---
name: bottleneck-analysis
description: >
  Locate the single binding constraint in a system and subordinate all
  other improvement effort to it. Use when improvement effort feels
  diffuse or isn't moving the outcome metric.
type: atomic
category: systems-strategy
difficulty: 2
tokens: ~750
dependencies: []
related: [systems-mapping, prioritization-triage]
---

# Bottleneck Analysis

Locate the single binding constraint in a system and subordinate all other improvement effort to it — the Theory of Constraints move.

## Why

Improving anything that isn't the constraint doesn't change system throughput — it just creates local optimization and inventory piling up elsewhere. Finding the actual constraint redirects effort to where it compounds.

## Use when / Don't use when

- **Use when:** improvement effort feels diffuse or isn't moving the outcome metric; "everything is a priority"; a process has an obvious slow point everyone routes around instead of fixing.
- **Don't use when:** the system genuinely has excess capacity everywhere — rare, but then any improvement helps.

## Inputs → Outputs

- **Inputs:** a system with a throughput or output goal.
- **Outputs:** the identified constraint, and a plan that subordinates non-constraint improvements to exploiting it.

## Principles

- A chain's throughput equals its weakest link's throughput — no other link's improvement matters until the weakest link changes.
- Before adding capacity to the constraint, first exploit it — remove waste at that exact point — it's usually cheaper.
- Once a constraint is resolved, the constraint moves elsewhere — this is a continuous process, not a one-time fix.

## Procedure

1. Define the system's throughput goal precisely.
2. Map the stages or components the work flows through.
3. Find where work queues up or where the output rate ceiling actually sits — not where people feel busiest, which is often a red herring.
4. Exploit it: remove waste, idle time, and low-value work at the constraint specifically, before spending on capacity.
5. Subordinate everything else — other stages should pace to the constraint, not run at their own max.
6. If still insufficient, elevate: add capacity at the constraint specifically.
7. Repeat — identify where the constraint moved to next.

## Common mistakes

- Optimizing a non-constraint stage because it's easier or more visible.
- Adding capacity before exploiting, an expensive fix for a cheap problem.
- Declaring victory after one round instead of repeating.

## Examples

- A hiring pipeline bottlenecked at reference checks, not sourcing.
- A factory line's slowest station.
- An engineering org bottlenecked at code review, not coding.

## Related

- [[systems-mapping]] — supplies the structural model this analysis works within.
- [[prioritization-triage]] — treats capacity as a constraint problem at the portfolio level.
