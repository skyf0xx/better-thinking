# 5 · Analysis & Critique

Stress-testing claims, arguments, and positions.

---

### assumption-audit `atomic · D2 · ~450 tok`
Surface the load-bearing assumptions beneath a claim or plan, and test each for fragility.

- **Why:** Conclusions are only as strong as their weakest unexamined assumption, and assumptions are invisible by default — that's what makes them assumptions. Naming them converts hidden risk into a checklist.
- **Inputs:** a claim, plan, or forecast → **Outputs:** a list of assumptions tagged load-bearing/cosmetic, each with a fragility note and how it could be tested.
- **Activate when:** before committing to a plan; a conclusion feels solid but stakes are high; someone says "obviously." **Skip when:** the claim is definitional or already fully specified.
- **Principles:** ask "what has to be true for this to hold?" not "what do I believe?"; not all assumptions matter equally — rank by what breaks if the assumption is false; the cheapest assumptions to test should be tested first; an assumption stated out loud can be disagreed with — that's the point.
- **Procedure:**
  1. State the claim/plan precisely.
  2. List everything that must be true for it to work — inputs, behaviors, environment, timing.
  3. Classify each: load-bearing (claim collapses without it) vs cosmetic (claim survives).
  4. For load-bearing assumptions, rate confidence and cost-to-test.
  5. Test or validate the cheapest, highest-doubt assumptions first.
  6. Report the surviving plan plus the assumptions still untested and their risk.
- **Mistakes:** listing assumptions without ranking (a wall of text nobody acts on); treating "obvious" as a reason to skip listing it; auditing once and never re-auditing as conditions change.
- **Examples:** a growth forecast assuming current conversion holds; a migration plan assuming zero data drift; a negotiation assuming the counterparty's stated priority is their real one.
- **Related:** [[first-principles]], [[premortem]], [[disconfirmation-search]]. **Prereqs:** none.

---

### steelmanning `atomic · D2 · ~450 tok`
Reconstruct the strongest possible version of a position before evaluating or arguing against it.

- **Why:** Arguing against the weakest form of an opposing view (the strawman) feels like victory and teaches nothing. Steelmanning forces contact with the position's actual force, which is where real disagreement — or real agreement — lives.
- **Inputs:** a position, argument, or person to disagree with → **Outputs:** the strongest coherent version of that position, in language its proponent would endorse, plus your actual point of departure from it.
- **Activate when:** about to argue against something; evaluating a proposal you're inclined to reject; writing a rebuttal. **Skip when:** the position is being evaluated for internal consistency only (use [[deductive-validation]]).
- **Principles:** if a proponent wouldn't recognize your summary as their view, you've built a strawman; charity means supplying the best available premises and context, not inventing an unrelated better argument; steelmanning is not agreeing — it's earning the right to disagree.
- **Procedure:**
  1. State the position as its weakest critics would (the strawman) — for contrast.
  2. Now reconstruct it with its best available evidence, most charitable premises, and the context that motivates it.
  3. Check: would a thoughtful proponent say "yes, that's my view, stated well"? If not, revise.
  4. Identify what the steelmanned version gets right.
  5. Locate your actual point of departure — the specific premise or evidence where you diverge.
  6. Respond to the steelman, not the strawman.
- **Mistakes:** steelmanning into a different, more convenient position; skipping straight to rebuttal without the proponent-check in step 3; steelmanning positions you already agree with (skip — no work to do there) instead of the ones you resist.
- **Examples:** rebutting a competitor's technical claim; responding to a policy you dislike; internal design review of an approach you'd have done differently.
- **Related:** [[devils-advocacy]] (inverse move — arguing against consensus), [[argument-mapping]], [[reductio]]. **Prereqs:** none.

---

### fallacy-detection `atomic · D2 · ~500 tok`
Scan an argument for named logical failure patterns, distinguishing a genuine fallacy from a merely weak or unwelcome argument.

