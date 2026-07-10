---
name: retrospective-facilitation
description: >
  A structured what-went-well, what-didn't, what-changes review that
  produces concrete action items rather than a venting session or a
  forgotten discussion. Use at the end of any bounded effort where
  future work would benefit from explicit learning.
type: composite
category: collaboration
difficulty: 2
tokens: ~790
dependencies: [after-action-review, active-listening, consensus-mapping]
related: [after-action-review, consensus-mapping, active-listening]
---

# Retrospective Facilitation

A structured what-went-well / what-didn't / what-changes review that produces concrete action items rather than a venting session or a forgotten discussion.

## Why

Unstructured retrospectives either avoid hard truths, because everyone's polite, or dwell on them unproductively, venting without resolution. The structure — separating observation from judgment, ending in committed actions — makes the review actually change future behavior.

## Use when / Don't use when

- **Use when:** the end of any bounded effort where future work would benefit from explicit learning; recurring cadence like sprint-end, project-end, incident post-mortem.
- **Don't use when:** the effort was too trivial to yield real learning, or a retro was just run and nothing has changed since.

## Inputs → Outputs

- **Inputs:** a completed effort, sprint, project, or incident.
- **Outputs:** documented learnings and a short list of owned, concrete action items.

## Principles

- Separate what happened (facts) from what it means (judgment) from what to do (action) — collapsing these stages produces blame instead of learning.
- Psychological safety is a precondition, not a nice-to-have.
- Every retro should produce a small number of owned action items, not a long list nobody's accountable for.

## Procedure

1. Set the frame: this is about the work and the system, not about blaming individuals.
2. Gather observations: what happened, factually, with a timeline if useful. Use `active-listening` to draw out quieter participants.
3. Separately, gather interpretation: what went well and why, what didn't and why, running `after-action-review`'s intended-versus-actual framing.
4. Use `consensus-mapping` if there's disagreement about the interpretation.
5. Generate action items: specific, owned, and scoped to what's actually within the team's control.
6. Assign owners and a review date; check at the next retro whether previous action items were actually completed.

## Common mistakes

- Collapsing fact-gathering and judgment into one rushed step, producing blame instead of insight.
- Generating action items with no owner, so they don't happen.
- Never checking whether last retro's action items were completed, teaching the team that retros don't matter.

## Examples

- A sprint retrospective.
- A post-incident review.
- An end-of-project debrief.

## Related

- [[after-action-review]] — the individual, lighter-weight version this group process builds on.
- [[consensus-mapping]] — surfaces disagreement about interpretation.
- [[active-listening]] — draws out quieter participants during observation gathering.
