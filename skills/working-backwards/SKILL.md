---
name: working-backwards
description: >
  Start from a concrete goal state and chain prerequisites backwards until
  reaching actions available right now. Use when planning toward a fixed
  outcome or deadline, when the goal is clear but the path isn't, or when
  writing the "press release" before the product.
type: atomic
category: problem-solving
difficulty: 2
tokens: ~820
dependencies: []
related: [backcasting, means-ends-analysis, premortem]
---

# Working Backwards

Start from a concrete goal state and chain prerequisites backwards until reaching actions available now.

## Why

Forward planning from the present explores a huge branching space and drifts toward whatever's comfortable. Backward chaining from a fixed goal prunes to the paths that actually terminate at success, and exposes prerequisite gaps far earlier than forward planning would.

## Use when / Don't use when

- **Use when:** planning toward a fixed outcome or deadline; the goal is clear but the path to it isn't; writing the "press release" before building the product it describes.
- **Don't use when:** the goal itself is uncertain — resolve the framing first, or use the longer-horizon strategic version of this move instead.

## Inputs → Outputs

- **Inputs:** a well-specified goal state.
- **Outputs:** a prerequisite chain from goal back to present, with the critical path and earliest-needed actions marked.

## Principles

- The goal must be specified concretely enough that arrival can actually be tested.
- Every step answers "what must be true immediately before this is achievable?"
- Prerequisites with long lead times dominate the schedule regardless of how small they otherwise seem.

## Procedure

1. Specify the goal state with acceptance criteria — how would you verify you've actually arrived?
2. Ask: what must be true immediately before the goal is achievable? List those preconditions.
3. Recurse on each precondition until reaching states that are already true now, or actions executable now.
4. Mark dependencies and lead times; extract the critical path through the chain.
5. Identify the earliest-needed irreversible commitments and long-lead items specifically.
6. Sanity-check forward: walk the chain front-to-back looking for hidden gaps the backward pass might have skipped, and report any that remain as residual uncertainty.

## Common mistakes

- Vague goal states ("be successful") that can't actually anchor a backward chain.
- Skipping the forward sanity-check pass — backward chains can silently omit enabling conditions that seemed too obvious to state.
- Treating the resulting chain as the only viable path rather than one plan among possible alternatives.

## Examples

- Planning a product launch by working backwards from the launch date.
- Deriving tonight's experiment from what the thesis defense will need to show.
- Structuring a legal case by working backwards from the verdict actually needed.

## Related

- [[backcasting]] — the same core move applied at a longer, strategic horizon with a deliberately chosen future.
- [[means-ends-analysis]] — subgoaling within this skill's recursion is itself a form of backward chaining.
- [[premortem]] — a natural next step to stress-test the resulting plan before committing to it.
