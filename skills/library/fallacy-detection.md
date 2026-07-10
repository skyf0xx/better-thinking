---
name: fallacy-detection
description: >
  Scan an argument for named logical failure patterns, distinguishing a
  genuine fallacy from a merely weak or unwelcome argument. Use when
  evaluating persuasive content, or when a conclusion seems to sneak past
  its support.
type: atomic
category: analysis
difficulty: 2
tokens: ~690
dependencies: []
related: [deductive-validation, argument-mapping, critical-reading]
---

# Fallacy Detection

Scan an argument for named logical failure patterns, distinguishing a genuine fallacy from a merely weak or unwelcome argument.

## Why

Naming a fallacy is powerful and easy to abuse — real fallacy-spotting requires showing the specific inferential gap, not just pattern-matching a label onto anything you dislike.

## Use when / Don't use when

- **Use when:** evaluating persuasive content; a conclusion seems to sneak past its support; debate moderation.
- **Don't use when:** you're pattern-matching to win rather than to check validity — that use corrodes the skill.

## Inputs → Outputs

- **Inputs:** an argument.
- **Outputs:** identified fallacies, if any, with the specific broken inference shown, separated from claims that are merely weak or unproven.

## Principles

- A fallacy is a *structural* defect in the inference, not a false conclusion or a conclusion you dislike.
- Naming the fallacy requires showing what's missing, not just applying a label.
- Common patterns: ad hominem, strawman, false dilemma, appeal to authority outside expertise, post hoc, motte-and-bailey, equivocation, circular reasoning.

## Procedure

1. Map the argument's structure using argument-mapping if it's complex.
2. Check each inferential step: does the conclusion actually follow, or is something being smuggled?
3. Match candidate fallacy patterns; for each match, show the specific missing link, not just the label.
4. Distinguish: is this a structural fallacy, or just a claim that's false, unproven, or weakly supported? Only the former gets the fallacy label.
5. Report the fallacy with its repair — what would the argument need to be valid?

## Common mistakes

- Fallacy-labeling as a rhetorical weapon instead of an analytic finding.
- Missing the repair step — naming without showing the gap isn't analysis.
- Calling every weak argument a "fallacy."

## Examples

- A sales pitch's false dilemma ("either buy this or stay vulnerable").
- A policy debate's motte-and-bailey.
- Auditing your own draft for a smuggled premise.

## Related

- [[deductive-validation]] — the general validity check this technique specializes with named patterns.
- [[argument-mapping]] — supplies the structure this technique scans.
- [[critical-reading]] — the broader extraction discipline this fallacy check fits within.
