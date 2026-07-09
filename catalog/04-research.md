# 4 · Evidence & Research

Finding out what's true.

---

### question-decomposition `atomic · D2 · ~450 tok`
Break a research question into independently answerable sub-questions whose answers compose back into the original.

- **Why:** Big questions are unanswerable as posed; research that starts without decomposition wanders. Sub-questions define what evidence would even count, and expose which part of the question is actually contested.
- **Inputs:** a research question → **Outputs:** a tree of sub-questions, each tagged answerable-by-what-kind-of-evidence, with the contested nodes marked.
- **Activate when:** starting any investigation; a question keeps producing vague answers; scoping a literature search. **Skip when:** the question is already atomic.
- **Principles:** decompose until each leaf names its evidence type (a lookup, a measurement, a judgment call); separate factual sub-questions from definitional and normative ones — they get different methods; the recomposition rule (how sub-answers combine) must be stated, or the tree is decoration.
- **Procedure:**
  1. Write the question; mark ambiguous terms and pin definitions.
  2. Split along its natural joints: factual components, causal components, evaluative components.
  3. Recurse until each leaf is answerable by a nameable method or source.
  4. Tag each leaf: known / findable / genuinely open / value judgment.
  5. State how the leaves recombine into an answer — and which leaf, if it falls a certain way, decides everything (the crux).
  6. Order investigation: cruxes and cheap lookups first.
- **Mistakes:** decomposing along available data instead of the question's logic; hiding a value judgment inside a factual-looking leaf; never stating the recomposition rule.
- **Examples:** "should we enter market X?" → size, accessibility, competitive response, our capability fit; "is this treatment effective?" → for whom, vs what, on which outcome, over what horizon.
- **Related:** [[mece-decomposition]], [[search-strategy]] (consumes the leaves), [[decision-framing]]. **Prereqs:** none.

---

### search-strategy `atomic · D2 · ~450 tok`
Plan queries, sources, and stop-conditions before searching, then adapt on evidence of coverage rather than fatigue.

- **Why:** Unplanned search finds whatever ranks first and stops when tired — a recipe for availability bias. A strategy with stop-conditions makes coverage a decision instead of an accident.
- **Inputs:** an answerable question (from [[question-decomposition]]) → **Outputs:** a source/query plan, a stop rule, and a coverage self-assessment after execution.
- **Activate when:** any search beyond one lookup; especially when the first page of results *agrees suspiciously*. **Skip when:** a canonical source is known.
- **Principles:** vary the *kind* of source (primary/secondary, pro/con, practitioner/academic), not just the query wording; search explicitly for disconfirming material — "X doesn't work," "X criticism," "X failed" — the confirming version finds itself; saturation (new sources repeat old ones) is the honest stop signal; track provenance so [[evidence-triangulation]] can detect shared upstream sources.
- **Procedure:**
  1. State what an answer would look like and what would count as enough.
  2. List source types most likely to hold it; note each type's characteristic bias.
  3. Draft queries including deliberately disconfirming formulations.
  4. Execute breadth-first; log source, claim, and *the source's source*.
  5. Check saturation and coverage: any viewpoint or source-type not yet sampled?
  6. Stop on the pre-set rule; report what was searched, what wasn't, and confidence in coverage.
- **Mistakes:** query monoculture (rephrasing the same assumption five ways); stopping at agreement without noticing all sources cite one origin; searching until confirmation arrives and calling it done.
- **Examples:** due diligence on a vendor's reliability claims; scoping prior art; checking whether a "well-known fact" survives its citations.
- **Related:** [[evidence-triangulation]], [[source-credibility]], [[disconfirmation-search]]. **Prereqs:** none.

---

### source-credibility `atomic · D2 · ~450 tok`
Grade a source on expertise, incentive, track record, and proximity to the events before letting its claims carry weight.

