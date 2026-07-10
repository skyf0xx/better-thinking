---
name: reductio
description: >
  Test a claim by assuming it's true, deriving its consequences, and
  hunting for a contradiction or absurdity. Use when a general rule is
  proposed, a definition or principle needs stress-testing, or an argument
  feels slippery.
type: atomic
category: reasoning
difficulty: 2
tokens: ~860
dependencies: []
related: [deductive-validation, structured-what-if, steelmanning]
---

# Reductio

Test a claim by assuming it's true, deriving its consequences, and hunting for a contradiction or absurdity.

## Why

Some claims are easier to refute than to directly evaluate. Following a claim mechanically to its logical conclusions is often the fastest way to expose a hidden flaw — or, just as usefully, to discover the claim is stronger than it first looked because it survives the pressure.

## Use when / Don't use when

- **Use when:** a general rule is proposed ("we should always/never X"); a definition or principle needs stress-testing; a proof or argument feels slippery without an obvious specific flaw.
- **Don't use when:** the claim is explicitly probabilistic or scoped — deriving edge-case absurdities from a statistical tendency just builds a strawman, not a real refutation.

## Inputs → Outputs

- **Inputs:** a claim, rule, or policy.
- **Outputs:** either a derived contradiction or absurd consequence, or increased confidence in the claim after it survives the attempt.

## Principles

- Take the claim fully seriously at its intended strength — a lazy reductio only refutes a strawman version.
- The contradiction must follow from the claim itself, not from an assumption smuggled in alongside it.
- An *unwelcome* consequence is not the same thing as an *absurd* one — don't conflate the two.

## Procedure

1. State the claim precisely, at the strength its proponent actually intends (steelman it first if needed).
2. Assume it true without reservation.
3. Derive consequences mechanically, paying particular attention to boundary conditions and extreme-but-valid cases.
4. Check each derived consequence: does it contradict the claim itself, contradict an accepted fact, or is it genuinely absurd?
5. Verify the absurdity actually traces back to the claim, and not to a smuggled auxiliary assumption added along the way.
6. Report the result: refuted, with the derivation shown, or survived, with the hardest case it was tested against — and note any case left untested as the residual uncertainty.

## Common mistakes

- Refuting an exaggerated version of the claim instead of the one actually intended.
- Treating "I don't like that outcome" as if it were a logical contradiction.
- Smuggling in an extra premise partway through that turns out to be the real source of the absurdity, not the original claim.

## Examples

- Stress-testing "all metrics should have owners" against metrics that genuinely span multiple teams.
- Testing a proposed legal rule at its most extreme but still-valid edge case.
- Checking a system invariant by assuming it holds and deriving whether an impossible state becomes reachable.

## Related

- [[deductive-validation]] — the general validity-checking machinery this skill applies in a specific, adversarial direction.
- [[structured-what-if]] — the same forward-tracing move used exploratively rather than to hunt for contradiction.
- [[steelmanning]] — often a necessary first step so the reductio targets the claim's real strength, not a weaker stand-in.
