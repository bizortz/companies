---
name: improvement-cycle
description: Cluster ops/learnings/, propose and evaluate targeted AGENTS.md/SKILL.md
  changes against ops/metrics-registry.yaml, keep or revert on measured outcome.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `org-improvement-lead` decides and logs to `ops/decision-log.md` and `ops/improvements/ledger.md` per `docs/automation-modes.md`, escalating only per `ops/always-ask.yaml`. This skill never edits `ops/metrics-registry.yaml`, `ops/targets.yaml`, or `ops/always-ask.yaml` — it reads them as fixed inputs.

# Improvement Cycle

## Purpose

Turn the raw findings accumulated in `ops/learnings/` into a small number of concrete, measured, reversible changes to the studio's own AGENTS.md/SKILL.md files — replacing `skill-improve`'s purely structural (`skill-test static`) scoring with an outcome loop that only keeps a change if it actually moved a real metric in `ops/metrics-registry.yaml`, and reverts it otherwise. This is the studio's only mechanism for self-modifying its own process documents; it must be conservative, auditable, and strictly bounded in scope.

## Trigger / Owner Agent

Owner: `org-improvement-lead`. Runs automatically at sprint end, triggered from `retrospective`'s Handoff step (see `skills/retrospective/SKILL.md`), and may also be run ad hoc after a significant `incident-response` or `kpi-review` finding.

## Inputs

- All `ops/learnings/*.md` entries written since the last `improvement-cycle` run.
- `ops/metrics-registry.yaml` — canonical metric definitions and `min_sample` values (read-only).
- `ops/improvements/ledger.md` — current open experiments, for the concurrency limits.
- `skills/skill-improve/SKILL.md` and `skills/skill-test/SKILL.md` — the structural static-check tooling this skill runs before applying any change.

## Procedure

1. **Cluster.** Group the new `ops/learnings/` entries since the last run by `affected agent/skill` and by `metric affected`. Rank clusters by (estimated metric impact, using the cluster's stated severities and metrics) x (frequency, the count of entries in the cluster).
2. **Propose.** For the top 3 ranked clusters, write a proposal to `ops/improvements/<id>.md` containing: the exact target file (one AGENTS.md or SKILL.md), an exact diff (not a vague description), a stated hypothesis connecting the diff to the target metric, the target metric id (from `ops/metrics-registry.yaml`), the evaluation window (N sprints or N days, sized so the metric's `min_sample` is achievable within it), and a rollback condition stated in advance (e.g. "revert if the target metric has not improved by the end of the window, or if any guardrail metric regresses beyond its own normal variance").
3. **Static-check before applying.** Run `skill-test static` (via `skill-improve`) against the proposed diff. If it introduces a structural regression (missing required section, frontmatter break, word-count failure), the proposal is rejected and logged as such in the ledger — it never reaches the apply step.
4. **Enforce concurrency limits.** Before applying, check `ops/improvements/ledger.md` for open experiments: skip a proposal whose target file already has an open experiment, and stop proposing once 3 experiments are open company-wide, regardless of how many good clusters remain — carry the rest to the next cycle.
5. **Apply.** Apply the diff on a branch or as a versioned copy (never overwrite the only copy of the file irreversibly) and record the baseline value(s) of the target metric (and any relevant guardrail metrics) at the moment of applying, per `ops/metrics-registry.yaml`'s `min_sample` — do not baseline off a reading below `min_sample`.
6. **Evaluate at window end.** After the evaluation window elapses, re-read the target metric (and guardrails) once `min_sample` is met. If the target metric moved in its registered `direction` and no guardrail metric regressed beyond its normal tolerance, **KEEP** the change (merge the branch / make the versioned copy canonical). Otherwise **REVERT** to the pre-experiment version.
7. **Log.** Record the full outcome — kept or reverted, with the before/after metric values and rationale — as a closing entry in `ops/improvements/ledger.md`, and log the decision to `ops/decision-log.md`.

## Output

Per proposal, write `ops/improvements/<id>.md`:

```markdown
# Improvement Proposal <id>

**Target file:**
**Cluster (learnings entries):**
**Diff:**
```diff
<exact diff>
```
**Hypothesis:**
**Target metric:** <id from ops/metrics-registry.yaml>
**Evaluation window:**
**Rollback condition:**
**skill-test static result:** PASS
```

And append the corresponding entry (opened, then closed) to `ops/improvements/ledger.md` per its schema.

## Pass/Fail Criteria

Pass: every applied change has a pre-stated hypothesis, target metric, window, and rollback condition; nothing is applied without a passing `skill-test static` result; concurrency limits (1 per file, 3 company-wide) are never exceeded; every outcome — kept or reverted — is logged in the ledger. Fail: a change applied without a pre-registered rollback condition, a fourth concurrent experiment, or a KEEP decision made without checking guardrail metrics.

## Handoff

Triggered by `retrospective`'s Handoff step at sprint end. Proposals that would require a `reportsTo` change, agent deletion, or an edit to a guardrailed file (see `agents/org-improvement-lead/AGENTS.md`'s Must NOT list) are written up as a **structural decision proposal** to `ceo` instead of being applied — this skill never self-applies an org-structure change.
