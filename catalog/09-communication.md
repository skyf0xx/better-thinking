# 9 · Communication

Making thought land in another mind.

---

### audience-modeling `atomic · D2 · ~450 tok`
Model the reader or listener's existing knowledge, goals, and likely objections before composing anything, and let that model drive every subsequent choice.

- **Why:** Content optimized for the writer's own understanding routinely fails the reader — too much unneeded context, too little of what they actually need, wrong things emphasized. Modeling the audience first fixes the target before aiming.
- **Inputs:** a communication task + what's known about the audience → **Outputs:** an audience model (knowledge, goal, likely objections, decision they need to make) that subsequent structuring decisions can be checked against.
- **Activate when:** before writing or presenting anything consequential; a draft isn't landing and it's unclear why. **Skip when:** writing purely for yourself (notes, journaling).
- **Principles:** what the audience needs to know is not what you find interesting about the topic — it's what closes their specific gap; assume less shared context than feels natural, but don't over-explain what they already know (both cost trust); the audience's objections are predictable if you model their incentives ([[incentive-analysis]]) and prior position; different audience members in one room may need different things — name the primary one.
- **Procedure:**
  1. Name the audience specifically (a role, not "readers in general").
  2. State what they already know and don't know about this topic.
  3. State what decision or action they need to take after receiving this — that's the actual goal, not "inform them."
  4. Predict their top 1–3 objections or points of skepticism.
  5. Note what they care about that you might not (their incentives, their constraints).
  6. Let this model drive structure, depth, and word choice in the actual composition.
- **Mistakes:** modeling the audience once, generically, and reusing it for every piece; writing to impress rather than to close the audience's specific gap; assuming your level of context is universal.
- **Examples:** an engineering design doc written for a non-technical stakeholder vs a peer reviewer; a sales pitch adapted per buyer persona; a doctor explaining a diagnosis to a patient vs to a colleague.
- **Related:** [[pyramid-structuring]], [[precision-questioning]], [[persuasive-case]]. **Prereqs:** none.

---

### pyramid-structuring `atomic · D2 · ~450 tok`
Lead with the answer, then support it with grouped, logically ordered reasons — inverting the build-up-to-the-conclusion instinct.

- **Why:** Readers (especially busy, senior, or skimming ones) decide whether to keep reading in the first sentence. Burying the conclusion under build-up loses them before they reach it — and even attentive readers process supporting detail better once they know what it's supporting.
- **Inputs:** a conclusion and its supporting reasons/evidence → **Outputs:** a structure with the answer first, reasons grouped and ordered beneath it, each reason similarly structured recursively.
- **Activate when:** writing any document or making any case meant to inform a decision; a draft currently builds up to its point instead of leading with it. **Skip when:** the piece is deliberately narrative/suspenseful (a different structure — see [[narrative-construction]] — is the point).
- **Principles:** state the main point in the first sentence or two, not the last paragraph; group supporting reasons so each group answers one implicit "why" or "how" question, not a random list; order groups by importance to the reader's decision, not by the order you thought of them; every level answers a question raised by the level above it — that's what makes it a pyramid rather than a list.
- **Procedure:**
  1. State the main conclusion/recommendation in one sentence.
  2. List the reasons supporting it; group related reasons together (MECE-style — [[mece-decomposition]]).
  3. Order the groups by what matters most to the reader's decision.
  4. Within each group, apply the same structure recursively if it's substantial: sub-conclusion first, then its support.
  5. Draft top-down: headline, then supporting structure, then details — never bottom-up.
  6. Check: could a reader stop after the first paragraph and still know your point? If not, restructure.
- **Mistakes:** building suspense into an informational document ("first, some background…"); ordering support chronologically (how you learned it) instead of by importance (what the reader needs); an executive summary that's actually just the introduction, not the conclusion.
- **Examples:** a consulting memo; a technical design doc's summary; an email requesting a decision; a legal brief's opening.
- **Related:** [[executive-summarization]], [[argument-construction]], [[progressive-disclosure]]. **Prereqs:** a formed conclusion.