- **Why:** Content persuades by fluency; credibility lives in metadata — who says it, how they'd know, and what they gain. Grading the source first prevents fluent nonsense from outranking awkward truth.
- **Inputs:** a source making claims → **Outputs:** a credibility grade with the specific caveats to apply to its claims.
- **Activate when:** weighing any consequential claim; sources conflict; a claim is surprising or convenient. **Skip when:** the claim is checkable directly — check it instead.
- **Principles:** proximity beats prestige — an eyewitness ranks a famous commentator; expertise is domain-specific and decays at the domain boundary; incentive doesn't disprove, it discounts — ask what the source gains if you believe them; a track record of *corrected* errors is a positive signal, not negative.
- **Procedure:**
  1. Identify the actual origin (the study, the witness, the dataset) versus the repeater.
  2. Proximity: how many hops from the events is this source?
  3. Competence: does the source have the expertise to know this — in *this* domain?
  4. Incentive: what does the source gain from your belief? Flag, don't auto-dismiss.
  5. Track record: prior accuracy, correction behavior, and whether they ever report against interest (strong positive signal).
  6. Grade: rely / use-with-caveats / corroborate-first / discount. Attach the specific caveat.
- **Mistakes:** halo transfer (expert in A trusted in B); genetic fallacy (dismissing true claims from biased sources — bias lowers weight, it doesn't flip truth); prestige substituting for proximity; ignoring statements-against-interest, the most underrated evidence.
- **Examples:** a vendor's benchmark vs a customer's; anonymous insider vs official statement; a celebrated pundit vs a boring domain specialist.
- **Related:** [[evidence-hierarchy]], [[incentive-analysis]], [[evidence-triangulation]]. **Prereqs:** none.

---

### evidence-triangulation `atomic · D2 · ~450 tok`
Require confirmation from *independent* sources, and actively test whether apparently separate sources share an upstream origin.

- **Why:** "Multiple sources confirm" is worthless if they all trace to one press release. Real corroboration requires independence, and independence must be verified — it's the most-faked property in the information ecosystem.
- **Inputs:** a claim + its supporting sources → **Outputs:** an independence-adjusted confidence: how many *effectively independent* confirmations exist.
- **Activate when:** a claim matters and multiple sources exist; consensus feels too smooth; citation-chasing any "well-established" fact. **Skip when:** one source is definitively authoritative (the primary document itself).
- **Principles:** N sources citing one origin = 1 source with amplification; independence means different methods, different incentives, different access — not just different logos; convergence of *independent* methods is the strongest ordinary evidence there is; disagreement among independents is information too — locate what they disagree about.
- **Procedure:**
  1. List the sources supporting the claim.
  2. Trace each to its origin: what is this source's source? Follow citations to the root.
  3. Cluster sources by shared origin. Count clusters, not sources.
  4. Assess method-diversity across clusters: same evidence type, or genuinely different routes to the claim?
  5. Weight: many clusters + diverse methods → strong; one cluster → single-source claim regardless of repetition count.
  6. Where independent clusters disagree, characterize the disagreement precisely — that's the live research question.
- **Mistakes:** counting citations as confirmations; treating media pickups of one wire story as corroboration; assuming institutional sources are independent of each other; ignoring the lone dissenting cluster because it's outnumbered by echoes.
- **Examples:** a "widely reported" statistic tracing to one advocacy white paper; validating an outage theory from logs *and* metrics *and* user reports; historical claims resting on a single chronicle.
- **Related:** [[source-credibility]], [[search-strategy]], [[bayesian-updating]] (independence determines how much each confirmation is worth). **Prereqs:** none.

---

### evidence-hierarchy `atomic · D3 · ~500 tok`
Rank the available evidence by its strength *for the specific claim class* — because evidence types have different power for different kinds of questions.

- **Why:** Anecdote, expert opinion, observational data, and experiment differ by orders of magnitude in reliability — but the ranking itself depends on the question (an RCT is gold for "does it work on average"; a mechanism study is better for "will it work *here*"). Explicit ranking stops the vivid from beating the valid.
- **Inputs:** a claim + a pile of heterogeneous evidence → **Outputs:** the evidence sorted by strength-for-this-claim, with the verdict weighted accordingly.
- **Activate when:** evidence conflicts; a decision leans on "studies show" or "experts say"; synthesizing mixed material. **Skip when:** all evidence is one type — assess quality within type instead.
- **Principles:** for causal claims: experiments > natural experiments > controlled observational > raw correlational > anecdote — *within each tier, quality still varies hugely*; for existence claims one good observation suffices; for "typical case" claims, representative sampling beats any single study; expert opinion is evidence about *judgment under uncertainty*, strong only where the expert has feedback-rich experience; the hierarchy ranks *types* — a flawed RCT loses to a strong cohort study ([[methodology-critique]] adjudicates).
- **Procedure:**
  1. Classify the claim: causal / existence / frequency / predictive / normative.
  2. Sort evidence into types; note the appropriate hierarchy for this claim class.
  3. Within each type, spot-check quality (sample, method, independence).
  4. Weight the verdict by the top-tier evidence; use lower tiers only to fill gaps the top tier doesn't cover (external validity, mechanisms, edge cases).
  5. Note the mismatches: strong evidence for a *nearby* claim being marketed as evidence for *this* claim.
  6. Report: verdict, the evidence carrying it, and what missing evidence tier would settle it.
- **Mistakes:** treating hierarchy as absolute rather than claim-relative; letting twenty anecdotes outvote one experiment; the bait-and-switch in step 5 (efficacy evidence sold as effectiveness); dismissing anecdotes entirely — they're hypothesis generators and existence proofs.
- **Examples:** drug efficacy (trial data vs clinician impressions); "remote work hurts productivity" (what evidence type even bears on it); an architecture choice supported by one blog post vs benchmark data.
- **Related:** [[methodology-critique]], [[statistical-audit]], [[bayesian-updating]]. **Prereqs:** none.

---

### critical-reading `atomic · D3 · ~500 tok`
Extract from a text its claims, evidence, assumptions, and omissions — reading what it does, not just what it says.

- **Why:** Texts are optimized to persuade; passive reading absorbs the author's frame along with their facts. Structured extraction separates what was *demonstrated* from what was *asserted* from what was *implied by omission*.
- **Inputs:** a document (paper, memo, article, contract, transcript) → **Outputs:** a claims inventory tagged by support level, the argument skeleton, the assumptions, and the notable silences.
- **Activate when:** any consequential document; especially polished, confident, or agreeable prose (agreement is when critical reading is hardest and most needed). **Skip when:** reading for orientation only — skim first, read critically what turns out to matter.
- **Principles:** identify the conclusion first, then audit backwards — texts bury weak links in the middle; distinguish demonstrated / cited / asserted / insinuated; what's *missing* is a claim too (the unmentioned comparison, the absent denominator, the competitor never named); note the frame before it notes you ([[frame-detection]]).
- **Procedure:**
  1. Skim for structure: what is this text trying to get the reader to believe or do?
  2. Extract the main claims verbatim; paraphrase-drift hides sleight of hand.
  3. Tag each claim's support: demonstrated here / cited (check the cite's actual content) / asserted / implied.
  4. Surface the assumptions the argument needs but never states.
  5. Hunt omissions: what would a knowledgeable skeptic expect this text to address? Its silence there is information.
  6. Separate verdicts: what did this text *establish*, vs merely *say*?
