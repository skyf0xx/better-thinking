---
name: reversibility-classification
description: >
  Classify a pending decision as a one-way or two-way door — cheap-reversible,
  costly-reversible, or effectively irreversible — and size the decision
  process accordingly. Use at first contact with any decision, before any
  other decision-making skill.
type: atomic
category: decision-making
difficulty: 1
tokens: ~890
dependencies: []
related: [effort-calibration, decision-framing, better-thinking]
---

# Reversibility Classification

Classify a decision as a one-way or two-way door, and size the decision process accordingly.

## Why

The most common process error is symmetric treatment of decisions: agonizing over reversible choices as if they were permanent, and rushing irreversible ones as if they could be corrected later. This 60-second classification fixes the allocation before either failure mode sets in, and is the input every other decision skill in this collection uses to size itself.

## Use when / Don't use when

- **Use when:** at first contact with any decision — this runs *before* [[decision-framing]] or any other decision skill.
- **Don't use when:** never; this is the router. Its own depth should scale down for obviously trivial decisions rather than being skipped.

## Inputs → Outputs

- **Inputs:** a pending decision.
- **Outputs:** a reversibility grade, the real cost-to-reverse, and a recommended process weight (decide now vs. lightweight analysis vs. full process).

## Principles

- Reversibility is a spectrum priced in cost-to-undo (money, time, trust, optionality) — not a binary.
- Decisions often look more irreversible than they are (many commitments can be renegotiated), and some look reversible but aren't (trust, public announcements, data leaks compound and don't undo cleanly).
- For genuine two-way doors, speed beats analysis — deciding fast and correcting course is cheaper than deciding slowly and "perfectly."

## Procedure

1. Ask: if this turns out wrong, what exactly does undoing it cost — and is anything unrecoverable (time, trust, legal exposure, compounding lock-in)?
2. Grade the decision: cheap-reversible / costly-reversible / effectively irreversible.
3. Check specifically for hidden irreversibles inside a choice that looks reversible: public commitments, data exposure, precedent-setting.
4. Match the process to the grade: cheap-reversible → decide now with sensible defaults and a review date; costly-reversible → lightweight analysis; irreversible → full decision-analysis plus a premortem.
5. Record the grade so escalation or de-escalation of process is legible to anyone else involved, and flag any uncertainty in the grade itself as the residual risk to watch.

## Common mistakes

- Prestige-driven overprocessing of decisions that are actually cheap to reverse.
- Missing the trust/precedent component that makes a nominally "reversible" action actually costly to undo.
- Treating hiring, pricing changes, and public statements as two-way doors when they routinely aren't.

## Examples

- Trying a new team standup format: cheap-reversible, just do it and adjust next week.
- Choosing a database for a new service: costly-reversible, worth a lightweight comparison.
- A public pricing change or a layoff: irreversible-adjacent, warrants the full process.

## Related

- [[effort-calibration]] — the general form of stakes-to-effort matching this skill feeds.
- [[decision-framing]] — the next step once the process weight is set.
- [[better-thinking]] — often invokes this skill directly when a task's shape is a decision.
