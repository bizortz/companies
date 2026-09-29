---
name: Improvement Cycle
assignee: org-improvement-lead
project: continuous-improvement
---

Run the `improvement-cycle` skill: cluster the `ops/learnings/` entries accumulated since the last run, rank clusters by metric impact x frequency, write proposals to `ops/improvements/<id>.md` for the top 3, static-check each with `skill-test static`, apply within the concurrency limits (one experiment per target file, three company-wide), track the target metric through its evaluation window against `ops/metrics-registry.yaml`, and keep or revert based on the measured outcome.

## Owner
`org-improvement-lead`

## Inputs
- `ops/learnings/` — every finding written since the last `improvement-cycle` run.
- `ops/metrics-registry.yaml` — canonical metric definitions and `min_sample` (read-only).
- `ops/improvements/ledger.md` — current open experiments, for concurrency-limit enforcement.

## Done Criteria
- Up to 3 new proposals written to `ops/improvements/<id>.md`, each with a diff, hypothesis, target metric, evaluation window, and rollback condition set before applying.
- Every applied change passed `skill-test static` with no regression.
- `ops/improvements/ledger.md` updated with the opened entries (and closed entries for any experiment whose window elapsed this cycle).
- Concurrency limits respected: no target file with two simultaneous open experiments, no more than 3 open company-wide.

## Next Task

**This task is recurring.** Its next task is itself: `improvement-cycle`, run again at the next sprint end (triggered from `retrospective`'s Handoff step), consuming whatever new `ops/learnings/` entries have accumulated since this run. There is no terminal state — this loop runs for the life of the studio.