- **Mistakes:** critique-by-vibes (disliking conclusions instead of auditing support); trusting citations without opening them (citations routinely don't say what they're cited for); reading hostile texts critically and friendly texts passively.
- **Examples:** a vendor whitepaper; a policy brief; an earnings call transcript; a methods section; your own draft, one day later.
- **Related:** [[argument-mapping]] (formalizes the skeleton), [[frame-detection]], [[statistical-audit]] (for the numbers). **Prereqs:** none.

---

### statistical-audit `atomic · D4 · ~600 tok`
Interrogate quantitative claims: base rates, denominators, comparison groups, significance, effect size, and the path the number took to reach you.

- **Why:** Numbers borrow authority from mathematics while their meaning is set by choices — what was counted, compared to what, and which results got published. Most misleading statistics are technically true.
- **Inputs:** a quantitative claim → **Outputs:** a verdict on what the number actually supports, with the specific distortions identified.
- **Activate when:** any statistic used to persuade; "X% more," "studies show," "record high," rankings, risk figures. **Skip when:** the number is decorative and nothing depends on it.
- **Principles:** no numerator without a denominator; no change without a base ("doubled" from what?); no comparison without the comparison group's composition; statistical significance ≠ practical importance — always ask for the effect size; the number you're seeing survived a selection process (of studies, timeframes, metrics) — ask what didn't survive.
- **Procedure:**
  1. Restate the claim with its exact quantities, units, population, and timeframe. Vagueness in any of these is finding #1.
  2. Denominator check: rate or raw count? Right base population?
  3. Comparison check: compared to what, and are the groups actually comparable (selection, composition, time)?
  4. Effect-size check: is the difference big enough to matter, apart from being "significant"? What's the absolute (not just relative) change?
  5. Selection check: why this metric, this timeframe, this subgroup? What do adjacent choices show?
  6. Survivorship/publication check: what's the path by which this number reached you, and what numbers didn't make it?
  7. Verdict: what the number honestly supports, what it's being used to imply, and the gap between them.
