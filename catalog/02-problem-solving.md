# 2 · Problem Solving

Getting from stuck to solved.

---

### problem-framing `atomic · D2 · ~500 tok`
Restate a problem several distinct ways before accepting any framing, because the framing chooses the solution space.

- **Why:** Most bad solutions are good solutions to the wrong problem. The initial framing arrives loaded with assumptions about cause, scope, and solution shape; generating rivals is the only defense.
- **Inputs:** a problem as first stated → **Outputs:** 3+ alternative framings, the chosen framing with justification, and what each rejected framing would have optimized for.
- **Activate when:** starting any nontrivial problem; when proposed solutions all feel wrong; when someone hands you a solution disguised as a problem ("we need a dashboard"). **Skip when:** the problem is routine and the framing is settled.
- **Principles:** a "problem" is a gap between a state and a standard — vary both; the presenting problem is often a symptom, a constraint, or someone's preferred solution; who owns the problem changes what the problem is.
- **Procedure:**
  1. Write the problem as given, verbatim.
  2. Identify the embedded assumptions: presumed cause, presumed solution shape, presumed owner, presumed constraint.
  3. Generate rival framings: zoom out (what goal does this serve?), zoom in (which sub-part actually hurts?), invert the actor (whose problem is this really?), question the standard (is the expectation wrong rather than the state?).
  4. For each framing, note what a solution would look like — different solution shapes confirm the framings are truly distinct.
  5. Choose the framing that best matches the underlying goal; record why.
  6. State what evidence would indicate the framing was wrong.
- **Mistakes:** framing-shopping until one yields the answer you wanted; infinite reframing as procrastination; accepting the requester's framing because they're senior.
- **Examples:** "the elevator is too slow" → boredom problem (mirrors) vs throughput problem; "we need more engineers" → scope problem vs process problem; "users can't find the button" → do they even need that action?
- **Related:** [[first-principles]], [[frame-detection]] (the critical-analysis twin), [[five-whys]]. **Prereqs:** none.

---

### mece-decomposition `atomic · D2 · ~450 tok`
Split a problem or space into parts that are Mutually Exclusive and Collectively Exhaustive, so nothing is double-counted or dropped.

