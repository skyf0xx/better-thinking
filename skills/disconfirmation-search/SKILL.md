---
name: disconfirmation-search
description: >
  Ask "what would change my mind?" and then actually search for it, rather
  than only seeking evidence that confirms a current belief. Use when a
  conclusion feels settled or obvious, before committing to a belief-driven
  action, or as a final check on any reasoning process.
type: atomic
category: metacognition
difficulty: 2
tokens: ~500
dependencies: []
related: [bias-audit, bayesian-updating, scientific-method]
---

# Disconfirmation Search

Ask "what would change my mind?" and then actually go look for it, rather than only seeking evidence that confirms the current belief.

## Why

The mind is fluent at generating supporting evidence for whatever it already believes, and sluggish at generating counter-evidence unprompted. Explicitly asking what would disconfirm the belief — and then actually searching for exactly that — is the single most reliable counter to confirmation bias available, and it's cheap enough to run on nearly every consequential conclusion.

## Use when / Don't use when

- **Use when:** a conclusion feels settled or obvious; before committing to a belief-driven action; as the final step of most reasoning processes, especially forecasting and diagnosis.
- **Don't use when:** the belief is genuinely inconsequential and nothing hinges on whether it's right.

## Inputs → Outputs

- **Inputs:** a belief or conclusion held with some confidence.
- **Outputs:** the specific evidence that would change the belief, and the result of an actual search for it (found / not found / inconclusive).

## Principles

- The question "what would change my mind?" must produce a *specific, checkable* answer — "if I saw evidence against it" is not specific enough to actually search for.
- If nothing comes to mind that would change the belief, the belief isn't actually evidence-based — it's a commitment, and that's worth knowing explicitly.
- Actually go look. Asking the question rhetorically without searching captures none of the benefit.

## Procedure

1. State the belief precisely.
2. Ask: what specific observation, if it existed, would make me doubt or abandon this belief?
3. If nothing comes to mind, that itself is the finding — flag the belief as currently unfalsifiable and examine why (is it actually well-supported, or just comfortable?).
4. If a specific disconfirming observation is named, actively search for it — don't just note it hypothetically and move on.
5. If found: update the belief accordingly, proportional to what was found.
6. If genuinely not found after a real search: report increased — not absolute — confidence, since the search itself is evidence, and state how thorough the search actually was as the residual uncertainty.

## Common mistakes

- Asking the question rhetorically without actually searching for the answer.
- Naming a disconfirming condition so extreme or unlikely that the search is meaningless theater.
- Treating "I looked and didn't find it" as proof rather than as evidence that should update confidence only proportionally to how hard and how well you actually looked.

## Examples

- Checking whether a hiring "gut read" survives actually looking at the candidate's track record and references.
- Testing a technical root-cause theory against the one specific log line that would disprove it, rather than the ones that fit.
- A forecaster explicitly naming what news would make them abandon their current prediction, then checking whether it has appeared.

## Related

- [[bias-audit]] — the broader check this technique serves as the primary counter to confirmation bias within.
- [[bayesian-updating]] — the formal mechanism for how a found disconfirmation should move the belief.
- [[scientific-method]] — the composite pipeline where this search is a standard closing step.
