---
name: progress-monitoring
description: >
  Periodically compare actual progress against the plan, and explicitly
  decide whether to continue, adjust, or replan, rather than drifting on
  autopilot. Use for any plan or project extending over multiple work
  sessions, especially after decision-analysis or ooda-loop commits to a
  course of action.
type: atomic
category: metacognition
difficulty: 2
tokens: ~450
dependencies: []
related: [tripwires, after-action-review, ooda-loop]
---

# Progress Monitoring

Periodically compare actual progress against the plan, and explicitly decide whether to continue, adjust, or replan — rather than drifting on autopilot.

## Why

Plans decay as they meet reality, but without a deliberate checkpoint, the drift between plan and actual progress accumulates unnoticed until it's a crisis. Scheduled, explicit comparison catches divergence while it's still cheap to correct.

## Use when / Don't use when

- **Use when:** any plan or project extends over multiple work sessions or a meaningful duration, especially after `decision-analysis` or `ooda-loop` commits to a course of action.
- **Don't use when:** the task is short enough to complete in one sitting with no meaningful checkpoint.

## Inputs → Outputs

- **Inputs:** an in-progress plan with a defined goal.
- **Outputs:** a progress-vs-plan comparison at each checkpoint, and an explicit continue/adjust/replan decision.

## Principles

- Set checkpoints in advance, tied to milestones or time, not to "whenever it feels necessary" — which under time pressure becomes never.
- Compare against the original plan, not a silently-updated version of it, or drift becomes invisible by definition.
- Divergence is information, not failure — the checkpoint's job is to surface it early, when correction is cheap.

## Procedure

1. At plan commitment, set explicit checkpoints, time-based or milestone-based — this pairs with `tripwires` from the original plan.
2. At each checkpoint, compare actual state against the original plan's expected state at this point.
3. Diagnose any gap: an execution issue, or was the plan's assumption wrong? Run an assumption check on the original plan if so.
4. Decide explicitly: continue as planned, adjust the plan, or trigger a fuller replan or reframing.
5. If continuing, note the checkpoint passed cleanly; if adjusting, update the plan and future checkpoints explicitly rather than silently.
6. Never skip a scheduled checkpoint under the pressure that's exactly why it was scheduled — report any skipped checkpoint as residual risk.

## Common mistakes

- Skipping checkpoints when busy — the precise moment they're most needed.
- Comparing against a plan that's been silently revised in your head rather than the original commitment, which hides real drift.
- Treating every divergence as reason to panic-replan instead of first diagnosing whether it's a minor execution issue.

## Examples

- A project's weekly milestone check against the original timeline.
- A personal goal's monthly review against the original target.
- An `ooda-loop`'s repeated cycle applied to a slower-moving plan.

## Related

- [[tripwires]] — the pre-committed trigger conditions this skill checks against at each pass.
- [[after-action-review]] — the retrospective sibling, run once the plan concludes rather than mid-flight.
- [[ooda-loop]] — the fast-cadence sibling for time-critical, rapidly changing situations.
