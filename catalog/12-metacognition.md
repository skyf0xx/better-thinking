# 12 · Metacognition

Thinking about the thinking itself. The kernel layer that routes and corrects all others.

---

### cognitive-triage `atomic · D3 · ~550 tok`
Classify an incoming task by its shape and stakes, and select which skills to deploy at what depth — the dispatcher that decides how much thinking machinery a task deserves.

- **Why:** Applying full analytical machinery to a trivial task wastes effort; applying none to a consequential one is negligent. A fast, explicit classification step routes effort proportionally before any substantive work begins.
- **Inputs:** an incoming task or question → **Outputs:** a task classification (shape + stakes + reversibility) and a selected set of skills/depth to apply.
- **Activate when:** always, as the first move on any nontrivial task — this is the entry point other skills get dispatched from. **Skip when:** never; scale its own depth instead — triage itself should take seconds for small tasks.
- **Principles:** classify by shape first (is this a decision, a diagnosis, a research question, a creative task, a communication task?) — shape determines which skill family is relevant at all; classify by stakes and reversibility second ([[reversibility-classification]] as input) — this determines depth; a task can be routine in domain but high-stakes in consequence (a "simple" email that will be read by the board) — don't classify by surface topic alone; re-triage if the task's shape turns out different mid-work.
- **Procedure:**
  1. Identify the task's shape: decision, diagnosis/investigation, research/evidence question, creative generation, communication, learning, negotiation/collaboration, or some combination.
  2. Identify stakes and reversibility — quick gut check or explicit [[reversibility-classification]] if unclear.
  3. Match shape + stakes to the relevant skill family and depth (a quick decision needs [[satisficing-thresholds]], not full [[decision-analysis]]; a high-stakes one needs the reverse).
  4. Note any cross-cutting needs — most nontrivial tasks benefit from at least [[epistemic-tagging]] and [[bias-audit]] regardless of shape.
  5. Proceed with the selected skills; re-triage explicitly if the task's actual shape reveals itself to be different once underway.
- **Mistakes:** applying a heavyweight composite to a low-stakes task out of habit or thoroughness-signaling; skipping triage on tasks that look routine but carry hidden stakes; triaging once and never revisiting even when the task's true shape becomes clear mid-work.
- **Examples:** routing "should we do X or Y" to [[decision-analysis]] but "which font should I use" to nothing; recognizing a "quick question" is actually a diagnosis needing [[differential-diagnosis]]; triaging a casual-sounding request that turns out to feed a board decision.
- **Related:** [[effort-calibration]], [[reversibility-classification]], every composite skill (this is their entry point). **Prereqs:** none.

---

### bias-audit `atomic · D3 · ~550 tok`
Run a targeted checklist of the specific cognitive biases a given task shape invites, rather than a generic "watch out for bias" gesture.

- **Why:** Generic bias-awareness rarely changes behavior because it isn't targeted — different task shapes invite different specific biases, and naming the right one for the situation is what actually catches it. A targeted checklist beats a vague caution.
- **Inputs:** a task, judgment, or conclusion + its shape (from [[cognitive-triage]]) → **Outputs:** the specific biases most likely to be operating, flagged with the concrete symptom to check for.
- **Activate when:** a conclusion arrived too easily or too quickly; high-stakes judgments; whenever [[cognitive-triage]] flags a task shape with known bias risks (forecasting → overconfidence; evaluating your own plan → optimism bias; hiring → affinity bias). **Skip when:** the task is too low-stakes to warrant the check.
- **Principles:** match the bias to the task shape — forecasting invites overconfidence and planning fallacy; evaluating evidence for a preferred conclusion invites confirmation bias; judging people invites halo effects and affinity bias; recent, vivid events invite availability bias in probability judgments; a bias check needs a concrete behavioral symptom to test for, not just the bias's name ("am I anchoring?" is unfalsifiable — "did I generate an independent estimate before seeing theirs?" is checkable).
- **Procedure:**
  1. Identify the task shape (forecast, evaluation, decision, judgment-of-person, negotiation, etc.).
  2. Select the 2–3 biases most characteristic of that shape (not a generic full list every time).
  3. For each, state the concrete, checkable symptom: what would this bias look like happening right now, specifically, in this conclusion?
  4. Check the actual reasoning against that symptom.
  5. Where a bias is plausibly present, apply the specific counter — [[disconfirmation-search]] for confirmation bias, [[reference-class-forecasting]] for planning fallacy/overconfidence, [[steelmanning]] for motivated reasoning.
  6. Report what was checked and what, if anything, was corrected.