- **Why:** Naming a fallacy is powerful and easy to abuse — real fallacy-spotting requires showing the specific inferential gap, not just pattern-matching a label onto anything you dislike.
- **Inputs:** an argument → **Outputs:** identified fallacies (if any) with the specific broken inference shown, separated from claims that are merely weak, unwelcome, or unproven.
- **Activate when:** evaluating persuasive content; a conclusion seems to sneak past its support; debate moderation. **Skip when:** you're pattern-matching to win rather than to check validity — that use corrodes the skill.
- **Principles:** a fallacy is a *structural* defect in the inference, not a false conclusion or a conclusion you dislike; naming the fallacy requires showing what's missing, not just applying a label; common patterns: ad hominem (attacking the source instead of the claim), strawman (arguing a distorted version), false dilemma (hiding real options), appeal to authority outside expertise, post hoc (sequence mistaken for cause), motte-and-bailey (defending a modest claim while asserting a bold one), equivocation (a term's meaning shifting mid-argument), circular reasoning (conclusion assumed in a premise).
- **Procedure:**
  1. Map the argument's structure ([[argument-mapping]] if complex).
  2. Check each inferential step: does the conclusion actually follow, or is something being smuggled?
  3. Match candidate fallacy patterns; for each match, show the specific missing link — not just the label.
  4. Distinguish: is this a structural fallacy, or just a claim that's false, unproven, or weakly supported? Only the former gets the fallacy label.
  5. Report the fallacy with its repair (what would the argument need to be valid?) — repair, don't just declare "gotcha."