---

### progressive-disclosure `atomic · D2 · ~450 tok`
Layer an explanation from gist to full depth, checking the audience's cognitive load at each layer before adding the next.

- **Why:** Dumping full detail immediately overwhelms; withholding all detail leaves the audience unable to act. Layering lets each audience member stop at the depth they need, and lets the explainer detect confusion before compounding it.
- **Inputs:** a complex topic + an audience with unknown depth-of-interest → **Outputs:** a layered explanation: a one-line gist, a short elaboration, and full detail available on demand, with checkpoints between layers.
- **Activate when:** explaining something complex to a mixed or unknown-depth audience; a first explanation attempt visibly overwhelmed the listener. **Skip when:** the audience's needed depth is already known precisely — go straight there.
- **Principles:** the first layer must stand alone as a complete (if shallow) answer, not a teaser; each subsequent layer adds detail without contradicting the previous layer's simplification — layers refine, they don't correct; check comprehension between layers rather than plowing through all of them regardless of response.
- **Procedure:**
  1. Compose the gist: one sentence that would satisfy someone who only has ten seconds.
  2. Compose the short elaboration: a paragraph adding the key mechanism or reasoning, still skippable.
  3. Prepare the full detail: available but not forced on the audience.
  4. Deliver layer one; check for the audience's response (confusion, satisfaction, a follow-up question) before proceeding.
  5. Deliver the next layer only as needed, following the audience's actual questions rather than a fixed script.
  6. Ensure the gist wasn't a lie — layers should refine, not reverse, what came before.
- **Mistakes:** a "gist" that's actually a teaser with no standalone value; barreling through all layers regardless of the audience's signals; a first layer that has to be unlearned once the detail arrives (oversimplification that misleads).
- **Examples:** explaining a technical incident to executives, then engineers, at different depths; a doctor's explanation of a diagnosis; documentation with a summary, then a guide, then a full reference.
- **Related:** [[audience-modeling]], [[explanatory-analogy]], [[pyramid-structuring]]. **Prereqs:** [[audience-modeling]] recommended.

---

### explanatory-analogy `atomic · D2 · ~450 tok`
Construct an analogy to make an unfamiliar idea graspable via a familiar one, then explicitly mark where the analogy breaks down.

- **Why:** Analogies are the fastest route into an unfamiliar concept, but an analogy presented without its limits gets over-applied by the listener — who will reason with the analogy past the point where it holds. Marking the breakage is what makes the analogy teach rather than mislead.
- **Inputs:** an unfamiliar concept + a target audience's familiar knowledge → **Outputs:** an analogy plus an explicit statement of where it stops mapping accurately.
- **Activate when:** introducing a genuinely new concept; a previous explanation attempt didn't land; simplifying for a non-expert audience. **Skip when:** precision is paramount and any distortion is unacceptable — use direct explanation instead.
- **Principles:** choose the source domain from what the *specific* audience actually knows well, not what's generically familiar; map structure (relations), not surface appearance — the best analogies transfer a mechanism; always state the boundary — "this is like X, except that…" — or the listener will over-extend it; one well-chosen analogy beats several competing ones, which confuse more than clarify.
- **Procedure:**
  1. Identify the core structure of the unfamiliar concept — the relation or mechanism that matters most.
  2. Search the audience's known domains for a matching structure (not just surface similarity).
  3. State the analogy concisely.
  4. Identify the point(s) where the analogy's structure diverges from the real concept.
  5. State the divergence explicitly as part of the explanation, not as an afterthought.
  6. Check the audience's resulting model — did they walk away with the mechanism, or just the surface image?
- **Mistakes:** choosing a vivid but structurally mismatched analogy; omitting the breakdown point, letting the audience over-extend the analogy into wrong conclusions; stacking multiple analogies that each map differently, fragmenting the mental model instead of building one.
- **Examples:** explaining a firewall as a building's security checkpoint (and where that breaks down); explaining compound interest via a snowball; explaining an immune system's tolerance via a bouncer who learns regulars.
- **Related:** [[analogical-reasoning]] (the reasoning engine this borrows), [[progressive-disclosure]], [[audience-modeling]]. **Prereqs:** none.