- **Mistakes:** relative risk without absolute risk ("40% increase" of something rare); comparing raw counts across differently-sized populations; percentage-of-percentage confusion; assuming a precise number is an accurate one; being *so* suspicious that all numbers are dismissed — the audit grades, it doesn't nuke.
- **Examples:** "crime doubled" (from 2 to 4 incidents); a fund's returns (surviving funds only); "users spend 3× longer" (which users, doing what, vs when); a medical screening's impressive sensitivity hiding a base-rate collapse.
- **Related:** [[bayesian-updating]] (base-rate machinery), [[methodology-critique]] (upstream: how the number was made). **Prereqs:** none.

---

### methodology-critique `atomic · D4 · ~550 tok`
Find the design flaws that break a study's claimed inference — auditing how the knowledge was manufactured, not just what it concludes.

- **Why:** A study's conclusions inherit the validity of its design, and design flaws are invisible in the abstract. Most contested empirical questions turn on methodology, so the critique skill *is* the evaluation skill.
- **Inputs:** a study/analysis with methods available → **Outputs:** a validity assessment: which claimed inferences survive, which break, and on what specific design choice.
- **Activate when:** a study anchors a decision; findings conflict across studies; results are surprising or suspiciously aligned with the funder. **Skip when:** methods aren't available — that absence is itself the finding.
- **Principles:** match the critique to the inference — a design fine for correlation breaks for causation; the four validity questions: measurement (does the instrument measure the construct?), internal (does the design support the causal claim?), statistical (is the analysis sound and adequately powered?), external (does it generalize to the population you care about?); researcher degrees of freedom (many analyses, one reported) inflate everything; a flaw must connect to a conclusion — flaw-listing without consequence is pedantry.
- **Procedure:**
  1. State the claimed inference precisely — what does the study say it showed?
  2. Measurement validity: what was actually measured, and how far is it from the construct in the claim?
  3. Internal validity: comparison group, assignment mechanism, confounders, attrition, blinding where relevant.
  4. Statistical validity: power, multiple comparisons, outcome switching, subgroup fishing.
  5. External validity: study population/conditions vs the target of the claim.
  6. For each flaw found: state *which conclusion* it breaks and how badly. Some flaws are cosmetic.
  7. Verdict: what this study establishes, at what strength, for whom.
