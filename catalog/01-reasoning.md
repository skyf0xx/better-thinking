# 1 · Foundational Reasoning

The inference primitives. Everything else composes these.

---

### first-principles `atomic · D3 · ~600 tok`
Decompose a problem into base truths and rebuild the solution without inherited assumptions.

- **Why:** Most reasoning is reasoning-by-convention; when the convention is wrong or the situation is novel, it fails silently. This skill escapes inherited framing.
- **Inputs:** a problem plus the conventional approach/beliefs around it → **Outputs:** a list of verified base facts, a list of discarded assumptions, a rebuilt solution path.
- **Activate when:** the standard answer feels expensive, impossible, or arbitrary; entering a novel domain; someone says "that's just how it's done." **Skip when:** the domain is mature and the convention is cheap to follow.
- **Principles:** distinguish physics from policy (what's truly impossible vs merely customary); every "requirement" must trace to a base fact or be discarded; rebuild bottom-up, not by patching the old design.
- **Procedure:**
  1. State the problem and the conventional solution.
  2. List every assumption embedded in the conventional solution.
  3. For each assumption ask: is this a law of the domain, or an artifact of history/incentive/habit? Keep only laws.
  4. State the surviving base truths explicitly.
  5. Rebuild a solution using only base truths, ignoring the old design.
  6. Compare rebuilt vs conventional; explain each divergence.
  7. Report which discarded assumptions carry the most risk if you're wrong about them.
- **Mistakes:** stopping decomposition one level too early (treating a convention as a law); rebuilding into the same design by anchoring; using it on well-solved problems where convention encodes real learning.
- **Examples:** questioning why a rocket costs $60M when its materials cost $2M; asking why a hiring process requires degrees; re-deriving a pricing model from unit costs instead of competitor prices.
- **Related:** [[assumption-audit]] (the extraction step generalized), [[chestertons-fence]] (the counterweight — understand before discarding). **Prereqs:** none.

---

### deductive-validation `atomic · D2 · ~450 tok`
Check whether a conclusion actually follows from its premises, independent of whether the premises are true.

- **Why:** Invalid arguments with true-sounding premises are the most persuasive form of wrong. Separating validity from truth catches them.
- **Inputs:** an argument (explicit or reconstructed) → **Outputs:** verdict of valid/invalid, the specific inferential gap if invalid, and separately, an assessment of premise truth.
- **Activate when:** evaluating any "therefore"; a conclusion feels off but the premises seem fine (or vice versa). **Skip when:** the argument is explicitly probabilistic — use [[bayesian-updating]].
- **Principles:** validity is about form, not content; an argument can be valid with false premises and invalid with true ones; hidden premises do the most damage.
- **Procedure:**
  1. Restate the argument as numbered premises and a conclusion.
  2. Surface unstated premises needed to make the inference work; add them explicitly.
  3. Test form: could the premises all be true while the conclusion is false? Construct the counterexample world if so.
  4. Only then assess each premise's truth independently.
  5. Report: valid/invalid, which premise is weakest, and what the argument actually establishes.
- **Mistakes:** rejecting valid arguments because you dislike the conclusion; accepting invalid ones because premises are true; forgetting step 2 (most real arguments are enthymemes).
- **Examples:** auditing a legal brief's chain of reasoning; checking whether benchmark results actually imply the claimed product superiority; testing a policy syllogism.
- **Related:** [[argument-mapping]] (lays out the structure this skill tests), [[fallacy-detection]], [[reductio]]. **Prereqs:** none.

---

### inductive-generalization `atomic · D2 · ~450 tok`
Generalize from observed instances to a rule, with explicit checks on sample size, representativeness, and scope.

- **Why:** Generalization is unavoidable; ungoverned generalization is how anecdotes become "facts." The checks turn it from a leap into a graded inference.
- **Inputs:** a set of observations → **Outputs:** a candidate generalization with explicit scope limits and a confidence grade.
- **Activate when:** concluding anything of the form "Xs tend to Y" from cases; evaluating someone else's generalization. **Skip when:** a mechanism-level explanation is available — prefer [[causal-analysis]].
- **Principles:** the sample's selection process matters more than its size; the generalization's scope must not exceed the sample's coverage; seek the counterexample before publishing the rule.
- **Procedure:**
  1. State the candidate rule and the instances supporting it.
  2. Describe how the instances were selected; name the selection biases that process invites.
  3. Check coverage: what sub-populations, conditions, or time periods does the sample miss?
  4. Actively search for counterexamples within reach.
  5. Narrow the rule's scope until it's supported by the actual coverage.
  6. Grade confidence and state what evidence would strengthen or break the rule.
- **Mistakes:** counting confirmations while never sampling for disconfirmations; generalizing from survivors (the dead don't report); scope creep between step 1 and how the rule gets used.
- **Examples:** deciding whether five user complaints indicate a systemic UX issue; judging if a drug's trial population licenses claims about the elderly; inferring a coding pattern from three repos.
- **Related:** [[reference-class-forecasting]], [[statistical-audit]], [[disconfirmation-search]]. **Prereqs:** none.

---

### abductive-inference `atomic · D3 · ~500 tok`
Generate multiple candidate explanations for an observation and rank them by explanatory quality — not by which came to mind first.

- **Why:** The first explanation generated becomes an anchor; unexamined, it wins by default. Forcing a slate of rivals and explicit ranking criteria breaks the anchor.
- **Inputs:** a surprising observation or pattern → **Outputs:** a ranked slate of ≥3 explanations with the discriminating evidence each would predict.
- **Activate when:** something unexpected happened and you're about to say "probably because…". **Skip when:** the space of causes is formally enumerable — use [[differential-diagnosis]].
- **Principles:** the best explanation is judged on scope, simplicity, and prior plausibility — jointly, not on fit alone; anything fits if it's vague enough; an explanation earns rank by predicting something the others don't.
- **Procedure:**
  1. State the observation precisely, separating it from interpretation.
  2. Generate ≥3 candidate explanations, deliberately including a boring one (chance, measurement error, selection effect).
  3. For each: what else would be true if this were the explanation?
  4. Score candidates on fit, prior plausibility, and simplicity.
  5. Identify the cheapest observation that discriminates the top two.
  6. Report the ranking, the discriminating test, and rank instability (how easily #2 overtakes #1).
- **Mistakes:** stopping at one hypothesis; omitting the boring explanations; scoring on fit alone (conspiracy theories fit everything); never running the discriminating test.
- **Examples:** why did signups drop 20% this week; why does the patient have these three symptoms together; why did the rival company suddenly cut prices.
- **Related:** [[competing-hypotheses]] (the full composite), [[bayesian-updating]] (formalizes step 4), [[causal-analysis]]. **Prereqs:** none.

---

### analogical-reasoning `atomic · D3 · ~550 tok`
Transfer structure from a well-understood source domain to a target problem, then explicitly verify the mapping holds where it matters.

- **Why:** Analogy is the fastest way to import a solved problem's machinery — and the fastest way to import wrong conclusions when surface similarity masks structural difference. The verification step is what makes it reasoning instead of rhetoric.
- **Inputs:** a target problem + one or more candidate source domains → **Outputs:** a structure mapping, the transferred insight, and a list of disanalogies with their consequences.
- **Activate when:** the problem resembles something solved elsewhere; generating approaches for a novel situation; evaluating someone's persuasive analogy. **Skip when:** direct analysis of the target is cheap — analogy is a bridge, not a destination.
- **Principles:** map relations, not surface features; an analogy is an argument only where the mapped structure is causally relevant; every analogy breaks somewhere — find where before relying on it.
- **Procedure:**
  1. State the target problem's essential structure (entities, relations, constraints).
  2. Search for source domains sharing that *relational* structure; list 2–3 candidates.
  3. For the best candidate, build the explicit mapping: what corresponds to what.
  4. Transfer the source's solution/lesson through the mapping.
  5. Hunt for disanalogies: relations in the target with no source counterpart and vice versa.
  6. Judge whether any disanalogy touches the causal path of the transferred lesson. If yes, discard or repair.
  7. Report the insight plus the boundary where the analogy stops working.
- **Mistakes:** matching on surface features ("both involve networks"); riding the analogy past its breaking point; adopting the first analogy instead of comparing several.
- **Examples:** using epidemiology to model misinformation spread; treating technical debt with financial-debt intuitions (and finding where that breaks); porting immune-system tolerance to content moderation.
- **Related:** [[explanatory-analogy]] (same machinery aimed at teaching), [[concept-blending]], [[mental-model-extraction]]. **Prereqs:** none.

---

### causal-analysis `atomic · D4 · ~650 tok`
Build an explicit causal model of a phenomenon, distinguishing causation from correlation, confounding, and selection.

- **Why:** Almost every intervention decision assumes a causal claim, and correlational data offers three rival stories for every pattern (X→Y, Y→X, Z→both). Making the graph explicit exposes which story is being assumed.
- **Inputs:** an observed relationship or a proposed intervention → **Outputs:** a causal graph (even informal), the rival explanations for the data, and what evidence would distinguish them.
- **Activate when:** any claim of the form "X causes/drives/leads to Y"; before intervening on X to change Y. **Skip when:** you only need prediction, not intervention — correlation suffices for forecasting.
- **Principles:** correlation licenses prediction, not intervention; always draw the confounder before believing the arrow; conditioning on a common effect *creates* fake correlation (collider bias); temporal order is necessary but not sufficient.
- **Procedure:**
  1. State the causal claim as an arrow: X → Y, with the population and timescale.
  2. Draw rival graphs: reverse causation, common cause(s) Z, selection effects in how the data was gathered.
  3. For each rival, name a concrete candidate (an actual plausible Z, an actual selection mechanism).
  4. Ask what the mechanism would be for the claimed arrow — trace the causal chain step by step.
  5. Identify discriminating evidence: natural experiments, dose-response, timing, what happens when X is removed.
  6. If intervention data exists, weight it above all observational data.
  7. Report the graph you believe, confidence, and the single most likely alternative.
- **Mistakes:** accepting mechanism-free correlations because the story is intuitive; ignoring selection in how the sample reached you; assuming the arrow's direction from narrative convention; treating "controlled for" as magic.
- **Examples:** does the new onboarding flow cause retention, or do motivated users complete both; does the medication help, or do healthier patients get prescribed it; did the reorg improve velocity or did the weak projects get cancelled simultaneously.
- **Related:** [[counterfactual-reasoning]] (the semantics of the arrows), [[statistical-audit]], [[root-cause-investigation]] (applies this backwards from an effect). **Prereqs:** none; [[sanity-checking]] helps.

---

### counterfactual-reasoning `atomic · D3 · ~500 tok`
Evaluate "what would have happened if X had been different" by constructing the minimally-changed alternative world.

- **Why:** Credit assignment, regret, blame, and impact evaluation all secretly depend on counterfactuals. Done implicitly, people change too much of the world at once and reach self-serving conclusions.
- **Inputs:** an actual outcome + a candidate difference-maker X → **Outputs:** the most plausible alternative history and a judgment of X's actual contribution.
- **Activate when:** attributing success/failure to a factor; evaluating a past decision; measuring the impact of anything ("did the campaign work?"). **Skip when:** you can just run the experiment — do that instead.
- **Principles:** change only X and what X causally forces — hold everything else fixed; evaluate the decision by what was knowable then, not by the outcome; multiple sufficient causes mean no single factor "made the difference."
- **Procedure:**
  1. Specify the actual world: outcome, and the factor X under evaluation.
  2. Construct the nearest world where X differs — change nothing else except X's downstream consequences.
  3. Trace forward: what plausibly happens in that world? Use base rates, not narrative.
  4. Check for redundant causation: would some other factor have produced the outcome anyway?
  5. State X's contribution: necessary, sufficient, contributory, or irrelevant.
  6. Flag the counterfactual's confidence — distant worlds are speculation, not analysis.
- **Mistakes:** rewriting many variables at once ("if I'd been smarter and earlier and richer…"); hindsight bias (importing knowledge into the alternative past); confusing "X preceded Y" with "no X, no Y."
- **Examples:** would the deal have closed without the discount; would the outage have happened without the config change; assessing a historical policy's effect.
- **Related:** [[causal-analysis]], [[decision-journaling]] (captures the ex-ante view that step 6 needs), [[after-action-review]]. **Prereqs:** none.

---

### bayesian-updating `atomic · D3 · ~600 tok`
Revise belief in a hypothesis by asking how much more likely the evidence is under that hypothesis than under its rivals.

- **Why:** Untrained belief revision overreacts to vivid evidence and underreacts to boring evidence. The likelihood-ratio question — "how surprising is this if I'm wrong?" — is the single highest-leverage correction in reasoning under uncertainty.
- **Inputs:** a prior belief (even rough), new evidence → **Outputs:** an updated probability with the reasoning shown.
- **Activate when:** new information arrives on an open question; you notice a belief flipping on a single data point; diagnosing from symptoms/signals. **Skip when:** the question is deductive or definitional.
- **Principles:** evidence supports H only insofar as it's more probable under H than under not-H; the prior is the base rate unless you have a reason it isn't; strong claims need evidence that would be *rare* if the claim were false; update incrementally — no data point deserves certainty.
- **Procedure:**
  1. State hypothesis H and its live rivals.
  2. Set a prior for H — anchor on a reference-class base rate; write it down.
  3. State the evidence E precisely.
  4. Estimate P(E|H) and P(E|¬H) — how expected is E under each? The ratio is the strength of the evidence.
  5. Update the prior in the direction and magnitude the ratio warrants (do the arithmetic if stakes justify it; otherwise shift qualitatively: ratio ≈1 → no update, 3 → mild, 10+ → strong).
  6. Sanity-check the posterior against base rates and against what you'd bet.
  7. State the posterior and what evidence would move it most next.
- **Mistakes:** ignoring the base rate (the classic: rare disease, decent test, wildly overestimated posterior); updating on evidence that's equally likely either way (P(E|H) ≈ P(E|¬H) is *noise*); double-counting correlated evidence as independent; choosing the prior after seeing the evidence.
- **Examples:** how much should a positive screening test raise disease probability; does a competitor's job posting really signal a pivot; how strongly does one failed test implicate the new commit.
- **Related:** [[reference-class-forecasting]] (supplies priors), [[confidence-calibration]] (audits outputs), [[competing-hypotheses]] (matrix form of the same logic). **Prereqs:** none.

---

### expected-value `atomic · D2 · ~450 tok`
Evaluate an uncertain option by weighing each outcome's payoff by its probability — including the unlikely tails.

- **Why:** Unaided judgment evaluates gambles by their most vivid outcome. EV thinking forces the full distribution into view, which is where asymmetric bets (small cost, huge upside — or the reverse) hide.
- **Inputs:** an option with uncertain outcomes → **Outputs:** an EV estimate, the outcome distribution, and flags where EV alone is a bad guide.
- **Activate when:** comparing gambles, bets, investments of time/money, insurance-shaped choices. **Skip when:** outcomes are certain, or a single catastrophic branch dominates (ruin isn't averaged away — flag it instead).
- **Principles:** value = Σ probability × payoff, over *all* branches; a 1% chance of −1000 outweighs a 90% chance of +5; EV is a long-run guide — for unrepeatable, ruin-risking choices, respect the variance too.
- **Procedure:**
  1. Enumerate the outcome branches, including "nothing happens" and the tail cases.
  2. Assign probabilities (base rates first); check they sum to ~1.
  3. Assign payoffs in a common unit, counting second-order costs.
  4. Compute/estimate the EV.
  5. Check the distribution: is the EV driven by a tiny-probability branch? Is any branch ruinous or irreversible?
  6. Report EV + the distribution shape + whether EV is even the right criterion here.
- **Mistakes:** truncating tails ("that won't happen"); using EV on one-shot ruin risks; precision theater — fake decimal places on made-up probabilities; ignoring the cost of the option you didn't take.
- **Examples:** whether to settle or litigate; whether a startup should take the acquisition offer; whether to buy the extended warranty; triaging which incident risks to mitigate.
- **Related:** [[risk-matrix]], [[monte-carlo-reasoning]] (when branches are too many to enumerate), [[cost-benefit]]. **Prereqs:** none.

---

### fermi-estimation `atomic · D2 · ~500 tok`
Bound an unknown quantity by decomposing it into factors you can estimate, then checking the result against independent anchors.

- **Why:** "No idea" is rarely true — you almost always know enough to get within 3–10×, which is enough to make most decisions. Decomposition converts one impossible estimate into several easy ones whose errors partially cancel.
- **Inputs:** a quantitative question with no direct data → **Outputs:** a point estimate with an explicit range and the decomposition shown.
- **Activate when:** sizing anything (market, cost, load, time, risk exposure) without data; sanity-checking someone else's number. **Skip when:** real data is a quick lookup away.
- **Principles:** decompose into factors you have anchors for; estimate in orders of magnitude first, refine second; use the geometric mean of your plausible bounds; two independent decomposition paths that agree are worth more than one careful path.
- **Procedure:**
  1. Restate the question with units and scope pinned down.
  2. Decompose into a product/sum of estimable factors.
  3. Estimate each factor with an explicit range (lower/upper you'd bet on); take geometric means.
  4. Combine; propagate the ranges, not just the points.
  5. Cross-check via a second, independent decomposition or a known anchor.
  6. Report estimate, range, and which factor contributes the most uncertainty.
- **Mistakes:** false precision (reporting 4 significant figures from 1-sig-fig inputs); decomposing into factors you know *less* about; forgetting the cross-check; anchoring all "independent" paths on the same hidden number.
- **Examples:** how many support tickets will this feature generate; what's the annual cost of that meeting; how much training data exists for this language; piano tuners in Chicago.
- **Related:** [[sanity-checking]] (the cross-check step standalone), [[uncertainty-decomposition]], [[reference-class-forecasting]]. **Prereqs:** none.

---

### reductio `atomic · D2 · ~400 tok`
Test a claim by assuming it's true, deriving its consequences, and hunting for a contradiction or absurdity.

- **Why:** Some claims are easier to refute than to evaluate. Following a claim to its logical conclusions is often the fastest way to expose a hidden flaw — or to discover the claim is stronger than it looked.
- **Inputs:** a claim, rule, or policy → **Outputs:** either a derived contradiction/absurd consequence, or increased confidence after the claim survives.
- **Activate when:** a general rule is proposed ("we should always/never X"); a definition or principle needs stress-testing; a proof or argument feels slippery. **Skip when:** the claim is explicitly probabilistic or scoped — deriving edge-case absurdities from a statistical tendency is a strawman.
- **Principles:** take the claim fully seriously — a lazy reductio refutes only the strawman; the contradiction must follow from the claim, not from added assumptions; an *unwelcome* consequence is not an *absurd* one.
- **Procedure:**
  1. State the claim precisely, at the strength its proponent intends ([[steelmanning]] if needed).
  2. Assume it true without reservation.
  3. Derive consequences mechanically, especially at boundary conditions and extreme-but-valid cases.
  4. Check each consequence: contradiction with the claim itself, with accepted facts, or genuinely absurd?
  5. Verify the absurdity traces to the claim and not to a smuggled auxiliary assumption.
  6. Report: refuted (with the derivation), or survived (with the hardest case it survived).
- **Mistakes:** refuting an exaggerated version; calling "I don't like that outcome" a contradiction; smuggling in an extra premise that's the real source of the absurdity.
- **Examples:** stress-testing "all metrics should have owners" against metrics spanning teams; testing a proposed legal rule at its edge cases; checking a system invariant by assuming it and deriving an impossible state.
- **Related:** [[deductive-validation]], [[structured-what-if]] (same move, exploratory rather than refutational), [[steelmanning]]. **Prereqs:** none.

---

### argument-mapping `atomic · D3 · ~500 tok`
Lay out an argument's claims, premises, warrants, and rebuttals as an explicit structure so its strength can be assessed part by part.

- **Why:** Prose hides argumentative structure; a paragraph can feel compelling while its actual support graph is one weak link. Mapping makes every dependency visible and attackable.
- **Inputs:** an argument in prose (yours or another's) → **Outputs:** a structured map — main claim, supporting premises, the warrant linking each, objections and their answers — with the weakest link flagged.
- **Activate when:** evaluating a long-form argument; writing one; a disagreement keeps going in circles (map both sides to find the actual crux). **Skip when:** the argument is one inferential step — just use [[deductive-validation]].
- **Principles:** every claim is supported, a supporter, or flagged as unsupported; the warrant (why does this premise support that claim?) is usually the buried weak part; an argument is only as strong as its weakest necessary link — but parallel independent lines add robustness.
- **Procedure:**
  1. Identify the main claim.
  2. Extract each supporting reason; note whether reasons are independent lines or links in one chain.
  3. For each link, articulate the warrant — the general rule that makes the premise relevant.
  4. Add known objections and rebuttals where they attach.
  5. Mark each node: established / plausible / contested / unsupported.
  6. Identify the crux: the node whose failure does the most damage.
  7. Report the map and the crux.
- **Mistakes:** mapping only the supporting side; treating chained dependencies as if they were independent corroboration; drowning in exhaustive mapping when only the crux matters.
- **Examples:** mapping a policy memo before the exec review; finding the crux of a technical design disagreement; structuring a legal argument's dependencies.
- **Related:** [[deductive-validation]] (tests each link), [[argument-construction]] (the generative direction), [[steelmanning]]. **Prereqs:** none.

---

### sanity-checking `atomic · D1 · ~400 tok`
Rapidly verify a result via units, magnitudes, boundary conditions, and independent approximations before trusting or shipping it.

- **Why:** Most gross errors are catchable in seconds by tests that don't require redoing the work. The habit of running them is worth more than most sophisticated methods, because it runs on *everything*.
- **Inputs:** any result — a number, a conclusion, a plan, a piece of writing → **Outputs:** pass, or a specific detected anomaly.
- **Activate when:** always — after any computation, estimate, or conclusion; before presenting anything. **Skip when:** never; scale the depth instead.
- **Principles:** check with methods *independent* of how the result was produced; extremes are where errors are loudest; an unexplained anomaly means stop, not shrug.
- **Procedure:**
  1. Units/type check: is the result even the right kind of thing?
  2. Magnitude check: within 10× of what a crude independent estimate gives?
  3. Boundary check: does the logic hold at zero, one, the maximum, the empty case?
  4. Consistency check: does it contradict anything else already established?
  5. Smell check: is it suspiciously round, suspiciously precise, or suspiciously convenient?
  6. If any check fails: locate the discrepancy before proceeding. Never annotate-and-continue.
- **Mistakes:** re-checking with the same method that produced the error; explaining anomalies away instead of chasing them; skipping checks when confident (confidence is when they're needed).
- **Examples:** a revenue projection that implies capturing 140% of the market; a model output in the wrong unit; a plan whose timeline assumes zero rework; a percentage over 100.
- **Related:** [[fermi-estimation]] (supplies the independent estimate), [[epistemic-tagging]]. **Prereqs:** none. *The cheapest skill in the collection and a dependency-of-convention for nearly every composite.*
