# 10 · Collaboration & Facilitation

Thinking well *with* others.

---

### active-listening `atomic · D2 · ~450 tok`
Paraphrase, label, and verify understanding before responding, so the response addresses what was actually meant rather than what was assumed.

- **Why:** Most listening is actually rehearsing a response while the other person talks. Paraphrase-and-verify forces genuine comprehension first, catches misunderstanding before it compounds, and — as a side effect — makes the speaker feel heard, which itself changes the conversation's trajectory.
- **Inputs:** another person speaking, especially about something emotionally or substantively important → **Outputs:** verified mutual understanding, and only then, a response.
- **Activate when:** any conversation where getting it right matters more than getting a response out fast — negotiations, difficult conversations, interviews, conflict. **Skip when:** the exchange is purely transactional and low-stakes.
- **Principles:** paraphrase content *and* label the emotion you're picking up ("it sounds like this was frustrating") — both are information; verify before responding — ask "did I get that right?" and actually wait; silence and a genuine question are more useful than a quick reassurance; understanding is not agreement — you can fully understand a position you still disagree with.
- **Procedure:**
  1. Listen fully before formulating a response — notice the impulse to plan your reply and set it aside.
  2. Paraphrase the content back in your own words, not a verbatim echo.
  3. Label the emotion you're perceiving, tentatively, as an offer to be corrected.
  4. Ask if you've understood correctly; treat correction as valuable information, not friction.
  5. Only after verified understanding, respond — with a question, empathy, or your own view as appropriate.
- **Mistakes:** paraphrasing content but skipping the emotional label; treating "did I get that right?" as rhetorical rather than genuinely waiting for correction; using active listening as a stalling technique while still just planning your rebuttal.
- **Examples:** a manager understanding an employee's concern before responding; a negotiation opening; a doctor eliciting a patient's actual concern, not just their stated symptom.
- **Related:** [[empathy-mapping]], [[precision-questioning]], [[nonviolent-communication]]. **Prereqs:** none.

---

### empathy-mapping `atomic · D2 · ~450 tok`
Reconstruct what another party sees, hears, thinks, feels, and needs, from their position rather than from your own assumptions about them.