- **Mistakes:** running a generic, unfocused "am I biased?" check that doesn't target anything specific; checking for bias only in conclusions you already doubt, not ones that feel comfortable (that's exactly where bias hides best); treating a bias-audit as a formality without applying an actual counter-technique when something is found.
- **Examples:** checking a project timeline for planning fallacy before committing to it; checking a hiring decision for affinity bias; checking a "the data clearly shows" claim for confirmation bias.
- **Related:** [[disconfirmation-search]], [[devils-advocacy]], [[confidence-calibration]]. **Prereqs:** [[cognitive-triage]] recommended to select the right biases to check.

---

### epistemic-tagging `atomic · D1 · ~400 tok`
Label every claim in a piece of reasoning as fact, inference, assumption, or speculation — making the reasoning's actual evidential structure visible.

- **Why:** Prose blends established fact with plausible inference with pure guesswork seamlessly, and readers (including the author, later) lose track of which is which. Explicit tagging prevents a speculation from quietly hardening into a treated-as-fact premise three steps later.
- **Inputs:** a piece of reasoning, analysis, or written conclusion → **Outputs:** the same content with each claim tagged by its epistemic status, and any status upgrades/downgrades flagged.
- **Activate when:** writing or reviewing any analysis where the confidence level of different claims matters; a conclusion needs its foundation audited. **Skip when:** the content is uniformly one type (all directly observed fact, e.g.) — tagging adds no information there.
- **Principles:** fact = directly verified/verifiable; inference = follows from facts via stated reasoning; assumption = accepted as a premise but not independently verified; speculation = a guess offered with low confidence — these four categories should stay visibly distinct throughout a chain of reasoning; a claim's tag can and should change as it's used elsewhere — an assumption in one paragraph shouldn't silently become a fact by the conclusion.
- **Procedure:**
  1. Go through the claims in the reasoning one at a time.
  2. Tag each: fact / inference / assumption / speculation.
  3. For inferences, check the reasoning connecting them to their source facts actually holds ([[deductive-validation]] if needed).
  4. Check for status drift: does an assumption or speculation get treated as settled fact later in the same piece?
  5. Where drift is found, either downgrade the later claim back to its honest status, or explicitly upgrade it with the evidence that would justify the promotion.
  6. Report the conclusion's actual epistemic foundation — how much of it rests on verified fact vs assumption.
- **Mistakes:** tagging once at the start and letting status silently drift through the rest of the document; treating "assumption" as a lesser or embarrassing tag to avoid using, rather than useful information; tagging so granularly that the exercise obscures more than it clarifies (tag at the claim level, not the word level).
- **Examples:** auditing an investment thesis for which parts are verified vs assumed; a legal memo separating established fact from inference from the client's account; a forecast report distinguishing data-backed claims from judgment calls.
- **Related:** [[assumption-audit]], [[critical-reading]], [[confidence-calibration]]. **Prereqs:** none.

---

### confidence-calibration `atomic · D3 · ~500 tok`
Attach probabilities to beliefs that match their actual hit rate over time, checked against base rates and scored against outcomes.

- **Why:** Unaided confidence is systematically miscalibrated — usually overconfident on specific predictions, sometimes underconfident on well-understood domains. Calibration is a trainable skill, but only if predictions are stated numerically and scored against what actually happens.
- **Inputs:** a belief or forecast → **Outputs:** a numeric confidence level (not a verbal hedge), ideally logged for future scoring against the actual outcome.
- **Activate when:** stating any forecast or belief that matters enough to act on; after [[structured-forecasting]] or [[decision-analysis]] produces a conclusion needing a confidence label; periodically, to review past calibration. **Skip when:** the claim is a certainty or near-certainty where numeric hedging adds noise (a settled fact).
- **Principles:** state confidence as a number or range, not a word ("likely," "probably") — words can't be scored later and different people read the same word as wildly different probabilities; calibration means: among all things you said "80% confident" about, roughly 80% should actually happen — not that any single 80% call felt right in hindsight; check against a base rate before trusting a gut confidence level ([[reference-class-forecasting]]); track a record over time — calibration is a property of a *set* of predictions, not any one prediction.
- **Procedure:**
  1. State the belief/forecast precisely enough to be scored later (a specific, resolvable outcome).
  2. Assign a numeric probability, anchored first to a base rate if one exists.
  3. Sanity-check: would you take a bet at these odds? If the stated number and the bet you'd actually take diverge, the stated number is performative, not calibrated — revise it.
  4. Log the prediction (pairs with [[decision-journaling]]) for later scoring.
  5. Periodically, score past predictions: of the ones called "70% confident," did roughly 70% happen? Adjust future confidence-setting habits based on the pattern (systematically over- or under-confident).
