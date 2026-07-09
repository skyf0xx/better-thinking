# Recipe: Design Thinking

**What it is:** the five-stage IDEO/Stanford d.school process — Empathize, Define, Ideate, Prototype, Test — for developing solutions grounded in real user needs rather than assumed ones.

## Skill sequence

1. **Empathize** — run **[[interview-synthesis]]** to gather real user input via non-leading questions, then **[[empathy-mapping]]** to reconstruct what users perceive, think, feel, and need, distinguished from what the team assumes. Prefer real interview data over a constructed empathy map wherever both are available — `empathy-mapping`'s own anti-trigger says as much.
2. **Define** — run **[[problem-framing]]** using the empathy output as raw material, generating multiple candidate framings of the user's actual problem before picking one. This is the stage most design-thinking exercises rush; `problem-framing`'s explicit "three or more alternative framings" requirement is the fix.
3. **Ideate** — run **[[ideation-sprint]]** (diverge → cross-pollinate → converge with phase gates) on the chosen framing. This replaces the vaguer "brainstorm a lot of ideas" instruction in most design-thinking writeups with an actual phase-gated procedure.
4. **Prototype** — outside this collection's scope. Cognitive Algorithms covers thinking procedures, not building artifacts; the prototyping stage is where the design proceeds to build tools, not reasoning tools.
5. **Test** — run a lightweight pass of **[[scientific-method]]** (hypothesize what the prototype should demonstrate → predict → test with users → attempt falsification → update), then feed findings back into step 1 for the next iteration.

## What this buys you over a plain design-thinking writeup

- "Empathize" stops meaning "imagine what users want" and starts meaning a traceable interview + empathy-map procedure with explicit unstated-need extraction.
- "Define" gets `problem-framing`'s discipline of generating rival framings instead of accepting the first plausible problem statement.
- "Ideate" gets explicit phase gates (diverge/cross-pollinate/converge) instead of an unstructured brainstorm that blurs generation and judgment.
- "Test" is evidence-gated via `scientific-method` rather than "show it to some users and see what they think."
- The loop is explicit: Test's output re-enters Empathize, so the process is iterative by construction, not by reminder.

## Residual gap

Prototype has no cognitive-algorithm equivalent by design — it's a doing stage, not a thinking stage. Teams applying this recipe still need their own tools (paper prototypes, code, physical mockups) for that step; this collection only covers the reasoning that brackets it.

## Related recipes

- [[lean-startup]] — the same empathize→test loop compressed and applied specifically to a business-model bet rather than a general user problem.
