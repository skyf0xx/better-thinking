# 13 · Ethics & Values

Reasoning about should, not just can.

---

### ethical-framework-rotation `atomic · D3 · ~500 tok`
Evaluate a decision or action through consequentialist, deontological, and virtue-ethics lenses in turn, and report where they agree and where they genuinely diverge.

- **Why:** Any single ethical framework has known blind spots — consequentialism can justify harmful means for good ends, deontology can produce rigid outcomes that ignore context, virtue ethics can be vague about specific action-guidance. Rotating through multiple frameworks surfaces disagreement that a single-lens analysis would hide, and convergence across frameworks is much stronger evidence than any one framework's verdict alone.
- **Inputs:** a decision or action with an ethical dimension → **Outputs:** a verdict from each of three lenses, with explicit agreement/disagreement noted, and — where they diverge — what's actually driving the disagreement.
- **Activate when:** a decision has a genuine ethical dimension beyond pure preference or efficiency; a decision "feels" uncomfortable in a way that isn't captured by cost-benefit alone; policy or precedent-setting decisions. **Skip when:** the question is purely factual or preferential with no real ethical stakes.
- **Principles:** consequentialist lens asks: what outcome does this produce, for whom, weighed how? Deontological lens asks: does this respect rules, rights, and duties regardless of outcome — would it be acceptable if universalized? Virtue lens asks: what would a person of good character do here, and what does this action express about character? Convergence across all three is strong evidence; divergence is not a tiebreak to resolve mechanically — it's the actual finding, worth sitting with rather than papering over.
- **Procedure:**
  1. State the decision or action precisely, including who's affected.
  2. **Consequentialist pass:** enumerate outcomes and who bears them ([[stakeholder-impact]]); weigh net welfare, not just the actor's own benefit.
  3. **Deontological pass:** identify relevant duties, rights, and rules; ask if the action could be universalized (would it still work if everyone in this position did it?) without contradiction or harm.
  4. **Virtue pass:** ask what this action reveals about character — honesty, courage, fairness, temperance — independent of the outcome or the rule.
  5. Compare the three verdicts. Where they agree, that's a robust conclusion. Where they diverge, identify precisely what's driving the split (a good outcome achieved through a rights violation; a dutiful act that produces real harm).
  6. Report the divergence honestly rather than picking the framework that gives the preferred answer.