- **Mistakes:** fallacy-labeling as a rhetorical weapon instead of an analytic finding; missing the repair step (naming without showing the gap isn't analysis); calling every weak argument a "fallacy"; overusing ad hominem accusations against legitimate credibility challenges ([[source-credibility]] is not ad hominem).
- **Examples:** a sales pitch's false dilemma ("either buy this or stay vulnerable"); a policy debate's motte-and-bailey; auditing your own draft for smuggled premises.
- **Related:** [[deductive-validation]], [[argument-mapping]], [[critical-reading]]. **Prereqs:** none.

---

### devils-advocacy `atomic · D2 · ~450 tok`
Deliberately construct the best case against the group's current consensus, as an assigned role rather than a personal stance.

- **Why:** Consensus suppresses dissent through social pressure long before anyone consciously agrees. An assigned adversarial role gives permission to voice the counter-case without it costing the speaker status — and surfaces objections that silent doubters were sitting on.
- **Inputs:** a consensus position or decision nearing agreement → **Outputs:** the strongest available case against it, explicitly delivered as a structured challenge (not a personal belief).
- **Activate when:** a group converges quickly or uniformly; a decision is high-stakes and unanimous; dissent has been notably absent. **Skip when:** the group is already fractured — more adversarial pressure isn't the missing ingredient there.
- **Principles:** the role is explicitly adopted and explicitly dropped — depersonalizing it is what makes it safe to use; the case must be genuinely researched, not performative contrarianism; rotate who holds the role so it doesn't become one person's brand (and get dismissed as such).
- **Procedure:**
  1. Name the consensus position precisely.
  2. Assign the role explicitly ("I'm going to argue against this now").
  3. Build the strongest real case against it: weak evidence supporting it, unconsidered options, risks being downplayed, incentives distorting the group's judgment.
  4. Present it as a structured challenge, not a mood.
  5. Group responds to the substance; the advocate drops the role afterward.
  6. Note which objections survived scrutiny — those get addressed in the plan.
- **Mistakes:** a token, half-hearted challenge nobody takes seriously; the same person always cast as the skeptic (they get discounted over time); confusing the role with the person's real opinion; running it after the decision is already locked in.
- **Examples:** board review of an acquisition; an engineering design review right before sign-off; a jury's deliberation.
- **Related:** [[red-teaming]] (the full adversarial composite), [[inversion]], [[steelmanning]] (steelman the consensus first, then attack that). **Prereqs:** none.

---

### incentive-analysis `atomic · D2 · ~450 tok`
Map who gains and who loses from a claim, decision, or outcome — *cui bono* as a structured question, not an accusation.

- **Why:** Incentives shape behavior even in honest actors, often below conscious awareness. Mapping them predicts behavior better than mapping stated intentions, and explains otherwise-puzzling positions.
- **Inputs:** a claim, proposal, or behavior → **Outputs:** a map of who benefits/loses, by how much, and whether the incentive plausibly explains the observed position.
- **Activate when:** a party's position seems to track their interest suspiciously well; evaluating advice from someone who benefits from your choice; designing systems where you need to predict gaming. **Skip when:** used as a substitute for actually checking the claim's truth (it discounts, it doesn't decide).
- **Principles:** incentive explains the *tendency*, not that any specific claim is false — it adjusts weight, it doesn't settle the matter; look at revealed incentive (what they're paid/promoted/rewarded for), not just stated motive; systems reliably get the behavior they measure and reward, regardless of stated intent.
- **Procedure:**
  1. Identify the parties with a stake in this claim/decision/outcome.
  2. For each, map what they gain or lose under each possible resolution.
  3. Compare their stated position to their incentive gradient — aligned or misaligned?
  4. Where aligned: discount the claim proportionally; seek independent corroboration ([[evidence-triangulation]]).
  5. Where misaligned (arguing against their own interest): weight this heavily — it's rare and informative.
  6. If designing a system: predict what behavior the incentive structure actually produces, independent of intended behavior.
- **Mistakes:** treating incentive-alignment as proof of falsehood (genetic fallacy); stopping at stated motive instead of revealed incentive; ignoring your own incentive in the analysis.
- **Examples:** a consultant recommending exactly the service they sell; evaluating a performance metric for what it will actually incentivize; a regulator's position vs the industry they came from.
- **Related:** [[source-credibility]], [[stakeholder-mapping]], [[game-theoretic-analysis]]. **Prereqs:** none.

---

### stakeholder-mapping `atomic · D2 · ~450 tok`
Chart every actor touched by a decision along interest and influence, to see whose consent, input, or resistance actually matters.

- **Why:** Plans fail when a stakeholder with real influence was never consulted, or effort is wasted persuading someone with no power to affect the outcome. The map makes engagement effort proportional to actual stakes.
- **Inputs:** a decision or change with multiple affected parties → **Outputs:** a stakeholder grid (interest × influence) with an engagement plan per quadrant.
- **Activate when:** organizational or multi-party decisions; change likely to meet resistance; planning communication or rollout. **Skip when:** the decision affects only the decider.
- **Principles:** influence ≠ formal authority — map actual power to help or block; high-influence/low-interest stakeholders are the most commonly missed and the most dangerous to ignore; interests can be latent — ask who would care once they noticed, not just who's vocal now.
- **Procedure:**
  1. List every party materially affected by or able to affect the decision.
  2. Rate each on interest (how much they care) and influence (how much they can shape the outcome).
  3. Place on the grid: high/high → manage closely and involve early; high influence/low interest → keep satisfied, don't overload with detail; high interest/low influence → keep informed; low/low → monitor.
  4. For high-influence stakeholders, run [[incentive-analysis]] to predict their actual position.
  5. Build an engagement plan per quadrant — different cadence and depth, not one blast communication.
  6. Revisit; interest and influence shift as the decision proceeds.
- **Mistakes:** mapping only the vocal stakeholders; conflating org-chart seniority with actual influence over this specific decision; one-size-fits-all communication instead of quadrant-specific engagement.
- **Examples:** a reorg's rollout plan; a regulatory change's affected-party map; a product decision's internal stakeholder set (sales, support, legal, eng).
- **Related:** [[incentive-analysis]], [[empathy-mapping]], [[negotiation]]. **Prereqs:** none.

---

### frame-detection `atomic · D3 · ~500 tok`
Identify how a question, comparison, or presentation is pre-loaded to favor a particular answer, before answering it.

- **Why:** The same facts framed differently produce different judgments (loss vs gain framing, the comparison set chosen, which baseline is implied). Detecting the frame is a prerequisite to answering the actual question rather than the one smuggled into the phrasing.
- **Inputs:** a question, comparison, or presented choice → **Outputs:** the frame made explicit, the answer under that frame, and the answer under at least one alternative frame.
- **Activate when:** a question has an oddly obvious answer; a choice is presented as binary; a statistic is framed as loss or gain, absolute or relative; evaluating your own instructions/prompts for embedded bias. **Skip when:** the frame is genuinely neutral and singular.
- **Principles:** the comparison baseline is a frame choice — "compared to what?" often does more work than any argument; loss-framing and gain-framing of identical facts provoke different risk preferences — check both; who chose the frame, and does its choice serve them; a reframe that changes the answer reveals the original answer was frame-dependent, not fact-dependent.
- **Procedure:**
  1. State the question or choice as given.
  2. Identify the implicit baseline/comparison, the implicit option set, and the gain/loss framing.
  3. Ask who chose this frame and what answer it favors.
  4. Reframe: invert gain/loss, change the comparison baseline, widen the option set.
  5. Answer under both frames; if they diverge, the honest answer addresses the divergence explicitly rather than picking one.
- **Mistakes:** detecting the frame and stopping there without re-answering; assuming all framing is manipulative (sometimes it's just how the fact is naturally described); missing your own frame when generating the question.
- **Examples:** "should we cut costs" vs "should we invest less in reliability"; a survival-rate stat vs the equivalent mortality-rate stat; "which vendor is cheaper" vs "what's the cost of the outcome each vendor's failure mode produces."
- **Related:** [[critical-reading]], [[problem-framing]], [[incentive-analysis]] (who benefits from this frame). **Prereqs:** none.

---

### structured-what-if `atomic · D2 · ~400 tok`
Take a conclusion as fixed and reason forward through its implications — the exploratory twin of [[reductio]], used to map consequences rather than to refute.

- **Why:** Many claims are neither obviously true nor false but under-explored — nobody has traced what would follow if they were true. Doing so surfaces implications that are themselves evidence for or against the claim, and prepares for the world where it holds.
- **Inputs:** a claim, trend, or scenario assumed true → **Outputs:** a traced set of downstream implications, with the most consequential and most surprising ones flagged.
- **Activate when:** scenario exploration; testing a claim's plausibility by its implications; preparing contingencies. **Skip when:** the goal is to find a contradiction — use [[reductio]] instead.
- **Principles:** trace implications mechanically and unemotionally, whether or not you want them true; a claim that implies something absurd is thereby weakened even without formal contradiction; second- and third-order implications are usually more informative than the first.
- **Procedure:**
  1. State the claim/scenario as given, fully.
  2. Trace immediate (first-order) implications.
  3. Trace what those imply in turn (second-order), especially behavioral adaptations.
  4. Flag implications that are surprising, costly, or that contradict other things you believe.
  5. Use the flags either to weight the claim's plausibility or to build contingency plans if the claim is a live possibility.
- **Mistakes:** stopping at first-order implications; motivated tracing (following implications you like further than ones you don't); confusing "this scenario would be bad" with "this scenario is unlikely."
- **Examples:** "what if this regulation passes as drafted?"; "what if this trend continues for five more years?"; exploring a competitor's stated strategy taken at face value.
- **Related:** [[reductio]], [[second-order-scan]], [[scenario-planning]]. **Prereqs:** none.

---

### competing-hypotheses `composite · D4 · ~1000 tok`
Analysis of Competing Hypotheses: rank rival explanations by how much the evidence *disconfirms* each, rather than how much confirms any single favorite.

- **Why:** Confirmation-seeking analysis lets any hypothesis with enough support "win," even when the evidence fits every rival equally well. Scoring by inconsistency exposes which evidence actually discriminates — and which hypothesis survives that scrutiny.
- **Inputs:** a question with multiple plausible explanations and a body of evidence → **Outputs:** an evidence × hypothesis matrix scored by inconsistency, the surviving hypothesis (or a genuine tie), and the diagnostic evidence that would break the tie.
- **Dependencies:** `abductive-inference`, `evidence-hierarchy`, `disconfirmation-search`, `bayesian-updating`.
- **Activate when:** high-stakes explanatory questions with ambiguous or contested evidence — intelligence-style assessment, complex diagnosis, contested historical or organizational questions. **Skip when:** one hypothesis is already overwhelmingly favored by direct evidence — this machinery is for genuine ambiguity.
- **Principles:** evidence that's consistent with *every* hypothesis is worthless for discrimination, however voluminous; the strongest hypothesis is the one with the *fewest* strong inconsistencies, not the most confirmations; disproof is more diagnostic than proof; write the matrix down — it externalizes the comparison the unaided mind can't hold.
- **Procedure:**
  1. Run `abductive-inference` to generate the full hypothesis set — include ones you find unlikely or unwelcome.
  2. List all relevant evidence, gathered independent of any hypothesis (avoid evidence hand-picked to support the favorite).
  3. Build the matrix: for each evidence × hypothesis cell, mark consistent / inconsistent / strongly inconsistent / not applicable. Grade each evidence item's reliability (`evidence-hierarchy`).
  4. Score each hypothesis by total inconsistency (weighted by evidence reliability) — not by count of confirmations.
  5. The hypothesis with the least, weakest inconsistency leads. If several are close, that closeness is itself the finding.
  6. Run `disconfirmation-search`: what evidence, if found, would most separate the leaders? Prioritize gathering it.
  7. Report the ranking, confidence (`bayesian-updating` on the margin), and the diagnostic evidence still missing.
- **Mistakes:** generating hypotheses then unconsciously gathering only confirming evidence; scoring by confirmation count (defeats the method's purpose); treating a narrow win as certainty; skipping the matrix and doing it "in your head" (it doesn't work in your head — that's the whole reason for the technique).
- **Examples:** intelligence assessment of an ambiguous geopolitical event; diagnosing why a metric moved when three plausible causes coincide; historical causation disputes; determining why a hire didn't work out.
- **Related:** [[differential-diagnosis]] (same logic, live/ongoing case), [[abductive-inference]] (feeds it), [[bayesian-updating]] (formalizes the scoring).

---

### red-teaming `composite · D4 · ~1000 tok`
A structured adversarial exercise: assign a team (or role) to attack a plan, argument, or system as a genuine opponent would, then feed findings back before commitment.

- **Why:** Self-critique is capped by the fact that the builder can't fully escape their own blind spots and investment. An adversary optimizing purely to break the thing finds what the builder structurally cannot.
- **Inputs:** a plan, system, argument, or product nearing commitment → **Outputs:** a findings report of exploitable weaknesses ranked by severity, and the plan's response to each.
- **Dependencies:** `premortem`, `devils-advocacy`, `assumption-audit`, `incentive-analysis`, `second-order-scan`.
- **Activate when:** the cost of being wrong in production/live exceeds the cost of a dedicated attack exercise; security-, safety-, or reputation-critical work; before major public commitments. **Skip when:** stakes don't justify the overhead — use [[premortem]] alone.
- **Principles:** the red team must be resourced and empowered to actually think like an adversary — real incentive to "win," not politeness; success is finding real weaknesses, not validating the plan (a red team that finds nothing either got a strong plan or wasn't trying); findings need a forced response — accept the risk, mitigate, or redesign — not just a list.
- **Procedure:**
  1. Define scope and rules of engagement: what's in bounds to attack, what "winning" looks like for the red team.
  2. Assign the adversarial role explicitly (a person, subteam, or structured self-exercise) — separate from the builders.
  3. Red team runs `assumption-audit` and `incentive-analysis` on the target to find exploitable weak points, then `premortem` framing ("we broke it — how?").
  4. Actively attempt exploits/attacks/counterarguments — not just list concerns, actually try to break it where feasible.
  5. Run `second-order-scan` on any successful attack: what does exploiting this enable next?
  6. Report findings ranked by severity × exploitability.
  7. Builders respond to each: fix, mitigate, accept-with-owner, or dispute-with-evidence. No silent drops.
- **Mistakes:** red team drawn from the same team with the same blind spots and incentives; findings collected but not force-ranked or force-responded-to; running it too late to change anything (theater); scope so narrow the real risks are out of bounds.
- **Examples:** penetration testing before launch; a legal team stress-testing their own case; war-gaming a competitor's response to a price change; adversarial review of an AI system's safety properties.
- **Related:** [[wargaming]] (multi-turn strategic version), [[devils-advocacy]] (lighter single-person version), [[premortem]]. **Prereqs:** stakes justify the overhead.

---

### peer-review `composite · D3 · ~850 tok`
Structured evaluation of another's work for correctness, rigor, and significance — feedback that a capable stranger could act on.

- **Why:** Unstructured review drifts to style nitpicks or vague praise, missing the load-bearing question: does this work actually establish what it claims? A repeatable structure catches that and produces actionable feedback either way.
- **Inputs:** a piece of work (paper, analysis, code design, proposal) + its claimed contribution → **Outputs:** a structured verdict — significance, correctness, and specific actionable revisions — separated from stylistic preference.
- **Dependencies:** `critical-reading`, `methodology-critique`, `assumption-audit`, `steelmanning`.
- **Activate when:** evaluating work before it ships, publishes, or gets relied upon; giving feedback that needs to be actionable, not just reactive. **Skip when:** a quick sanity pass suffices — full peer review has real overhead.
- **Principles:** evaluate the claim actually made, not a stronger or weaker one you'd have preferred (`steelmanning`); separate "this is wrong" from "this is not how I'd have done it" — only the former is a correctness finding; every criticism should be actionable or it's not feedback, it's a mood; significance and correctness are independent axes — correct-but-trivial and wrong-but-important are both real categories.
- **Procedure:**
  1. Run `critical-reading`: extract the claimed contribution and its support.
  2. Assess significance: if true, does this matter? To whom, how much?
  3. Assess correctness: run `methodology-critique` and `assumption-audit` on the support. Does the evidence establish the claim at the strength claimed?
  4. Steelman weak points before flagging them — is there a reading where this concern doesn't apply?
  5. Separate findings into: must-fix (breaks the claim), should-fix (weakens confidence), and stylistic (preference, optional).
  6. Write the review: verdict, top findings ranked by severity, and for each, what specifically would resolve it.
- **Mistakes:** style creep dominating the review; vague verdicts ("needs work") without the specific fix; reviewing the work you wish they'd done instead of the one they did; asymmetric harshness based on the author's status.
- **Examples:** reviewing a research paper or grant proposal; a technical design review; editing a colleague's strategy memo; assessing a junior's analysis before it goes to a client.
- **Related:** [[methodology-critique]] (the correctness engine), [[feedback-delivery]] (how to deliver the verdict), [[revision-pass]].

---

### case-analysis `composite · D3 · ~900 tok`
IRAC generalized: identify the issue, determine the governing rules/principles, apply them to the facts, and reach a conclusion — a structure for any rule-governed judgment.

- **Why:** Judgment under a rule system (legal, policy, contractual, procedural) fails when the issue is misidentified or the rule is applied to facts it doesn't actually govern. The four-part structure forces each link to be checked separately.
- **Inputs:** a fact pattern + a governing rule system → **Outputs:** the issue framed precisely, the applicable rule(s) stated, the application reasoned through, and a conclusion with its confidence and the strongest counter-analysis.
- **Dependencies:** `question-decomposition`, `argument-mapping`, `steelmanning`, `analogical-reasoning`.
- **Activate when:** applying any rule system to a specific situation — legal questions, policy compliance, contractual interpretation, procedural rulings, even codified organizational policy. **Skip when:** no governing rule system exists — this isn't for open-ended judgment calls.
- **Principles:** the issue must be stated precisely enough that the rule's applicability is testable — vague issues let any rule seem to apply; rules have elements — check each one against the facts, not the rule's gist; precedent applies through `analogical-reasoning` — the mapping must hold, not just the surface similarity; a conclusion should state its confidence and the best counter-argument, since rule application is rarely airtight.
- **Procedure:**
  1. **Issue:** state the precise question the facts raise under the rule system. Run `question-decomposition` if it bundles multiple issues.
  2. **Rule:** identify the governing rule(s), stated with their actual elements/conditions — not summarized loosely.
  3. **Application:** work through each element against the specific facts. Where a similar prior case/precedent is used, verify the analogy holds (`analogical-reasoning`) rather than assuming surface similarity suffices.
  4. Run `steelmanning` on the counter-position — the strongest argument the rule doesn't apply, or applies differently.
  5. **Conclusion:** state the answer, its confidence, and what fact — if different — would flip it.
  6. Map the full reasoning (`argument-mapping`) if the analysis will be scrutinized or contested.
- **Mistakes:** stating the issue too broadly (invites rule-shopping); applying the rule's "spirit" while skipping its actual elements; one-sided application with no counter-analysis; treating a loose analogy to precedent as binding.
- **Examples:** contract interpretation dispute; whether an action violates a specific policy; regulatory compliance determination; applying an internal engineering standard to an edge-case design.
- **Related:** [[argument-mapping]], [[analogical-reasoning]], [[steelmanning]]. Consumed by legal and compliance-adjacent workflows generally.
