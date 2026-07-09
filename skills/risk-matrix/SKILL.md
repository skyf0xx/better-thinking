---
name: risk-matrix
description: >
  Grade risks by likelihood times impact, assign responses by quadrant,
  and re-grade on a schedule — a register, not a ritual. Use when planning
  anything with multiple failure modes, or for periodic review of an
  ongoing effort.
type: atomic
category: decision-making
difficulty: 2
tokens: ~880
dependencies: []
related: [expected-value, premortem, tripwires]
---

# Risk Matrix

Grade risks by likelihood × impact, assign responses by quadrant, and re-grade on a schedule — a register, not a ritual.

## Why

Ungraded risk lists get attention allocated by vividness rather than actual importance. The two-axis grade forces both the boring-but-likely risks and the unlikely-but-ruinous ones into view together, and quadrant-based response rules prevent both paranoia over minor risks and neglect of severe ones.

## Use when / Don't use when

- **Use when:** planning anything with multiple distinct failure modes; periodic review of an ongoing effort's risk posture.
- **Don't use when:** one dominant risk deserves full standalone analysis rather than being flattened into a single grid cell.

## Inputs → Outputs

- **Inputs:** an endeavor and its enumerated risks (often sourced from a premortem or inversion exercise).
- **Outputs:** a graded risk register with an owner, a response, and an early indicator per material risk.

## Principles

- Likelihood comes from base rates where they exist, not from gut feel or vibes.
- Impact includes recovery cost and knock-on effects, not just the immediate direct damage.
- Responses are a fixed menu — avoid, mitigate, transfer, accept — and "accept" must always be an explicit choice, never a silent default.
- A register nobody ever revisits is theater, not risk management.

## Procedure

1. Enumerate risks (often fed from a premortem); state each as event → consequence, not a vague noun ("vendor risk" becomes "vendor X misses the Q3 integration date, slipping launch").
2. Grade likelihood (anchored to base rates where available) and impact (including recovery costs and knock-on effects).
3. Place each risk on the grid: high-likelihood/high-impact gets avoided or the plan restructured; high-likelihood/low-impact gets cheap, batched mitigations; low-likelihood/high-impact gets mitigation or transfer plus an early indicator; low/low gets accepted explicitly.
4. Assign each material risk an owner and an early indicator that would signal it's materializing.
5. Set a re-grading cadence, since likelihoods drift as conditions change — report the current grading's freshness as the residual uncertainty.

## Common mistakes

- Vague risk statements that can't actually be graded on either axis.
- Multiplying likelihood and impact into a fake-precise combined score ("risk score 12") that hides the underlying judgment calls.
- No owner assigned — a risk without an owner tends to get accepted by accident rather than by decision.
- Registering risks once and never revisiting the register as conditions change.

## Examples

- A launch's risk register, reviewed weekly through the rollout.
- A clinical trial's risk plan, covering both patient safety and operational risks.
- Expedition planning; a periodic vendor portfolio review.

## Related

- [[expected-value]] — the continuous, numeric version of this same likelihood × impact logic.
- [[premortem]] — commonly the source that feeds this skill's risk enumeration step.
- [[tripwires]] — the mechanism for operationalizing each risk's early indicator into a pre-committed action.