- **Why:** Overlapping parts cause double-counting and turf confusion; gaps cause the real cause/option/risk to be invisible. MECE structure turns "analyze this" into a checklist of smaller analyses.
- **Inputs:** a problem, question, or space to be analyzed → **Outputs:** a tree of parts with the cutting principle named at each level.
- **Activate when:** sizing or diagnosing anything ("where is the revenue leak?"); dividing work; structuring a document or investigation. **Skip when:** the space is genuinely non-decomposable or a holistic judgment is the point.
- **Principles:** each split uses exactly one cutting principle (by stage, by segment, by component — never mixed at one level); exhaustive means adding an explicit "other/none of the above" bucket when unsure; the right cut is the one that isolates the variance.
- **Procedure:**
  1. State the whole precisely (what's in scope).
  2. Choose a cutting principle; state it.
  3. Enumerate the parts; verify no overlap (an item can land in only one) and no gap (everything lands somewhere — add "other" if needed).
  4. Recurse into the parts that matter; stop when a part is directly answerable.
  5. Audit: does variance concentrate in one branch? If parts all matter equally, the cut probably isn't pulling weight — try another principle.
- **Mistakes:** mixed cutting principles ("by region, plus the enterprise segment"); fake exhaustiveness (no "other" bucket); decomposing along available data instead of causal structure; MECE theater — a beautiful tree that doesn't isolate anything.
- **Examples:** profit dropped — decompose price × volume × mix by segment; a page is slow — decompose by request phase; enumerate risk categories for a launch.
- **Related:** [[question-decomposition]], [[fermi-estimation]] (uses decomposition for numbers), [[bottleneck-analysis]] (finds which branch binds). **Prereqs:** none.

---

### working-backwards `atomic · D2 · ~450 tok`
Start from a concrete goal state and chain prerequisites backwards until reaching actions available now.

- **Why:** Forward planning from the present explores a huge branching space and drifts toward the comfortable. Backward chaining from the goal prunes to paths that actually terminate at success, and exposes prerequisite gaps early.
- **Inputs:** a well-specified goal state → **Outputs:** a prerequisite chain from goal back to present, with the critical path and earliest-needed actions marked.
- **Activate when:** planning toward a fixed outcome or deadline; the goal is clear but the path isn't; writing the "press release" before the product. **Skip when:** the goal itself is uncertain — use [[problem-framing]] or [[backcasting]] at strategy scale first.
- **Principles:** the goal must be specified concretely enough to test arrival; every step answers "what must be true immediately before this?"; prerequisites that require long lead times dominate the schedule regardless of their size.
- **Procedure:**
  1. Specify the goal state with acceptance criteria — how would you verify you've arrived?
  2. Ask: what must be true immediately before the goal is achievable? List those preconditions.
  3. Recurse on each precondition until reaching states that are true now or actions executable now.
  4. Mark dependencies and lead times; extract the critical path.
  5. Identify the earliest-needed irreversible commitments and long-lead items.
  6. Sanity-check forward: walk the chain front-to-back looking for hidden gaps.
- **Mistakes:** vague goal states ("be successful") that can't anchor the chain; forgetting the forward pass (backward chains can skip enabling conditions that seem obvious); treating the chain as the only path.
- **Examples:** planning a product launch from the launch date backwards; deriving tonight's experiment from the thesis defense; structuring a legal case from the verdict you need.
- **Related:** [[backcasting]] (same move at strategy horizon), [[means-ends-analysis]], [[premortem]] (stress-tests the resulting plan). **Prereqs:** none.

---

### means-ends-analysis `atomic · D3 · ~450 tok`
Repeatedly identify the biggest difference between the current state and the goal state, and apply the operator that best reduces it.

- **Why:** When no complete plan is visible, difference-reduction makes progress anyway — and its explicit bookkeeping (state, differences, operators) prevents the wandering that unstructured effort produces.
- **Inputs:** current state, goal state, and a repertoire of available operators/actions → **Outputs:** a sequence of applied operators, or a precise statement of the blocking difference no operator addresses.
- **Activate when:** navigating toward a goal with no known route (debugging, negotiation gaps, research programs); classic "I know where I want to be but not how." **Skip when:** a known algorithm or full plan exists — just execute it.
- **Principles:** name the differences explicitly, then rank by importance; if the best operator can't apply yet, achieving *its preconditions* becomes the new subgoal (this recursion is the engine); watch for loops — reducing one difference by enlarging another.
- **Procedure:**
  1. Describe current state and goal state in comparable terms.
  2. List the differences; rank by importance.
  3. Select the operator most relevant to the top difference.
  4. If it applies: apply it, reassess state, return to step 2.
  5. If it doesn't apply: set up its preconditions as a subgoal and recurse.
  6. If no operator touches the top difference: report the blocking gap precisely — that statement is itself progress.
  7. Track visited states; if cycling, escalate to [[problem-framing]] or [[constraint-relaxation]].
- **Mistakes:** hill-climbing into dead ends (sometimes the path increases the difference temporarily); grinding on the tractable difference instead of the important one; failing to notice a loop.
- **Examples:** debugging by reducing the diff between expected and actual behavior; closing a negotiation gap term by term; getting a stuck proof to the known-lemma frontier.
- **Related:** [[working-backwards]] (subgoaling is backward chaining), [[bottleneck-analysis]]. **Prereqs:** none.

---

### inversion `atomic · D1 · ~400 tok`
Solve the opposite problem — "how would I guarantee failure?" — and negate the answers.

- **Why:** Failure modes are often more enumerable than success paths, and prevention is often cheaper than achievement. Minds generate hazards more fluently than plans; inversion exploits that asymmetry.
- **Inputs:** a goal or plan → **Outputs:** a ranked list of failure-guaranteeing behaviors and their negations as guardrails.
- **Activate when:** planning anything ("avoid stupidity before seeking brilliance"); success criteria are vague but failure is obvious; a team is stuck generating positive ideas. **Skip when:** avoiding failure isn't the same as succeeding and the constructive path is what's missing.
- **Principles:** ask "what would make this fail *certainly*?" not just "what could go wrong"; the most valuable inversions are behaviors you're already doing; not-failing is necessary but not sufficient — inversion yields guardrails, not strategy.
- **Procedure:**
  1. State the goal.
  2. Invert: "How would I guarantee this fails?" Generate exhaustively — behaviors, omissions, attitudes, structures.
  3. Rank by (a) how reliably each causes failure and (b) how likely you are to actually do it.
  4. Negate the top items into explicit guardrails or stop-doing rules.
  5. Check the current plan against each guardrail; flag violations.
- **Mistakes:** producing only exotic failure modes while missing the mundane ones (neglect, drift, boredom); treating the guardrail list as a strategy; stopping at listing without auditing the current plan against it.
- **Examples:** "how would I make this migration fail?" → no rollback plan, big-bang cutover; "how would I ruin this hire's first month?"; "how do I guarantee nobody reads this report?"
- **Related:** [[premortem]] (inversion applied to a specific plan with a timeline), [[devils-advocacy]]. **Prereqs:** none.

---

### constraint-relaxation `atomic · D2 · ~450 tok`
Remove constraints one at a time to discover which ones actually bind, which are self-imposed, and what solutions live just outside them.

- **Why:** Stuck problems are usually over-constrained, and several of the constraints are assumptions nobody decided. Systematically relaxing them separates the physics from the habit and reveals where the solution space actually opens up.
- **Inputs:** a stuck problem + its constraint list (explicit and implicit) → **Outputs:** classification of each constraint (hard / negotiable / self-imposed), and candidate solutions unlocked by each relaxation.
- **Activate when:** all candidate solutions violate something; the problem feels impossible; costs seem irreducible. **Skip when:** the problem is under-constrained — add constraints instead ([[creative-constraints]]).
- **Principles:** implicit constraints (assumed budget, assumed actor, assumed sequence) bind harder than stated ones because nobody examines them; relax one at a time or you learn nothing about which mattered; "what would you do with infinite X?" is a probe, not a plan — the value is seeing which solutions *almost* survive realistic X.
- **Procedure:**
  1. List all constraints — stated ones, then hunt for implicit ones (who, when, how much, in what order, using what).
  2. For each, ask: who imposed this, and what happens if violated? Classify hard / negotiable / self-imposed.
  3. Relax constraints one at a time; for each relaxation, sketch the best solution now available.
  4. For each attractive unlocked solution, ask: what's the *minimum* relaxation that keeps it viable?
  5. Take negotiable constraints that block good solutions back to their owners.
  6. Report: which constraint binds, and the best solution per feasible relaxation.
- **Mistakes:** relaxing several constraints at once; treating organizational constraints as physical ones (or vice versa); enjoying the fantasy solutions without running step 4.
- **Examples:** "the report must be weekly" — says who?; assuming the fix must avoid downtime when a 5-minute window is available; assuming the team can't hire contractors.
- **Related:** [[first-principles]], [[triz-contradiction]], [[bottleneck-analysis]] (the quantitative sibling). **Prereqs:** none.

---

### five-whys `atomic · D1 · ~400 tok`
Iterate "why did that happen?" past the symptom until reaching a cause at the level of process or design — something fixable that prevents recurrence.

- **Why:** First answers are symptoms; fixes applied at symptom level recur. The discipline is not the number five but refusing to stop at a cause you can't act on or that would recur anyway.
- **Inputs:** an observed failure or defect → **Outputs:** a causal chain from symptom to actionable root cause, with the fix level marked.
- **Activate when:** any recurring problem; postmortems; a fix was applied and the problem came back. **Skip when:** causes are multiple and interacting — use [[root-cause-investigation]] or [[causal-analysis]]; a linear why-chain will oversimplify.
- **Principles:** each "why" must be answered with evidence, not plausibility; stop at a cause that is (a) actionable and (b) would prevent recurrence — that's usually process/design, rarely a person; "human error" is never a root cause, it's a symptom of a system that permits it.
- **Procedure:**
  1. State the problem concretely (what, when, impact).
  2. Ask why it happened; verify the answer with evidence before accepting it.
  3. Repeat on each answer. Branch if a why has multiple verified causes.
  4. Stop when the cause is actionable-and-preventive; typically 3–7 levels.
  5. Check the chain backwards: does each cause, if removed, actually break the chain?
  6. Report the chain and the level at which the fix is being applied — and what recurrence at that level would mean.
- **Mistakes:** accepting plausible-but-unverified whys (chain becomes fiction); stopping at "someone made a mistake"; forcing a single chain when causes branch; ritually asking exactly five.
- **Examples:** outage → deploy bug → missing test → no test requirement for config changes → config treated as "not code"; missed quarter → pipeline gap → lead gen paused → budget process artifact.
- **Related:** [[root-cause-investigation]] (the full composite), [[causal-analysis]], [[problem-framing]]. **Prereqs:** none.

---

### solution-space-mapping `atomic · D2 · ~450 tok`
Enumerate the *families* of possible solutions before evaluating any candidate, so the choice is made from the full space rather than the first basin found.

- **Why:** The first workable idea recruits all subsequent effort ("design fixation"). Mapping families — not just instances — reveals whole regions that were never considered and makes "compared to what?" answerable.
- **Inputs:** a framed problem → **Outputs:** a taxonomy of solution approaches with at least one concrete instance each, plus the axes that distinguish them.
- **Activate when:** about to commit design/architecture/strategy effort to the first plausible approach; someone asks "what are our options?" and the honest answer is "the one I thought of." **Skip when:** the space is genuinely known and small.
- **Principles:** enumerate at the level of *approach*, not variant (three caching strategies are one family); the axes that generate the families matter more than the list; include the null solution (do nothing) and the dissolve solution (make the problem irrelevant).
- **Procedure:**
  1. Identify 2–4 axes along which solutions can differ (where in the pipeline, who acts, prevention vs cure, buy vs build…).
  2. Generate the family grid from the axes; add families the grid missed.
  3. Always include: do-nothing, and dissolve-the-problem.
  4. Populate each family with one concrete representative.
  5. Kill families that violate hard constraints — record why, since constraints change.
  6. Hand the survivors to evaluation ([[weighted-scoring]] / [[decision-analysis]]).
- **Mistakes:** listing five variants of one approach and calling it a space; skipping the do-nothing baseline; evaluating while enumerating (kills generation); losing the rejected-families record.
- **Examples:** reducing churn — product fixes vs pricing vs onboarding vs customer selection vs expectations-setting; treating pain — remove cause vs block signal vs raise tolerance; scaling a service — optimize vs shard vs cache vs shed load vs renegotiate the SLA.
- **Related:** [[morphological-analysis]] (the systematic-combinatorial version), [[divergent-ideation]], [[decision-framing]]. **Prereqs:** [[problem-framing]] recommended.

---

### triz-contradiction `atomic · D4 · ~550 tok`
Resolve "improving X necessarily worsens Y" by refusing the trade-off and applying contradiction-breaking patterns instead.

- **Why:** Trade-off acceptance is the default failure of mature optimization: teams split the difference forever. TRIZ's insight is that inventive solutions usually *dissolve* the contradiction — the trade-off was an artifact of one design assumption.
- **Inputs:** a stated trade-off between two desired properties → **Outputs:** the contradiction stated sharply, candidate dissolutions via standard patterns, and the assumption each dissolution breaks.
- **Activate when:** every option sacrifices something important; a parameter has been pushed to a "fundamental" limit; the team is negotiating percentages of a compromise. **Skip when:** the trade-off is genuinely thermodynamic/information-theoretic — verify before accepting, but they exist.
- **Principles:** state the contradiction at physical/mechanism level, not preference level; most contradictions dissolve by *separation* — the two demands don't actually apply at the same time, place, scale, or condition; someone in another domain has solved this contradiction's abstract form.
- **Procedure:**
  1. State the contradiction: improving property A by mechanism M worsens property B because ⟨causal link⟩.
  2. Interrogate the causal link — the contradiction lives there, not in A or B.
  3. Try separation patterns: in **time** (A when needed, B otherwise), in **space** (A here, B there), in **scale** (A at the part level, B at the system level), on **condition** (A under load, B at rest).
  4. Try transformation patterns: segmentation, asymmetry, do-it-in-advance, turn the harm into a benefit, self-service (the system provides its own fix).
  5. For each candidate, name the design assumption it abandons.
  6. Verify the top candidate against the actual constraint set; report which contradiction remains, if any.
- **Mistakes:** stating the contradiction at preference level ("cheap vs good") where no mechanism is visible; treating separation as a hack rather than the solution; giving up because the first pattern doesn't apply.
- **Examples:** strong-but-light (composites: strength at micro-scale, lightness at macro); secure-but-usable (strict auth only on sensitive actions — separation on condition); fast-release-but-stable (feature flags — separation in space/population).
- **Related:** [[constraint-relaxation]], [[first-principles]], [[concept-blending]]. **Prereqs:** [[causal-analysis]] helps with step 2.

---

### structured-problem-solving `composite · D3 · ~900 tok`
Polya's loop industrialized: understand the problem, plan an approach, execute with monitoring, and review — with explicit gates between phases.

- **Why:** Most failed problem-solving fails at phase discipline: executing before understanding, or never reviewing. The gates catch this. This is the general-purpose composite for any nontrivial problem that doesn't fit a more specific pipeline.
- **Inputs:** any nontrivial problem → **Outputs:** a solution plus a record of the approach, verification, and extracted lessons.
- **Dependencies:** `problem-framing`, `mece-decomposition`, `solution-space-mapping`, `working-backwards`, `sanity-checking`, `progress-monitoring`, `after-action-review`.
- **Activate when:** the problem is nontrivial, unfamiliar, and no specialized composite (diagnosis, decision, research) fits better. **Skip when:** a specialized pipeline exists — route there.
- **Principles:** don't plan until you can restate the problem and its constraints from scratch; don't execute until the plan has a first checkpoint; a solved problem isn't finished until verified and mined for reusable structure.
- **Procedure:**
  1. **Understand:** run `problem-framing`; state givens, constraints, and the acceptance test. *Gate: can you restate the problem cold?*
  2. **Plan:** run `solution-space-mapping`; pick an approach; decompose via `mece-decomposition` or `working-backwards`; define checkpoints. *Gate: does the plan have a first falsifiable milestone?*
  3. **Execute:** work the plan under `progress-monitoring`; on divergence, diagnose whether the plan or the framing is wrong before pushing harder.
  4. **Verify:** run `sanity-checking` against the acceptance test from step 1 — the original one, not a quietly weakened version.
  5. **Review:** run a lightweight `after-action-review`; extract the reusable pattern.
- **Mistakes:** gate-skipping under time pressure (the gates exist *for* time pressure); silently redefining success in step 4; treating step 5 as optional (it's where the compounding happens).
- **Examples:** an ambiguous client engagement; a research question with no obvious method; a gnarly operations problem.
- **Related:** [[decision-analysis]], [[root-cause-investigation]], [[scientific-method]] — the sibling composites for choice-shaped, failure-shaped, and truth-shaped problems.

---

### root-cause-investigation `composite · D3 · ~900 tok`
Evidence-driven investigation of a failure: establish the timeline, generate causal hypotheses, test against evidence, and verify the fix prevents recurrence.

- **Why:** Post-incident narratives converge on the first plausible story, and fixes applied to wrong causes create false confidence plus recurrence. This pipeline forces evidence to lead and story to follow.
- **Inputs:** a failure/incident/defect → **Outputs:** verified causal chain, contributing factors, fix at the preventive level, and recurrence indicators.
- **Dependencies:** `five-whys`, `causal-analysis`, `abductive-inference`, `evidence-triangulation`, `assumption-audit`, `tripwires`.
- **Activate when:** the failure matters enough to prevent, not just patch; the same problem has recurred; multiple factors seem entangled. **Skip when:** cause is obvious and singular — plain `five-whys` suffices.
- **Principles:** timeline before theory; every causal link needs evidence, not plausibility; hunt for *contributing conditions*, not just the trigger — triggers are unpredictable, conditions are fixable; the investigation isn't done until "how will we know if it recurs?" is answered.
- **Procedure:**
  1. Freeze the facts: build a timeline of events with evidence for each entry; separate observation from inference ([[epistemic-tagging]] discipline).
  2. Run `abductive-inference` to generate ≥3 causal stories, including the boring ones.
  3. Test each story against the timeline; discard those the evidence contradicts. Use `evidence-triangulation` on load-bearing facts.
  4. For the surviving story, run `five-whys` down to process/design level; run `causal-analysis` to separate trigger from standing conditions.
  5. Run `assumption-audit` on the conclusion: what would have to be true for this story to be wrong?
  6. Design the fix at the preventive level; set `tripwires` for recurrence.
  7. Report: chain, evidence, fix level, residual risk.
- **Mistakes:** narrative lock-in after step 2; fixing the trigger and leaving the conditions; skipping step 6 so recurrence goes undetected; blame absorbing the analysis ("human error" endpoint).
- **Examples:** production outage postmortem; a clinical adverse event review; why a good candidate declined the offer; why the quarterly forecast missed by 30%.
- **Related:** [[differential-diagnosis]] (when the failure is ongoing and you must find the cause to stop it), [[after-action-review]] (lighter, for non-failure learning).

---

### differential-diagnosis `composite · D4 · ~950 tok`
Enumerate the possible causes of an observed condition, order them by probability and severity, and run the tests that discriminate fastest — medicine's algorithm, generalized.

- **Why:** Debugging-by-hunch tests hypotheses in the order they came to mind. Ordering by prior × severity × test-cost, and choosing tests for *discrimination power*, finds the cause faster and never silently drops the dangerous possibility.
- **Inputs:** an ongoing abnormal condition (system, organism, organization) → **Outputs:** a ranked differential, test results, the confirmed cause (or narrowed set), and explicitly ruled-out dangerous causes.
- **Dependencies:** `abductive-inference`, `bayesian-updating`, `reference-class-forecasting` (priors), `sanity-checking`, `disconfirmation-search`.
- **Activate when:** something is actively wrong, multiple causes are possible, and testing is costly — debugging, medical-style triage, churn spikes, machine faults. **Skip when:** one cause is near-certain, or the condition is historical (use [[root-cause-investigation]]).
- **Principles:** common things are common — priors come from base rates, not memorability; "can't-miss" causes get tested early even when improbable, because the cost of missing them dominates; the best next test is the one whose result most reshapes the ranking per unit cost; diagnosis is iterative — each result re-ranks the list.
- **Procedure:**
  1. Characterize the condition precisely: what's abnormal, since when, what changed around onset, what's *normal* (pertinent negatives).
  2. Generate the differential via `abductive-inference`: plausible causes + the dangerous ones regardless of plausibility.
  3. Assign priors from base rates (`reference-class-forecasting`); tag each cause with severity-if-missed.
  4. Order the worklist by prior, promoted by severity and demoted by test cost.
  5. Choose the test with the best discrimination-per-cost — prefer tests that split the list, not tests that confirm the favorite.
  6. Update the ranking on each result via `bayesian-updating`. Prune what's ruled out; add what new evidence suggests.
  7. Stop when one cause explains all findings *and* the can't-miss causes are affirmatively excluded. Run `disconfirmation-search` on the final answer.
  8. Report: cause, confidence, what was ruled out, and what re-presentation would reopen the case.
- **Mistakes:** anchoring on the first hypothesis and ordering tests to confirm it; satisfaction-of-search (stopping at one cause when two are present); never writing the differential down (the unlisted cause can't be found); ignoring pertinent negatives.
- **Examples:** intermittent API latency (differential: GC, noisy neighbor, connection pool, DNS, retry storm); patient fatigue workup; sudden CAC increase (tracking bug vs mix shift vs competitor vs seasonality); an engine misfire.
- **Related:** [[root-cause-investigation]] (post-hoc sibling), [[competing-hypotheses]] (same logic for beliefs instead of live systems).