---

### narrative-construction `atomic · D3 · ~500 tok`
Structure material as setup, tension, and resolution so it holds attention and creates meaning through sequence, not just content.

- **Why:** Facts presented in logical (not narrative) order inform but rarely move anyone to remember or act. Narrative structure — establishing stakes, building tension, resolving it — is how humans naturally encode and retain meaning.
- **Inputs:** a set of events, facts, or a case → **Outputs:** a narrative arc: setup (stakes, context), tension (the complication or conflict), resolution (what happened or what should happen).
- **Activate when:** the goal is retention, persuasion, or emotional engagement, not just information transfer; telling a case study, a pitch, an incident story. **Skip when:** the goal is pure reference lookup — narrative structure gets in the way there (use [[pyramid-structuring]]).
- **Principles:** stakes must be established before tension, or the tension has nothing to matter against; tension should come from a genuine complication, not manufactured drama — a real narrative's tension is the actual difficulty; resolution should follow causally from the tension, not arrive as a non-sequitur; narrative and accuracy aren't in tension — selecting and sequencing true material is not distortion, as long as omissions don't change the meaning.
- **Procedure:**
  1. Identify the actual stakes: what did the audience (or the protagonist) have to lose or gain?
  2. Establish setup: enough context that the stakes are legible, no more.
  3. Identify the central tension: the real obstacle, conflict, or uncertainty.
  4. Sequence events to build that tension rather than flattening it into a list.
  5. Resolve: show what happened or is proposed, and connect it causally back to the tension.
  6. Check for accuracy: does the sequencing distort what actually happened, or just select and order truthfully?
- **Mistakes:** skipping stakes-setup, so the "tension" lands flat; manufacturing false tension not present in the actual material; a resolution that doesn't address the stated tension (narrative whiplash); using narrative structure for reference material where it obscures rather than clarifies.
- **Examples:** a case study of an incident response; a founder's pitch narrative; a courtroom opening statement; a retrospective told as a story rather than a bullet log.
- **Related:** [[pyramid-structuring]] (its opposite for reference material), [[audience-modeling]], [[persuasive-case]]. **Prereqs:** none.

---

### argument-construction `atomic · D2 · ~450 tok`
Build a claim-evidence-warrant chain with counterargument slots designed in from the start, rather than bolted on defensively.

- **Why:** Arguments built without anticipating objections either ignore them (weak) or address them as a defensive afterthought (weak differently). Building counterargument slots into the structure from the start produces an argument that survives contact with a skeptical reader.
- **Inputs:** a claim to argue for → **Outputs:** a structured argument: claim, evidence, the warrant connecting them, and pre-addressed counterarguments.
- **Activate when:** writing persuasive content meant to survive scrutiny — proposals, briefs, pitches. **Skip when:** the audience isn't skeptical and persuasion isn't the goal — informational writing wants [[pyramid-structuring]] instead.
- **Principles:** the warrant — why this evidence supports this claim — usually needs to be stated explicitly, not assumed shared; address the strongest counterargument, not the weakest (steelman it — [[steelmanning]] — before answering it); a claim with no acknowledged counterargument reads as either naive or evasive to a sophisticated audience.
- **Procedure:**
  1. State the claim precisely.
  2. Select evidence that actually supports this specific claim (not a nearby one).
  3. State the warrant: the reasoning connecting the evidence to the claim explicitly.
  4. Run [[steelmanning]] on the likely counterargument(s); select the strongest.
  5. Address it directly in the argument's structure — not as a buried footnote, but as an acknowledged and answered point.
  6. Order: claim → evidence/warrant → counterargument and response → restated claim with earned confidence.
