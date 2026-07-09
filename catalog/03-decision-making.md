# 3 · Decision Making

Choosing well under constraints and uncertainty.

---

### decision-framing `atomic · D2 · ~500 tok`
Define what is actually being decided — options, decider, criteria, stakes, and deadline — before any evaluation begins.

- **Why:** Most decision failures are framing failures: a binary presented where options are many, criteria discovered mid-argument, nobody knowing who decides. Ten minutes of framing prevents most of it.
- **Inputs:** a choice situation, however vague → **Outputs:** a decision statement: the question, the option set, the decider, the criteria, the information deadline, and what happens by default if no decision is made.
- **Activate when:** any nontrivial choice, especially group ones; a debate is circling; someone asks "what do you think?" about a decision that hasn't been framed. **Skip when:** trivial stakes — see [[reversibility-classification]] first.
- **Principles:** the default (no-decision) path is always an option and often the hidden favorite; binary choices are usually a failure of option generation; "who decides" and "who is consulted" must be distinct and named; a decision without a deadline is a discussion.
- **Procedure:**
  1. Write the decision as a question with a deadline.
  2. Name the decider, the consulted, and the informed.
  3. State the default: what happens if no decision is made by the deadline?
  4. List the options; if fewer than three, generate more ([[solution-space-mapping]]).
  5. Elicit criteria *before* comparing options; note whose criteria they are.
  6. State the stakes and reversibility ([[reversibility-classification]]) to size the process.
  7. Publish the frame; proceed to evaluation.
- **Mistakes:** evaluating during framing (criteria get reverse-engineered from a favorite); leaving the default path unexamined; framing the question so one option is the only sane answer ([[frame-detection]] on yourself).
- **Examples:** "should we rewrite the service?" reframed with the real option set (rewrite / strangle / patch / freeze); a family relocation decision; a hiring committee that discovers members were optimizing different criteria.
- **Related:** [[problem-framing]] (upstream), [[decision-analysis]] (consumes this frame), [[expectation-contracting]]. **Prereqs:** none.

---

### weighted-scoring `atomic · D2 · ~450 tok`
Score options against explicitly weighted criteria, using the matrix to expose disagreement and sensitivity — not to outsource the decision.

