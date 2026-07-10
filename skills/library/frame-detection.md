---
name: frame-detection
description: >
  Identify how a question, comparison, or presentation is pre-loaded to
  favor a particular answer, before answering it. Use when a question
  has an oddly obvious answer, or a choice is presented as binary.
type: atomic
category: analysis
difficulty: 3
tokens: ~700
dependencies: []
related: [critical-reading, problem-framing, incentive-analysis]
---

# Frame Detection

Identify how a question, comparison, or presentation is pre-loaded to favor a particular answer, before answering it.

## Why

The same facts framed differently produce different judgments — loss versus gain framing, the comparison set chosen, which baseline is implied. Detecting the frame is a prerequisite to answering the actual question rather than the one smuggled into the phrasing.

## Use when / Don't use when

- **Use when:** a question has an oddly obvious answer; a choice is presented as binary; a statistic is framed as loss or gain; evaluating your own instructions or prompts for embedded bias.
- **Don't use when:** the frame is genuinely neutral and singular.

## Inputs → Outputs

- **Inputs:** a question, comparison, or presented choice.
- **Outputs:** the frame made explicit, the answer under that frame, and the answer under at least one alternative frame.

## Principles

- The comparison baseline is a frame choice — "compared to what?" often does more work than any argument.
- Loss-framing and gain-framing of identical facts provoke different risk preferences — check both.
- Who chose the frame, and does its choice serve them?
- A reframe that changes the answer reveals the original answer was frame-dependent, not fact-dependent.

## Procedure

1. State the question or choice as given.
2. Identify the implicit baseline or comparison, the implicit option set, and the gain/loss framing.
3. Ask who chose this frame and what answer it favors.
4. Reframe: invert gain/loss, change the comparison baseline, widen the option set.
5. Answer under both frames; if they diverge, the honest answer addresses the divergence explicitly.

## Common mistakes

- Detecting the frame and stopping there without re-answering.
- Assuming all framing is manipulative when sometimes it's just how a fact is naturally described.
- Missing your own frame when generating the question.

## Examples

- "Should we cut costs" versus "should we invest less in reliability."
- A survival-rate stat versus the equivalent mortality-rate stat.
- "Which vendor is cheaper" versus "what's the cost of each vendor's failure mode."

## Related

- [[critical-reading]] — the extraction discipline this check runs inside.
- [[problem-framing]] — the generative counterpart, for framing your own problems well.
- [[incentive-analysis]] — often explains who benefits from a given frame.