- **Mistakes:** perfectionism (no study is flawless; the question is whether the flaws touch the conclusion); asymmetric rigor (auditing only studies you dislike); missing outcome-switching because you never checked the pre-registration; critiquing statistics when the fatal wound is measurement.
- **Examples:** a hiring-tool vendor study with a survivorship-selected sample; a nutrition finding built on food-frequency recall; an A/B test analyzed with peeking; an education intervention evaluated by its designers.
- **Related:** [[evidence-hierarchy]], [[statistical-audit]], [[peer-review]] (the composite around this). **Prereqs:** [[causal-analysis]] recommended.

---

### claim-verification `composite · D3 · ~850 tok`
Journalism-grade fact-checking of a specific claim: decompose it, trace to origin, triangulate independently, and grade the verdict.

- **Why:** Claims travel farther than their evidence. A repeatable verification pipeline replaces "sounds right" with a graded verdict — and does it fast enough to run routinely.
- **Inputs:** a specific factual claim → **Outputs:** a verdict (verified / partly / unsupported / false / unverifiable) with the evidence trail.
- **Dependencies:** `question-decomposition`, `search-strategy`, `source-credibility`, `evidence-triangulation`, `statistical-audit`, `epistemic-tagging`.
- **Activate when:** a claim is load-bearing for a decision or about to be repeated onward; a statistic is doing heavy rhetorical work. **Skip when:** nothing depends on it.
- **Principles:** verify the claim *as stated* — verified adjacent claims are how misinformation launders itself; the origin is the unit of verification, not the repetitions; absence of confirmation ≠ refutation — "unverifiable" is an honest verdict; time-box it ([[effort-calibration]]) — verification effort should scale with the claim's load.
- **Procedure:**
  1. Fix the claim verbatim; run `question-decomposition` if it bundles several assertions (verify each; the bundle's truth is the conjunction).
  2. Trace to origin: follow the citation chain to the primary source. Note where the chain breaks or mutates — mutation *is* a finding.
  3. Audit the origin with `source-credibility`; if quantitative, run `statistical-audit` on the original number, not the retelling.
  4. Run `evidence-triangulation`: independent confirmations, counted by origin-cluster.
  5. Search for the rebuttal (`search-strategy` disconfirming queries): has this been debunked, corrected, or retracted?
  6. Grade: verified / verified-with-distortion (true origin, mutated in transit) / unsupported / false / unverifiable. Tag residual uncertainty (`epistemic-tagging`).
- **Mistakes:** verifying the paraphrase instead of the claim; stopping at a "reputable" repeater; treating the origin's existence as its correctness; over-verifying trivia while load-bearing claims skate.
- **Examples:** a statistic in a strategy memo before board presentation; a historical "quote"; a rival's benchmark claim; a viral study result.
- **Related:** [[critical-reading]] (upstream extraction of what to verify).

---

### interview-synthesis `composite · D3 · ~900 tok`
Design non-leading questions, conduct inquiry-driven interviews, and cluster raw responses into findings that survive scrutiny — UX research's core loop, generalized.

- **Why:** People misreport their own behavior, and interviewers hear what they hoped to hear. Discipline at both ends — question design and synthesis — is what separates evidence from collected anecdotes.
- **Inputs:** a learning goal + access to relevant people → **Outputs:** clustered findings with supporting quotes, confidence grades, and an explicit line between observation and interpretation.
- **Dependencies:** `question-decomposition`, `active-listening`, `precision-questioning`, `inductive-generalization`, `epistemic-tagging`, `frame-detection`.
- **Activate when:** the knowledge lives in people's experience (users, experts, witnesses, stakeholders); validating assumptions about what others think or do. **Skip when:** behavior is directly observable — watch instead of ask; or the question is factual with better sources.
- **Principles:** past behavior over hypothetical opinion — "walk me through the last time" beats "would you"; the interviewer's hypothesis must not leak into the questions (`frame-detection` on your own script); synthesis clusters *observations*, and interpretation is a separate, labeled step; disconfirming interviewees are worth double — sample for them.
- **Procedure:**
  1. Define learning goals via `question-decomposition`: what decisions will this research feed?
  2. Draft the guide: open behavioral questions, no embedded conclusions; audit with `frame-detection`. Plan the sample deliberately — include likely disconfirmers.
  3. Conduct with `active-listening`: follow the surprise, not the script; use `precision-questioning` to get from generality ("it's confusing") to instance ("show me where").
  4. Record observations verbatim; tag interpretation separately at capture time (`epistemic-tagging`).
  5. Cluster observations across interviews; a finding needs multiple independent instances (`inductive-generalization` checks on sample coverage).
  6. For each finding: state it, grade its support (how many, how independent, how direct), and attach the disconfirming evidence found.
  7. Report findings separate from recommendations; note which learning goals remain open.
- **Mistakes:** leading questions ("wouldn't it be easier if…"); treating stated intent as predicted behavior; clustering by theme-you-expected rather than what's in the data; sample of the willing (only fans respond); quotes selected to decorate a pre-existing conclusion.
- **Examples:** discovery interviews before building a feature; expert elicitation on a risk; exit interviews mined for systemic patterns; witness interviews in an investigation.
- **Related:** [[delphi-aggregation]] (structured expert version), [[empathy-mapping]] (consumes the output).

---

### scientific-method `composite · D4 · ~1000 tok`
The full empirical loop: hypothesize, operationalize predictions, design a test that could fail, run it, attempt falsification, and update.

- **Why:** Beliefs that never risk contact with disconfirming reality drift toward convenience. The method's power is the *pre-commitment*: saying what you expect before looking, so reality can actually disagree with you.
- **Inputs:** a question or tentative belief about how something works → **Outputs:** an updated, calibrated belief with the test record — including what would still overturn it.
- **Dependencies:** `abductive-inference`, `assumption-audit`, `bayesian-updating`, `disconfirmation-search`, `sanity-checking`, `confidence-calibration`, `causal-analysis`.
- **Activate when:** a belief is testable and consequential; a debate could be settled by looking; building anything on an unvalidated assumption. **Skip when:** the question is normative or definitional — no experiment bears on it.
- **Principles:** a hypothesis that cannot fail is not knowledge, it's decoration; predictions are stated *before* observation, with the discriminating power made explicit (what result would each rival hypothesis predict?); one disconfirmation outweighs many confirmations, but check the instrument before the theory; negative results are results — record them.
- **Procedure:**
  1. State the question; run `abductive-inference` to generate rival hypotheses (≥2 — a lone hypothesis can only be confirmed, never compared).
  2. Run `assumption-audit`: what does each hypothesis assume? Which assumptions are load-bearing and untested?
  3. Operationalize: for each hypothesis, a concrete prediction — what will be observed, measured how, under what conditions. Prefer predictions where the rivals *diverge*.
  4. Design the cheapest test with real discriminating power; state in advance what result supports what ([[causal-analysis]] discipline if the claim is causal).
  5. Run it. Record everything, including the awkward parts.
  6. Compare outcome to the pre-committed predictions. Run `sanity-checking` on surprises — instrument error first, then theory.
  7. Update via `bayesian-updating`; run `disconfirmation-search` on the winner — what's the next observation that could still overturn it?
  8. Report belief, confidence (`confidence-calibration`), the test record, and the standing falsification conditions.
- **Mistakes:** predictions written after the data (HARKing); testing only the favorite hypothesis; rescuing a failed hypothesis with unplanned auxiliary assumptions ("it works, just not on Tuesdays"); running the expensive definitive test before the cheap discriminating one; treating one confirmation as proof.
- **Examples:** A/B testing a pricing hypothesis; debugging via predicted-vs-observed behavior at each layer; testing a coaching intervention on your own team; validating a market assumption with a smoke test.
- **Related:** [[differential-diagnosis]] (find-the-cause variant), [[structured-forecasting]] (when tests must wait for reality), [[decision-analysis]] (consumes the validated beliefs).
