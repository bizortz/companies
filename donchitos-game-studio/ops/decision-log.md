# Decision Log

Append-only record of every decision made above specialist level in this
studio, per `docs/automation-modes.md` and `COMPANY.md`'s Autonomous
Operating Protocol. Never truncate or remove entries — if a decision is
later reversed, add a new entry noting the reversal rather than editing the
original.

## Format

Each entry:

```markdown
## [id] — [date] — [agent]

**Decision:** [what was decided]
**Options considered:** [list of options that were weighed]
**Rationale:** [why this option was chosen]
**Reversibility:** reversible | costly | irreversible
**Expected metric impact:** [what KPI/metric this is expected to move, and how]
```

`id` is a short sequential identifier, e.g. `D-0001`, unique within this file.

---

## D-0000 — 2026-09-29 — ceo

**Decision:** Adopt the autonomous operating model described in `COMPANY.md`
and `docs/automation-modes.md` for all studio operations going forward,
replacing the prior Question → Options → Decision → Draft → Approval
collaborative protocol.
**Options considered:** (1) Keep the collaborative protocol as-is; (2) adopt
a partial "guided" model with human checkpoints at major decisions; (3)
adopt full autonomy with a small fixed always-ask list.
**Rationale:** The studio has no standing human decision-maker to ask, and
frequent human gates are incompatible with running a live mobile game
studio that must ship, patch, and operate continuously. A small, fixed
always-ask list (`ops/always-ask.yaml`) covers the cases where getting it
wrong is genuinely irreversible or externally binding (money, legal, first
release/pricing, personal data, production data deletion); everything else
is faster and just as accountable when logged here instead of gated.
**Reversibility:** costly (reverting would require re-adding human-gate
language across dozens of agents/skills, but is not technically
irreversible).
**Expected metric impact:** Expected to increase throughput (cycle time from
decision to shipped artifact) substantially, at the cost of requiring this
decision log to be the primary audit mechanism instead of live approval.
