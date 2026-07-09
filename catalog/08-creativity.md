# 8 · Creativity

Generating options that weren't on the table.

---

### divergent-ideation `atomic · D1 · ~400 tok`
Generate a large quantity of ideas with judgment explicitly deferred, on the principle that quantity produces quality's raw material.

- **Why:** Evaluating each idea as it's generated kills fluency — the mind self-censors toward the safe and obvious. Deferring judgment to a separate pass produces both more ideas and, reliably, better ones deeper in the list.
- **Inputs:** a prompt or problem open to multiple solutions → **Outputs:** a large raw list of ideas, unevaluated, ready for a separate convergence pass.
- **Activate when:** starting any generative task before a single approach has been chosen; a group is anchoring on the first idea proposed; brainstorming sessions. **Skip when:** evaluation criteria are the actual bottleneck, not idea supply — use [[idea-convergence]] or [[weighted-scoring]] instead.
- **Principles:** defer all judgment during generation — no "that won't work" until the separate convergence phase; quantity correlates with quality — the 50th idea is, on average, more novel than the 5th; build on others' ideas rather than only originating your own; write every idea down, including the obvious and the silly — they often trigger better ones downstream.
- **Procedure:**
  1. State the prompt precisely; set a target quantity or time-box, not a quality bar.
  2. Generate rapidly; capture everything without commentary or filtering.
  3. When generation slows, apply a push technique (constraint, random stimulus, reversal — see [[scamper]], [[random-stimulus]]) to break the plateau.
  4. Continue past the first plateau — the second wave after a push is often where the novel ideas live.
  5. Stop at the time-box or quantity target; hand the full raw list to a separate convergence step. Do not evaluate yet.
- **Mistakes:** silently evaluating while "generating" (self-censorship disguised as brainstorming); stopping at the first plateau instead of pushing through it; mixing generation and evaluation in a group setting, which suppresses quieter contributors' ideas.
- **Examples:** naming a product; generating candidate root causes before diagnosis; listing possible marketing channels; generating alternative interpretations of an ambiguous result.
- **Related:** [[idea-convergence]] (the required next phase), [[scamper]], [[morphological-analysis]]. **Prereqs:** none.

---

### scamper `atomic · D1 · ~450 tok`
Transform an existing thing by systematically applying seven operations: Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse.

- **Why:** Most novel ideas are recombinations or transformations of existing ones, not creations from nothing. SCAMPER supplies a checklist of transformation types so generation doesn't rely on unstructured inspiration.
- **Inputs:** an existing product, process, or concept to transform → **Outputs:** a set of variant ideas, one or more per operation applied.
- **Activate when:** improving or reinventing something that already exists; stuck after direct brainstorming; a mature product/process needs fresh angles. **Skip when:** starting from nothing (no existing thing to transform) — use [[divergent-ideation]] or [[random-stimulus]] instead.
- **Principles:** apply each operation deliberately and separately — don't skip to the ones that feel natural; a forced operation ("what if we eliminated this entirely?") often produces the most useful idea precisely because it's unnatural; treat the seven letters as prompts, not a rigid sequence.
- **Procedure:**
  1. State the thing being transformed precisely.
  2. **Substitute:** what component, material, person, or process could replace a part of this?
  3. **Combine:** what could this be merged or bundled with?
  4. **Adapt:** what else is like this, and what could be borrowed from it?
  5. **Modify/magnify/minify:** what if a dimension were exaggerated or shrunk?
  6. **Put to another use:** who else, or what else, could this serve as-is or with tweaks?
  7. **Eliminate:** what could be removed, simplified, or made unnecessary?
  8. **Reverse/rearrange:** what if the order, direction, or roles were inverted?
  9. Collect the resulting ideas; hand to convergence.
- **Mistakes:** only applying the operations that feel comfortable and skipping the rest; treating the output of each operation as a finished idea rather than raw material; running it without a clear starting artifact.
- **Examples:** redesigning an onboarding flow; reinventing a stale product line; improving a recurring meeting format; revising a pricing model.
- **Related:** [[divergent-ideation]], [[morphological-analysis]]. **Prereqs:** none.

---

### morphological-analysis `atomic · D2 · ~450 tok`
Decompose a design space into independent dimensions, enumerate the values each can take, then systematically recombine them to surface combinations nobody would have thought to propose directly.

