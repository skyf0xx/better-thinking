# 11 · Learning & Teaching

Acquiring and transmitting understanding.

---

### self-explanation `atomic · D1 · ~400 tok`
Explain material in your own plain terms, out loud or in writing, and treat every gap or hand-wave in that explanation as a gap in your actual understanding.

- **Why:** Recognition (this looks familiar) is easily mistaken for understanding, but recognition doesn't transfer. The act of generating an explanation forces retrieval and exposes exactly where the model breaks down — which passive review never does.
- **Inputs:** material you believe you understand → **Outputs:** a plain-language explanation, with the specific points where it broke down or got hand-wavy flagged as the actual study targets.
- **Activate when:** after learning something and before assuming it's understood; before teaching or presenting it to someone else; when a familiar-feeling topic needs to be actually verified. **Skip when:** the material is genuinely simple enough that the check is unnecessary.
- **Principles:** explain to an imagined listener with no prior context — this forces you past your own compressed mental shorthand; a hand-wave ("and then it just works") is a precise map of what you don't understand; explaining from memory, not while re-reading the source, is what makes this diagnostic rather than just summarizing.
- **Procedure:**
  1. Close the source material.
  2. Explain the concept from memory, in plain language, as if to someone unfamiliar with it.
  3. Notice every point where the explanation gets vague, jumps a step, or relies on "it just does X."
  4. Mark those points as the actual gaps — not the topic broadly, but the specific step.
  5. Return to the source specifically to close those gaps, not to re-review everything.
  6. Re-explain from memory to confirm the gap closed.
- **Mistakes:** re-reading instead of recalling from memory (defeats the retrieval effect); treating fluent-sounding explanation as proof of understanding without probing the mechanism steps; explaining only the parts already comfortable and skipping the hard parts.
- **Examples:** explaining a new algorithm before using it in code; explaining a legal concept before applying it to a case; a student self-testing before an exam.
- **Related:** [[knowledge-gap-analysis]], [[transfer-testing]], [[error-analysis]]. **Prereqs:** none.

---

### knowledge-gap-analysis `atomic · D2 · ~450 tok`
Map what's known, what's unknown-but-findable, and what's unknown-unknown for a task, so effort goes to the actual gap rather than re-covering the known.

- **Why:** Learning effort defaults to comfortable review of what's already known, because the genuinely unknown is harder to locate and harder to sit with. Explicitly mapping the boundary redirects effort to where it's needed.
- **Inputs:** a task or domain to become competent in → **Outputs:** a three-part map (known / known-unknown / unknown-unknown, best-effort) with a prioritized closing plan for the gaps that matter.
- **Activate when:** starting to learn a new domain or skill for a specific task; feeling like "I don't know what I don't know." **Skip when:** the domain is narrow and fully specified already.
- **Principles:** known-unknowns (you know the question exists, just not the answer) are addressable directly; unknown-unknowns require deliberately probing the domain's edges — talking to experts, surveying the field's structure — since you can't look up a question you don't know to ask; not all gaps matter equally — prioritize by what the task actually requires, not by completeness for its own sake.
- **Procedure:**
  1. State the task and what competent performance requires.
  2. List what's already known and verified (via [[self-explanation]] if uncertain).
  3. List known-unknowns: specific questions you know you need answered.
  4. Probe for unknown-unknowns: what would an expert in this domain check that a novice wouldn't think to ask? Survey the field's map/outline, talk to a practitioner, or find a syllabus/framework covering the domain's scope.
  5. Prioritize gaps by relevance to the task, not comprehensiveness.
  6. Build a closing plan targeting the highest-priority gaps first.
- **Mistakes:** only addressing known-unknowns while unknown-unknowns silently determine failure; treating gap-mapping as a one-time exercise instead of revisiting as the task's real shape emerges; over-indexing on comprehensive coverage instead of task-relevant priority.
- **Examples:** onboarding into a new codebase or domain; preparing for a negotiation in an unfamiliar industry; a new manager mapping what they don't know about their team's actual work.
- **Related:** [[question-decomposition]], [[mental-model-extraction]], [[curriculum-design]]. **Prereqs:** none.

---

### mental-model-extraction `atomic · D3 · ~500 tok`
Distill an expert's practice, a corpus, or a body of experience into an explicit, transferable model — making tacit expertise teachable.

