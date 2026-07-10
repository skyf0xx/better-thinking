---
name: evidence-triangulation
description: >
  Require confirmation from independent sources, and actively test
  whether apparently separate sources share an upstream origin. Use when
  a claim matters and multiple sources exist, when consensus feels too
  smooth, or when citation-chasing a "well-established" fact.
type: atomic
category: research
difficulty: 2
tokens: ~890
dependencies: []
related: [source-credibility, search-strategy, bayesian-updating]
---

# Evidence Triangulation

Require confirmation from *independent* sources, and actively test whether apparently separate sources share an upstream origin.

## Why

"Multiple sources confirm it" is worthless if every one of those sources ultimately traces to the same single press release. Real corroboration requires genuine independence, and that independence has to be actively verified — it's one of the most-faked properties in the entire information ecosystem.

## Use when / Don't use when

- **Use when:** a claim matters and multiple sources exist for it; a consensus feels suspiciously smooth; citation-chasing any "well-established" fact.
- **Don't use when:** one source is already definitively authoritative — the primary document itself, for instance.

## Inputs → Outputs

- **Inputs:** a claim plus its supporting sources.
- **Outputs:** an independence-adjusted confidence — how many *effectively independent* confirmations actually exist.

## Principles

- N sources all citing one shared origin amounts to one source with amplification, not N confirmations.
- Independence means different methods, different incentives, different access — not merely different logos or bylines.
- Convergence of genuinely independent methods is the strongest form of ordinary evidence available.
- Disagreement among independent sources is itself information — locate precisely what they disagree about.

## Procedure

1. List the sources supporting the claim.
2. Trace each one to its origin: what is this source's own source? Follow the citation chain all the way to its root.
3. Cluster the sources by shared origin, and count clusters rather than raw sources.
4. Assess method-diversity across the clusters: is this the same evidence type repeated, or genuinely different routes to the same claim?
5. Weight accordingly: many clusters with diverse methods is strong evidence; a single cluster is a single-source claim, however many times it's been repeated.
6. Where independent clusters disagree, characterize the disagreement precisely — that disagreement is the live, residual research question.

## Common mistakes

- Counting citations as if each one were an independent confirmation.
- Treating multiple media pickups of one wire story as genuine corroboration.
- Assuming institutional sources are automatically independent of each other when they may share the same underlying pipeline.
- Ignoring a lone dissenting cluster simply because it's outnumbered by echoes of the same origin.

## Examples

- A "widely reported" statistic that traces back to a single advocacy white paper.
- Validating an outage theory using logs, metrics, and user reports as genuinely independent evidence streams.
- A historical claim that turns out to rest entirely on a single original chronicle.

## Related

- [[source-credibility]] — grades each individual source before this skill clusters them.
- [[search-strategy]] — the upstream process that gathers the sources this skill evaluates.
- [[bayesian-updating]] — independence determines how much weight each confirmation deserves.