- **Why:** Unstructured comparison lets one vivid attribute dominate silently. The matrix forces every criterion into the open and shows *why* an option wins — and where a judgment flip would change the answer.
- **Inputs:** ≥2 options + elicited criteria → **Outputs:** a scored matrix, the winner, and a sensitivity note (which weight/score changes flip the result).
- **Activate when:** multi-attribute choices among comparable options (vendors, candidates, designs, sites). **Skip when:** one criterion is truly lexicographic (a hard constraint — filter first, don't weight); or options differ in kind, not degree.
- **Principles:** hard constraints filter before scoring — weighting a dealbreaker at 40% is how dealbreakers sneak through; weights encode values and belong to the decider, not the analyst; the matrix's job is to localize disagreement to a specific cell.
- **Procedure:**
  1. Filter options through hard constraints first.
  2. List criteria; merge overlapping ones (double-listing is double-weighting).
  3. Set weights before scoring any option; have the decider own them.
  4. Score option-by-criterion with a defined scale; note evidence quality per cell.
  5. Compute totals — then immediately run sensitivity: which single cell or weight change flips the winner?
  6. If the result offends intuition, locate the disagreement in a specific cell — either the matrix is missing a criterion or the intuition is wrong. Resolve explicitly.
  7. Report winner, margin, and the flip conditions.
- **Mistakes:** reverse-engineering weights to crown the favorite; correlated criteria double-counting a theme; false precision (scores of 7.5 vs 8 on gut feel); ignoring the intuition mismatch instead of mining it.
- **Examples:** vendor selection; choosing between job offers; prioritizing which market to enter; apartment hunting.
- **Related:** [[decision-analysis]], [[satisficing-thresholds]] (the cheaper alternative), [[sensitivity-analysis]]. **Prereqs:** [[decision-framing]].

---

### cost-benefit `atomic · D2 · ~450 tok`
Tally the full costs and benefits of an action — including opportunity cost, hidden costs, and to-whom-they-accrue — before judging it worthwhile.

- **Why:** Untrained tallies count visible, near-term, own-side effects and miss opportunity cost, maintenance burden, and externalities — systematically flattering action over inaction.
- **Inputs:** a proposed action → **Outputs:** a ledger of costs and benefits with timing, bearer, and confidence per entry; a net judgment with the dominant uncertainties flagged.
- **Activate when:** justifying or challenging any investment of money, time, or attention. **Skip when:** stakes are trivial ([[effort-calibration]]) or the decision is dominated by one factor.
- **Principles:** the opportunity cost — best foregone alternative — is a real cost and is always missing from the first draft; count ongoing costs (maintenance, attention, complexity), not just acquisition; note *who* bears each cost — a net-positive action can be a transfer from someone who wasn't consulted; sunk costs are not costs.
- **Procedure:**
  1. State the action and the comparison baseline (usually: best alternative use of the resources, not "nothing").
  2. List benefits with timing and confidence.
  3. List costs: direct, ongoing, attention/complexity, and risk-bearing.
  4. Add the opportunity cost explicitly as a line item.
  5. Mark the bearer of each entry; flag asymmetries (benefits to us, costs to them).
  6. Net it out; state which 1–2 uncertain entries dominate the conclusion.
- **Mistakes:** baseline = "do nothing" when a live alternative exists; ignoring maintenance tails; counting sunk costs; treating hard-to-quantify entries as zero.
- **Examples:** whether to build the internal tool; whether a meeting series earns its collective hours; whether a regulation's compliance burden matches its protection; adopting a dependency.
- **Related:** [[expected-value]] (when entries are probabilistic), [[second-order-scan]] (finds the hidden entries), [[prioritization-triage]]. **Prereqs:** none.

---

### reversibility-classification `atomic · D1 · ~350 tok`
Classify a decision as a one-way or two-way door, and size the decision process accordingly.

- **Why:** The most common process error is symmetric treatment: agonizing over reversible choices and rushing irreversible ones. This 60-second classification fixes the allocation.
- **Inputs:** a pending decision → **Outputs:** a reversibility grade, the real cost-to-reverse, and a recommended process weight (decide now vs full analysis).
- **Activate when:** first contact with any decision — this runs *before* other decision skills. **Skip when:** never; it's the router.
- **Principles:** reversibility is a spectrum priced in cost-to-undo (money, time, trust, optionality), not a binary; decisions look more irreversible than they are (commitments can be renegotiated) *and* some look reversible but aren't (trust, announcements, data leaks); for two-way doors, speed beats analysis — deciding fast and correcting is cheaper than deciding perfectly.
- **Procedure:**
  1. Ask: if this turns out wrong, what exactly does undoing it cost — and is anything unrecoverable (time, trust, legal exposure, compounding lock-in)?
  2. Grade: cheap-reversible / costly-reversible / effectively irreversible.
  3. Check for hidden irreversibles in a "reversible" choice: public commitments, data exposure, precedent-setting.
  4. Match process: cheap-reversible → decide now with defaults and a review date; costly → lightweight analysis; irreversible → full [[decision-analysis]] + [[premortem]].
  5. Record the grade so escalation/de-escalation is legible to others.
- **Mistakes:** prestige-driven overprocessing of reversible calls; missing the trust/precedent component of "reversible" actions; treating hiring, pricing, and public statements as two-way doors.
- **Examples:** trying a new standup format (cheap-reversible: just do it); choosing a database (costly-reversible: lightweight analysis); a public pricing change or layoff (irreversible-adjacent: full process).
- **Related:** [[effort-calibration]] (the general form), [[decision-framing]]. **Prereqs:** none.

---

### premortem `atomic · D2 · ~450 tok`
Assume the plan has already failed, then work backwards to explain why — converting hindsight's clarity into foresight.

- **Why:** Prospective critique ("what could go wrong?") is socially costly and cognitively weak; retrospective explanation is fluent and safe. The temporal trick — *it failed; why?* — unlocks failure modes that direct questioning never surfaces.
- **Inputs:** a concrete plan with a timeline → **Outputs:** a ranked list of failure causes with early-warning signs and mitigations, plus plan modifications.
- **Activate when:** before committing to any significant plan; when a team is uniformly optimistic; before irreversible steps. **Skip when:** the plan is a cheap experiment whose failure *is* the information.
- **Principles:** phrase in past tense — "it failed" not "it might fail"; generate independently before discussing (group discussion collapses diversity); prioritize failures that are both likely and preventable; the output is plan changes, not a worry list.
- **Procedure:**
  1. Set the scene: it's ⟨date after the plan's horizon⟩; the plan failed badly.
  2. Independently generate reasons it failed — internal (our execution, our assumptions) and external (environment, adversaries, luck). Push past the first five; the interesting ones come late.
  3. Consolidate; rank by likelihood × preventability.
  4. For the top items: identify the earliest observable warning sign, and the mitigation or plan change.
  5. Install the warning signs as [[tripwires]]; amend the plan; record what was deliberately accepted as residual risk.
- **Mistakes:** running it as generic risk brainstorming (losing the past-tense trick); only listing external causes (comfortable) and no self-inflicted ones; generating without changing the plan; doing it after commitment as theater.
- **Examples:** product launch premortem surfacing "we never defined success, so we declared victory and moved on"; a migration premortem catching the rollback gap; a research project premortem catching the unvalidated data dependency.
- **Related:** [[inversion]] (the general move), [[tripwires]], [[red-teaming]] (adversarial big sibling). **Prereqs:** a concrete plan.

---

### second-order-scan `atomic · D3 · ~450 tok`
Trace the consequences of consequences — asking "and then what?" through at least two rounds of reactions and adaptations.

- **Why:** First-order effects are the ones designed; second-order effects are the ones that actually determine outcomes, because people, markets, and systems *adapt* to the intervention. Most policy and incentive failures are unexamined second-order effects.
- **Inputs:** a proposed action or change → **Outputs:** a consequence tree ≥2 levels deep, with adaptation-driven effects flagged and net assessment revised.
- **Activate when:** changing incentives, rules, prices, metrics, or interfaces that people/systems will respond to. **Skip when:** the affected system can't adapt (inanimate, one-shot).
- **Principles:** ask "who reacts to this, and what do they do?" — effects on *behavior* dominate effects on *state*; every metric becomes a target and stops measuring (Goodhart) — run the scan on any new metric; delayed effects escape attention precisely because of the delay; some second-order effects reverse the first-order sign.
- **Procedure:**
  1. State the action and its intended (first-order) effect.
  2. List the parties and systems affected, including non-obvious ones (competitors, adjacent teams, future selves).
  3. For each: how do they *adapt* once the change lands? What's their best response?
  4. Trace those adaptations' effects — this is the second order. Repeat once more for the big branches.
  5. Flag effects that are delayed, compounding, or sign-reversing.
  6. Revise the net assessment; where uncertainty is high, propose a reversible probe instead.
- **Mistakes:** stopping at effects-on-state and skipping effects-on-behavior; assuming adaptations are edge cases rather than the main event; scanning so exhaustively that no action survives (pair with [[effort-calibration]]).
- **Examples:** paying per bug fixed → bug farming; free returns → changed buying behavior → margin collapse; a new lane → induced demand; publishing team metrics → metric gaming plus morale effects.
- **Related:** [[systems-mapping]] (formalizes the structure), [[game-theoretic-analysis]] (when adapters are strategic), [[chestertons-fence]]. **Prereqs:** none.

---

### satisficing-thresholds `atomic · D2 · ~400 tok`
Define "good enough" criteria in advance, then take the first option that clears them — bounding search cost on decisions that don't reward optimization.

- **Why:** Optimization has costs — time, option paralysis, post-choice regret — that routinely exceed the value gap between "best" and "clearly sufficient." Pre-committed thresholds convert an unbounded search into a bounded one.
- **Inputs:** a choice with a stream/pool of options and nontrivial search cost → **Outputs:** explicit threshold criteria, a search budget, and a stopping rule.
- **Activate when:** many adequate options exist and differences among the adequate are small or unknowable (tools, venues, phrasings, most purchases); analysis is becoming procrastination. **Skip when:** outcomes are heavy-tailed and choice quality compounds (hires, partners, architectures) — there, optimization pays.
- **Principles:** set thresholds *before* seeing options, or the favorite will set them; the threshold encodes real requirements — everything above it is noise by declaration; a search budget (time or option-count) belongs in the rule; classify the decision's tail-weight first — satisficing heavy-tailed decisions is the failure mode.
- **Procedure:**
  1. Confirm this decision is satisfice-appropriate: are differences among acceptable options actually consequential? If yes → optimize instead.
  2. Write threshold criteria: the must-haves, with measurable levels.
  3. Set a search budget: max options examined or time spent.
  4. Search; take the first option clearing all thresholds.
  5. If budget exhausts with no option clearing: lower the *least load-bearing* threshold explicitly, or escalate the search — a conscious renegotiation, not drift.
  6. Stop evaluating after choosing. No retrospective shopping.
- **Mistakes:** satisficing the heavy-tailed decisions; thresholds quietly rewritten mid-search to justify a favorite; continuing to compare after committing.
- **Examples:** choosing a library for a non-core function; picking a venue; selecting "a good enough" analysis method under deadline; most procurement.
- **Related:** [[effort-calibration]], [[weighted-scoring]] (the optimizing sibling), [[prioritization-triage]]. **Prereqs:** none.

---

### risk-matrix `atomic · D2 · ~450 tok`
Grade risks by likelihood × impact, assign responses by quadrant, and re-grade on a schedule — a register, not a ritual.

- **Why:** Ungraded risk lists get attention allocated by vividness. The two-axis grade forces the boring-but-likely and the unlikely-but-ruinous into view, and quadrant-based response rules prevent both paranoia and neglect.
- **Inputs:** an endeavor and its enumerated risks (from [[premortem]] / [[inversion]]) → **Outputs:** a graded risk register with an owner, response, and early indicator per material risk.
- **Activate when:** planning anything with multiple failure modes; periodic review of an ongoing effort. **Skip when:** one dominant risk deserves full analysis instead of a grid cell.
- **Principles:** likelihood comes from base rates where they exist, not vibes; impact includes recovery cost and knock-on effects, not just direct damage; responses are a fixed menu — avoid, mitigate, transfer, accept — and *accept* must be explicit, never default; a register nobody revisits is theater.
- **Procedure:**
  1. Enumerate risks (feed from [[premortem]]); state each as event → consequence, not a vague noun ("vendor risk" → "vendor X misses the Q3 integration date, slipping launch").
  2. Grade likelihood (anchored to base rates) and impact (including recovery + knock-ons).
  3. Place on the grid. High-L/high-I: avoid or restructure the plan. High-L/low-I: cheap mitigations, batch them. Low-L/high-I: mitigation or transfer (insurance-shaped), plus an early indicator. Low/low: accept explicitly.
  4. Assign each material risk an owner and an early indicator ([[tripwires]]).
  5. Set the re-grading cadence; likelihoods drift.
- **Mistakes:** vague risk statements that can't be graded; multiplying grades into fake precision ("risk score 12"); no owner (a risk without an owner is accepted by accident); registering once and never revisiting.
- **Examples:** launch risk register; clinical trial risk plan; expedition planning; vendor portfolio review.
- **Related:** [[expected-value]] (continuous version), [[premortem]] (feeds it), [[tripwires]]. **Prereqs:** none.

---

### prioritization-triage `atomic · D2 · ~450 tok`
Rank competing demands by value, urgency, and cost-of-delay under explicit capacity limits — and make the cut line real.

- **Why:** Without explicit triage, work is ordered by recency, loudness, and ease. The scarce resource isn't effort but *capacity*, and every yes is a hidden no; triage makes the no's chosen instead of accidental.
- **Inputs:** a demand list + a capacity estimate → **Outputs:** an ordered list with an explicit cut line, and the named things below it.
- **Activate when:** demand exceeds capacity (always); starting a planning cycle; feeling busy but unproductive. **Skip when:** a single deadline dominates everything — just do that.
- **Principles:** urgency and importance are independent axes and urgency is the usual liar; cost-of-delay distinguishes "valuable" from "valuable *now*" — some value decays, some doesn't; the list below the cut line is the actual decision; ordering interacts with dependencies and batch effects — pure scoring ignores sequencing value.
- **Procedure:**
  1. List all demands, including the invisible ones (maintenance, recovery, thinking time).
  2. Estimate per item: value, cost-of-delay (what decays if deferred a cycle?), and effort.
  3. Kill or delegate items failing an importance floor — before ranking, not after.
  4. Rank by value-adjusted-for-delay per unit effort; then adjust for dependencies and batching.
  5. Draw the cut line at realistic capacity (planned capacity × historical delivery ratio).
  6. Name what's below the line; notify affected parties. This step is the triage.
  7. Re-triage on cadence or on material new information — not on every loud request.
- **Mistakes:** ranking without a cut line (a wish list); capacity fantasy; letting urgency proxy for importance; re-triaging reactively so the loudest requester always wins; never counting maintenance load.
- **Examples:** sprint planning; an ER's actual triage; a founder's week; choosing which fires *not* to fight during an incident.
- **Related:** [[cost-benefit]], [[satisficing-thresholds]], [[bottleneck-analysis]] (capacity is a constraint problem). **Prereqs:** none.

---

### decision-analysis `composite · D4 · ~1100 tok`
The full pipeline for consequential choices: frame, generate options, model uncertainty, score, stress-test, decide, and record.

- **Why:** High-stakes decisions fail at whichever stage was skipped — usually option generation or stress-testing. The pipeline guarantees every stage runs at a depth proportional to stakes.
- **Inputs:** a consequential, non-obvious choice → **Outputs:** a decision with documented rationale, the losing options and why, sensitivity flags, tripwires, and a journal entry for later scoring.
- **Dependencies:** `decision-framing`, `reversibility-classification`, `solution-space-mapping`, `weighted-scoring`, `expected-value`, `premortem`, `second-order-scan`, `tripwires`, `decision-journaling`, `confidence-calibration`.
- **Activate when:** [[reversibility-classification]] grades the decision costly-reversible or worse and options are genuinely open. **Skip when:** the door is two-way (decide fast, review later) or one option dominates on all criteria.
- **Principles:** process weight scales with irreversibility; option generation is where decisions are actually won — evaluation just confirms; uncertainty gets modeled, not adjectives; the decision isn't done until its revisit conditions are installed.
- **Procedure:**
  1. Run `reversibility-classification`; confirm this pipeline is warranted. Set the process budget.
  2. Run `decision-framing`: question, decider, criteria, deadline, default path.
  3. Run `solution-space-mapping`; ensure ≥3 genuinely distinct options plus the default.
  4. Model uncertainty: for each option, the key uncertain outcomes with probabilities (`expected-value` where payoffs are commensurable).
  5. Evaluate: `weighted-scoring` across criteria; run its sensitivity step hard — which judgment flips the result?
  6. Stress-test the leading option: `premortem` + `second-order-scan`. Amend or switch if wounds are fatal.
  7. Decide. Write the rationale, the runner-up, and *why the runner-up lost* — that's what gets revisited if conditions change.
  8. Install `tripwires`: what observations would reopen the decision.
  9. Log via `decision-journaling` with calibrated confidence (`confidence-calibration`) for later scoring.
- **Mistakes:** running the full pipeline on two-way doors (process as procrastination); skipping step 6 because the leader "feels solid" (that feeling is the reason to run it); rationale written after the fact to sound inevitable; no tripwires, so the decision silently becomes dogma.
- **Examples:** build-vs-buy on a core system; a market-entry decision; choosing a therapy path from mixed evidence; relocating a family.
- **Related:** [[structured-problem-solving]] (when it isn't a choice among options), [[scenario-planning]] (when uncertainty is about the world, not the options), [[negotiation]] (when the options are held by a counterparty).
