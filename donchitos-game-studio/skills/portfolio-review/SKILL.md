---
name: portfolio-review
description: Continue / scale / sunset ruling per title across the studio's full
  portfolio, against ops/targets.yaml.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `ceo` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md` and per the CEO's own AGENTS.md (portfolio decisions are the CEO's non-delegable authority).

# Portfolio Review

## Purpose

Produce the CEO's standing ruling on every title in the studio's live/in-development portfolio: continue as-is, scale (increase UA/live-ops investment), or sunset (wind down). This is the CEO's recurring exercise of portfolio authority and must be grounded entirely in `ops/targets.yaml` thresholds and current `kpi-review`/`market-scan`/finance data — never a qualitative call made without the numeric backing the CEO's own AGENTS.md requires before any greenlight/kill-adjacent decision.

## Trigger / Owner Agent

Owner: `ceo`. Runs on a standing cadence (default quarterly, per the CEO's Quarterly Strategy Note cycle) and whenever a `soft-launch` KILL/RESHAPE verdict or two consecutive off-target `kpi-review` flags force an out-of-cycle review for a specific title.

## Inputs

- Latest `ops/metrics/<date>.md` (`kpi-review`) for every live title.
- `ops/targets.yaml` — the thresholds each title is judged against.
- `market-scan` output — has the competitive/market context shifted since the title launched?
- Finance runway report from `finance-controller` — can the portfolio afford to keep funding a marginal title?

## Procedure

1. For every title in the portfolio, pull its latest `kpi-review` metrics and compare against `ops/targets.yaml`.
2. Classify each title: **exceeds targets** (scale candidate), **meets targets** (continue as-is), **misses one or more targets** (investigate: is it a fixable design/monetization/UA issue, or fundamental?), or **sustained multi-review miss** (sunset candidate).
3. For any scale or sunset candidate, cross-check against `market-scan` (has the segment changed?) and the finance runway report (does scaling or continuing fit the budget?).
4. Issue a ruling per title: **CONTINUE**, **SCALE** (with what's being scaled — UA budget, live-ops cadence, team allocation), or **SUNSET** (with a wind-down plan: player communication, refund/support handling via `player-support`, team reallocation).
5. Any sunset decision that involves a live game with active players is a significant enough action that the CEO must state the reversibility and rationale explicitly in the decision log, per the CEO's own AGENTS.md decision-record requirement — sunset is not on `ops/always-ask.yaml`'s fixed list, so it is not a human gate, but it is logged with full rationale regardless.
6. Log every ruling to `ops/decision-log.md` and notify the affected title's owning agents (`producer`, `publishing-director`, `live-ops-designer`).

## Output

Write to `ops/reports/portfolio/<date>.md`:

```markdown
# Portfolio Review — <date>

| Title | Latest KPI review | vs ops/targets.yaml | Classification | Ruling | Rationale |
|---|---|---|---|---|---|

## Sunset Wind-Down Plans (if any)
[Per-title plan: player comms, refund/support handling, team reallocation]

## Scale Investments (if any)
[Per-title: what is being scaled and by how much]
```

## Pass/Fail Criteria

Pass: every ruling traces to `ops/targets.yaml` numbers and cited `kpi-review`/`market-scan`/finance data; sunset rulings include a wind-down plan. Fail: a ruling issued without a cited metric comparison, or a sunset with no wind-down plan.

## Handoff

Hands off SCALE rulings to `ua-manager` (ua-campaign) and `live-ops-designer`; SUNSET rulings to `producer` (team reallocation), `player-support` (player communication/refunds), and `finance-controller` (budget release); all rulings feed the next Quarterly Strategy Note.
