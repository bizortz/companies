---
name: kpi-review
description: Standing KPI report — D1/D7/D30, ARPDAU, CPI, ROAS, LTV, crash-free
  rate — with delta vs ops/targets.yaml. Feeds every downstream gate.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `analytics-engineer` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`, escalating only per `ops/always-ask.yaml`.

# KPI Review

## Purpose

Produce the studio's standing source of truth on live-title performance: retention, monetization, acquisition efficiency, and stability, measured against `ops/targets.yaml`. This is a required input to the CEO's portfolio decisions, `soft-launch` exit verdicts, and `ua-campaign` reallocation — no downstream gate should re-derive these numbers independently.

## Trigger / Owner Agent

Owner: `analytics-engineer`. Runs on a standing cadence (default weekly for live titles, per the cadence set during `soft-launch` for titles still in that phase) and on demand whenever `ceo`, `publishing-director`, or `ua-manager` needs a current read before a decision.

## Inputs

- Raw analytics/telemetry data sources (whatever the studio's actual analytics pipeline is — SDK event streams, store consoles, ad-network dashboards).
- `ops/targets.yaml` — the thresholds every metric is compared against.
- `ops/metrics-registry.yaml` — the canonical definition, source, and `min_sample` for every metric this report includes; this skill must use those definitions exactly, not an ad hoc variant.
- Prior `ops/metrics/<date>.md` reports, for trend computation.

## Procedure

1. Pull each required metric — D1/D7/D30 retention, ARPDAU, CPI, ROAS, LTV, crash-free session rate — using the exact definition and source specified in `ops/metrics-registry.yaml`. If a metric's `min_sample` has not been reached, report it as "insufficient sample" rather than presenting a noisy number as final.
2. Compute the delta versus the corresponding threshold in `ops/targets.yaml` for every metric that has one, and versus the prior report for trend direction.
3. Flag any metric that has crossed a threshold in the wrong `direction` (per `ops/metrics-registry.yaml`'s `direction: up|down` field) for two consecutive reviews — this is the signal that should trigger a design/UA/monetization response, not a single noisy data point.
4. Write the report.
5. Append a structured finding to `ops/learnings/<date>-kpi-review.md` per the evidence-capture procedure (see `docs/` or `ops/metrics-registry.yaml` header for the required fields: finding, affected agent/skill, evidence, metric affected, severity) whenever this review surfaces a threshold miss, a trend reversal, or a sample-size gap worth flagging to the improvement loop.
6. Log the report and any threshold-breach escalation to `ops/decision-log.md`.

## Output

Write to `ops/metrics/<date>.md`:

```markdown
# KPI Review — <date>

| Metric | Value | Sample size | min_sample met? | Target (ops/targets.yaml) | Delta | Trend |
|---|---|---|---|---|---|---|
| D1 retention | | | | | | |
| D7 retention | | | | | | |
| D30 retention | | | | | | |
| ARPDAU | | | | | | |
| CPI | | | | | | |
| ROAS | | | | | | |
| LTV | | | | | | |
| Crash-free sessions | | | | | | |

## Flags
[Any metric off-target for 2+ consecutive reviews]

## Learnings Logged
[Link to any ops/learnings/<date>-kpi-review.md entries created this run]
```

## Pass/Fail Criteria

Pass: every metric uses the `ops/metrics-registry.yaml` definition verbatim; insufficient-sample metrics are labeled, not presented as final; consecutive-review flags are computed from actual prior reports, not assumed. Fail: a metric reported without meeting `min_sample` and without the insufficient-sample label, or a definition that diverges from the registry.

## Handoff

Hands off to `ceo` (portfolio decisions), `soft-launch` (exit verdicts), `ua-campaign` (reallocation), and `improvement-cycle` (via the `ops/learnings/` entries this review writes).
