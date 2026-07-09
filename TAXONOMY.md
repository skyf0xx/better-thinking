# Taxonomy of Cognitive Skills

**135 skills · 107 atomic (A) · 28 composite (C)** across 13 categories. Full specifications live in [catalog/](catalog/). Format: `name` (type · difficulty) — one-liner.

Sources mined: cognitive science, psychology, philosophy, education, scientific research, systems engineering, military strategy, intelligence analysis (CIA structured analytic techniques), decision science, economics, product management, UX research, design thinking, negotiation, executive coaching, journalism, law (IRAC), medicine (differential diagnosis), academia, creative writing.

---

## 1. Foundational Reasoning — [catalog/01-reasoning.md](catalog/01-reasoning.md)

The inference primitives everything else builds on.

- `first-principles` (A·D3) — decompose to base truths and rebuild without inherited assumptions
- `deductive-validation` (A·D2) — check whether a conclusion actually follows from its premises
- `inductive-generalization` (A·D2) — generalize from instances with explicit sample-quality checks
- `abductive-inference` (A·D3) — generate and rank candidate explanations for an observation
- `analogical-reasoning` (A·D3) — transfer structure from a source domain, then verify the mapping holds
- `causal-analysis` (A·D4) — build a causal graph; separate correlation, confounding, and causation
- `counterfactual-reasoning` (A·D3) — evaluate "what if X had been different" with minimal-change worlds
- `bayesian-updating` (A·D3) — revise probabilities by likelihood ratios, starting from explicit priors
- `expected-value` (A·D2) — weigh outcomes by probability × payoff, including tail terms
- `fermi-estimation` (A·D2) — bound an unknown quantity via decomposition into estimable factors
- `reductio` (A·D2) — assume the claim, derive consequences, hunt for contradiction
- `argument-mapping` (A·D3) — lay out claims, premises, warrants, and rebuttals as an explicit structure
- `sanity-checking` (A·D1) — fast dimensional, magnitude, and boundary-condition verification

## 2. Problem Solving — [catalog/02-problem-solving.md](catalog/02-problem-solving.md)

Getting from a stuck state to a solved one.

- `problem-framing` (A·D2) — restate the problem several ways before accepting any framing
- `mece-decomposition` (A·D2) — split a problem into exhaustive, non-overlapping parts
- `working-backwards` (A·D2) — start from the goal state and chain prerequisites backwards
- `means-ends-analysis` (A·D3) — repeatedly reduce the largest gap between current and goal state
- `inversion` (A·D1) — solve "how do I guarantee failure?" and negate it
- `constraint-relaxation` (A·D2) — drop constraints one at a time to find which one binds
- `five-whys` (A·D1) — iterate "why?" past symptoms toward process-level causes
- `solution-space-mapping` (A·D2) — enumerate option *families* before committing to any candidate
- `triz-contradiction` (A·D4) — resolve "improving X worsens Y" via contradiction-breaking patterns
- `structured-problem-solving` (C·D3) — Polya's loop: understand → plan → execute → review
- `root-cause-investigation` (C·D3) — evidence-driven causal drilldown with fix verification
- `differential-diagnosis` (C·D4) — enumerate hypotheses, order by prior × severity, run discriminating tests

## 3. Decision Making — [catalog/03-decision-making.md](catalog/03-decision-making.md)

Choosing well under constraints and uncertainty.

- `decision-framing` (A·D2) — define the actual decision, options, decider, stakes, and deadline
- `weighted-scoring` (A·D2) — score options against explicitly weighted criteria
- `cost-benefit` (A·D2) — tally full costs and benefits, including opportunity cost and hidden costs
- `reversibility-classification` (A·D1) — sort decisions into one-way vs two-way doors; size effort accordingly
- `premortem` (A·D2) — assume the plan failed; work backwards to today's preventable causes
- `second-order-scan` (A·D3) — trace "and then what?" consequences two or more steps out
- `regret-minimization` (A·D1) — evaluate options from the perspective of your future self
- `satisficing-thresholds` (A·D2) — set "good enough" criteria in advance to prevent endless optimization
- `risk-matrix` (A·D2) — grade risks by likelihood × impact; assign mitigations by quadrant
- `prioritization-triage` (A·D2) — rank work by value, urgency, and cost-of-delay under capacity limits
- `decision-analysis` (C·D4) — full pipeline: frame → generate → model uncertainty → score → stress-test → decide

