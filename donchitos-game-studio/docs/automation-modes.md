# Automation Modes

Adapted from Claude-Code-Game-Studios (`Donchitos/Claude-Code-Game-Studios`,
commit `7ed2c3e9c46c880c9780fbce49266e7edfa15141`, `.claude/docs/automation-modes.md`,
`usage: adapted`). Rewritten for this studio's autonomous operating model:
the upstream document defaulted to `collaborative` and required a human
decision-maker at nearly every gate; this studio defaults to, and normally
runs exclusively in, `autonomous` mode. This document is the source of truth
for how every agent and skill decides when to act on its own, when to
escalate to another agent, and when (rarely) to stop for a human.

## Default mode: `autonomous`

Every skill and agent in this package operates in `autonomous` mode unless a
project explicitly and temporarily overrides it (e.g. to onboard a new human
producer who wants to watch a few cycles first). There is no per-skill
exemption list — hotfix, gate-check, day-one-patch, and setup-engine all run
autonomously like everything else, because the studio has no user to ask.
Their heightened risk is handled instead by mandatory decision-log entries,
peer/manager review (see `docs/director-gates.md` and
`docs/coordination-rules.md`), and the always-ask list below.

## The three modes (for compatibility with imported upstream skill text)

Some adapted skill bodies still reference `collaborative` / `guided` /
`autonomous` as a configurable `modes.automation` value inherited from
upstream tooling. Where that language appears, resolve it as follows:

| Mode | Status in this studio | Behavior |
|------|------------------------|----------|
| `collaborative` | Not used in normal operation | Upstream's original behavior: a human is asked at every decision. Retained only as a concept for onboarding/demo runs; never the default. |
| `guided` | Not used in normal operation | Upstream's halfway mode: a human is asked only for "major" decisions. Not used because this studio has no standing human decision-maker to ask. |
| `autonomous` | **Default and normal mode** | The owning agent decides and proceeds. No draft review, no "may I write?" prompt. Every decision above specialist level is recorded in `ops/decision-log.md`. The only interruptions are the fixed `automation_always_ask` list below. |

If a skill's inlined upstream text still says "ask the user" or presents an
interactive question, treat that instruction as superseded by this document:
decide autonomously, using the decision rule below, and log it.

## Decision flow (see also `COMPANY.md` → Autonomous Operating Protocol)

1. The owning agent (the specialist or lead whose domain the decision falls
   in) decides.
2. If the decision crosses that agent's domain boundary (affects another
   department's scope, budget, or timeline), it escalates to its manager.
3. Director-level conflicts (Creative Director / Technical Director /
   Producer disagreeing) escalate to the CEO.
4. The CEO's decision is final.
5. Every decision made above specialist level is appended to
   `ops/decision-log.md` with: `id, date, agent, decision, options
   considered, rationale, reversibility (reversible|costly|irreversible),
   expected metric impact`.

## `automation_always_ask` — the only human gates

Even in `autonomous` mode, the following categories always stop and require
explicit human sign-off before proceeding. This list is authoritative and is
also stored machine-readably in `ops/always-ask.yaml`; the two must be kept
in sync.

1. Spending real money above `SPEND_LIMIT_USD` per week.
2. First public release, or any price change.
3. Accepting legal terms or contracts.
4. Handling personal data outside policy.
5. Deleting production data.

No other category — not scope changes, not file deletions, not schema
changes, not architecture decisions, not version bumps, not external API
calls — triggers a human gate by default. Those upstream categories are
instead handled by: recording the decision in `ops/decision-log.md`,
following `docs/error-recovery-protocol.md` if something goes wrong, and
routing genuine cross-domain disagreement through the escalation chain above
rather than to a human.

## Decision Log Format

Appended to `ops/decision-log.md` (created if absent, append-only, never
truncated):

```markdown
## [id] — [date] — [agent]

**Decision:** [what was decided]
**Options considered:** [list of options that were weighed]
**Rationale:** [why this option was chosen]
**Reversibility:** reversible | costly | irreversible
**Expected metric impact:** [what KPI/metric this is expected to move, and how]
```

### What to log

- Log every decision that would previously have been an interactive question
  to a human — including framing/option choices, not only final approvals.
- Collapse a single multi-part decision into one entry; list each part under
  **Options considered** / **Decision** rather than emitting one entry per
  sub-choice.
- Do not log routine, easily-reversible micro-choices with no scope/budget/
  timeline impact (e.g. which section to draft first) — log decisions that
  change project state, direction, scope, or spend.
- When genuinely unsure whether something needs a decision-log entry, log it
  anyway — failing toward more auditability, not less.

## Error handling

If a decision, skill run, or automated action fails or produces an
unexpected result, follow `docs/error-recovery-protocol.md` rather than
stopping and waiting for a human — recovery, rollback, and retry are handled
by the owning agent and escalated per the decision flow above only if the
protocol's own escalation criteria are met.

## Setting/checking the mode

Projects may record `modes.automation` in `project.yaml` for compatibility
with imported upstream skill logic that still reads that key. If unset, or
if the value is anything other than `autonomous`, agents should treat the
effective mode as `autonomous` for all decisions except those in
`automation_always_ask` — this package does not ship a `collaborative` or
`guided` runtime path, only the documentation of what those upstream terms
mean if encountered in older skill text.