- **Mistakes:** using vague verbal hedges instead of numbers, making the claim unfalsifiable and unscoreable; treating one correct high-confidence call as proof of good calibration (it's the long-run hit rate across many calls that matters, not any single one); never closing the loop — stating confidence but never checking it against outcomes, so no actual calibration learning occurs.
- **Examples:** a forecaster's track record scored via Brier score; an engineer's "I'm 90% sure this will fix it" checked against how often that's been true; a doctor's diagnostic confidence calibrated against outcomes over a career.
- **Related:** [[reference-class-forecasting]], [[decision-journaling]], [[structured-forecasting]]. **Prereqs:** none, but improves with [[decision-journaling]] as a feedback loop.

---

### disconfirmation-search `atomic · D2 · ~450 tok`
Ask "what would change my mind?" and then actually go look for it, rather than only seeking evidence that confirms the current belief.

- **Why:** The mind is fluent at generating supporting evidence for whatever it already believes and sluggish at generating counter-evidence unprompted. Explicitly asking what would disconfirm the belief — and then searching for exactly that — is the single most reliable counter to confirmation bias.
- **Inputs:** a belief or conclusion held with some confidence → **Outputs:** the specific evidence that would change the belief, and the result of an actual search for it (found / not found / inconclusive).
- **Activate when:** a conclusion feels settled or obvious; before committing to a belief-driven action; as the final step of most reasoning composites ([[scientific-method]], [[competing-hypotheses]], [[differential-diagnosis]]). **Skip when:** the belief is genuinely inconsequential.
- **Principles:** the question "what would change my mind?" must produce a *specific, checkable* answer — "if I saw evidence against it" is not specific enough to search for; if you can't articulate anything that would change your mind, the belief isn't actually evidence-based — it's a commitment, and that's worth knowing; actually go look — asking the question without searching captures none of the benefit.
- **Procedure:**
  1. State the belief precisely.
  2. Ask: what specific observation, if it existed, would make me doubt or abandon this belief?
  3. If nothing comes to mind, that itself is the finding — flag the belief as unfalsifiable-as-currently-held and examine why.
  4. If a specific disconfirming observation is named, actively search for it — don't just note it hypothetically.
  5. If found: update the belief accordingly ([[bayesian-updating]]).
  6. If genuinely not found after a real search: report increased (not absolute) confidence, since the search itself is evidence.
- **Mistakes:** asking the question rhetorically without actually searching; naming a disconfirming condition so extreme or unlikely that the search is meaningless theater; treating "I looked and didn't find it" as proof rather than as evidence that should update confidence proportionally to how hard you looked.
- **Examples:** checking whether a hiring "gut read" would survive looking at the candidate's actual track record; testing a technical root-cause theory against the one log line that would disprove it; a forecaster asking what news would make them abandon their current prediction.
- **Related:** [[bias-audit]], [[bayesian-updating]], [[scientific-method]]. **Prereqs:** none.

---

### progress-monitoring `atomic · D2 · ~450 tok`
Periodically compare actual progress against the plan, and explicitly decide whether to continue, adjust, or replan — rather than drifting on autopilot.

- **Why:** Plans decay as they meet reality, but without a deliberate checkpoint, the drift between plan and actual progress accumulates unnoticed until it's a crisis. Scheduled, explicit comparison catches divergence while it's still cheap to correct.
- **Inputs:** an in-progress plan with a defined goal → **Outputs:** a progress-vs-plan comparison at each checkpoint, and an explicit continue/adjust/replan decision.
- **Activate when:** any plan or project extends over multiple work sessions or a meaningful duration; especially after [[decision-analysis]] or [[ooda-loop]] commits to a course of action. **Skip when:** the task is short enough to complete in one sitting with no meaningful checkpoint.
- **Principles:** set checkpoints in advance, tied to milestones or time, not to "whenever it feels necessary" (which under time pressure becomes never); compare against the *original* plan, not a silently-updated version of it — otherwise drift becomes invisible by definition; divergence is information, not failure — the checkpoint's job is to surface it early, when correction is cheap.
- **Procedure:**
  1. At plan commitment, set explicit checkpoints (time-based or milestone-based) — this pairs with [[tripwires]] from the original plan.
  2. At each checkpoint, compare actual state against the original plan's expected state at this point.
  3. Diagnose any gap: execution issue, or was the plan's assumption wrong ([[assumption-audit]] on the original plan)?
  4. Decide explicitly: continue as planned, adjust the plan, or trigger a fuller replan/reframing.
  5. If continuing, note the checkpoint passed cleanly; if adjusting, update the plan (and future checkpoints) explicitly rather than silently.
  6. Never skip a scheduled checkpoint under the pressure that's exactly why it was scheduled.
- **Mistakes:** skipping checkpoints when busy (the precise moment they're most needed); comparing against a plan that's been silently revised in your head rather than the original commitment, hiding real drift; treating every divergence as reason to panic-replan instead of first diagnosing whether it's a minor execution issue.
- **Examples:** a project's weekly milestone check against the original timeline; a personal goal's monthly review; an [[ooda-loop]]'s repeated cycle applied to a slower-moving plan.
- **Related:** [[tripwires]], [[after-action-review]], [[ooda-loop]]. **Prereqs:** an existing plan with milestones.

---

### effort-calibration `atomic · D2 · ~450 tok`
Match the depth of analysis applied to a task's actual stakes and reversibility, resisting both under-thinking high-stakes calls and over-analyzing trivial ones.

- **Why:** Effort allocation is rarely deliberate — it tracks how interesting or comfortable a task is, not its actual importance. Explicitly calibrating effort to stakes prevents both costly negligence and wasted analysis-paralysis.
- **Inputs:** a task + its stakes/reversibility assessment → **Outputs:** an explicit effort level (quick call / moderate analysis / full process) matched to that assessment.
- **Activate when:** paired with [[cognitive-triage]] on every nontrivial task; noticing you're either speeding through something important or laboring over something trivial. **Skip when:** never — this runs alongside triage as a standing check.
- **Principles:** stakes and reversibility ([[reversibility-classification]]) — not interest level, not social pressure, not how the task was phrased — should set the effort dial; the cost of over-analysis (time, opportunity cost, decision fatigue on later choices) is real and should be weighed, not treated as free; when genuinely unsure how much a task matters, that uncertainty itself is informative — err toward a bit more care until it resolves.
- **Procedure:**
  1. Assess stakes: what's the cost of a wrong call here?
  2. Assess reversibility: how expensive is it to correct later if wrong?
  3. Set the effort level explicitly: quick heuristic call (low stakes or easily reversible), moderate structured analysis (meaningful stakes, correctable), full rigorous process (high stakes, hard to reverse).
  4. Notice and correct mismatches: are you spending senior-decision-level effort on a reversible triviality, or dashing through something that deserves real analysis?
  5. Proceed at the calibrated level, and don't second-guess the choice mid-task unless new information changes the stakes assessment.
- **Mistakes:** letting how *interesting* a problem is (rather than its stakes) set the effort level; treating all decisions as equally deserving of full rigor (burns out the capacity to actually do full rigor where it matters); under-investing in a high-stakes call because it's socially awkward to take it seriously.
- **Examples:** spending five minutes on a reversible tool choice instead of a week; giving a one-way-door hiring decision the full process instead of a snap read; not over-processing a cheap, quickly-correctable experiment.
- **Related:** [[reversibility-classification]], [[cognitive-triage]], [[satisficing-thresholds]]. **Prereqs:** none.

---

### decision-journaling `atomic · D1 · ~400 tok`
Record the forecast, reasoning, and confidence at the moment of a decision — before the outcome is known — so it can be honestly scored later.

- **Why:** Hindsight bias silently rewrites remembered confidence and reasoning to match however things turned out. A contemporaneous record, written before the outcome, is the only reliable way to later assess whether the decision process — not just the result — was actually good.
- **Inputs:** a decision being made now → **Outputs:** a timestamped record of the decision, the reasoning, the alternatives considered, and the confidence level — written before the outcome is known.
- **Activate when:** any consequential decision, especially ones where you'll be tempted to judge yourself later by the outcome rather than the process; paired with the final step of [[decision-analysis]] and [[structured-forecasting]]. **Skip when:** the decision is too trivial to be worth revisiting.
- **Principles:** write it *before* the outcome is known — a journal entry written after the fact is worthless for this purpose, however honest the intent; record the reasoning and confidence, not just the choice — the goal is to later evaluate whether the *process* was sound, independent of how it turned out; a good decision can have a bad outcome and vice versa — the journal is what lets you tell the difference later instead of conflating them.
- **Procedure:**
  1. At the moment of deciding, write: the decision, the key alternatives considered and why they lost, the main uncertainty, and a numeric confidence level.
  2. Note what would change your mind (pairs with [[disconfirmation-search]]) and any [[tripwires]] set.
  3. Store it somewhere it will actually be revisited — not buried and forgotten.
  4. When the outcome becomes known, compare it against the original entry — not your current memory of what you thought.
  5. Score separately: was the *process* sound given what was knowable then, and was the *confidence* well-calibrated (feeds [[confidence-calibration]])?
- **Mistakes:** writing the entry after the outcome is already known or suspected (defeats the entire purpose); recording only the decision, not the reasoning and confidence, which makes later process-evaluation impossible; judging past decisions purely by outcome instead of using the journal to separate process quality from luck.
- **Examples:** an investor's pre-trade journal; a hiring manager's pre-decision notes on a candidate; a product team's pre-launch prediction log.
- **Related:** [[confidence-calibration]], [[counterfactual-reasoning]], [[after-action-review]]. **Prereqs:** none.

---

### after-action-review `composite · D2 · ~800 tok`
Compare intended outcome against actual outcome, diagnose the gap, and extract what to keep, drop, and change — a lightweight, general-purpose learning loop for any completed effort.

- **Why:** Experience alone doesn't produce learning — it requires an explicit comparison between what was intended and what happened, since memory alone tends to smooth over the gap or misattribute its cause. A short structured review captures the lesson while it's still fresh and specific.
- **Inputs:** a completed action, decision, or effort with an original intention → **Outputs:** a documented comparison of intended vs actual, the diagnosed cause of any gap, and specific keep/drop/change items.
- **Dependencies:** `counterfactual-reasoning`, `decision-journaling` (if available), `epistemic-tagging`.
- **Activate when:** after any effort worth learning from — not only failures, successes deserve review too (to learn why, not just assume it'll repeat); lighter-weight than [[root-cause-investigation]], suited to routine use. **Skip when:** the effort was too trivial to yield a reusable lesson.
- **Principles:** compare against the *original* intention (use `decision-journaling` if it exists) — not a retroactively adjusted version of what you meant to do, which erases the actual lesson; review successes as rigorously as failures — a success with the wrong causal story teaches the wrong lesson for next time; the output must be specific and actionable (keep/drop/change), not a general mood about how it went.
- **Procedure:**
  1. State the original intention/plan, ideally from a contemporaneous source (`decision-journaling`) rather than memory.
  2. State what actually happened, factually (`epistemic-tagging` to separate fact from interpretation).
  3. Identify the gap, if any, between intended and actual.
  4. Diagnose the cause: was the plan wrong, the execution wrong, or was it an unforeseeable factor? Use `counterfactual-reasoning` — would a different choice plausibly have changed the outcome, or was this outcome likely regardless?
  5. For successes, explicitly check the causal story isn't just a comfortable narrative — did the plan actually cause the good outcome, or did it succeed despite the plan for unrelated reasons?
  6. Extract specific items: what to keep doing, what to stop doing, what to change — each tied to the diagnosed cause, not a vague impression.
- **Mistakes:** reviewing only failures and skipping successes, which teaches nothing about why the good outcomes actually happened; comparing against a memory of the plan that's already drifted toward matching the outcome; producing vague takeaways ("communicate better") instead of specific, actionable changes.
- **Examples:** reviewing a completed project against its original charter; a personal review of a negotiation outcome; reviewing why a successful launch actually succeeded, to know what to repeat.
- **Related:** [[retrospective-facilitation]] (group version), [[decision-journaling]] (the ideal input), [[root-cause-investigation]] (heavier version for serious failures).