## 4. Evidence & Research — [catalog/04-research.md](catalog/04-research.md)

Finding out what's true.

- `question-decomposition` (A·D2) — break a research question into independently answerable sub-questions
- `search-strategy` (A·D2) — plan queries, sources, and stop-conditions before searching
- `source-credibility` (A·D2) — grade a source on expertise, incentive, track record, and proximity
- `evidence-triangulation` (A·D2) — require independent confirmation; detect shared upstream sources
- `evidence-hierarchy` (A·D3) — rank evidence types by strength for the specific claim class
- `critical-reading` (A·D3) — extract claims, evidence, assumptions, and omissions from a text
- `statistical-audit` (A·D4) — interrogate the numbers: base rates, denominators, significance, effect size
- `data-quality-assessment` (A·D3) — evaluate provenance, completeness, bias, and fitness of a dataset
- `methodology-critique` (A·D4) — find design flaws that break a study's claimed inference
- `claim-verification` (C·D3) — journalism-grade fact-check pipeline for a specific claim
- `literature-synthesis` (C·D4) — systematic survey: gather, grade, extract, reconcile, summarize
- `interview-synthesis` (C·D3) — design non-leading questions, gather responses, cluster into findings
- `scientific-method` (C·D4) — hypothesize → predict → test → attempt falsification → update

## 5. Analysis & Critique — [catalog/05-analysis.md](catalog/05-analysis.md)

Stress-testing claims, arguments, and positions.

- `assumption-audit` (A·D2) — surface load-bearing assumptions and test each for fragility
- `steelmanning` (A·D2) — reconstruct the strongest version of a position before judging it
- `fallacy-detection` (A·D2) — scan an argument for named logical failure patterns
- `devils-advocacy` (A·D2) — build the best case *against* the current consensus position
- `incentive-analysis` (A·D2) — ask *cui bono*: map who gains from each claim or outcome
- `stakeholder-mapping` (A·D2) — chart actors by interest, influence, and alignment
- `frame-detection` (A·D3) — identify how a question's framing pre-loads its answer
- `structured-what-if` (A·D2) — take a fixed conclusion as given and reason its implications
- `competing-hypotheses` (C·D4) — ACH: rank hypotheses by evidence *inconsistency*, not confirmation
- `red-teaming` (C·D4) — full adversarial exercise against a plan, argument, or system
- `peer-review` (C·D3) — structured evaluation of someone's work: correctness, rigor, significance
- `case-analysis` (C·D3) — IRAC generalized: issue → governing rules → application → conclusion

## 6. Systems & Strategy — [catalog/06-systems-strategy.md](catalog/06-systems-strategy.md)

Thinking about wholes, dynamics, and adversaries.

- `systems-mapping` (A·D4) — model stocks, flows, delays, and boundaries of a system
- `feedback-loop-analysis` (A·D3) — find reinforcing and balancing loops driving behavior
- `bottleneck-analysis` (A·D2) — locate the binding constraint; subordinate everything else to it
- `leverage-points` (A·D4) — rank intervention points by depth (parameters → structure → goals → paradigms)
- `game-theoretic-analysis` (A·D4) — model players, payoffs, and equilibria of strategic interaction
- `chestertons-fence` (A·D1) — before removing anything, reconstruct why it exists
- `backcasting` (A·D2) — define the desired future state and derive the path backwards
- `ooda-loop` (C·D3) — observe → orient → decide → act, iterated faster than conditions change
- `scenario-planning` (C·D4) — build divergent plausible futures; test strategies across all of them
- `wargaming` (C·D4) — simulate adversary moves and countermoves over multiple turns
- `strategic-planning` (C·D5) — diagnosis → guiding policy → coherent actions (Rumelt kernel)

