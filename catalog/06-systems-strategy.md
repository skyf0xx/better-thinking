# 6 · Systems & Strategy

Thinking about wholes, dynamics, and adversaries.

---

### systems-mapping `atomic · D4 · ~600 tok`
Model a system's stocks, flows, delays, and boundaries explicitly, so its behavior can be reasoned about structurally rather than narratively.

- **Why:** Complex behavior (oscillation, overshoot, collapse) usually comes from structure — delays and feedback — not from any single villain or event. A narrative explanation misses this; a stock-flow map exposes it.
- **Inputs:** a system exhibiting some behavior of interest → **Outputs:** a stock-and-flow map with delays marked, plus the structural explanation for the observed behavior.
- **Activate when:** behavior seems to have no single cause; oscillation, lag, or overshoot is observed; a system resists an obvious-seeming fix. **Skip when:** the system is simple and linear — a direct cause suffices.
- **Principles:** stocks are accumulations (things you could photograph); flows change them over time; delays between action and visible effect are the single biggest cause of oscillation and overshoot; system boundaries are chosen, not given — what's "outside the system" is often where the real leverage or the real cost hides.
- **Principles (cont'd):** behavior emerges from structure — the same structure produces the same class of behavior regardless of the specific actors in it.
- **Procedure:**
  1. Identify the stocks (accumulated quantities: inventory, trust, backlog, headcount, debt).
  2. Identify the flows in and out of each stock, and what controls their rate.
  3. Mark delays between a control action and its visible effect on the stock.
  4. Draw feedback: does a stock's level influence its own flows, directly or indirectly? (Feeds [[feedback-loop-analysis]].)
  5. Set the boundary explicitly: what's inside the model, what's treated as external/given — and note what that choice hides.
  6. Explain the observed behavior structurally: which stock, flow, or delay produces it?
  7. Identify where an intervention would act on structure rather than just pushing on a symptom.
- **Mistakes:** confusing a flow (rate) with a stock (level) — "hiring is high" (flow) vs "we're understaffed" (stock, driven by flows over time); ignoring delays and expecting immediate feedback from an action; drawing the boundary to exclude the actual cause.
- **Examples:** why a hiring surge doesn't fix understaffing for months; inventory bullwhip in a supply chain; why a popular feature's support burden shows up a quarter later; a forest fire fuel-accumulation model.
- **Related:** [[feedback-loop-analysis]], [[leverage-points]], [[bottleneck-analysis]]. **Prereqs:** none, but pairs tightly with [[feedback-loop-analysis]].

---

### feedback-loop-analysis `atomic · D3 · ~500 tok`
Identify the reinforcing (amplifying) and balancing (self-correcting) loops that drive a system's behavior over time.

- **Why:** Most persistent behaviors — growth, decline, equilibrium, oscillation — are loop-driven, and the loop type predicts the shape of the behavior before you even have data. Recognizing which loop dominates tells you whether to accelerate, dampen, or redirect it.
- **Inputs:** a system or trend with an observable pattern over time → **Outputs:** the dominant loop(s) identified, their type, and the point where intervention changes the loop's behavior.
- **Activate when:** something is growing, shrinking, or oscillating and you want to know why it will continue or stop; designing an intervention meant to persist. **Skip when:** the behavior is a one-off event, not a pattern.
- **Principles:** reinforcing loops amplify — more begets more (or less begets less) — and explain runaway growth or collapse; balancing loops seek a target and resist change — they explain why some things "snap back"; every reinforcing loop is eventually capped by a balancing loop (a limit) — the question is which one binds and when; the loop with the shortest delay dominates short-term behavior; the loop with the longest reach often dominates long-term behavior.
- **Procedure:**
  1. Describe the behavior pattern observed (growing, shrinking, oscillating, stable).
  2. Trace the causal loop: does A increase B, which increases A (reinforcing), or does A increase B, which decreases A (balancing)?
  3. Identify all loops touching the variable of interest; note which dominates currently and why.
  4. For reinforcing loops, find the limit that will eventually cap them — it's usually already operating, just weaker.
  5. For balancing loops, find the target they're defending — interventions that fight the target get absorbed; interventions that change the target work.
  6. Recommend intervention at the loop level: strengthen/weaken a specific loop, or shift a balancing loop's target — not a one-off push against current behavior.
- **Mistakes:** pushing against a balancing loop's target instead of changing the target (the system reabsorbs the push); missing that a runaway reinforcing loop is about to hit its cap; treating a loop-driven pattern as caused by a single triggering event.
- **Examples:** viral growth (reinforcing) hitting market saturation (balancing cap); a thermostat-like pricing/demand cycle; why adding process to fix quality issues sometimes makes throughput-driven quality issues worse (wrong loop targeted); habit formation loops.
- **Related:** [[systems-mapping]] (the structural substrate), [[leverage-points]], [[second-order-scan]]. **Prereqs:** [[systems-mapping]] helpful for complex cases.

---

### bottleneck-analysis `atomic · D2 · ~450 tok`
Locate the single binding constraint in a system and subordinate all other improvement effort to it — the Theory of Constraints move.

- **Why:** Improving anything that isn't the constraint doesn't change system throughput — it just creates local optimization and inventory piling up elsewhere. Finding the actual constraint redirects effort to where it compounds.
- **Inputs:** a system with a throughput or output goal → **Outputs:** the identified constraint, and a plan that subordinates non-constraint improvements to exploiting it.
- **Activate when:** improvement effort feels diffuse or isn't moving the outcome metric; "everything is a priority"; a process has an obvious slow point everyone routes around instead of fixing. **Skip when:** the system genuinely has excess capacity everywhere (rare) — then any improvement helps.
- **Principles:** a chain's throughput equals its weakest link's throughput, full stop — no other link's improvement matters until the weakest link changes; before adding capacity to the constraint, first *exploit* it (remove waste at that exact point) — it's usually cheaper; once a constraint is resolved, the constraint moves elsewhere — this is a continuous process, not a one-time fix.
- **Procedure:**
  1. Define the system's throughput goal precisely.
  2. Map the stages/components the work flows through.
  3. Find where work queues up or where the output rate ceiling actually sits — that's the constraint (not where people feel busiest, which is often a red herring).
  4. Exploit it: remove waste, idle time, and low-value work at the constraint specifically, before spending on capacity.
  5. Subordinate everything else: other stages should pace to the constraint, not run at their own max (which just builds queue).
  6. If still insufficient, elevate: add capacity at the constraint specifically.
  7. Repeat — identify where the constraint moved to next.
- **Mistakes:** optimizing a non-constraint stage because it's easier or more visible; adding capacity before exploiting (expensive fix for a cheap problem); declaring victory after one round instead of repeating.
- **Examples:** a hiring pipeline bottlenecked at reference checks, not sourcing; a factory line's slowest station; an engineering org bottlenecked at code review, not coding; a sales funnel's actual drop-off stage.
- **Related:** [[constraint-relaxation]], [[systems-mapping]], [[prioritization-triage]]. **Prereqs:** none.

---

### leverage-points `atomic · D4 · ~600 tok`
Rank potential interventions by depth — from adjusting parameters to changing rules, structure, goals, or paradigms — since deeper points change more with less effort.

- **Why:** Effort naturally flows to the shallowest, most tangible leverage points (tweak a number) because they're easiest to act on — but they're also the weakest. Explicitly scanning deeper points (rules, information flows, goals, paradigms) finds where small changes produce large system-wide shifts.
- **Inputs:** a system + a desired change in its behavior → **Outputs:** candidate interventions ranked by leverage depth, with the effort-to-impact tradeoff named per depth level.
- **Activate when:** an intervention has been tried at the obvious level and didn't stick; seeking high-impact, resource-constrained interventions; a system keeps producing the same outcome despite parameter tweaks. **Skip when:** a shallow fix is genuinely sufficient and durability doesn't matter.
- **Principles:** shallow leverage (numbers: budgets, quotas, rates) is easy to pull but easy for the system to absorb or revert; deep leverage (rules, power structure, information flows, goals, the paradigm/mindset generating the goals) is harder to pull but the system can't easily undo it; deeper is not always better — it's also higher risk and slower; changing *who has access to what information* is an underused, moderate-depth lever.
- **Procedure:**
  1. State the desired change in system behavior.
  2. Scan for candidate interventions across depth levels: parameters (numbers, rates) → buffers/stocks → structure (physical/organizational) → rules (incentives, constraints, who decides) → information flows (who sees what, feedback visibility) → goals (what the system is optimizing for) → paradigm (the unstated worldview generating the goals).
  3. For each candidate, estimate effort to pull the lever and durability of the effect once pulled.
  4. Check history: has a shallow fix been tried here before and reverted? That's evidence the real leverage is deeper.
  5. Choose the shallowest lever that will actually be durable — deepest-possible is not the goal, appropriately-deep is.
  6. Note the risk: deeper levers have wider blast radius — pair with [[second-order-scan]].
- **Mistakes:** always reaching for the parameter lever (budgets, targets) because it's legible and reversible, then being surprised it doesn't stick; going straight to paradigm-level intervention when a rule change would have sufficed; ignoring information-flow changes, often the highest leverage-per-effort lever available.
- **Examples:** a metric target keeps getting gamed (parameter-level fix fails) until the *measured goal itself* changes (goal-level); an org's speed problem solved not by more people but by exposing decision latency to leadership (information-flow level); changing default enrollment instead of running an awareness campaign.
- **Related:** [[systems-mapping]], [[feedback-loop-analysis]], [[second-order-scan]]. **Prereqs:** [[systems-mapping]] recommended for nontrivial systems.

---

### game-theoretic-analysis `atomic · D4 · ~600 tok`
Model a strategic interaction's players, available moves, payoffs, and information to identify likely equilibria and exploitable asymmetries.

- **Why:** When outcomes depend on others' choices that depend on yours, single-actor optimization gives wrong answers. Modeling the interaction explicitly reveals what a rational counterpart will actually do — often counter to what they say.
- **Inputs:** a strategic situation with ≥2 interacting parties whose outcomes are interdependent → **Outputs:** the game's structure (players, moves, payoffs, information), likely equilibrium behavior, and the point of maximum leverage.
- **Activate when:** negotiating, competing, or designing mechanisms/incentives where others will respond strategically; predicting a rival's move; auditing whether a policy is game-able. **Skip when:** the other party's behavior is fixed/non-strategic — this is overkill for non-interactive decisions.
- **Principles:** payoffs must be modeled from each player's perspective, not yours — their rational move depends on *their* incentives; check what's common knowledge vs private information — information asymmetry changes the game entirely; a stated threat or promise is only credible if it's rational for them to follow through when the moment comes; repeated interaction changes the game — cooperation can be rational in a repeated game where it isn't in a one-shot game.
- **Procedure:**
  1. Identify the players and their available moves.
  2. Estimate each player's payoff for each outcome combination — from their perspective and incentives, not yours ([[incentive-analysis]]).
  3. Identify what's common knowledge vs privately known by each side.
  4. Determine if it's one-shot or repeated — repeated games support cooperation and reputation effects that one-shot games don't.
  5. Find the likely equilibrium: what does each player do if they assume the others act rationally in their own interest?
  6. Check credibility of any threats/promises in the model — would the player actually want to follow through when the time came?
  7. Identify your highest-leverage move: where can you change the *other* player's payoffs or information, not just react to them?
- **Mistakes:** modeling the other side's payoffs as if they shared your values; assuming a stated threat is credible without checking if carrying it out would be rational for them; treating a repeated interaction as one-shot (destroys cooperation) or vice versa; ignoring that your own move changes their optimal response (non-strategic best-response thinking).
- **Examples:** pricing decisions anticipating a competitor's response; a negotiation's opening-offer strategy; designing an auction or incentive mechanism resistant to gaming; predicting whether a rival will match a price cut.
- **Related:** [[incentive-analysis]], [[negotiation]], [[wargaming]] (multi-turn extension), [[second-order-scan]]. **Prereqs:** none, but [[incentive-analysis]] sharpens it.

---

### chestertons-fence `atomic · D1 · ~350 tok`
Before removing or changing something that seems useless, reconstruct why it was put there in the first place.

- **Why:** Things that look pointless from the outside often encode hard-won knowledge about a failure mode you haven't personally experienced yet. Removing them without understanding them is how the failure mode returns.
- **Inputs:** an existing rule, process, structure, or artifact that seems unnecessary → **Outputs:** the reconstructed original rationale, a verdict on whether it still applies, and a removal plan if it doesn't.
- **Activate when:** about to remove, simplify, or bypass something inherited whose purpose isn't obvious; "why do we even do this?" moments. **Skip when:** the origin is already fully known and documented — go straight to the verdict.
- **Principles:** "I don't see the point of this" is a report about your knowledge, not about the fence's uselessness; find the person or failure that motivated it before deciding; some fences really are obsolete — the goal is an informed removal, not permanent deference.
- **Procedure:**
  1. Identify the fence: the specific rule/step/structure in question.
  2. Ask: who put this here, and what problem were they solving? Investigate — don't guess.
  3. If the origin can't be reconstructed, treat that as a yellow flag, not a green light: proceed cautiously, perhaps with a reversible trial removal.
  4. Determine whether the original condition that motivated the fence still holds.
  5. If it doesn't hold: remove it, but note what monitoring would catch the failure mode returning.
  6. If it does hold, or is unclear: keep it, and document the rationale for the next person who asks this question.
- **Mistakes:** removing first and discovering the reason the hard way; treating every inherited rule as sacred regardless of changed conditions (the opposite failure); accepting "we've always done it this way" as the reconstructed rationale (that's an absence of one).
- **Examples:** a deployment step that looks redundant until you learn it prevents a specific data-corruption class; a legal boilerplate clause; an org policy from a past incident nobody remembers.
- **Related:** [[first-principles]] (the counterweight — willingness to discard), [[assumption-audit]]. **Prereqs:** none.

---

### backcasting `atomic · D2 · ~450 tok`
Define a desired future state in detail, then work backward to derive the sequence of changes that would produce it — strategy's version of [[working-backwards]].

- **Why:** Forecasting extrapolates from the present and tends to reproduce it with minor variation. Backcasting starts from a deliberately chosen future and asks what must change to reach it — better suited when the goal is transformation, not prediction.
- **Inputs:** a time horizon + a desired future state → **Outputs:** a backward path of milestones and changes from that future to the present, with the first actionable step identified.
- **Activate when:** setting long-horizon strategy or vision; current trends don't lead anywhere close to the desired outcome; planning around a discontinuity you intend to cause. **Skip when:** the future state isn't really in question — use [[working-backwards]] for shorter, more concrete goals instead.
- **Principles:** describe the future state concretely — vague visions can't be backward-chained; permit the path to require things that don't exist yet (unlike forecasting, backcasting isn't bound by extrapolating current capability); check the path against constraints only after the ideal path is drawn, or you'll re-derive the present.
- **Procedure:**
  1. Set the horizon and describe the desired future state concretely and specifically.
  2. Describe the present state on the same dimensions.
  3. Work backward from the future: what had to be true one step before arrival? Keep stepping back.
  4. Continue until the chain reaches the present state or near-present actions.
  5. Only now check feasibility/constraints on each step — resist doing this during generation.
  6. Identify the first actionable step and the earliest hard commitment point.
  7. Compare to a forward-extrapolated forecast; the gap between them is the actual strategic challenge.
- **Mistakes:** vague future states ("be the market leader") that can't anchor a backward chain; constraint-checking too early, which collapses the vision back to incremental present-day thinking; treating the backward path as a guaranteed forecast rather than a designed intention.
- **Examples:** a climate target's required policy sequence; a company's 10-year platform vision worked backward to this year's roadmap; a personal long-horizon career design.
- **Related:** [[working-backwards]] (shorter horizon), [[scenario-planning]] (for uncertain rather than chosen futures), [[strategic-planning]]. **Prereqs:** none.

---

### ooda-loop `composite · D3 · ~800 tok`
Observe, orient, decide, act — iterated fast enough that your tempo outpaces the environment's rate of change or an adversary's own loop.

- **Why:** In fast-changing or adversarial situations, being *approximately right, quickly, repeatedly* beats being precisely right once, slowly — because the situation moves before a slow analysis finishes. The loop's power is in the iteration rate, not any single pass's rigor.
- **Inputs:** a fast-moving or adversarial situation requiring repeated action under incomplete information → **Outputs:** a sequence of fast decision cycles, each updating on the last cycle's results.
- **Dependencies:** `sanity-checking`, `bayesian-updating`, `progress-monitoring`, `effort-calibration`.
- **Activate when:** conditions change faster than a full analysis cycle; competitive/adversarial dynamics where tempo itself is an advantage; incident response. **Skip when:** conditions are stable and getting it right once matters more than getting it fast repeatedly — use [[decision-analysis]] instead.
- **Principles:** orientation (your mental model, shaped by culture, experience, prior information) is the crux — most OODA failures are orientation failures, not observation or decision failures; the loop is disrupted, not completed, when the situation changes mid-cycle — that's normal, restart the loop rather than forcing the old plan; speed of the *whole loop*, not any one stage, is the target metric; act to gather better information, not only to finish — the action itself can be a probe (`effort-calibration` on each cycle's depth).
- **Procedure:**
  1. **Observe:** gather current, direct information — not last cycle's stale picture. Note what's actually changed.
  2. **Orient:** update your mental model against the new observation (`bayesian-updating`); explicitly check whether your orienting assumptions still hold — this is where most loops break down unnoticed.
  3. **Decide:** commit to the best action given current orientation, sized appropriately for the uncertainty (`effort-calibration` — don't over-plan a fast-moving situation).
  4. **Act:** execute; treat the action partly as a probe that will generate the next cycle's observation.
  5. Immediately re-enter Observe with the results. Run `progress-monitoring` across cycles to catch drift or a stuck loop.
  6. If the situation outpaces your loop (you're consistently reacting to stale orientation), the priority becomes *shrinking cycle time*, even at the cost of rigor per cycle.
- **Mistakes:** treating it as a one-time sequential process instead of a tight repeating loop; over-investing in the Decide stage's rigor while Observe/Orient go stale; failing to update Orient (fighting the last cycle's situation); confusing action-for-progress with action-for-information.
- **Examples:** incident response; a startup responding to a fast-moving competitive threat; a fighter-pilot-style tactical scenario; live negotiation adjustment.
- **Related:** [[wargaming]] (models the adversary's loop explicitly), [[progress-monitoring]], [[scenario-planning]] (slower-tempo cousin).

---

### scenario-planning `composite · D4 · ~1000 tok`
Construct several divergent, internally consistent futures and test candidate strategies against all of them, rather than betting everything on one forecast.

- **Why:** Point forecasts are almost always wrong, and strategies optimized for one forecast are fragile when reality lands elsewhere. Building multiple plausible futures and demanding a strategy survive across them produces robustness that no single best-guess forecast can.
- **Inputs:** a strategic question with a meaningful time horizon and real uncertainty about the environment → **Outputs:** 3–4 divergent scenarios, each internally coherent, plus a strategy assessment of what performs well across them and what's a bet on one future only.
- **Dependencies:** `uncertainty-decomposition`, `structured-what-if`, `second-order-scan`, `sensitivity-analysis`, `tripwires`.
- **Activate when:** long-horizon strategic decisions where the environment (market, technology, regulation, competition) is genuinely uncertain, not just internally uncertain. **Skip when:** the horizon is short enough that a single forecast is reliable, or the decision doesn't depend on how the environment unfolds.
- **Principles:** scenarios are not predictions and not a probability-weighted set — they're a deliberately spread set designed to bracket the plausible range; the two or three axes of deepest uncertainty (not the many minor ones) generate the scenario set; a scenario must be internally consistent — pick a coherent combination of driver outcomes, not a grab-bag; the point is testing strategy robustness, not picking the "right" scenario in advance.
- **Procedure:**
  1. Frame the strategic question and horizon.
  2. Run `uncertainty-decomposition`: identify the critical uncertainties — the few drivers that are both highly uncertain and highly impactful (most drivers are one or the other; focus on both).
  3. Select the 2 axes of deepest uncertainty; cross them to generate 3–4 scenario "quadrants," or hand-author 3–4 divergent coherent narratives if the drivers aren't cleanly orthogonal.
  4. Flesh out each scenario with `structured-what-if`: what does this world look like in detail, and what does it imply for the question at hand?
  5. Test each candidate strategy against every scenario: does it work, fail, or need adaptation?
  6. Favor strategies that are robust across scenarios (`sensitivity-analysis` on strategy performance vs scenario) over those optimal in only one.
  7. Where a robust strategy doesn't exist, identify the earliest signal (`tripwires`) that would indicate which scenario is unfolding, and build the option to pivot.
  8. Run `second-order-scan` on the chosen strategy within its best-fit scenario — check for adaptation effects.
- **Mistakes:** treating one scenario as "the forecast" and just planning for it (defeats the entire method); generating scenarios that are all mild variations of the present (not divergent enough to test robustness); too many scenarios (dilutes attention — 3–4 is the practical range); skipping the tripwires step, leaving the org blind to which future is arriving.
- **Examples:** energy company planning across divergent regulatory/price futures; a startup's product strategy across different competitive-response scenarios; national security planning; a company's AI-adoption strategy across different capability-trajectory scenarios.
- **Related:** [[backcasting]] (chosen future vs uncertain futures), [[wargaming]] (adversarial version), [[structured-forecasting]] (probabilistic single-path version), [[decision-analysis]].

---

### wargaming `composite · D4 · ~950 tok`
Simulate an adversary's moves and countermoves across multiple turns to stress-test a strategy against active opposition, not a static environment.

- **Why:** Strategies evaluated against a passive environment miss the fact that a capable adversary adapts to whatever you do. Turn-based simulation with a genuinely adversarial opposing side surfaces the counter-moves a static plan can't see coming.
- **Inputs:** a strategy or plan + a capable, motivated adversary → **Outputs:** a multi-turn simulation record, the adversary's most damaging counter-strategy found, and plan revisions that survive it.
- **Dependencies:** `game-theoretic-analysis`, `incentive-analysis`, `red-teaming`, `second-order-scan`.
- **Activate when:** competitive strategy against a specific capable rival; military, security, or high-stakes competitive planning; testing a negotiating strategy against a sophisticated counterpart. **Skip when:** there's no real adversary — the challenge is environmental, not strategic (use [[scenario-planning]]).
- **Principles:** the opposing side must be played to genuinely win, not to lose gracefully — a wargame with a compliant adversary tests nothing; play multiple turns — single-turn exercises miss the adaptation dynamics that define real strategic interaction; the most valuable output is usually the adversary's move nobody on the planning side considered; separate the "blue" (planning) and "red" (adversary) teams so red isn't anchored on blue's assumptions.
- **Procedure:**
  1. Define the objective, the players, the turn structure, and what "winning" means for each side.
  2. Model the adversary's actual incentives and constraints (`incentive-analysis`, `game-theoretic-analysis`) — not a strawman opponent.
  3. Assign a red team empowered and motivated to find the plan's most damaging exploit (`red-teaming` posture).
  4. Play turn 1: blue commits to a move; red responds with their best countermove given blue's action and their own incentives.
  5. Run `second-order-scan` after each exchange — what does this move open up for subsequent turns?
  6. Continue for multiple turns; log every red counter-move that damaged blue's position.
  7. Debrief: which red moves were most damaging and least anticipated? Revise blue's strategy specifically against those.
  8. Re-run the revised strategy against the same or a fresh red team to confirm the fix holds.
- **Mistakes:** a red team that plays weakly, unconsciously protecting blue's plan; stopping after one turn (misses adaptation); blue team also serving as red (can't escape their own blind spots); treating the wargame's specific move sequence as a prediction rather than a stress test.
- **Examples:** competitive response simulation before a major product launch; a negotiation rehearsal against a sophisticated counterparty; military course-of-action wargaming; regulatory-response simulation before a public policy change.
- **Related:** [[game-theoretic-analysis]] (the modeling substrate), [[red-teaming]] (single-round sibling), [[scenario-planning]].

---

### strategic-planning `composite · D5 · ~1100 tok`
Rumelt's kernel: an honest diagnosis of the situation, a guiding policy for dealing with it, and a set of coherent actions — the discipline that separates strategy from goal-setting.

- **Why:** Most "strategy" documents are just ambitious goals with no theory of how to get there and no honest account of the obstacle. The kernel forces the diagnosis and the coherence check that goal-setting skips.
- **Inputs:** an organization or effort facing a significant challenge or opportunity → **Outputs:** a diagnosis of the core challenge, a guiding policy for addressing it, and a set of mutually reinforcing actions — explicitly not a list of goals.
- **Dependencies:** `problem-framing`, `first-principles`, `bottleneck-analysis`, `leverage-points`, `second-order-scan`, `premortem`.
- **Activate when:** setting direction for an organization, team, or major effort facing real obstacles (not just "grow more"); a strategy conversation keeps producing aspirations instead of a plan. **Skip when:** the challenge is tactical/local — use [[structured-problem-solving]] or [[decision-analysis]] instead.
- **Principles:** a goal ("double revenue") is not a strategy — a strategy explains *how*, given specific obstacles; the diagnosis must be honest about the actual obstacle, including organizationally uncomfortable causes, or the whole kernel is built on sand; the guiding policy is an approach to the obstacle, not a list of things that would be nice; actions must be coherent — each reinforcing the others, not a portfolio of unrelated initiatives bundled under one banner.
- **Procedure:**
  1. **Diagnosis:** run `problem-framing` and `first-principles` on the situation — what is the actual challenge, stated causally, not just as a gap from aspiration? Include obstacles that are organizationally inconvenient to name.
  2. Run `bottleneck-analysis` and `leverage-points` on the diagnosis: what's the binding constraint, and at what depth does it need to be addressed?
  3. **Guiding policy:** state the overall approach for dealing with the diagnosed obstacle — an approach, not a target. It should rule things out as much as it rules things in.
  4. **Coherent actions:** derive a small set of actions that reinforce each other under the guiding policy. Check coherence explicitly: does action A make action B more effective, or are they just riding in the same document?
  5. Stress-test with `premortem`: assuming this strategy failed in a year, why? Revise the diagnosis or actions accordingly.
  6. Run `second-order-scan` on the leading action: how does the environment/competition adapt once this strategy is visible?
  7. Publish the kernel compactly — diagnosis, policy, actions — resisting the pull to pad it into a goals list.
- **Mistakes:** substituting a goal or aspiration for a diagnosis ("our strategy is to be #1"); an action list that's really an assortment of good ideas with no coherence or common leverage point; skipping the honest-obstacle step because it implicates current leadership or past decisions; conflating strategic planning with annual budgeting.
- **Examples:** a company's response to a disruptive competitor; a nonprofit's theory of change; a team's technical strategy for addressing accumulated debt while still shipping; a country's industrial policy.
- **Related:** [[backcasting]], [[scenario-planning]] (for uncertain-environment strategy), [[decision-analysis]] (for the individual bets within the strategy).