- **Why:** Direct brainstorming samples the design space unevenly, clustering near familiar combinations. Building the full grid of dimensions × values forces exposure to the whole space, including the unclaimed corners.
- **Inputs:** a design or configuration problem with identifiable independent dimensions → **Outputs:** a dimension × value matrix, and a curated set of novel combinations worth exploring.
- **Activate when:** designing something with several genuinely independent parameters (a product configuration, a policy design, a narrative structure); the existing options all cluster around one combination. **Skip when:** the dimensions aren't actually independent — the grid produces nonsense combinations if they interact tightly.
- **Principles:** dimensions must be as independent as possible, or the grid generates mostly invalid combinations; enumerate the *range* of values per dimension, including extremes, before combining; the grid's size grows multiplicatively — sample or filter deliberately rather than evaluating every cell; the value is in combinations nobody proposed directly, so scan for the unusual cells, not just the familiar ones.
- **Procedure:**
  1. Identify the problem's key dimensions (aim for 3–6; more becomes unwieldy).
  2. For each dimension, list its possible values, including extreme or unconventional ones.
  3. Build the grid (mentally or explicitly) — the full cross-product of dimension values.
  4. Eliminate cells that are logically or physically impossible (dimension interactions found here should feed back into whether the dimensions were truly independent).
  5. Scan for unusual, under-explored combinations — especially ones combining an extreme value from one dimension with a conventional value from another.
  6. Select promising cells; develop them into concrete concepts.
- **Mistakes:** choosing dimensions that are actually correlated, producing a grid full of impossible cells; evaluating every single cell exhaustively instead of scanning for promising ones; treating the grid as the final design instead of raw material to develop further.
- **Examples:** product configuration space (form factor × power source × connectivity × price tier); a narrative's structural options (perspective × timeline × resolution type); policy design (enforcement mechanism × incentive type × scope).
- **Related:** [[divergent-ideation]], [[solution-space-mapping]] (family-level version of the same instinct), [[scamper]]. **Prereqs:** none.

---

### random-stimulus `atomic · D1 · ~400 tok`
Force an association between the problem and a deliberately unrelated prompt to escape the local basin of familiar ideas.

