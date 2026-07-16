# Recipe: Jobs-to-be-Done (JTBD)

**What it is:** Clayton Christensen's framework for market/product research — before building anything, establish what "job" people are actually "hiring" a product to do, so a market need is verified rather than assumed.

## Skill sequence

1. **Decompose the research question** — run **[[question-decomposition]]** to break "is there a real market here" into the specific sub-questions that would actually settle it (who has this job, how are they doing it today, what's unsatisfying about that, what would "hired" look like). Most JTBD efforts skip straight to interviews without first deciding what the interviews need to establish.
2. **Gather the job** — run **[[interview-synthesis]]** on real conversations with people in the target situation, using non-leading questions to surface the job-to-be-done rather than a stated feature request. The output is the job, the current workaround, and the friction in that workaround — not a features wishlist.
3. **Triangulate the signal** — run **[[evidence-triangulation]]** across independent sources (interviews, existing usage data, forum/support-ticket language, competitor switching behavior) before trusting the job as real. A single enthusiastic interview is the classic false positive this step exists to catch.
4. **Rank rival explanations** — run **[[competing-hypotheses]]** on why people currently behave the way they do: is it really the job you think it is, or a cheaper explanation (habit, lack of awareness of alternatives, a constraint unrelated to the job)? Disconfirm before committing.
5. **Audit the resulting thesis** — run **[[assumption-audit]]** on the market thesis that comes out of steps 2–4 — what has to be true for this job to be worth building for, and which of those load-bearing claims are actually unverified.
6. **Hand off** — if the thesis survives, its output (a falsifiable "customers hire X to do Y instead of Z" statement) is the correctly-shaped input for [[lean-startup]]'s "Frame the bet" step. JTBD answers "is there a hypothesis worth testing"; lean-startup tests it.

## What this buys you over a plain JTBD writeup

- The research question is decomposed *before* interviewing, instead of interviews happening first and a job getting reverse-engineered from whatever people said.
- The job is triangulated across sources rather than accepted from one compelling conversation — the single most common way JTBD research produces a false market signal.
- Rival, cheaper explanations for current behavior are explicitly ranked against the "job" story instead of assumed away.
- The final thesis gets an assumption audit before a single line of product work depends on it.
- The output is shaped to plug directly into `lean-startup`'s framing step, so JTBD and build-measure-learn compose into one continuous pipeline instead of two disconnected exercises.

## Residual gap

Actually recruiting and scheduling interview subjects, and any quantitative market-sizing math beyond triangulating qualitative signal, are outside this collection's scope — this recipe covers the reasoning applied to what people say and do, not the logistics of reaching them.

## Related recipes

- [[lean-startup]] — JTBD determines whether a falsifiable hypothesis exists at all; lean-startup takes that hypothesis and runs the build-measure-learn loop on it.
- [[design-thinking]] — shares the empathize-first instinct, but JTBD is narrower and more falsification-oriented: it exists specifically to kill false market signals before they become build decisions.
- [[growth-loop-design]] — a natural downstream consumer: once JTBD establishes the real job and friction, that same Who×Job×Friction material seeds growth-loop-design's ideation step directly.