## 7. Forecasting & Uncertainty — [catalog/07-forecasting.md](catalog/07-forecasting.md)

Putting honest numbers on the future.

- `reference-class-forecasting` (A·D3) — start from the base rate of similar cases (the outside view)
- `uncertainty-decomposition` (A·D3) — split uncertainty into reducible vs irreducible; state ranges, not points
- `sensitivity-analysis` (A·D3) — vary inputs to find which assumptions actually move the conclusion
- `trend-breakpoint-analysis` (A·D3) — extrapolate trends while hunting for saturation and regime change
- `tripwires` (A·D2) — pre-commit to indicators that will trigger a belief or plan update
- `monte-carlo-reasoning` (A·D3) — mentally sample many runs of an uncertain process instead of one story
- `structured-forecasting` (C·D4) — superforecaster pipeline: decompose, base-rate, adjust, calibrate, schedule updates

## 8. Creativity — [catalog/08-creativity.md](catalog/08-creativity.md)

Generating options that weren't on the table.

- `divergent-ideation` (A·D1) — quantity-first generation with judgment explicitly deferred
- `scamper` (A·D1) — transform an existing thing via substitute/combine/adapt/modify/put-to-other-use/eliminate/reverse
- `morphological-analysis` (A·D2) — decompose into dimensions, enumerate values, recombine systematically
- `random-stimulus` (A·D1) — force association with an unrelated prompt to escape a local basin
- `creative-constraints` (A·D2) — add artificial constraints to provoke non-obvious solutions
- `concept-blending` (A·D3) — merge two frames into a new space with emergent properties
- `perspective-rotation` (A·D2) — re-solve the problem under systematically different viewpoints
- `idea-convergence` (A·D2) — cluster, score, and select from an idea pool without killing variance too early
- `ideation-sprint` (C·D2) — diverge → cross-pollinate → converge, with explicit phase gates

## 9. Communication — [catalog/09-communication.md](catalog/09-communication.md)

Making thought land in another mind.

- `audience-modeling` (A·D2) — model the reader's knowledge, goals, and objections before writing
- `pyramid-structuring` (A·D2) — lead with the answer; support with grouped, ordered reasons
- `progressive-disclosure` (A·D2) — layer explanation from gist to depth, checking load at each layer
- `explanatory-analogy` (A·D2) — construct an analogy, then explicitly mark where it breaks
- `narrative-construction` (A·D3) — structure material as setup → tension → resolution
- `argument-construction` (A·D2) — build claim → evidence → warrant chains with counterargument slots
- `executive-summarization` (A·D2) — compress to decision-relevant essentials with an action ask
- `precision-questioning` (A·D2) — ask questions that isolate exactly the missing variable
- `nonviolent-communication` (A·D2) — observation → feeling → need → request, without evaluation-smuggling
- `feedback-delivery` (A·D2) — situation → behavior → impact, separated from identity and advice
- `revision-pass` (A·D2) — self-edit in ordered passes: structure, argument, clarity, economy
- `persuasive-case` (C·D3) — audience-modeled argument with objections pre-handled
- `difficult-conversations` (C·D3) — prepare and conduct a high-stakes conversation without losing the relationship

## 10. Collaboration & Facilitation — [catalog/10-collaboration.md](catalog/10-collaboration.md)

Thinking well *with* others.