- **Mistakes:** omitting the warrant, assuming the evidence "obviously" supports the claim; addressing only a weak counterargument (looks evasive to anyone who knows the strong one); tacking the counterargument on as an afterthought rather than integrating it.
- **Examples:** a proposal defending a controversial technical choice; a legal brief; an op-ed; a research paper's discussion section.
- **Related:** [[argument-mapping]], [[steelmanning]], [[persuasive-case]] (the composite this feeds). **Prereqs:** none.

---

### executive-summarization `atomic · D2 · ~400 tok`
Compress material to its decision-relevant essentials plus an explicit action ask, cutting everything the decision doesn't need.

- **Why:** Decision-makers' scarce resource is attention, not information — most material they receive has too much of the latter and too little of the former. A true executive summary isn't a shorter version of the document; it's the different document a decision-maker actually needs.
- **Inputs:** a full document or analysis + the decision it should inform → **Outputs:** a compressed summary: the conclusion, the key support, and a specific action ask, sized to the decision-maker's actual need.
- **Activate when:** any document going to someone who needs to decide or act, not just absorb; a draft summary is really just a shortened intro. **Skip when:** the audience needs the full detail as their primary artifact (a reference doc, not a decision brief).
- **Principles:** lead with the conclusion and the ask, not the background (pairs with [[pyramid-structuring]]); include only what's decision-relevant — interesting-but-not-decision-relevant material belongs in an appendix, not the summary; state the specific action requested — "FYI" is not an ask; length is a design choice, not a leftover — cut to what the decision needs, no more.
- **Procedure:**
  1. Identify the decision or action this document should produce.
  2. State the conclusion/recommendation in the first line.
  3. State the specific ask: approve, decide between options, provide input by a date, note and file.
  4. Include only the support directly relevant to that decision — 2–4 key points, not a compressed retelling of everything.
  5. Push everything else (methodology, full data, exploratory tangents) to an appendix or a "more detail available" pointer.
  6. Check: could the reader act on the summary alone? If not, what's missing is decision-relevant; if yes, anything beyond that is excess.
- **Mistakes:** writing a shortened introduction and calling it a summary (still leads with background, not conclusion); omitting a specific ask, leaving the reader unsure what's wanted from them; cramming supporting detail into the summary "just in case."
- **Examples:** a board memo's first page; an incident report's summary for leadership; a research summary for a non-specialist funder.
- **Related:** [[pyramid-structuring]], [[audience-modeling]], [[precision-questioning]]. **Prereqs:** a completed analysis or document to summarize.

---

### precision-questioning `atomic · D2 · ~450 tok`
Ask questions engineered to isolate exactly the missing variable, rather than general questions that invite a general (and often unhelpful) answer.

- **Why:** Vague questions get vague answers; the responder fills the gap with whatever's easiest to say, not necessarily what the asker needed. A precisely targeted question makes the needed information the path of least resistance to answer.
- **Inputs:** an information gap or point of confusion → **Outputs:** a targeted question that, if answered, closes the specific gap — plus a habit of follow-up when the answer doesn't.
- **Activate when:** eliciting requirements, debugging someone's confused explanation, running a user interview, negotiating specifics. **Skip when:** genuine open exploration is the goal — precision would prematurely narrow it (use open prompts instead, then [[active-listening]]).
- **Principles:** ask about specific instances ("walk me through the last time X happened") rather than generalities ("does X happen often?") — instances are checkable, generalities invite unreliable self-report; a question that can be answered "it depends" hasn't isolated the variable yet — narrow further; when an answer doesn't close the gap, that's information — the gap was somewhere else than assumed.
- **Procedure:**
  1. State precisely what's unknown — the specific variable, not the general topic.
  2. Draft a question that could only be answered by supplying that variable.
  3. Prefer concrete/instance-based phrasing over abstract/frequency phrasing.
  4. Ask; if the answer is vague or off-target, that reveals the gap was misdiagnosed — refine and re-ask rather than accepting a non-answer.
  5. Continue narrowing until the specific unknown is actually resolved.
