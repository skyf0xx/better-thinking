---
name: five-whys
description: >
  Iterate "why did that happen?" past the symptom until reaching a cause
  at the level of process or design — something fixable that prevents
  recurrence. Use for any recurring problem, postmortems, or when a fix
  was applied and the problem came back.
type: atomic
category: problem-solving
difficulty: 1
tokens: ~790
dependencies: []
related: [root-cause-investigation, causal-analysis, problem-framing]
---

# Five Whys

Iterate "why did that happen?" past the symptom until reaching a cause at the level of process or design — something fixable that prevents recurrence.

## Why

First answers are almost always symptoms; fixes applied at the symptom level recur, because the generating cause was never touched. The discipline isn't asking "why" exactly five times — it's refusing to stop at a cause that isn't actionable or wouldn't prevent recurrence.

## Use when / Don't use when

- **Use when:** any recurring problem; postmortems; a fix was applied and the problem came back.
- **Don't use when:** causes are multiple and interacting — a linear chain will oversimplify a genuinely tangled situation; use a fuller investigation instead.

## Inputs → Outputs

- **Inputs:** an observed failure or defect.
- **Outputs:** a causal chain from symptom to actionable root cause, with the fix level marked explicitly.

## Principles

- Each "why" must be answered with evidence, not plausibility.
- Stop at a cause that is both actionable and preventive — usually a process or design issue, rarely a person.
- "Human error" is never a root cause; it's a symptom of a system that permitted the error to matter.

## Procedure

1. State the problem concretely: what happened, when, and its impact.
2. Ask why it happened; verify the answer with evidence before accepting it as the next link.
3. Repeat on each answer. Branch if a "why" has multiple verified causes.
4. Stop when the cause is actionable and preventive — typically 3 to 7 levels, not a fixed count of five.
5. Check the chain backwards: does removing each cause actually break the chain?
6. Report the chain and the fix level — and what recurrence at that level would mean, as the residual risk.

## Common mistakes

- Accepting plausible-but-unverified answers, turning the chain into fiction dressed as analysis.
- Stopping at "someone made a mistake" instead of asking what allowed the mistake to matter.
- Forcing a single chain when causes actually branch.
- Ritually asking exactly five whys regardless of where the actionable cause was reached.

## Examples

- Outage → deploy bug → missing test → no test requirement for config changes → configuration treated as "not code."
- Missed quarterly target → pipeline gap → lead generation paused → a budget process artifact nobody flagged.

## Related

- [[root-cause-investigation]] — the fuller, evidence-gated composite for when causes are multiple or entangled.
- [[causal-analysis]] — the deeper mechanism-level tool when correlation and causation need to be disentangled explicitly.
- [[problem-framing]] — often the actual issue when a "why" chain keeps producing unsatisfying answers.