- **Why:** Experts routinely can't fully articulate what they do — much of their skill is compiled into fast, tacit pattern recognition. Deliberately reconstructing the model behind their judgment is what makes it transferable to someone else, rather than staying locked in one person's head.
- **Inputs:** access to an expert's judgment/decisions (direct or via a corpus of their work) → **Outputs:** an explicit model — the cues they attend to, the heuristics they apply, the exceptions they carve out — that a novice could learn from.
- **Activate when:** trying to learn from an expert whose explanations feel thin ("I just know"); building training material or documentation from tacit expertise; onboarding a successor. **Skip when:** the expertise is already fully codified and explicit — nothing to extract.
- **Principles:** ask about specific past instances/decisions, not general philosophy — "walk me through the last hard case" surfaces the actual model, "what's your approach?" surfaces a post-hoc rationalization; look for what the expert notices that a novice wouldn't (the actual differentiator) rather than generic advice; test the extracted model against a new instance to see if it actually predicts the expert's judgment.
- **Procedure:**
  1. Gather specific instances of the expert's judgment — actual decisions, actual cases, not generalized advice.
  2. For each instance, probe (`precision-questioning`) what specifically they noticed, what they weighed, and why this case differed from a superficially similar one that would have gotten a different call.
  3. Look across instances for repeated cues and decision rules — that's the model taking shape.
  4. Draft the model explicitly: the cues attended to, the heuristics applied, the known exceptions.
  5. Test it: present the model's predictions on a new case to the expert — where do they disagree with the model's call? That disagreement refines the model further.
  6. Iterate until the model's predictions match the expert's actual judgment closely.
- **Mistakes:** accepting the expert's stated general philosophy as the model, when their actual practice on specific cases contradicts or refines it; extracting from too few instances to see the real pattern; skipping the validation step, so an untested model gets taught as if proven.
- **Examples:** turning a master diagnostician's intuition into a checklist; codifying a senior negotiator's read on when to walk away; documenting a veteran engineer's debugging instincts.
- **Related:** [[analogical-reasoning]], [[interview-synthesis]], [[curriculum-design]]. **Prereqs:** [[precision-questioning]] helps.

---

### deliberate-practice-design `atomic · D3 · ~500 tok`
Isolate a specific weakness, design a drill at the edge of current ability, and add immediate feedback — the structure that turns repetition into improvement.

- **Why:** Mere repetition (playing more games, writing more code) plateaus fast, because it doesn't target the specific bottleneck skill or provide the feedback needed to correct it. Deliberate practice's structure — narrow target, edge-of-ability difficulty, immediate feedback — is what actually produces improvement.
- **Inputs:** a skill area with a plateaued or slow-improving performer → **Outputs:** a drill targeting the specific weak sub-skill, calibrated to be hard but achievable, with a feedback mechanism attached.
- **Activate when:** general practice has plateaued; a specific weakness has been identified but not isolated into a targeted drill; designing training or coaching programs. **Skip when:** the learner is still in broad exposure/exploration phase — deliberate practice targets a known bottleneck, and one may not yet be identifiable.
- **Principles:** target one specific sub-skill at a time, not the whole performance — global practice diffuses the improvement signal; difficulty should sit at the edge of current ability — too easy produces no adaptation, too hard produces frustration without learning; feedback must be immediate and specific, or errors get practiced as often as corrections; volume without targeting is just repetition, not deliberate practice.
- **Procedure:**
  1. Identify the specific sub-skill that's the current bottleneck (via [[error-analysis]] on recent performance).
  2. Design a drill isolating that sub-skill, stripped of the surrounding task's other demands.
  3. Calibrate difficulty: challenging enough to require real effort, achievable enough that success is reachable with focus.
  4. Build in immediate feedback — a way to know right away whether each attempt succeeded and why.
  5. Practice in focused, bounded sessions rather than diffuse extended repetition.
  6. Reassess after a practice block: has the bottleneck moved? Re-target the new bottleneck.
- **Mistakes:** practicing the whole task repeatedly instead of isolating the weak sub-skill; setting difficulty too low (comfortable but non-adaptive) or too high (frustrating, no clear feedback signal); no feedback loop, so errors get reinforced as often as corrected.
- **Examples:** a musician drilling a specific difficult passage in isolation rather than playing the whole piece repeatedly; a programmer targeting a specific weak algorithm category; a public speaker drilling openings separately from full talks.
- **Related:** [[error-analysis]], [[scaffolding]], [[transfer-testing]]. **Prereqs:** [[error-analysis]] to identify the target.

---

### scaffolding `atomic · D3 · ~450 tok`
Provide support calibrated to the edge of a learner's current ability, and deliberately withdraw it as competence grows.