- **Why:** Idea generation tends to circle a small set of familiar concepts once the obvious ones are exhausted. An unrelated stimulus breaks that gravity by forcing a connection through genuinely foreign material.
- **Inputs:** a problem stuck in familiar territory + a source of random stimuli (word, image, object, unrelated domain) → **Outputs:** ideas generated by forcing connections between the stimulus and the problem.
- **Activate when:** divergent ideation has plateaued; the same handful of ideas keep resurfacing in different words. **Skip when:** generation hasn't plateaued yet — use plain [[divergent-ideation]] first; this is a rescue technique, not a starting move.
- **Principles:** the stimulus must be genuinely unrelated, or the technique just reproduces familiar associations; the connection is *forced*, not found — the value is in the reaching, not in a natural fit; treat every generated idea as raw material, however tenuous the link to the stimulus.
- **Procedure:**
  1. Confirm generation has plateaued on the direct approach.
  2. Select a random stimulus unrelated to the problem domain (a random word, an object in the room, an unrelated industry's practice).
  3. List the stimulus's properties, associations, or how that unrelated domain solves its analogous problems.
  4. Force a connection: for each property/association, ask "how does this relate to our problem?" — even absurd initial connections often lead somewhere via a second step.
  5. Capture whatever ideas emerge; don't filter for plausibility yet.
  6. Repeat with a fresh stimulus if the well runs dry again.
- **Mistakes:** picking a stimulus that's secretly related to the problem (defeats the purpose); giving up on a connection too quickly instead of pushing through the initial absurdity; treating this as the primary generation technique rather than a plateau-breaker.
- **Examples:** using an unrelated industry's logistics model to rethink a supply chain; a random object's properties triggering a new UI metaphor; a nature analogy breaking an engineering design fixation.
- **Related:** [[divergent-ideation]], [[analogical-reasoning]], [[concept-blending]]. **Prereqs:** a plateaued generation session.

---

### creative-constraints `atomic · D2 · ~400 tok`
Deliberately add artificial constraints to a generative task, since bounded problems provoke more inventive solutions than open ones.

- **Why:** Unlimited freedom paradoxically produces conventional output — without a forcing function, the mind defaults to the familiar. A well-chosen constraint eliminates the easy answers and forces genuine invention.
- **Inputs:** an open-ended generative task → **Outputs:** ideas generated under an artificial constraint, plus an assessment of which constraint-forced ideas survive removing the constraint.
- **Activate when:** ideation under full freedom is producing only conventional output; a team needs to break out of "the way we've always done it." **Skip when:** the task is already meaningfully constrained (real-world constraints are enough; don't stack artificial ones on top).
- **Principles:** the constraint should eliminate the *default* solution specifically, not just add friction randomly; arbitrary constraints work — the mind doesn't need the constraint to be "meaningful" to be provoked by it; after generating under constraint, test whether the idea holds up once the artificial constraint is lifted — some ideas only make sense within it.
- **Procedure:**
  1. Identify the default, obvious solution the task keeps producing.
  2. Choose a constraint that specifically rules that default out (a budget of zero, a deadline of one day, no use of the primary resource, a required absurd element).
  3. Generate solutions within the constraint via [[divergent-ideation]].
  4. For promising ideas, test removing the constraint: does the idea still hold value, or was it only a workaround?
  5. Keep the ideas that survive constraint removal; discard pure workarounds unless the constraint is permanent.
- **Mistakes:** choosing a constraint too weak to eliminate the default answer; forgetting to test ideas after removing the constraint (keeping brittle workarounds); applying constraints to an already tightly-constrained problem, adding friction without payoff.
- **Examples:** "design this with zero budget" to find the truly essential feature; "explain this in one sentence" to force clarity; a writing exercise banning the most common word in the genre.
- **Related:** [[divergent-ideation]]. **Prereqs:** none.

---

### concept-blending `atomic · D3 · ~500 tok`
Merge two distinct conceptual frames into a new blended space, then develop the emergent properties that neither source frame had alone.

- **Why:** Some of the most novel ideas aren't found in either source domain but emerge specifically from their combination — properties that exist only in the blend. This is a stronger, generative move than simple analogy transfer.
- **Inputs:** two distinct conceptual frames or domains → **Outputs:** a blended concept with its emergent properties identified and developed.
- **Activate when:** two domains both seem relevant but neither alone solves the problem; naming or designing something that needs to evoke two different ideas at once. **Skip when:** a straightforward transfer from one domain suffices — that's [[analogical-reasoning]], simpler and often sufficient.
- **Principles:** a blend is not an average of the two frames — it's a new space with its own emergent logic, which is where the value lives; identify what structure each frame contributes before merging, so the blend is intentional rather than accidental; the interesting output is usually the property that surprises you — neither source frame predicted it.
- **Procedure:**
  1. Name the two source frames precisely; identify each one's key structure (roles, relations, dynamics).
  2. Find the partial mapping between them — what corresponds to what, and where do they diverge?
  3. Construct the blend: a space that inherits selected structure from both, resolving conflicts deliberately.
  4. Run the blend forward — what happens in this blended space that wouldn't happen in either source alone? These are the emergent properties.
  5. Evaluate whether the emergent properties are useful, novel, and coherent — or just confused.
  6. Develop the useful ones into concrete ideas.
- **Mistakes:** producing a superficial mashup (just naming two things together) instead of running the blend's emergent logic forward; forcing a blend where the frames don't share enough structure to merge coherently; stopping at the mapping step without generating the emergent properties, which is where the actual creative payoff is.
- **Examples:** a "wiki" (encyclopedia + open collaborative editing) as a blend with emergent properties (versioning, edit wars) neither source predicted; gamification blending game mechanics with a non-game task; a hybrid organizational structure blending startup and cooperative governance.
- **Related:** [[analogical-reasoning]], [[random-stimulus]]. **Prereqs:** none.

---

### perspective-rotation `atomic · D2 · ~450 tok`
Re-solve the same problem from a series of systematically different viewpoints, then compare what each vantage surfaces.

- **Why:** A single viewpoint anchors the whole solution space around what that vantage notices. Rotating through genuinely different viewpoints — including non-human and adversarial ones — surfaces considerations invisible from the default seat.
- **Inputs:** a problem being solved from one habitual viewpoint → **Outputs:** solutions or insights generated from multiple deliberate viewpoints, compared for what each uniquely reveals.
- **Activate when:** a solution feels complete but stakeholder pushback keeps surfacing; designing for users unlike yourself; a decision looks different depending on who you ask. **Skip when:** the problem genuinely has only one relevant perspective.
- **Principles:** choose viewpoints deliberately different from the default and from each other — a rotation through similar viewpoints adds little; include viewpoints normally excluded (the harshest critic, the most vulnerable stakeholder, a non-expert, an adversary, a future/past version of the situation); the value is in the *differences* between viewpoints' outputs, not in any single one being "right."
- **Procedure:**
  1. Solve or analyze the problem from the default/habitual viewpoint first; note it explicitly so it can be compared.
  2. Select 3–4 deliberately different viewpoints (a specific persona, an adversary, a regulator, a beginner, a domain expert from an unrelated field, a future retrospective view).
  3. Re-solve or re-analyze from each viewpoint in turn, genuinely inhabiting its priorities and blind spots rather than just labeling the same answer with a new name.
  4. Compare outputs: where do they converge (robust insight) and where do they diverge (viewpoint-dependent, worth resolving explicitly)?
  5. Integrate: which divergences reveal a real gap in the original solution?
- **Mistakes:** rotating through viewpoints that are all subtly the same (e.g., different flavors of "expert"); doing this superficially — describing the viewpoint instead of actually reasoning from within it; treating one viewpoint's answer as automatically overriding the others instead of integrating the divergence.
- **Examples:** designing a policy from the perspective of its most affected minority; redesigning a product by rotating through novice, power-user, and support-team viewpoints; strategy review from a regulator's and a competitor's vantage.
- **Related:** [[empathy-mapping]], [[stakeholder-mapping]], [[red-teaming]]. **Prereqs:** none.

---

### idea-convergence `atomic · D2 · ~450 tok`
Cluster, score, and select from a large idea pool without prematurely killing the variance that divergent generation worked to produce.

- **Why:** Divergent ideation fails if the follow-on evaluation just picks the most familiar-sounding idea from the pile. Convergence needs its own discipline — clustering to find themes, and scoring that doesn't punish novelty for being unfamiliar.
- **Inputs:** a large raw idea pool (from [[divergent-ideation]] or similar) → **Outputs:** a shortlist of selected ideas with rationale, plus the clusters/themes the pool revealed.
- **Activate when:** immediately after any divergent generation phase; too many options exist to evaluate individually. **Skip when:** the pool is already small enough to compare directly ([[weighted-scoring]] suffices).
- **Principles:** cluster before scoring — grouping related ideas reveals themes and prevents near-duplicates from splitting votes; score on criteria set *before* seeing which idea would win under them (same discipline as [[weighted-scoring]]); protect at least one wildcard — the least conventional idea that clears a minimum bar — from being cut purely for unfamiliarity; convergence is a separate pass from generation, never interleaved.
- **Procedure:**
  1. Cluster the raw idea pool into themes; note ideas that don't fit any cluster (often the most novel — don't discard automatically).
  2. Set evaluation criteria explicitly, before scoring individual ideas.
  3. Score representative ideas per cluster, not every single raw idea.
  4. Select a shortlist balancing top scorers with at least one deliberate wildcard.
  5. For shortlisted ideas, note what would need to be true for them to work — sets up further development or a decision pipeline.
- **Mistakes:** scoring the raw, unclustered pool (near-duplicate conventional ideas dominate by sheer count); setting criteria after seeing the ideas (reverse-engineered to favor a favorite); cutting every unconventional idea because it scores awkwardly on criteria built around the familiar.
- **Examples:** narrowing 60 brainstormed product names to 5; selecting from a morphological-analysis grid's promising cells; picking finalist concepts from an ideation sprint.
- **Related:** [[divergent-ideation]] (upstream), [[weighted-scoring]], [[ideation-sprint]]. **Prereqs:** a generated idea pool.

---

### ideation-sprint `composite · D2 · ~800 tok`
Diverge, cross-pollinate, and converge in explicit phase-gated stages, so a group generates broadly before narrowing and never blurs the two.

- **Why:** Group ideation's most common failure is collapsing divergence and convergence into one continuous conversation, where early critique suppresses the very ideas that later turn out best. Hard phase gates protect divergence long enough to pay off.
- **Inputs:** a problem suited to group or extended solo ideation → **Outputs:** a shortlist of developed concepts plus the full raw pool for future reference.
- **Dependencies:** `divergent-ideation`, `scamper` or `random-stimulus` (plateau-breakers), `idea-convergence`.
- **Activate when:** a group needs to generate and select new concepts under time pressure; kicking off a design or strategy effort that needs fresh options. **Skip when:** the problem needs individual deep work more than breadth, or only one person is involved with a narrow, well-defined space.
- **Principles:** each phase has a different, incompatible mindset (generative vs evaluative) — never run them simultaneously; cross-pollination (sharing/building on others' ideas) between individual and group generation multiplies output beyond either alone; explicit phase gates (a stated transition) give quieter contributors protection from premature critique.
- **Procedure:**
  1. **Frame:** state the problem and constraints precisely (`problem-framing` upstream if not already done).
  2. **Diverge (solo):** individuals run `divergent-ideation` independently first, to avoid anchoring on the first spoken idea.
  3. **Cross-pollinate:** share individual lists; explicitly build on others' ideas ("yes, and…"); apply `scamper` or `random-stimulus` if the group plateaus.
  4. **Gate:** declare divergence closed. No new criticism of ideas generated so far is allowed to leak backward.
  5. **Converge:** run `idea-convergence` — cluster, set criteria, score, shortlist with a protected wildcard.
  6. **Develop:** briefly flesh out the shortlist into concepts concrete enough for the next decision stage.
- **Mistakes:** letting evaluation comments happen during the diverge phase (kills the phase's purpose even if unintentional); skipping the solo-first step and going straight to group brainstorming (anchors everyone on the loudest first idea); no explicit gate, so the group drifts from generating into arguing without noticing.
- **Examples:** a product naming sprint; a design studio's concept-generation day; a hackathon's ideation kickoff; a strategy offsite's opening session.
- **Related:** [[divergent-ideation]], [[idea-convergence]], [[session-design]] (structures the surrounding meeting).
