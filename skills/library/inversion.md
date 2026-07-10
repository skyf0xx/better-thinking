---
name: inversion
description: >
  Solve the opposite problem — "how would I guarantee failure?" — and
  negate the answers into guardrails. Use when planning anything, when
  success criteria are vague but failure is obvious, or when a team is
  stuck generating only positive ideas.
type: atomic
category: problem-solving
difficulty: 1
tokens: ~790
dependencies: []
related: [premortem, devils-advocacy]
---

# Inversion

Solve the opposite problem — "how would I guarantee failure?" — and negate the answers.

## Why

Failure modes are often far more enumerable than success paths, and prevention is frequently cheaper than achievement. Minds generate hazards more fluently than they generate plans, and inversion is a direct way to exploit that asymmetry for something useful.

## Use when / Don't use when

- **Use when:** planning anything ("avoid stupidity before seeking brilliance"); success criteria are vague but failure is obvious; a team is stuck trying to generate positive ideas directly.
- **Don't use when:** avoiding failure isn't the same thing as succeeding, and what's actually missing is the constructive path forward, not a list of things to avoid.

## Inputs → Outputs

- **Inputs:** a goal or plan.
- **Outputs:** a ranked list of failure-guaranteeing behaviors, and their negations turned into explicit guardrails.

## Principles

- Ask "how would I guarantee this fails *certainly*?" — not the softer "what could go wrong," which invites a weaker, less generative answer.
- The most valuable inversions are usually behaviors you're already doing, not exotic hypotheticals.
- Not-failing is necessary but not sufficient for success — inversion produces guardrails, not a strategy on its own.

## Procedure

1. State the goal clearly.
2. Invert it: "How would I guarantee this fails?" Generate exhaustively — behaviors, omissions, attitudes, structural flaws.
3. Rank the list by how reliably each item causes failure, and by how likely you are to actually be doing it already.
4. Negate the top items into explicit guardrails or stop-doing rules.
5. Check the current plan against each guardrail and flag any violations found — those violations are the residual risk worth acting on immediately.

## Common mistakes

- Producing only exotic, dramatic failure modes while missing the mundane ones — neglect, drift, boredom — that are actually more common.
- Treating the resulting guardrail list as if it were a complete strategy on its own.
- Stopping at listing failure modes without ever auditing the current plan against them.

## Examples

- "How would I make this migration fail?" surfaces: no rollback plan, a big-bang cutover with no incremental rollout.
- "How would I ruin this new hire's first month?" surfaces onboarding gaps worth fixing proactively.
- "How do I guarantee nobody reads this report?" surfaces structural and framing problems before the report is even written.

## Related

- [[premortem]] — inversion applied to one specific, concrete plan with a timeline, typically run as a group exercise.
- [[devils-advocacy]] — a complementary adversarial technique, applied specifically against a group's existing consensus.