- **Why:** Too much support prevents the learner from building the ability themselves (they succeed via the scaffold, not their own skill); too little support at the wrong stage causes failure that teaches nothing. Calibrating support to the zone just beyond independent ability, and fading it, is what actually builds capability.
- **Inputs:** a learner working on a task beyond their current independent ability → **Outputs:** a support structure appropriate to their current level, with an explicit fade plan as competence grows.
- **Activate when:** teaching or onboarding anyone into a task harder than their current independent capability; designing curriculum or training progressions. **Skip when:** the task is already within the learner's independent ability — scaffolding there just creates dependency.
- **Principles:** identify the zone between what the learner can do alone and what they can't do even with help — support belongs in the zone between (doable with help, not yet doable alone); the specific type of support matters — sometimes it's a worked example, sometimes a partial solution, sometimes just a prompting question; scaffolding must be actively withdrawn on a plan, or it becomes a permanent crutch instead of a temporary bridge.
- **Procedure:**
  1. Assess what the learner can currently do independently.
  2. Assess what's beyond reach even with support (not yet the target — that's premature).
  3. Identify the zone in between: doable with help, not yet doable alone — that's where the task should be pitched.
  4. Choose the support type: worked examples, partial scaffolds (some steps done, others left), prompting questions, or direct modeling — matched to what's actually missing.
  5. As the learner succeeds with support, deliberately reduce it — fewer prompts, more independent steps.
  6. Confirm the skill transferred by testing fully unsupported performance.
- **Mistakes:** pitching the task in the "can't do even with help" zone (produces failure, not learning); leaving scaffolding in place indefinitely instead of fading it (creates dependency, not competence); providing the wrong type of support (e.g., giving the answer when a prompting question would have let them find it themselves).
- **Examples:** a coding bootcamp's progression from guided exercises to independent projects; training wheels removed progressively; a manager delegating with decreasing check-in frequency as a report's competence grows.
- **Related:** [[deliberate-practice-design]], [[curriculum-design]], [[transfer-testing]]. **Prereqs:** an assessed ability level.

---

### learning-objectives `atomic · D2 · ~450 tok`
Define what a learner should be able to do, observably, and at what cognitive level — before designing any instruction toward it.

