---
name: incident-response
description: Runbook for a crash spike or store rejection — triage, mitigate,
  root-cause, and report.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `devops-engineer` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`. Deleting production data (e.g. rolling back a data migration) is always subject to the `delete_production_data` gate in `ops/always-ask.yaml`.

# Incident Response

## Purpose

Provide a consistent runbook for the two most common production incidents this studio faces: a live crash-rate spike, and a store rejection blocking a release. Speed and a clear mitigation-before-root-cause order matter more here than in most skills — a live incident should not wait on a full investigation before mitigating player impact.

## Trigger / Owner Agent

Owner: `devops-engineer`. Triggered automatically by a crash-free-session-rate breach in `ops/metrics-registry.yaml`'s guardrail range, by `qa-lead`/`security-engineer` flagging a spike, or by a rejection notice from `store-submission`.

## Inputs

- Crash telemetry / stability dashboards.
- `ops/metrics/<date>.md` (crash-free session rate trend).
- The store rejection notice text, if applicable, from `store-submission`.
- `design/perf-budget.md` for the stability floor being breached.

## Procedure

1. **Triage first.** Classify severity immediately: is this affecting all users, a device tier, a specific OS version, or a specific region/build? Use the crash telemetry's own breakdown, not a guess.
2. **Mitigate before root-causing.** If a specific recent build, feature flag, or server-side config is the likely trigger (e.g. crash rate spiked immediately after a release or live-ops config push), roll it back or disable the flag immediately — do not wait for full root-cause analysis if a safe, reversible mitigation is available. Any action that would delete production data as part of mitigation (e.g. reverting a data migration) requires the `delete_production_data` gate.
3. For a **store rejection**: read the actual rejection reason from the store; do not assume it matches a past rejection's cause. Route to the owning agent for the flagged area (`legal-compliance-officer` for privacy, `monetization-designer` for IAP, `aso-specialist` for listing content, `unity-specialist`/`engine-programmer` for a technical guideline violation) and re-run `store-submission` once fixed.
4. Once mitigated, perform root-cause analysis: reproduce if possible, identify the specific code/config/content change responsible, and file a bug via `bug-report`/route through `bug-triage`.
5. Communicate status: notify `producer`, `release-manager`, and (if player-facing) `community-manager`/`player-support` with current status and expected resolution.
6. After resolution, write the incident report and append a structured finding to `ops/learnings/<date>-incident-response.md` (finding, affected agent/skill, evidence, metric affected, severity) so the improvement loop can see whether this incident reveals a systemic gap (e.g. a missing pre-release check).
7. Log the full incident timeline to `ops/decision-log.md`.

## Output

Write to `ops/incidents/<date>-<slug>.md`:

```markdown
# Incident — <slug> — <date>

**Type:** crash spike | store rejection
**Severity:** [S1-S4, per bug-triage's severity scale]
**Detected via:**
**Timeline:**
- [time] Detected
- [time] Mitigated (action taken)
- [time] Root cause identified
- [time] Resolved

**Root cause:**
**Mitigation:**
**Follow-up bug/task:** [link]
**Learning entry:** [link to ops/learnings/ entry]
```

## Pass/Fail Criteria

Pass: mitigation happens before full root-cause completion when a safe rollback exists; the actual store rejection text (not an assumption) drives routing; a learnings entry is filed. Fail: root-cause analysis blocking mitigation when a safe rollback was available, or a rejection routed based on a guessed cause.

## Handoff

Hands off the root-cause bug to `bug-triage`, the learnings entry to `improvement-cycle`, and status updates to `producer`/`release-manager`/`community-manager` throughout.