- `active-listening` (A·D2) — paraphrase, label, and verify before responding
- `empathy-mapping` (A·D2) — reconstruct what another party sees, thinks, feels, and needs
- `batna-analysis` (A·D2) — establish each side's best alternative to agreement before negotiating
- `interest-based-bargaining` (A·D3) — trade on underlying interests, not stated positions
- `consensus-mapping` (A·D2) — measure gradient of agreement instead of forcing binary votes
- `session-design` (A·D2) — design a working session backwards from its intended output
- `expectation-contracting` (A·D1) — make roles, deliverables, and definitions-of-done explicit up front
- `negotiation` (C·D4) — full pipeline: prepare BATNAs → probe interests → invent options → converge
- `conflict-mediation` (C·D4) — surface each side's narrative, find compatible interests, broker agreement
- `delphi-aggregation` (C·D3) — aggregate independent estimates through anonymous iterative rounds
- `retrospective-facilitation` (C·D2) — structured what-went-well / what-didn't / what-changes review
- `coaching-dialogue` (C·D3) — GROW: goal → reality → options → will, led by questions not answers

## 11. Learning & Teaching — [catalog/11-learning.md](catalog/11-learning.md)

Acquiring and transmitting understanding.

- `self-explanation` (A·D1) — explain the material in plain terms; gaps in the explanation are gaps in understanding
- `knowledge-gap-analysis` (A·D2) — map what is known, unknown, and unknown-unknown for a task
- `mental-model-extraction` (A·D3) — distill an expert practice or corpus into a transferable model
- `deliberate-practice-design` (A·D3) — isolate a weakness, design drills at the edge of ability, add feedback
- `scaffolding` (A·D3) — support at the edge of current ability, removed as competence grows
- `learning-objectives` (A·D2) — define observable outcomes at the right cognitive level (Bloom)
- `error-analysis` (A·D2) — classify mistakes by type and root cause; target the pattern, not the instance
- `transfer-testing` (A·D3) — verify understanding by applying it in a structurally novel context
- `socratic-teaching` (C·D3) — lead a learner to construct the insight through sequenced questions
- `curriculum-design` (C·D4) — sequence objectives, instruction, practice, and assessment coherently

## 12. Metacognition — [catalog/12-metacognition.md](catalog/12-metacognition.md)

Thinking about the thinking itself. The layer that routes and corrects all others.

- `cognitive-triage` (A·D3) — classify the task and select which skills to deploy at what depth
- `bias-audit` (A·D3) — run a targeted checklist of the biases this task shape invites
- `epistemic-tagging` (A·D1) — label every claim as fact / inference / assumption / speculation
- `confidence-calibration` (A·D3) — attach probabilities that match actual hit rates; check against base rates
- `disconfirmation-search` (A·D2) — ask "what would change my mind?" and go look for it
- `progress-monitoring` (A·D2) — periodically check plan-vs-progress and replan on divergence
- `effort-calibration` (A·D2) — match depth of analysis to stakes and reversibility
- `decision-journaling` (A·D1) — record forecast, reasoning, and confidence at decision time for later scoring
- `after-action-review` (C·D2) — intended vs actual → why the gap → what to keep, drop, and change

## 13. Ethics & Values — [catalog/13-ethics.md](catalog/13-ethics.md)

Reasoning about should, not just can.

- `ethical-framework-rotation` (A·D3) — evaluate through consequentialist, deontological, and virtue lenses; report divergence
- `stakeholder-impact` (A·D2) — enumerate affected parties and the distribution of harms and benefits
- `value-tradeoffs` (A·D3) — make competing values explicit and price the exchange rate between them

---

## Cross-cutting notes

- **The metacognition category is the kernel.** `cognitive-triage` is the dispatcher that decides which other skills load; `epistemic-tagging`, `confidence-calibration`, and `effort-calibration` are invariants that should run inside *every* composite.
- **Some atomic skills are shared organs.** `assumption-audit`, `steelmanning`, `premortem`, `evidence-triangulation`, and `second-order-scan` each appear as dependencies of 4+ composites — see the dependency graph in [ROADMAP.md](ROADMAP.md).
- **Category placement is primary-home, not exclusive.** `confidence-calibration` lives in metacognition but is load-bearing for forecasting; `steelmanning` lives in analysis but is essential to communication. The `related` links carry these edges.
