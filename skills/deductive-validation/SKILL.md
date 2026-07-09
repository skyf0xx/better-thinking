---
name: deductive-validation
description: >
  Check whether a conclusion actually follows from its premises, independent
  of whether the premises are true. Use when evaluating any "therefore," or
  when a conclusion feels off but the premises seem fine (or vice versa).
type: atomic
category: reasoning
difficulty: 2
tokens: ~790
dependencies: []
related: [argument-mapping, fallacy-detection, reductio]
---

# Deductive Validation

Check whether a conclusion actually follows from its premises, independent of whether the premises are true.

## Why

Invalid arguments with true-sounding premises are the most persuasive form of wrong, because the truth of the premises distracts from the broken inference between them and the conclusion. Separating validity (does it follow?) from truth (are the premises correct?) catches these before they pass unchallenged.

## Use when / Don't use when

- **Use when:** evaluating any "therefore"; a conclusion feels off but the premises seem fine, or vice versa.
- **Don't use when:** the argument is explicitly probabilistic — use a Bayesian update instead of a validity check, since probabilistic arguments aren't meant to be deductively airtight.

## Inputs → Outputs

- **Inputs:** an argument, explicit or reconstructed from prose.
- **Outputs:** a verdict of valid or invalid, the specific inferential gap if invalid, and — kept separate — an assessment of premise truth.

## Principles

- Validity is about form, not content. An argument can be valid with false premises, and invalid with true ones — these are independent questions.
- Hidden premises do the most damage; most real arguments are enthymemes (they omit a premise the speaker assumes is obvious).

## Procedure

1. Restate the argument as numbered premises and a conclusion.
2. Surface unstated premises needed to make the inference actually work; add them explicitly rather than assuming them.
3. Test form: could all the premises be true while the conclusion is false? If so, construct that counterexample world.
4. Only after the form is checked, assess each premise's truth independently.
5. Report: valid or invalid, which premise is weakest, and what the argument actually establishes — including any part that remains genuinely uncertain.

## Common mistakes

- Rejecting valid arguments because you dislike the conclusion.
- Accepting invalid arguments because the premises happen to be true.
- Forgetting step 2 — most arguments in the wild are missing a premise, and skipping its extraction hides the real point of disagreement.

## Examples

- Auditing a legal brief's chain of reasoning for a gap between the cited precedent and the claimed conclusion.
- Checking whether benchmark results actually imply the claimed product superiority, or just correlate with it.
- Testing a policy argument's syllogism for a smuggled, unstated premise.

## Related

- [[argument-mapping]] — lays out the full structure this skill tests link by link.
- [[fallacy-detection]] — a named-pattern-matching companion for common ways validity breaks.
- [[reductio]] — often the next move once a claim has been restated precisely enough to test.