- **Mistakes:** running only the framework that happens to support a pre-existing preference (framework-shopping); treating disagreement between lenses as a bug to resolve by force rather than a genuine signal about the decision's difficulty; skipping the exercise on decisions that "feel fine" — that's often exactly where a blind spot hides.
- **Examples:** a business decision that's profitable (consequentialist win) but relies on a misleading disclosure (deontological problem); a policy that's dutifully rule-following but produces bad outcomes for a vulnerable group; a personal choice evaluated for what it says about the kind of person you're becoming.
- **Related:** [[stakeholder-impact]], [[value-tradeoffs]], [[steelmanning]] (apply to the position you're inclined to reject). **Prereqs:** none.

---

### stakeholder-impact `atomic · D2 · ~450 tok`
Enumerate every party affected by a decision and map the distribution of harms and benefits across them — including parties with no voice in the decision.

- **Why:** Decisions are evaluated by default from the decider's own vantage, which systematically under-weights costs borne by people not in the room. Explicit enumeration catches distributional effects — including on people who can't advocate for themselves in this process — before they become a surprise.
- **Inputs:** a decision or action → **Outputs:** a map of affected parties with the harm/benefit each bears, and a flag on any party disproportionately burdened without proportionate voice or benefit.
- **Activate when:** any decision affecting people beyond the decider; especially decisions where the affected and the deciding parties differ (the classic setup for externalized harm). **Skip when:** the decision affects only the decider themselves.
- **Principles:** include indirect and downstream parties, not just the immediately obvious ones — a policy's effects ripple; parties with no voice in the decision (future generations, absent third parties, the less powerful side of an asymmetric relationship) deserve deliberate inclusion, since they won't surface themselves; distribution matters as much as total welfare — a net-positive decision that concentrates cost on one powerless group is a different ethical situation than one that spreads cost evenly.
- **Procedure:**
  1. List every party materially affected, direct and indirect ([[stakeholder-mapping]] as the structural tool).
  2. Deliberately check for parties with no voice in this decision process — who's affected but not consulted or represented?
  3. For each party, estimate the harm and benefit they bear.
  4. Check the distribution: is cost concentrated on a party with little power or voice, while benefit accrues elsewhere?
  5. Flag any severe or irreversible harm to any single party, even if net outcomes are positive — aggregation can hide a serious localized harm.
  6. Report the map, with the distributional flag as a first-class finding, not a footnote.
- **Mistakes:** stopping at the directly obvious stakeholders and missing indirect/downstream ones; evaluating only net/aggregate welfare and missing a concentrated, severe harm to a minority party; never checking for voiceless parties, who by definition won't raise their hand to be included.
- **Examples:** a policy change's effects on a population that wasn't consulted; a company decision's effects on contractors vs employees; an environmental decision's effects on future generations.
- **Related:** [[stakeholder-mapping]], [[ethical-framework-rotation]], [[second-order-scan]]. **Prereqs:** none.

---

### value-tradeoffs `atomic · D3 · ~500 tok`
Make competing values explicit and price the actual exchange rate between them, rather than letting a decision silently smuggle in one value's priority over another.

- **Why:** Real decisions routinely trade one genuine value against another (speed vs safety, autonomy vs equity, privacy vs transparency) — but this trade is often made implicitly, without anyone deciding on purpose what the exchange rate should be. Making it explicit turns a hidden default into a deliberate, defensible choice.
- **Inputs:** a decision where two or more legitimate values conflict → **Outputs:** the competing values named explicitly, the actual exchange rate the decision implies, and a deliberate judgment on whether that rate is the right one.
- **Activate when:** a decision keeps stalling because "it depends what you prioritize"; two people disagree despite agreeing on the facts (the disagreement is values, not evidence); a decision has an uncomfortable tradeoff being avoided rather than named. **Skip when:** the values genuinely don't conflict in this case — check first before assuming a tradeoff exists.
- **Principles:** name both values precisely — vague value labels ("fairness," "innovation") hide the actual conflict; state the exchange rate the decision implies as concretely as possible ("this saves 2 days at a cost of a 5% higher defect rate") — pricing it, even roughly, is what makes the tradeoff visible instead of assumed; a values disagreement can't be resolved by more evidence — recognizing that early prevents an unproductive argument that pretends to be about facts.
- **Procedure:**
  1. Identify the two (or more) values genuinely in tension for this specific decision.
  2. State each precisely — not as a slogan, but as what it actually requires in this context.
  3. Estimate the exchange rate the leading option implies: how much of value A is being given up for how much of value B?
  4. Ask whether that rate is the one you'd endorse on reflection, or whether it's arrived at by default/inertia rather than judgment.
  5. Where people disagree, check whether the disagreement is actually about facts (resolvable by evidence) or about the exchange rate itself (a genuine values disagreement, resolvable only by explicit judgment or negotiation, not more data).
  6. Report the tradeoff and the judgment made, so it's visible and revisitable rather than buried.
- **Mistakes:** treating a values disagreement as if more evidence would resolve it; leaving the exchange rate implicit, so the decision silently favors whichever value the loudest voice in the room happens to prioritize; false-precision pricing a genuinely incommensurable tradeoff (some exchange rates should stay qualitative, not be forced into fake numbers).
- **Examples:** a product's speed-to-market vs quality tradeoff, priced explicitly rather than assumed; a policy balancing individual privacy against collective safety; a personal choice between career advancement and family time.
- **Related:** [[ethical-framework-rotation]], [[weighted-scoring]] (the mechanical sibling, for non-ethical multi-criteria tradeoffs), [[decision-framing]]. **Prereqs:** none.
