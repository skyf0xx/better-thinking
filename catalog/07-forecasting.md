# 7 · Forecasting & Uncertainty

Putting honest numbers on the future.

---

### reference-class-forecasting `atomic · D3 · ~500 tok`
Forecast by starting from the base rate of similar past cases (the outside view), then adjusting for what's genuinely different about this case — in that order.

- **Why:** Inside-view forecasting (reasoning from this case's specific plan and details) is systematically optimistic because it only models how things go right. Anchoring on how similar efforts actually turned out corrects the bias before adjustment even begins.
- **Inputs:** a forecasting question about a specific case → **Outputs:** a base-rate anchored estimate, adjusted for named differences, with the adjustment's direction and size justified separately from the anchor.
- **Activate when:** estimating duration, cost, or success probability for any project, launch, or plan; anytime an inside-view estimate feels notably better than how "these things" usually go. **Skip when:** truly no reference class exists (rare) — then fall back to [[fermi-estimation]].
- **Principles:** find the reference class *before* looking at this case's specifics, or the class gets gerrymandered to fit the desired answer; the base rate is the anchor — adjustments should be modest and individually justified, not a wholesale override; "this time is different" is sometimes true — but it needs a specific, checkable reason, not a feeling.
- **Procedure:**
  1. Define the reference class: what set of past cases is genuinely comparable to this one? Choose the class before considering this case's specifics.
  2. Gather the base rate from that class: typical outcome, typical variance, typical failure modes.
  3. Only now, examine what's specifically different about this case.
  4. For each named difference, adjust the estimate — state the direction and rough magnitude, and why.
  5. Check total adjustment size against the base rate's variance — a small number of modest adjustments is more credible than one that moves the estimate outside the observed range of the reference class.
  6. Report the base rate, the adjustments, and the final estimate, so a reviewer can audit each step.
- **Mistakes:** choosing the reference class after seeing the desired answer (class-shopping); skipping straight to inside-view reasoning ("but our team is different"); adjustment creep — enough small justified-sounding adjustments to arrive wherever you wanted anyway.
- **Examples:** software project timeline estimation (reference class: similar past projects, not this team's plan); startup success-rate estimation; renovation cost/time estimates; forecasting how long a negotiation will take.
- **Related:** [[inductive-generalization]], [[fermi-estimation]], [[structured-forecasting]] (uses this as a component). **Prereqs:** none.

---

### uncertainty-decomposition `atomic · D3 · ~500 tok`
Split uncertainty about a quantity into its reducible and irreducible components, and report ranges rather than false-precision points.

- **Why:** A single-point estimate hides whether the number is a near-certainty or a coin flip, and hides whether more research would even help. Decomposing uncertainty tells you both — and where to spend effort narrowing it.
- **Inputs:** an uncertain quantity or forecast → **Outputs:** a range (not a point), broken into reducible uncertainty (could be narrowed with more information/effort) and irreducible uncertainty (genuinely stochastic or unknowable at this cost).
- **Activate when:** any forecast or estimate that will inform a decision; a point estimate is being treated as exact; deciding whether more research is worth the cost. **Skip when:** the quantity is actually knowable cheaply — just go look it up.
- **Principles:** report a range with a stated confidence level, not a bare point — the range is the honest answer; ask "would more information narrow this?" — if yes, it's reducible (a research/effort question); if no, it's irreducible (a risk-management question) and no amount of analysis will shrink it further; conflating the two leads to either wasted research effort or false confidence.
- **Procedure:**
  1. State the quantity and produce an initial range (not a point) via whatever method fits ([[fermi-estimation]], [[reference-class-forecasting]]).
  2. For the width of the range, ask what's driving it: missing information, or genuine randomness/unpredictability in the underlying process?
  3. Sort the drivers into reducible (more data, better model, more time would narrow this) and irreducible (inherent variance — weather, individual choice, true novelty).
  4. For reducible uncertainty: estimate the cost of narrowing it and whether that's worth doing before deciding ([[sensitivity-analysis]] to check if it would even change the decision).
  5. For irreducible uncertainty: treat it as a distribution to plan around, not a puzzle to solve — build in margin or optionality instead.
  6. Report the range, its composition, and the recommendation (narrow further vs plan around it).
- **Mistakes:** reporting a point estimate because ranges feel weak or evasive; trying to research away irreducible uncertainty (wasted effort); treating reducible uncertainty as irreducible and never bothering to narrow it when it was cheap to do so.
- **Examples:** a project timeline's confidence interval and what's driving its width; a revenue forecast's weather-like vs knowable components; medical prognosis ranges; estimating a technology's maturation timeline.
- **Related:** [[sensitivity-analysis]], [[monte-carlo-reasoning]], [[confidence-calibration]]. **Prereqs:** none.

---

### sensitivity-analysis `atomic · D3 · ~500 tok`
Vary each input assumption to find which ones actually move the conclusion — separating load-bearing assumptions from decorative ones.

- **Why:** Complex estimates rest on many assumptions, but usually only one or two actually determine the answer. Testing each in turn finds those — telling you where to focus scrutiny and where precision is wasted effort.
- **Inputs:** an estimate or model with multiple input assumptions → **Outputs:** a ranked list of which inputs move the conclusion most, and the conclusion's stability across plausible input ranges.
- **Activate when:** a model or estimate has several assumptions of uneven confidence; deciding where to spend validation effort; presenting a number that needs to survive scrutiny. **Skip when:** the estimate has one obviously dominant input already — the ranking would be trivial.
- **Principles:** vary one input at a time, holding others fixed, to isolate its individual effect; vary each across its *plausible* range, not an arbitrary ±10% — a wide-uncertainty input deserves a wide test range; an input that barely moves the conclusion doesn't need more precision, however uncertain it is; if the conclusion flips within the plausible range of a single input, that's the finding — report it as a conditional, not a point.
- **Procedure:**
  1. List all input assumptions and their plausible ranges (not just point values).
  2. For each input, hold all others at their central estimate and vary this one across its range; record the conclusion's change.
  3. Rank inputs by how much they move the conclusion per unit of their own uncertainty.
  4. For the top 1–2 inputs, consider joint variation (do they interact, amplifying or offsetting each other?).
  5. Identify any input whose plausible range flips the decision/conclusion — name it explicitly as the crux.
  6. Report: the conclusion's stability, the dominant input(s), and where further precision would and wouldn't help.
- **Mistakes:** varying all inputs at once (can't isolate which one matters); testing implausibly narrow or wide ranges; polishing precision on a non-dominant input while the crux input stays a guess; presenting the base case without disclosing that it flips under plausible variation.
- **Examples:** a financial model's dependence on churn rate vs CAC; an engineering estimate's dependence on one uncertain integration; a policy's cost-benefit case under different discount rates.
- **Related:** [[uncertainty-decomposition]], [[weighted-scoring]] (sensitivity step there), [[monte-carlo-reasoning]]. **Prereqs:** none.

---

### trend-breakpoint-analysis `atomic · D3 · ~500 tok`
Extrapolate an observed trend while actively hunting for the mechanisms that would cause it to saturate, reverse, or undergo regime change.

- **Why:** Naive extrapolation assumes whatever's been happening keeps happening, but almost every real trend is a growth curve's early segment, not a line — it hits a ceiling, an inflection, or a shock. Finding the breakpoint mechanism ahead of time beats being surprised by it.
- **Inputs:** a historical trend → **Outputs:** a near-term extrapolation plus the identified mechanisms that would cause a breakpoint, and their rough timing/probability.
- **Activate when:** any trend is being extrapolated to justify a forecast or plan; a trend has "always" gone one direction; growth or decline seems too steady to trust blindly. **Skip when:** the horizon is short enough that breakpoints are implausible within it.
- **Principles:** most real-world trends are S-curves, not lines — the question is where you are on the curve, not whether the curve exists; a trend continues because a mechanism sustains it — identify that mechanism, then ask what would exhaust or disrupt it; the scarcest resource, the strongest constraint, or the most saturated segment usually signals where the curve bends first.
- **Procedure:**
  1. Plot/describe the trend and its recent trajectory.
  2. Identify the mechanism sustaining it: what's actually driving the growth/decline?
  3. Ask what would exhaust that mechanism — a finite resource, a saturating population, a diminishing marginal effect, a competitive response, a regulatory reaction.
  4. Estimate how close the trend currently is to that limit (`fermi-estimation` if needed).
  5. Extrapolate short-term (where the mechanism still holds) separately from long-term (where breakpoints become live).
  6. Report the extrapolation with the identified breakpoint mechanisms and their earliest plausible timing as explicit caveats, not footnotes.
- **Mistakes:** extrapolating a line indefinitely because the recent data is linear (all S-curves look linear in the middle); ignoring the sustaining mechanism entirely — "it's been going up, so it'll keep going up"; dismissing genuine long-run trends as certain-to-break when the mechanism is actually structural and durable.
- **Examples:** a product's user-growth curve approaching market saturation; a cost-decline curve (e.g., a technology's price trend) and what sustains it; a hiring trend heading toward a labor-market ceiling.
- **Related:** [[reference-class-forecasting]], [[leverage-points]] (mechanism thinking), [[structured-forecasting]]. **Prereqs:** none.

---

### tripwires `atomic · D2 · ~400 tok`
Pre-commit to specific, observable indicators that will trigger a belief update, plan change, or decision review — decided before you're emotionally invested in the outcome.

- **Why:** Beliefs and plans drift toward whatever's comfortable to keep believing; in the moment, disconfirming signals get explained away. Pre-committed tripwires, set before that pressure exists, force the update to actually happen.
- **Inputs:** a belief, plan, or forecast with meaningful stakes → **Outputs:** a small set of specific, observable, pre-committed indicators, each paired with the action it triggers.
- **Activate when:** committing to any plan or forecast with real stakes; after [[premortem]] or [[decision-analysis]] identifies key risks; entering an uncertain or adversarial situation ([[ooda-loop]], [[scenario-planning]]). **Skip when:** the situation is too short-lived for monitoring to matter.
- **Principles:** the indicator must be specific and observable in advance — "if things go badly" is not a tripwire; pair every tripwire with a pre-decided action, or it's just a wish to notice something someday; set tripwires when you're not yet invested — the whole value is removing the in-the-moment temptation to rationalize; too many tripwires get ignored — pick the few that actually matter.
- **Procedure:**
  1. From the plan/belief's risk analysis (`premortem`, `assumption-audit`), identify the handful of signals that would most clearly indicate things are off track.
  2. For each, define the specific, observable threshold — a number, an event, a date passed without expected progress.
  3. Pair each threshold with the pre-decided action: reassess, pause, pivot, escalate, or abandon.
  4. Record the tripwires somewhere they'll actually be checked — not buried in a planning doc never revisited.
  5. When a tripwire fires, take the paired action — or explicitly and consciously renegotiate it, rather than silently ignoring it.
- **Mistakes:** vague tripwires that can't be objectively checked; tripwires with no paired action (monitoring without commitment); setting them after you're already invested (they get rationalized away just like anything else); too many to actually track.
- **Examples:** "if CAC exceeds $X by month 3, pause the channel"; "if the vendor misses two consecutive milestones, trigger the backup plan"; a medical treatment's stop-rule; an investment's pre-set exit trigger.
- **Related:** [[premortem]], [[decision-journaling]], [[risk-matrix]]. **Prereqs:** a plan or belief with identified risks.

---

### monte-carlo-reasoning `atomic · D3 · ~500 tok`
Mentally (or computationally) sample many possible runs of an uncertain process, instead of reasoning about one representative story.

- **Why:** When outcomes depend on the combination of several independent uncertain factors, intuition tends to reason about one plausible scenario at a time and misses how the combination of many small uncertainties produces a wide — and often skewed — outcome distribution.
- **Inputs:** a process with multiple uncertain, roughly independent inputs → **Outputs:** an outcome distribution (even a rough sketch of one) rather than a single-scenario story, with the tail behavior noted.
- **Activate when:** an outcome depends on several compounding uncertain factors; a single "expected case" story is being used to plan for a process that's actually quite variable; tail risk matters. **Skip when:** one factor dominates — sensitivity analysis on that factor is simpler and sufficient.
- **Principles:** don't reason about "the" scenario — reason about the *distribution* of scenarios; when uncertain factors combine multiplicatively or with dependencies, the tails are often fatter than intuition expects; a distribution's mean and its most likely single outcome (mode) can differ substantially, especially when skewed — planning for "the expected case" can mean planning for something that individually is unlikely.
- **Procedure:**
  1. Identify the independent (or roughly independent) uncertain inputs to the process.
  2. Estimate a plausible range/distribution shape for each (even qualitatively: "usually here, sometimes much higher").
  3. Mentally sample several combinations — not just "everything average" and "everything bad," but genuinely varied combinations, including ones where some inputs are good and others bad simultaneously.
  4. Sketch the resulting outcome distribution: where does it cluster, how fat are the tails, is it skewed?
  5. Identify what specifically drives the worst outcomes — usually a particular combination, not any single input alone.
  6. Plan against the distribution (buffer, optionality, contingency) rather than against the single expected-case story.
- **Mistakes:** planning for "the average scenario" when the distribution is skewed and the average is rarely the actual outcome; assuming independence when inputs are actually correlated (correlated bad inputs co-occurring is how tail risk happens); doing this so informally that it collapses back into "just imagine one bad case."
- **Examples:** project timeline risk when multiple independent tasks can each slip; portfolio risk from multiple correlated positions; capacity planning under variable demand and variable failure rates simultaneously.
- **Related:** [[uncertainty-decomposition]], [[expected-value]], [[sensitivity-analysis]]. **Prereqs:** none.

---

### structured-forecasting `composite · D4 · ~1000 tok`
The superforecaster pipeline: decompose the question, anchor on a base rate, adjust with named evidence, express calibrated confidence, and schedule updates.

- **Why:** Forecasting accuracy research consistently shows the same disciplined process beats both raw expertise and unaided intuition. The gains come from decomposition, outside-view anchoring, and disciplined updating — not from any special genius.
- **Inputs:** a forecasting question with a resolvable outcome and horizon → **Outputs:** a probability (or range) with the reasoning shown, a calibration check, and a schedule for revisiting.
- **Dependencies:** `question-decomposition`, `reference-class-forecasting`, `bayesian-updating`, `uncertainty-decomposition`, `confidence-calibration`, `tripwires`.
- **Activate when:** a forecast will inform a real decision and is specific/resolvable enough to be scored later; recurring forecasting needs (planning cycles, risk assessment). **Skip when:** the question can't be made resolvable — sharpen the question first, or this pipeline has nothing to grip.
- **Principles:** decompose before estimating — compound questions get compound answers; start from the outside view, adjust modestly with inside-view evidence, in that order; express uncertainty as a probability or range, not a verbal hedge ("likely," "possible") that can't be scored; a forecast isn't finished until it has a revisit trigger — forecasts decay as the world changes.
- **Procedure:**
  1. Sharpen the question until it's resolvable: specific outcome, specific timeframe, specific resolution criteria. Run `question-decomposition` if it's compound.
  2. Establish the outside view: `reference-class-forecasting` for a base rate.
  3. Gather the specific evidence for this case; weigh it via `bayesian-updating` against the base rate — resist swinging further than the evidence's actual strength warrants.
  4. Run `uncertainty-decomposition`: how wide should the confidence range genuinely be, and is more research worth it before finalizing?
  5. State the forecast as a number or range, not a word. Run `confidence-calibration`: does this number reflect genuine hit-rate expectations, or optimism/pessimism bias?
  6. Set `tripwires` for what evidence would most shift the forecast, and schedule a revisit date.
  7. After resolution (when it comes), score the forecast against the outcome and feed the result back into your calibration record.
- **Mistakes:** anchoring on inside-view story-telling before checking the base rate; expressing confidence in unscoreable verbal terms; treating a forecast as permanent once made instead of updating on schedule; never closing the loop — skipping the post-resolution scoring that's the entire mechanism for improving calibration over time.
- **Examples:** forecasting whether a project ships on time; estimating the probability a deal closes this quarter; geopolitical or market forecasting; predicting whether a policy will pass.
- **Related:** [[decision-analysis]] (consumes the forecast), [[scenario-planning]] (for multi-path futures rather than a single probability), [[delphi-aggregation]] (aggregating multiple forecasters).