- **Mistakes:** asking leading questions that supply the expected answer; accepting a vague response as sufficient because re-asking feels awkward; asking about generalities/opinions when the instance/behavior is what's actually needed.
- **Examples:** debugging "it's slow sometimes" into a specific reproducible case; a user interview probing "walk me through the last time you tried to do this" instead of "do you find this hard?"; negotiation clarifying a vague objection into its specific concern.
- **Related:** [[active-listening]], [[interview-synthesis]], [[audience-modeling]]. **Prereqs:** none.

---

### nonviolent-communication `atomic · D2 · ~500 tok`
Structure a difficult message as observation, feeling, need, and request — stripped of evaluation and blame — so it can be heard rather than defended against.

- **Why:** Evaluative language ("you always…", "you're being…") triggers defensiveness before the actual need is even heard. Separating observable fact from feeling from need from request removes the accusation and leaves something the other person can actually act on.
- **Inputs:** a grievance, conflict, or difficult message to deliver → **Outputs:** a message structured as observation → feeling → need → request, free of judgment-laden language.
- **Activate when:** delivering feedback or a grievance likely to trigger defensiveness; a conflict conversation; any message where "you did X wrong" would derail into an argument about the accusation instead of the underlying issue. **Skip when:** the situation calls for a directive instruction, not a negotiated understanding (an emergency, a clear policy violation).
- **Principles:** observation is what a camera would record — no adjectives implying judgment ("you were late" not "you're inconsiderate"); feeling is your own internal state, owned as yours, not attributed as a fact about the other person; need is the underlying human need behind the feeling, not a strategy ("I need to feel respected," not "I need you to text back faster" — that's the request); the request is specific, actionable, and genuinely a request, not a disguised demand.
- **Procedure:**
  1. State the observation: the specific, factual, camera-checkable event — strip out adjectives and generalizations ("always," "never").
  2. State the feeling it produced in you, owned as your own experience.
  3. Identify the underlying need the feeling points to.
  4. Formulate a specific, doable request — not vague ("be better") and not a disguised ultimatum.
  5. Deliver in that order; check the listener didn't hear an accusation — if defensiveness appears, the observation step likely still contained judgment.
- **Mistakes:** an "observation" that's actually a judgment in disguise ("you were dismissive" is an interpretation, not an observation); skipping the need and going straight from feeling to request (loses the "why," making the request seem arbitrary); a "request" phrased as an ultimatum.
- **Examples:** giving a partner feedback about a recurring conflict; addressing a colleague's missed commitment without triggering defensiveness; a manager raising a performance concern.
- **Related:** [[feedback-delivery]] (workplace-specific sibling), [[active-listening]], [[difficult-conversations]]. **Prereqs:** none.

---

### feedback-delivery `atomic · D2 · ~450 tok`
Deliver feedback as situation → behavior → impact, keeping it separated from identity judgments and from unsolicited advice.

- **Why:** Feedback that judges character ("you're not detail-oriented") produces defensiveness and rarely changes behavior; feedback that names the specific situation, behavior, and impact gives the recipient something concrete to act on without an identity threat to defend against.
- **Inputs:** an observed behavior and its impact → **Outputs:** a feedback message structured as situation, behavior, impact, with an optional forward-looking ask — free of character judgment.
- **Activate when:** giving performance or behavioral feedback in any professional or collaborative context. **Skip when:** the relationship calls for the fuller NVC structure ([[nonviolent-communication]]) because personal needs, not just workplace behavior, are at stake.
- **Principles:** name the specific situation (when/where) so the feedback isn't generalized into an identity trait; describe the behavior observably, not interpretively ("you interrupted three times" not "you were disrespectful"); state the actual impact — on the work, the team, the outcome — so the behavior's relevance is clear; end with a forward-looking ask when appropriate, not just a critique with nowhere to go.
- **Procedure:**
  1. Identify the specific situation: when and where this happened.
  2. Describe the observable behavior — what was said or done, not your interpretation of motive.
  3. State the impact: what resulted, on the work/team/relationship/outcome.
  4. Pause for the recipient's perspective — they may have context that changes the picture.
  5. If forward-looking, add a specific, actionable request or offer of support.
  6. Avoid trait language throughout ("you are…") — stay in situation/behavior/impact.
- **Mistakes:** generalizing a single incident into a trait ("you always…"); describing motive instead of observable behavior ("you didn't care" vs "you didn't respond for three days"); giving feedback with no forward path, leaving the recipient nowhere to go with it; skipping their side of the story.
- **Examples:** a manager addressing a missed deadline; peer feedback after a presentation; a coach addressing a recurring performance pattern.
- **Related:** [[nonviolent-communication]], [[coaching-dialogue]], [[difficult-conversations]]. **Prereqs:** none.

---

### revision-pass `atomic · D2 · ~450 tok`
Self-edit a draft in ordered, single-focus passes — structure, then argument, then clarity, then economy — rather than trying to fix everything at once.

- **Why:** Editing for everything simultaneously misses things, because attention is divided across incompatible concerns (a structural fix changes what needs a clarity fix). Ordered single-focus passes catch more and waste less rework.
- **Inputs:** a completed draft → **Outputs:** a revised draft, having passed through each focus in order, with earlier passes not re-litigated by later ones.
- **Activate when:** revising any consequential piece of writing before it ships. **Skip when:** the piece is genuinely low-stakes and a single read-through suffices.
- **Principles:** fix structure before sentences — polishing a paragraph that gets cut in the next pass is wasted work; each pass has one job — resist fixing a clarity issue during the structure pass; read the later passes aloud or against a fresh eye when possible, since silent self-reading skips over habituated errors; cutting is usually more valuable than adding at this stage.
- **Procedure:**
  1. **Structure pass:** does the order serve the reader ([[pyramid-structuring]])? Cut, reorder, or merge sections before touching sentences.
  2. **Argument pass:** does each claim have support ([[argument-mapping]])? Are counterarguments addressed? Fix logic gaps.
  3. **Clarity pass:** is each sentence understandable on one read? Cut jargon not serving the audience ([[audience-modeling]]).
  4. **Economy pass:** cut every word, sentence, or section that doesn't earn its place. Read for length last, not first.
  5. Final read for the whole: does it read as one coherent piece, not four disconnected passes stapled together?
- **Mistakes:** doing all passes at once (misses issues, since attention fragments); polishing sentences before the structure is settled (wasted work when that section gets cut); skipping the economy pass because the piece already "feels done."
- **Examples:** revising a strategy memo before it goes to leadership; editing a blog post; tightening a proposal before submission.
- **Related:** [[pyramid-structuring]], [[argument-mapping]], [[peer-review]] (external version of this). **Prereqs:** a completed draft.

---

### persuasive-case `composite · D3 · ~850 tok`
Build an audience-modeled argument with objections pre-handled — the composite that turns a claim into a case someone else will actually accept.

- **Why:** Persuasion fails at either end: not knowing the audience, or not surviving their pushback. Combining audience modeling with structured argument-building and pre-emptive counterargument handling addresses both failure points in one pipeline.
- **Inputs:** a claim you want an audience to accept or act on → **Outputs:** a structured, delivered case — audience-fit, evidenced, counterargument-hardened.
- **Dependencies:** `audience-modeling`, `argument-construction`, `steelmanning`, `pyramid-structuring`, `narrative-construction` (optional).
- **Activate when:** making a case to a specific audience with real stakes and plausible resistance — a pitch, a proposal, a negotiation opener. **Skip when:** the audience is already aligned — a persuasive structure is unneeded overhead for an easy yes.
- **Principles:** persuasion starts with the audience's existing model, not your own reasoning path to the conclusion; the strongest counterargument gets addressed, not the weakest (`steelmanning` before responding); structure carries as much weight as content — the same case lands differently ordered.
- **Procedure:**
  1. Run `audience-modeling`: their knowledge, goal, incentives, likely objections.
  2. Run `argument-construction`: claim, evidence, warrant, with the objections from step 1 fed in as the counterargument slots to pre-address via `steelmanning`.
  3. Structure via `pyramid-structuring`: conclusion first, then the case, ordered by what matters most to *this* audience's decision (not your own sense of logical build-up).
  4. If emotional engagement or memorability matters more than a fast decision, layer in `narrative-construction` around the core structure — stakes, tension, resolution — without burying the lead.
  5. Deliver; watch for the specific objection surfacing despite pre-handling — that's a signal the audience model in step 1 was incomplete, not that the objection is unaddressable.
- **Mistakes:** building the case from your own reasoning path instead of the audience's decision path; skipping straight to persuasion techniques without first modeling who's being persuaded; over-narrativizing a case that needed a fast, structured yes/no.
- **Examples:** a fundraising pitch; a policy proposal to a skeptical committee; an internal case for a controversial technical direction.
- **Related:** [[argument-construction]], [[audience-modeling]], [[negotiation]] (when the audience is a counterparty with competing interests, not just a skeptic).

---

### difficult-conversations `composite · D3 · ~950 tok`
Prepare for and conduct a high-stakes conversation — sharing a hard truth, addressing a conflict, delivering unwelcome news — without sacrificing the relationship or dodging the substance.

- **Why:** Difficult conversations fail in two opposite directions: avoided entirely (the issue festers) or delivered as an ambush (the relationship breaks). Preparation that separates the facts from the story you've told yourself, plus a structure that invites the other side in, threads that needle.
- **Inputs:** a conversation both necessary and likely to be emotionally charged → **Outputs:** a conducted conversation that addressed the substance and preserved (or appropriately recalibrated) the relationship.
- **Dependencies:** `nonviolent-communication`, `active-listening`, `empathy-mapping`, `steelmanning`.
- **Activate when:** a conversation has been avoided because it's uncomfortable but the cost of continued avoidance is rising; conflict has an emotional charge that a purely factual message would mishandle. **Skip when:** the matter is simple enough for direct, low-stakes feedback (`feedback-delivery` alone suffices).
- **Principles:** separate the facts of what happened from the story you've constructed about why (motives, character) — the story is usually where the conversation goes wrong; every difficult conversation carries three layers — the "what happened" content, the feelings involved, and each party's sense of identity at stake — prepare for all three, not just the first; the goal is usually mutual understanding and a path forward, not "winning" the account of events.
- **Procedure:**
  1. **Prepare:** separate observable facts from your interpretation/story about them. Run `empathy-mapping` on the other party — what do they likely see, feel, need?
  2. Run `steelmanning` on their probable position — enter the conversation able to state it fairly.
  3. Identify your actual goal: understanding, a changed behavior, a repaired relationship, a decision — be specific, since vague goals produce meandering conversations.
  4. **Open:** state the issue using `nonviolent-communication` structure — observation, feeling, need — avoiding the story/interpretation in the opening.
  5. **Listen:** use `active-listening` genuinely — invite and absorb their account before defending your own; their story may reveal facts that change your interpretation.
  6. **Navigate identity:** if either party's sense of competence, worth, or belonging feels threatened, name that directly rather than letting it drive the conversation from underneath.
  7. **Close:** summarize the shared understanding (even if disagreement remains) and agree on a concrete next step or request.
- **Mistakes:** opening with the story/interpretation instead of the observable facts (triggers immediate defensiveness); preparing your talking points but not genuinely preparing to listen; avoiding the identity layer, so it silently sabotages an otherwise well-structured conversation; treating "difficult" as license to skip listening because you've already decided you're right.
- **Examples:** telling a business partner their approach isn't working; addressing a betrayal of trust; a performance conversation that could end in termination; a family conflict conversation.
- **Related:** [[nonviolent-communication]], [[active-listening]], [[conflict-mediation]] (third-party version), [[coaching-dialogue]].