- **Why:** Predicting others' behavior or designing for their needs from your own vantage systematically imports your own priorities and blind spots. Deliberately reconstructing their actual situation catches what a self-referential guess misses.
- **Inputs:** a specific other party (individual, role, or persona) → **Outputs:** a structured picture of what they perceive, think, feel, and need — distinguished from what you assume or wish they thought.
- **Activate when:** designing for users; preparing for a negotiation or difficult conversation; predicting a stakeholder's reaction. **Skip when:** direct data (an actual interview, actual observed behavior) is available — use that over a constructed map.
- **Principles:** ground the map in actual evidence about this party where available — an empathy map built on stereotype is worse than useless; separate what they say from what they likely think/feel — these often diverge; their needs are usually more stable and more legitimate than their stated positions — map both, but weight needs higher for solution design.
- **Principles (cont'd):** the map is a hypothesis to test against real behavior, not a conclusion.
- **Procedure:**
  1. Specify the party precisely (a real individual or a well-evidenced persona, not a vague stereotype).
  2. What do they see/hear: what's their actual environment, information, and context?
  3. What do they think/feel: their likely internal state, informed by evidence, not projection.
  4. What do they say/do: their observable behavior and statements — including where these seem to conflict with the thinks/feels layer.
  5. What do they need: the underlying need behind their stated wants (pairs with [[nonviolent-communication]]'s need/strategy distinction).
  6. Use the map to generate hypotheses; verify against real interaction where possible ([[interview-synthesis]]).
- **Mistakes:** building the map from assumption or stereotype instead of evidence; conflating what they say with what they need; treating the finished map as settled fact rather than a testable hypothesis.
- **Examples:** a UX research persona; preparing for a negotiation with an unfamiliar counterparty; a policy designed around a mapped constituency's actual situation.
- **Related:** [[active-listening]], [[stakeholder-mapping]], [[interview-synthesis]]. **Prereqs:** none.

---

### batna-analysis `atomic · D2 · ~450 tok`
Establish your own and (as best estimable) the other side's best alternative to a negotiated agreement, before negotiating.

- **Why:** Without a clear BATNA, negotiators either accept bad deals out of fear of walking away, or overplay a weak hand. Knowing the real walk-away point — for both sides — is what actually determines bargaining power, far more than tactics.
- **Inputs:** an upcoming negotiation → **Outputs:** your BATNA (quantified where possible), your reservation point, an estimate of the other side's BATNA, and the resulting zone of possible agreement (ZOPA).
- **Activate when:** before any negotiation with real stakes; when feeling pressure to accept a deal, which is exactly when BATNA clarity is most needed and most likely to have eroded. **Skip when:** stakes are trivial (the price is fixed and non-negotiable, or the amount doesn't matter).
- **Principles:** your BATNA is not your ideal outcome — it's what happens if this negotiation fails entirely, so it must be evaluated honestly, not optimistically; a strong BATNA is leverage regardless of whether you disclose it; the other side's BATNA is usually estimable from their circumstances and incentives ([[incentive-analysis]]) even without direct access; if there's no positive ZOPA (your minimum exceeds their maximum), the honest move is recognizing no deal should happen — not more tactics.
- **Procedure:**
  1. Identify your realistic alternative if this negotiation fails — not a fantasy alternative, an honest one.
  2. Quantify or otherwise evaluate that alternative to set your reservation point (the worst deal you'd still accept over no deal).
  3. Estimate the other side's likely BATNA from their circumstances, incentives, and public information.
  4. Estimate their reservation point from their BATNA.
  5. Identify the ZOPA: the range, if any, where both reservation points overlap.
  6. Enter the negotiation with your BATNA improved as much as possible beforehand — the best move before negotiating is often strengthening your alternative, not rehearsing tactics.
- **Mistakes:** confusing your ideal outcome with your BATNA; skipping the other side's BATNA analysis and negotiating blind to their real constraints; entering a negotiation without having tried to actually strengthen your BATNA in advance (e.g., securing a competing offer).
- **Examples:** a salary negotiation; a vendor contract negotiation; a real estate deal; an international dispute's positioning.
- **Related:** [[negotiation]] (the composite this feeds), [[incentive-analysis]], [[interest-based-bargaining]]. **Prereqs:** none.

---

### interest-based-bargaining `atomic · D3 · ~500 tok`
Negotiate on the underlying interests behind each side's stated positions, rather than splitting the difference between the positions themselves.

- **Why:** Positions are often incompatible even when the underlying interests aren't — two parties can both get what they actually need through a solution neither stated position anticipated. Bargaining on positions alone leaves this value on the table.
- **Inputs:** a negotiation where stated positions conflict → **Outputs:** the interests underlying each position, and options that satisfy both sides' interests better than any position-splitting compromise.
- **Activate when:** a negotiation has stalled on incompatible positions; both sides seem to be optimizing for the wrong variable. **Skip when:** the negotiation is genuinely zero-sum on a single dimension (pure price, nothing else at stake) — then it's just [[batna-analysis]] and leverage.
- **Principles:** ask "why do you want that?" of every stated position — the answer is the interest; interests are often compatible even when positions aren't (both sides can want "certainty," achieved differently); generate options before committing to a position — invent multiple ways to satisfy both sides' interests, then select; separate the people from the problem — attack the problem jointly, not each other.
- **Procedure:**
  1. State each side's stated position explicitly.
  2. For each, ask why — repeatedly if needed — until reaching the underlying interest (security, recognition, autonomy, resource need, timeline).
  3. Check for compatible or complementary interests hidden behind incompatible positions.
  4. Generate multiple options that could satisfy the interests, before evaluating any (borrow [[divergent-ideation]] discipline — defer judgment during generation).
  5. Evaluate options jointly against both sides' interests, using objective criteria where possible rather than raw leverage.
  6. Select and formalize the option that best satisfies both sides' actual interests.
- **Mistakes:** stopping at the first "why" instead of digging to the real interest; treating interest-based bargaining as a way to disguise a fixed position rather than genuinely opening to new options; skipping straight to a proposed solution before both sides' interests are actually understood.
- **Examples:** two departments fighting over budget, where the real interests are predictability (one side) and flexibility (the other) — solvable without a zero-sum budget fight; a labor negotiation where "wage increase" masks an interest in fairness/recognition; a custody arrangement negotiation.
- **Related:** [[batna-analysis]], [[negotiation]], [[empathy-mapping]]. **Prereqs:** none.

---

### consensus-mapping `atomic · D2 · ~400 tok`
Measure the actual gradient of agreement across a group instead of forcing a binary vote that hides where the real disagreement lives.

- **Why:** A binary vote collapses a spectrum of "strongly for" to "strongly against, will actively block" into a single number, hiding both near-unanimous soft support and a small but intense veto-level objection. Mapping the gradient makes the group's real state visible before it's acted on.
- **Inputs:** a group facing a decision with varying levels of agreement → **Outputs:** a gradient map of the group's position, with any veto-level objections surfaced explicitly rather than averaged away.
- **Activate when:** a group decision needs real buy-in, not just a nominal majority; a quick vote feels like it's hiding real dissent. **Skip when:** a simple majority vote is genuinely sufficient and buy-in from the minority isn't required for implementation to succeed.
- **Principles:** use a gradient scale (e.g., enthusiastic support → support with reservations → neutral → disagree but will go along → block) rather than binary yes/no; a single strong "block" carries different weight than several "reservations" and should be surfaced, not averaged into the mean; the goal is often not unanimous enthusiasm but the absence of unaddressed blocking objections.
- **Procedure:**
  1. State the proposal precisely enough to be rated.
  2. Have each participant rate their position on a gradient scale, ideally simultaneously (to avoid anchoring on the first vocal response).
  3. Map the distribution: where does the group cluster, and where's the spread?
  4. Surface any block-level objections explicitly — don't let them wash out in an averaged score.
  5. For blocks or strong reservations, understand the underlying concern ([[interest-based-bargaining]] if needed) before proceeding.
  6. Decide: proceed with addressed concerns noted, revise the proposal, or escalate if a genuine block remains.
- **Mistakes:** converting the gradient back into a binary average, which hides exactly what the technique was meant to surface; letting the loudest objector's position stand in for the whole group's gradient; using this technique for decisions where genuine buy-in isn't actually necessary (adds process cost without payoff).
- **Examples:** a team deciding on a technical direction; a co-op's governance vote; a jury's deliberation check-in before a final verdict push.
- **Related:** [[interest-based-bargaining]], [[retrospective-facilitation]], [[session-design]]. **Prereqs:** none.

---

### session-design `atomic · D2 · ~450 tok`
Design a working session backwards from its intended output, choosing structure, participants, and format to produce that output rather than defaulting to a status-update meeting.

- **Why:** Most unproductive meetings have no designed output — they default to a generic agenda-and-discussion format regardless of purpose. Designing backward from the actual needed artifact fixes format, attendance, and time allocation together.
- **Inputs:** a purpose requiring a group session → **Outputs:** a session design: the specific output artifact, the right participants, the format matched to that output, and a facilitation plan.
- **Activate when:** convening any group session beyond a routine sync; a recurring meeting has drifted from its original purpose. **Skip when:** the need is pure information broadcast — that's an email/doc, not a session.
- **Principles:** define the output artifact first (a decision, a ranked list, a shared understanding, a generated option set) — the format follows from this, not the other way around; invite only who's needed for *this* output — decider, informed, and consulted are different guest lists; different outputs need incompatible formats (divergent generation and convergent decision-making don't mix in one unstructured hour — see [[ideation-sprint]]'s phase gates); a session with no clear output should probably be a document instead.
- **Procedure:**
  1. State the specific output artifact this session must produce.
  2. Check: could this output be achieved without a synchronous session (a doc + async comments)? If yes, skip the meeting.
  3. Choose participants based on the output — who decides, who must be consulted, who merely needs to be informed (the last group doesn't need to attend live).
  4. Choose the format matched to the output type (decision → structured decision process; ideas → phase-gated ideation; alignment → structured discussion with explicit gradient check).
  5. Allocate time per phase, with the output-producing phase getting the most protected time, not the leftover.
  6. Close by confirming the output was actually produced, not just discussed.
- **Mistakes:** defaulting to "let's discuss" without a target artifact; inviting everyone who might be interested rather than who's needed for the output; running generation and decision in the same undifferentiated block of time.
- **Examples:** a design review redesigned around producing a specific decision rather than open discussion; a retrospective structured to output concrete action items; a planning meeting redesigned to actually produce a prioritized backlog.
- **Related:** [[expectation-contracting]], [[ideation-sprint]], [[retrospective-facilitation]]. **Prereqs:** none.

---

### expectation-contracting `atomic · D1 · ~400 tok`
Make roles, deliverables, and definitions-of-done explicit before work begins, converting assumed alignment into checkable agreement.

- **Why:** Most collaboration friction traces back to differing assumptions about who owns what and what "done" means — assumptions nobody stated because each side thought they were obvious. A short explicit contract prevents the argument that happens later when the gap surfaces.
- **Inputs:** a collaborative effort about to start → **Outputs:** an explicit, mutually confirmed statement of roles, deliverables, and completion criteria.
- **Activate when:** starting any collaboration with unclear or unstated role boundaries; delegating work; cross-team projects. **Skip when:** the working relationship is well-established and the task is routine within it.
- **Principles:** "done" needs a checkable definition, not a feeling — specify the artifact or state that constitutes completion; roles (who decides, who executes, who's consulted) should be named per-decision-point, not assumed globally; the contract should be confirmed by both sides, not just stated by one — silence isn't agreement.
- **Procedure:**
  1. State the deliverable(s) and their definition of done, specifically enough to be checkable.
  2. State roles: who decides, who executes, who's consulted, who's informed — for the key decision points, not just generically.
  3. State the timeline and any dependencies each side owns.
  4. Confirm explicitly with the other party — ask them to restate their understanding, don't assume silence means agreement.
  5. Revisit if scope or roles shift materially during the work — silent scope drift recreates the original problem.
- **Mistakes:** assuming a shared definition of "done" without stating it; announcing the contract without confirming the other side's understanding matches; setting it once and never revisiting as the work evolves.
- **Examples:** delegating a project to a report; a cross-functional project's kickoff; a freelance engagement's scope agreement; a research collaboration's authorship and contribution agreement.
- **Related:** [[decision-framing]], [[session-design]]. **Prereqs:** none.

---

### negotiation `composite · D4 · ~1050 tok`
The full pipeline: prepare BATNAs, probe for underlying interests, generate joint options, and converge on an agreement that survives both sides' scrutiny.

- **Why:** Negotiations conducted without preparation default to positional bargaining and leave value on the table, or collapse into a bad deal driven by fear of walking away. The full pipeline systematically captures the value interest-based approaches can find while keeping leverage realities in view.
- **Inputs:** an upcoming negotiation with a counterparty → **Outputs:** an agreement (or a deliberate no-deal) that reflects both sides' actual interests and each side's real leverage.
- **Dependencies:** `batna-analysis`, `empathy-mapping`, `interest-based-bargaining`, `active-listening`, `game-theoretic-analysis` (for complex/repeated negotiations).
- **Activate when:** any negotiation with meaningful stakes — commercial, employment, interpersonal, diplomatic. **Skip when:** the terms are truly fixed and non-negotiable (posted price, take-it-or-leave-it with no room) — negotiation effort there is wasted.
- **Principles:** preparation determines most of the outcome, before either side says a word; interests unlock value positions can't reach, but BATNA still sets the floor beneath which no interest-based creativity should push you; understanding (`active-listening`) is not concession — fully grasping their position costs nothing and reveals options; walking away is a legitimate, sometimes correct, outcome.
- **Procedure:**
  1. **Prepare:** run `batna-analysis` — your alternative, your reservation point, their estimated BATNA, the resulting ZOPA (if any).
  2. Run `empathy-mapping` on the counterparty: their likely interests, constraints, and pressures beyond what they'll state.
  3. **Open:** state your position, then genuinely elicit theirs; use `active-listening` to verify you understand their actual position before responding.
  4. **Probe interests:** run `interest-based-bargaining` — ask why behind stated positions on both sides; find compatible interests behind incompatible positions.
  5. **Invent options:** generate multiple ways to satisfy both sides' interests before committing to any (defer evaluation, per [[divergent-ideation]] discipline).
  6. For complex or repeated negotiations, run `game-theoretic-analysis` on how each proposed structure incentivizes future behavior, not just this deal.
  7. **Converge:** select the option best satisfying both sides' interests within each side's reservation point; use objective criteria to justify terms where possible (reduces perceived unfairness).
  8. If no option clears both reservation points, recognize and accept no-deal rather than forcing a bad agreement — that's a correct outcome the preparation was designed to reveal.
- **Mistakes:** skipping BATNA preparation and negotiating from fear or hope instead of a known floor; treating interest-based bargaining as a soft alternative to leverage rather than a complement to it; anchoring immediately on positions and never reaching the interest layer; forcing a deal when no real ZOPA exists.
- **Examples:** a job offer negotiation; a vendor contract; a business partnership dissolution; an international trade negotiation.
- **Related:** [[batna-analysis]], [[interest-based-bargaining]], [[conflict-mediation]] (third-party facilitated version), [[game-theoretic-analysis]].

---

### conflict-mediation `composite · D4 · ~950 tok`
As a third party, surface each side's narrative and underlying interests, find compatible ground, and broker an agreement neither side could reach alone.

- **Why:** Parties in conflict are often too invested in their own narrative to hear the other's, and too anchored on positions to see compatible interests. A mediator's structural advantage is exactly this outside position — used well, it does what direct negotiation between the parties couldn't.
- **Inputs:** two or more parties in unresolved conflict + a mediator role → **Outputs:** a mediated agreement or, at minimum, mutual understanding of the other's position and a defined next step.
- **Dependencies:** `active-listening`, `empathy-mapping`, `interest-based-bargaining`, `steelmanning`, `nonviolent-communication`.
- **Activate when:** direct negotiation between parties has stalled or is too charged for them to conduct alone; a neutral structure is needed to make progress. **Skip when:** the parties can and should resolve it directly — mediation shouldn't substitute for direct communication capability the parties actually have.
- **Principles:** the mediator holds the process, not the outcome — pushing a preferred resolution undermines the role's legitimacy; each side needs to feel genuinely heard by the mediator before they can hear the other side — sequence matters; `steelmanning` each side's position to the other (mediator-translated) often lands better than the original party's own framing, stripped of its adversarial heat; the goal may be agreement, or may just be de-escalation and a defined next step — both are legitimate outcomes.
- **Procedure:**
  1. Meet with each side separately first if the conflict is heated; use `active-listening` fully — each side needs to feel heard before joint work can proceed.
  2. Run `empathy-mapping` on each side to understand their actual situation, not just their stated complaint.
  3. Identify each side's underlying interests via `interest-based-bargaining` probing, done separately if needed.
  4. Bring sides together (when ready); restate each side's position using `steelmanning` and `nonviolent-communication` structure — observation and need, not accusation — to lower defensiveness.
  5. Guide toward compatible interests found in step 3; facilitate joint option generation rather than proposing your own solution.
  6. If agreement isn't reachable, secure a defined smaller next step (a cooling-off structure, a partial agreement, a process for continuing) rather than forcing false resolution.
- **Mistakes:** the mediator taking a side or pushing their own preferred solution; skipping separate initial listening and going straight to a joint session while the conflict is still hot; declaring failure when no full agreement is reached instead of securing the achievable partial outcome.
- **Examples:** a manager mediating between two conflicting team members; a family mediation; a community dispute resolution process; cross-team conflict over resourcing.
- **Related:** [[negotiation]], [[difficult-conversations]], [[active-listening]].

---

### delphi-aggregation `composite · D3 · ~850 tok`
Aggregate independent expert estimates through anonymous, iterative rounds with feedback — avoiding the groupthink and status-anchoring that live group discussion produces.

- **Why:** Bringing experts into a room to reach consensus is vulnerable to the loudest voice, the highest-status participant, and premature anchoring on the first number spoken. Anonymous iteration lets each expert's independent judgment register, then converges through evidence exchange rather than social pressure.
- **Inputs:** a forecasting or estimation question + a panel of relevant experts → **Outputs:** a converged (or explicitly still-divergent) estimate, with the reasoning behind outlying views surfaced.
- **Dependencies:** `question-decomposition`, `reference-class-forecasting`, `confidence-calibration`.
- **Activate when:** a question needs expert judgment but a live group discussion would risk anchoring or status effects; forecasting under genuine expert disagreement. **Skip when:** the question is empirically resolvable directly — don't substitute elicitation for available data.
- **Principles:** the first round must be genuinely independent and anonymous — no expert should see others' estimates before submitting their own; between rounds, share the distribution of estimates and the *reasoning* behind outliers, not just the numbers — reasoning is what should move minds, not social pressure toward the mean; convergence isn't the goal in itself — a persistent, well-reasoned outlier is valuable information, not noise to be smoothed away.
- **Procedure:**
  1. Frame the question precisely (`question-decomposition` if compound); ensure it's resolvable/estimable.
  2. Round 1: each expert independently submits an estimate with reasoning, anonymously, without seeing others' responses.
  3. Aggregate: show the panel the distribution of estimates and the anonymized reasoning behind outliers, especially the extremes.
  4. Round 2: each expert revises their estimate independently, having seen the distribution and reasoning (not just the numbers).
  5. Repeat for 2–3 rounds or until movement stabilizes.
  6. Report the final distribution; explicitly surface any persistent, well-reasoned disagreement rather than papering over it with a simple average.
- **Mistakes:** running it as a live discussion with names attached (defeats the anonymity that prevents status anchoring); sharing only the numeric distribution between rounds without the reasoning (loses the actual information content); forcing consensus by stopping only when everyone agrees, discarding a legitimately informative holdout.
- **Examples:** technology forecasting panels; expert elicitation for a risk assessment; estimating an uncertain project cost across senior engineers; policy-impact forecasting.
- **Related:** [[structured-forecasting]] (individual version), [[interview-synthesis]], [[consensus-mapping]].

---

### retrospective-facilitation `composite · D2 · ~800 tok`
A structured what-went-well / what-didn't / what-changes review that produces concrete action items rather than a venting session or a forgotten discussion.

- **Why:** Unstructured retrospectives either avoid hard truths (everyone's polite) or dwell on them unproductively (venting without resolution). The structure — separating observation from judgment, ending in committed actions — makes the review actually change future behavior.
- **Inputs:** a completed effort, sprint, project, or incident → **Outputs:** documented learnings and a short list of owned, concrete action items.
- **Dependencies:** `after-action-review`, `active-listening`, `consensus-mapping`.
- **Activate when:** the end of any bounded effort where future work would benefit from explicit learning; recurring cadence (sprint-end, project-end, incident post-mortem). **Skip when:** the effort was too trivial to yield real learning, or a retro was just run and nothing has changed since.
- **Principles:** separate what happened (facts) from what it means (judgment) from what to do (action) — collapsing these stages produces blame instead of learning; psychological safety is a precondition, not a nice-to-have — people won't surface real issues if the retro has ever been used against them; every retro should produce a small number of *owned* action items, not a long list nobody's accountable for.
- **Procedure:**
  1. Set the frame: this is about the work and the system, not about blaming individuals (make this explicit, especially in a team that's had a hard outcome).
  2. Gather observations: what happened, factually — timeline if useful. Use `active-listening` to draw out quieter participants.
  3. Separately, gather interpretation: what went well and why, what didn't and why — run `after-action-review`'s intended-vs-actual framing.
  4. Use `consensus-mapping` if there's disagreement about the interpretation — surface it rather than averaging it away.
  5. Generate action items: specific, owned, and scoped to what's actually within the team's control.
  6. Assign owners and a review date; check at the next retro whether previous action items were actually completed — this closes the loop and is what most retros skip.
- **Mistakes:** collapsing fact-gathering and judgment into one rushed step, producing blame instead of insight; generating action items with no owner (they don't happen); never checking whether last retro's action items were completed, which teaches the team that retros don't matter.
- **Examples:** a sprint retrospective; a post-incident review; an end-of-project debrief; a season debrief for a sports team.
- **Related:** [[after-action-review]], [[consensus-mapping]], [[active-listening]].

---

### coaching-dialogue `composite · D3 · ~850 tok`
GROW: goal, reality, options, will — a question-led dialogue that helps someone reach their own insight and commitment, rather than being handed a solution.

- **Why:** Advice handed down is more easily discarded than an insight someone reaches themselves, and often misses context the advisor doesn't have. A well-run question sequence gets to a better, more owned outcome than direct instruction — at the cost of taking longer.
- **Inputs:** a person facing a decision or challenge, in a coaching (not directing) relationship → **Outputs:** the person's own articulated goal, honest assessment of current reality, generated options, and a committed next action.
- **Dependencies:** `active-listening`, `precision-questioning`, `divergent-ideation` (lightweight).
- **Activate when:** the person has the capability to solve their own problem and would benefit more from ownership than from a direct answer; a mentoring or management relationship where growth matters, not just the immediate outcome. **Skip when:** the situation needs a fast, directive answer — an emergency, a clear policy question, or genuine lack of relevant knowledge on the coachee's part where teaching (see [[socratic-teaching]] or direct instruction) is more appropriate.
- **Principles:** ask, don't tell — the coach's job is to sharpen the coachee's own thinking via questions, resisting the urge to supply the answer; reality must be assessed honestly before options are generated, or the options solve the wrong problem; the "will" stage must produce a specific commitment, not a vague intention, or the dialogue doesn't translate into change.
- **Procedure:**
  1. **Goal:** ask what they want from this conversation and, more broadly, from the situation — sharpen a vague goal into something specific via `precision-questioning`.
  2. **Reality:** ask what's actually happening now — facts, not story; use `active-listening` to draw out the honest picture, including what they might be avoiding.
  3. **Options:** ask what options they see, deferring judgment (`divergent-ideation` lightweight) — resist supplying your own options unless genuinely stuck, and even then offer rather than prescribe.
  4. **Will:** ask what they'll actually commit to, by when, and what might get in the way — press for specificity.
  5. Close by having them state the commitment in their own words.
- **Mistakes:** answering your own questions when the coachee pauses (collapses back into advice-giving); rushing to options before reality is honestly assessed; ending without a specific, owned commitment, leaving the conversation as pleasant but inert.
- **Examples:** a manager's 1:1 helping a report work through a stuck project; an executive coaching session; a mentor helping a mentee decide between paths.
- **Related:** [[active-listening]], [[socratic-teaching]], [[feedback-delivery]].
