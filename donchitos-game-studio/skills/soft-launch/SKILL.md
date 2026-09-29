---
name: soft-launch
description: Plan and adjudicate a soft launch — markets, duration, KPI gates,
  and the exit verdict against ops/targets.yaml.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `publishing-director` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`, escalating global-launch-worthy verdicts to `ceo` per the CEO's portfolio-decision authority.

# Soft Launch

## Purpose

Plan a soft launch in a limited set of markets to validate retention, monetization, and stability against `ops/targets.yaml` thresholds before committing UA budget and the `first_release_or_price_change` gate to a global launch. Produce both the plan (before) and the exit verdict (after) as one continuous artifact.

## Trigger / Owner Agent

Owner: `publishing-director`. Runs as `mobile-launch` task 5, immediately after the soft-launch build passes `store-submission`.

## Inputs

- `ops/targets.yaml` — the KPI gates the soft launch must clear.
- `design/perf-budget.md` — stability/performance floor.
- `market-scan` output — informs market selection (choose markets with a comparable audience profile to the eventual global target, not just the cheapest CPI market).
- `ops/releases/<title>-submission-<date>.md` — confirms the build is live in the chosen markets.

## Procedure

1. Select soft-launch markets based on audience comparability to the global target (language, platform mix, spending behavior similarity) per `market-scan`, not solely cost — state the rationale.
2. Set the soft-launch duration and the specific KPI gates it must clear, pulled directly from `ops/targets.yaml` (D1/D7/D30 retention floors, ARPDAU floor, payback-days ceiling, crash-free rate) — never a number invented ad hoc for this launch.
3. Confirm analytics instrumentation (with `analytics-engineer`) is live and correctly attributing before the clock starts.
4. Monitor via `kpi-review` at the cadence appropriate to the soft-launch duration (e.g. weekly).
5. At the end of the duration, compare final metrics against the gates set in step 2 using the same `kpi-review` output.
6. Issue the exit verdict: **PASS** (proceed to global launch decision), **EXTEND** (metrics are trending toward the gate but need more time/sample, per `min_sample` in `ops/metrics-registry.yaml`), or **KILL/RESHAPE** (metrics clearly miss the gate — return to design or kill the title, per the CEO's portfolio authority for a kill).
7. Log the plan and the verdict to `ops/decision-log.md`.

## Output

Write to `ops/reports/soft-launch/<title>.md` (append the verdict section when the launch concludes):

```markdown
# Soft Launch — <title>

## Plan
- Markets: [list + rationale]
- Duration: [N days/weeks]
- KPI gates (from ops/targets.yaml): [table of metric, floor/ceiling, source]

## Monitoring
[Links to kpi-review reports through the duration]

## Exit Verdict
**Verdict:** PASS | EXTEND | KILL/RESHAPE
**Metrics vs gates:** [table]
**Rationale:**
```

## Pass/Fail Criteria

Pass: gates are set from `ops/targets.yaml` before the launch starts, not adjusted afterward to fit the result; verdict is issued only once `min_sample` (per `ops/metrics-registry.yaml`) is reached. Fail: a gate redefined after seeing the data, or a verdict issued before minimum sample size.

## Handoff

PASS hands off to `mobile-launch` task 7 (go/no-go global launch, owner `ceo`). EXTEND loops back to continued monitoring. KILL/RESHAPE hands off to `ceo` for a portfolio-review ruling and to `game-designer`/`creative-director` if reshape is the chosen path.
