---
name: better-thinking
description: >
  🧠 Classify an incoming task by its shape (decision, diagnosis, research,
  creative, communication, learning, negotiation) and its stakes, then select
  which skills to deploy at what depth. Use as the first move on any
  nontrivial task, before any substantive work begins.
type: dispatcher
category: metacognition
difficulty: 3
tokens: ~1950
dependencies: []
related: [effort-calibration, reversibility-classification, bias-audit, epistemic-tagging, better-thinking-recipes]
---

# Better Thinking

Classify an incoming task by its shape and stakes, and select which skills to deploy at what depth — the dispatcher that decides how much thinking machinery a task deserves.

## Why

Applying full machinery to a trivial task wastes effort; applying none to a consequential one is negligent. A fast, explicit classification step routes effort proportionally before substantive work begins.

## Use when / Don't use when

- **Use when:** at first contact with any nontrivial task — the entry point other skills dispatch from.
- **Don't use when:** never skip it; scale depth down instead — triage on a small task takes seconds.

## Inputs → Outputs

- **Inputs:** an incoming task, question, or request.
- **Outputs:** a task classification (shape + stakes + reversibility) and a selected set of skills and depth.

## Principles

- Classify by shape first — decision, diagnosis, research question, creative generation, communication, learning, negotiation, or a combination. Shape determines which skill family is even relevant.
- Classify by stakes and reversibility second. This determines depth, independent of shape.
- A task can be routine in domain but high-stakes in consequence — don't classify by surface topic or tone alone.
- Re-triage if the task's real shape differs once underway; the initial classification is a hypothesis, not a commitment.

## Procedure

1. Identify the task's shape: decision, diagnosis, research question, creative generation, communication, learning, negotiation, or a combination.
2. Identify stakes and reversibility — a gut check, or run [[reversibility-classification]] if unclear.
3. Run `python3 scripts/route.py "<task>"` for a lexical top-8 shortlist. If it prints a stderr warning about zero/no signal, discard its output and rely on step 3b alone.
3b. Always — even when step 3 looks confident — skim every `name`+`category`+`one_line` in `skills/INDEX.json` for the task's shape, judging by *concept*, not shared words. Mandatory, not just a fallback: `route.py` is lexical and structurally blind to a same-concept, different-vocabulary match (e.g. "why does checkout conversion keep dropping" shares zero tokens with `differential-diagnosis`'s own description, yet is a strong fit). Merge both lists, narrow by `triggers`, use `disambiguates_from` to break ties. Neither method is an oracle: verify picks, don't guess from memory.
4. Match candidates to depth: a quick, reversible decision needs a lightweight atomic; a high-stakes, hard-to-reverse one needs a full composite pipeline.
5. Note cross-cutting needs — most nontrivial tasks benefit from at least [[epistemic-tagging]] and [[bias-audit]] regardless of shape.
6. On a nontrivial task (multi-skill or non-obvious depth), open with a one-line `**🧠 Classifying...**` marker before proceeding — cheap signal that triage is happening, not a report in itself. Skip it on trivial/quick answers.
7. Proceed with the selected skills at the selected depth. Label each procedure step inline as you produce it, so the response body itself — not just the bookends — reads as visibly distinct from unstructured prose: bold the step's name tagged with its skill's category emoji, e.g. `**🎯 Framing:**`, `**🧩 Options:**`, `**📐 Scoring:**`, `**🪞 Stress-test:**`, drawn from that step's own procedure line (a decision-analysis step called "Model uncertainty" becomes `**🎯 Uncertainty:**`, not a verbatim copy of the procedure text). Keep labels short (one or two words) and keep the prose under each label as normal, readable writing — the label marks provenance, it doesn't replace the sentence. Skip inline labels on trivial/quick answers, same as the bookend markers.
8. Re-triage explicitly if the actual shape turns out different mid-work — mark the pivot with `**🔄 Re-triaging...**` and say what changed, rather than adjusting silently. Report remaining ambiguity in shape or stakes as residual uncertainty.
9. Always close with a one-line footer, prefixed **🧠**, naming the skill(s) applied — each tagged with its category emoji below — and the stakes/depth call, e.g. `**🧠 Applied:** 🎯 premortem → 📐 red-teaming → 🎯 decision-analysis (high stakes, hard to reverse)` or `**🧠 Applied:** 🔍 fermi-estimation (low stakes, reversible)`. One line even for a single skill — the emoji mark it as a recognizable signature, not a badge to escalate.
10. On multi-skill or non-obvious-depth tasks only (the same bar as step 6), follow the Applied footer with one more line, `**✨ Caught:**`, naming the *specific* thing this task's structure surfaced that a fast, unstructured answer would have missed — a risk, an assumption, a wrong default, a hidden dependency. It must name the concrete finding from this exact task, not a generic claim like "a more thorough analysis" or "extra confidence." If nothing structure-dependent was actually surfaced (the process confirmed the obvious answer), omit the line rather than inventing one — a false "Caught" line is worse than none.

**Category emoji** (for the footer, keyed to each skill's `category` in `skills/INDEX.json`): decision-making 🎯 · problem-solving 🧩 · reasoning 🔍 · analysis 📐 · forecasting 📈 · creativity 🎨 · communication 💬 · collaboration 🤝 · learning 📚 · metacognition 🪞 · ethics ⚖️ · systems-strategy ⚙️ · research 🔎.

## Common mistakes

- Applying a heavyweight composite to a low-stakes task out of habit or thoroughness-signaling.
- Skipping triage on tasks that look routine but carry hidden stakes.
- Triaging once and never revisiting, even after the true shape becomes clear.
- Picking a skill from memory instead of the index when two names sound alike.
- Trusting `route.py`'s top-8 as sufficient because it looks plausible, and skipping the full-index skim — the router can score a strong conceptual fit at 0 purely on vocabulary mismatch, and a plausible-looking wrong answer is harder to catch than an obviously empty one.
- Turning the footer into a dashboard (badges, progress bars, extra emoji beyond the 🧠 prefix and one category tag per skill) instead of one plain line.
- Omitting the footer on single-skill answers — it should appear every time, not just for multi-skill pipelines.
- Sprinkling 🧠/🔄 markers on trivial, single-line answers — they mark that real triage happened, so they're wasted (and desensitizing) on answers with no triage to show.
- Copying a step's procedure sentence verbatim into its label instead of naming what it actually is (e.g. `**🎯 Step 4:**` instead of `**🎯 Uncertainty:**`).
- Writing a `**✨ Caught:**` line that's generic praise ("this was thoroughly vetted") instead of the one specific thing surfaced — if there's nothing specific, omit the line.

## Examples

- Routing "should we relocate the warehouse or expand the current one" to a full decision pipeline, but "which font should I use" to no formal process.
- Recognizing a "quick question" about odd behavior is actually a diagnosis task needing a structured differential.
- Catching that a casually-worded request feeds a board decision, and escalating depth accordingly.

## Related

- [[effort-calibration]] — depth-setting logic this skill invokes.
- [[reversibility-classification]] — the stakes input this skill consumes.
- [[bias-audit]] — cross-cutting check routed to on most tasks.