- **Why:** Instruction designed without a clear, observable target tends to optimize for covering content rather than producing capability. Naming the objective at the right cognitive level (recall vs application vs synthesis) determines what teaching method and assessment will actually work.
- **Inputs:** a learning goal → **Outputs:** an objective stated as an observable behavior at a specified cognitive level (Bloom's taxonomy or equivalent), which the rest of instruction design targets.
- **Activate when:** designing any teaching, training, or documentation with a specific capability goal; a course or onboarding plan currently just lists topics instead of outcomes. **Skip when:** the "learning" is purely for interest/enrichment with no specific capability target.
- **Principles:** state the objective as an observable action ("can diagnose X given Y"), not a vague aspiration ("understands X"); name the cognitive level explicitly — remembering a fact, applying a procedure, analyzing a novel case, and creating something new are different targets requiring different instruction and different assessment; instruction and assessment should match the objective's level — a recall-level quiz can't verify an application-level objective.
- **Procedure:**
  1. State what the learner should be able to *do*, not just know, at the end.
  2. Identify the cognitive level: recall, comprehension, application, analysis, synthesis/creation, evaluation.
  3. Phrase the objective with an observable verb matched to that level (define/explain vs apply/diagnose vs design/critique).
  4. Check: could you write an assessment task that would directly verify this objective? If not, it's still too vague.
  5. Use the objective and its level to select the instruction method (see [[curriculum-design]]) and the assessment ([[transfer-testing]]).
- **Mistakes:** writing objectives as topics ("covers X") instead of capabilities ("can do X"); mismatching assessment level to objective level (testing recall for an application-level goal); objectives so vague that no assessment could confirm them.
- **Examples:** a training program's stated outcomes; a course syllabus's learning goals; an onboarding plan's competency checklist.
- **Related:** [[curriculum-design]], [[transfer-testing]], [[knowledge-gap-analysis]]. **Prereqs:** none.

---

### error-analysis `atomic · D2 · ~450 tok`
Classify mistakes by type and root cause, and target instruction or practice at the pattern behind them — not at the individual instance.

- **Why:** Correcting each mistake as a one-off instance misses the underlying pattern generating a whole class of errors. Classifying errors by cause (a missing concept, a misapplied rule, a careless slip) determines what kind of intervention will actually fix it.
- **Inputs:** a set of mistakes/errors from performance → **Outputs:** an error taxonomy with root causes, and the specific pattern(s) worth targeting.
- **Activate when:** reviewing test results, code review feedback, or any recurring-mistake pattern; designing a targeted intervention rather than generic "be more careful" feedback. **Skip when:** there's only one isolated mistake with no pattern to extract.
- **Principles:** distinguish a slip (knew the right answer, executed carelessly) from a misconception (systematically wrong mental model) from a gap (never learned this) — each needs a different fix; look across multiple errors for the repeated pattern rather than treating each as independent; the same surface mistake can stem from different root causes in different people — diagnose, don't assume.
- **Procedure:**
  1. Collect a representative set of errors, not just the most recent one.
  2. For each, classify: slip (careless, knew better), misconception (systematic wrong model), or gap (never learned).
  3. Look for the repeated pattern across errors — often several surface mistakes trace to one underlying misconception.
  4. For misconceptions, identify specifically what the wrong model is (not just that it's wrong) — this is what teaching needs to directly address and correct.
  5. Target the intervention to the cause: slips need attention/process fixes, misconceptions need direct confrontation with the wrong model, gaps need instruction.
  6. Re-test after intervention to confirm the pattern, not just the instance, is resolved.
- **Mistakes:** treating every error as a slip ("be more careful") when it's actually a misconception requiring real correction; correcting instances one by one without ever extracting the pattern; assuming the same error type has the same cause across different learners.
- **Examples:** grading a batch of exams for the recurring misconception, not just marking each wrong answer; code review patterns revealing a systematic misunderstanding of a language feature; a coach identifying a repeated technical flaw across multiple performances.
- **Related:** [[deliberate-practice-design]], [[self-explanation]], [[root-cause-investigation]] (same logic, applied to systems instead of learners). **Prereqs:** none.

---

### transfer-testing `atomic · D3 · ~450 tok`
Verify real understanding by applying it in a structurally novel context — one that shares the underlying principle but not the surface features of how it was learned.

- **Why:** Performance on problems structurally identical to the training examples can reflect pattern-matching to surface features rather than genuine understanding of the underlying principle. A structurally novel test is what actually distinguishes the two.
- **Inputs:** a claimed understanding of a concept or skill → **Outputs:** a verdict on whether the understanding transfers, tested via a novel-surface, same-principle application.
- **Activate when:** confirming a learner (including yourself) actually understands a principle, not just recognizes familiar problems; before relying on a skill in a new context. **Skip when:** near-transfer within the same context is all that's actually needed (rare, but sometimes true).
- **Principles:** the test problem must share the deep structure (the actual principle) while differing in surface features (context, framing, domain) from how it was learned; failure on a transfer test is diagnostic, not just disappointing — it locates exactly which part of the "understanding" was actually surface pattern-matching; near-transfer (same domain, new instance) is weaker evidence than far-transfer (different domain, same principle).
- **Procedure:**
  1. Identify the underlying principle the learner is meant to have grasped.
  2. Construct a test scenario with different surface features but the same underlying principle.
  3. Present it without signaling "this is the same as what you learned" — the whole test is whether they see the structural match themselves.
  4. Observe whether they apply the principle correctly, or fail to recognize its relevance under the new surface.
  5. On failure, diagnose (via [[error-analysis]]) whether the gap is the principle itself or just the transfer/recognition step.
  6. Prefer far-transfer tests (different domain) over near-transfer (same domain, new numbers) for a stronger verdict.
- **Mistakes:** testing with a superficially different but structurally identical problem (still surface pattern-matching, not real transfer); interpreting a failed transfer test as "they don't understand at all" rather than diagnosing which piece broke; only ever testing near-transfer, overestimating how robust the understanding is.
- **Examples:** testing a math principle in a word-problem context different from how it was taught; testing whether a negotiation principle learned in one domain applies in an unrelated one; a hiring interview's case study designed to differ from the candidate's past work.
- **Related:** [[self-explanation]], [[error-analysis]], [[analogical-reasoning]]. **Prereqs:** a stated learning objective.

---

### socratic-teaching `composite · D3 · ~900 tok`
Lead a learner to construct an insight themselves through a sequenced series of questions, rather than delivering the conclusion directly.

- **Why:** An insight the learner constructs themselves is more durable and better integrated than one they're told, because the reasoning path — not just the conclusion — gets built and owned. The skill is in the sequencing: each question should be answerable from what the learner already has, and should set up the next.
- **Inputs:** a learner with the prerequisite knowledge to reach a target insight, given the right sequence of questions → **Outputs:** the learner arriving at the insight themselves, with the reasoning path they used made explicit.
- **Dependencies:** `knowledge-gap-analysis`, `precision-questioning`, `scaffolding`.
- **Activate when:** the learner has the prerequisites to reach the insight and time allows for the (slower) discovery process; a delivered answer has previously failed to stick. **Skip when:** the learner lacks the prerequisites (questions alone can't summon knowledge they don't have — teach the prerequisite directly first), or time genuinely doesn't allow the slower path.
- **Principles:** each question must be answerable using what the learner already knows or can directly observe — a question that requires the missing insight to answer isn't scaffolded properly; the sequence should narrow toward the target insight without ever stating it — if you have to give the answer, the sequence broke down at that point, not "failed"; genuine curiosity about their answer, not a rhetorical trap toward a predetermined "gotcha," keeps this a real dialogue rather than a lecture in disguise.
- **Procedure:**
  1. Identify the target insight precisely, and run `knowledge-gap-analysis` to confirm the learner has the prerequisites to reach it.
  2. Design a question sequence: start from what they already know or can observe; each question's answer should supply what the next question needs.
  3. Ask the first question; use `precision-questioning` discipline — specific enough to be answerable, not so leading it gives away the answer.
  4. When the learner answers, build the next question from their actual answer (not a scripted next step) — this keeps it a real dialogue.
  5. If they get stuck, back up and scaffold (`scaffolding`) with an easier intermediate question rather than supplying the answer.
  6. When they reach the insight, have them state it in their own words and, ideally, explain how they got there — this cements the reasoning path, not just the conclusion.
- **Mistakes:** asking questions with an unreachable answer given the learner's current knowledge (frustration, not discovery); caving and delivering the answer at the first sign of struggle instead of backing up to scaffold; running a scripted sequence regardless of the learner's actual answers, turning it into a lecture with question marks.
- **Examples:** a teacher leading a student to derive a mathematical relationship rather than stating it; a manager helping a report discover a design flaw themselves rather than pointing it out; classic Socratic dialogue on a philosophical question.
- **Related:** [[scaffolding]], [[precision-questioning]], [[coaching-dialogue]] (same spirit, applied to decisions rather than insights).

---

### curriculum-design `composite · D4 · ~1000 tok`
Sequence learning objectives, instruction, and assessment coherently across a full learning arc — from where the learner starts to where they need to end up.

- **Why:** Ad hoc instruction (a pile of good individual lessons with no overall sequence) leaves gaps and redundancies invisible until a learner fails downstream. Designing the full arc — objectives, sequence, instruction method, assessment — as one coherent system catches this before it costs a learner's time.
- **Inputs:** a target capability + a starting population's current level → **Outputs:** a sequenced curriculum: ordered objectives, matched instruction methods, and assessments that verify each stage before the next depends on it.
- **Dependencies:** `learning-objectives`, `knowledge-gap-analysis`, `scaffolding`, `deliberate-practice-design`, `transfer-testing`.
- **Activate when:** designing a training program, course, or structured onboarding — anything with multiple sequenced learning stages. **Skip when:** the learning need is a single isolated skill with no real prerequisite chain — a single [[learning-objectives]] pass suffices.
- **Principles:** sequence by prerequisite dependency, not by topic convenience — a learner shouldn't hit stage 3's material needing stage 5's concept; each stage needs its own objective (`learning-objectives`) and its own way to verify mastery before the learner proceeds, or gaps compound silently; instruction method should match the objective's cognitive level at each stage — a recall-level early stage might use direct instruction, an application-level later stage needs `deliberate-practice-design`; build in `transfer-testing`, not just recall checks, at key checkpoints — passing a recall quiz can mask a transfer failure that derails later stages.
- **Procedure:**
  1. Define the terminal capability precisely (`learning-objectives` for the end-state).
  2. Run `knowledge-gap-analysis` against the target learner population's actual starting point.
  3. Decompose the terminal objective into a prerequisite chain of sub-objectives — what must be mastered before what.
  4. Sequence stages by that dependency chain, not by superficial topic grouping.
  5. For each stage, set the objective's cognitive level and match instruction accordingly — direct teaching for recall/comprehension stages, `scaffolding` plus `deliberate-practice-design` for application/analysis stages.
  6. Insert assessment checkpoints between stages, including `transfer-testing` at key junctures, not just end-of-course.
  7. Pilot with a small group; use checkpoint failures to find where the sequence assumed a prerequisite that wasn't actually built.
- **Mistakes:** sequencing by topic/chapter convenience instead of actual prerequisite dependency; skipping checkpoint assessment, letting a gap at stage 2 silently sabotage stage 5; using recall-level assessment throughout even when later objectives require application/transfer, masking real gaps until it's too late to cheaply fix them.
- **Examples:** a technical training program's module sequence; a university course's syllabus design; a company's structured onboarding curriculum; a coaching program's skill progression.
- **Related:** [[learning-objectives]], [[scaffolding]], [[knowledge-gap-analysis]], [[socratic-teaching]] (as one instruction method within the curriculum).
