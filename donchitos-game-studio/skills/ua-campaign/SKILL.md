---
name: ua-campaign
description: Build a user-acquisition campaign plan, creative matrix, and budget
  pacing schedule, bounded by SPEND_LIMIT_USD.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `ua-manager` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`. Any spend above `spend_limit_usd` in `ops/always-ask.yaml` in a rolling 7-day window always requires the `real_money_spend` human gate — this skill must check that limit before committing any budget.

# UA Campaign

## Purpose

Produce a user-acquisition campaign plan — channel mix, creative matrix, targeting, and a budget pacing schedule — for a soft launch, global launch, or scale-up phase. Every budget figure in the plan must be checked against the current `spend_limit_usd` in `ops/always-ask.yaml`; this skill never authorizes spend past that ceiling on its own authority.

## Trigger / Owner Agent

Owner: `ua-manager`. Runs at `mobile-launch` task 8 (scale-up, after a PASS soft-launch verdict and a global go decision), and re-runs whenever `publishing-director` commissions a new campaign or `kpi-review` shows CPI/ROAS drifting outside `ops/targets.yaml`.

## Inputs

- `ops/targets.yaml` — CPI ceiling and payback-days ceiling the campaign must respect.
- `ops/always-ask.yaml` — `spend_limit_usd`, the hard gate on weekly real-money spend.
- `market-scan` and `soft-launch` results — informs channel and market prioritization.
- `design/aso/<title>-listing-<date>.md` — creative/value-prop consistency with the store listing.

## Procedure

1. Confirm the current `spend_limit_usd` from `ops/always-ask.yaml` before drafting any budget number; treat it as a hard ceiling per rolling 7-day window, not a target.
2. Select channels based on the soft-launch's observed CPI/ROAS by channel (if available) and `market-scan` competitive intelligence, rather than defaulting to the same channel mix every time without evidence.
3. Build a creative matrix: creative concept x format x channel, each tied to a specific hook from the game's actual pillars/value proposition (from `design/aso/` and `creative-director`'s pillars) — no generic stock-style creative briefs.
4. Set a budget pacing schedule across the campaign duration that never projects a rolling-7-day spend above `spend_limit_usd`; if the desired campaign scale requires exceeding it, stop and route the request to the `real_money_spend` human gate with the specific ask and expected ROAS rationale, rather than pacing around the limit to avoid triggering it.
5. Set the CPI ceiling and payback-days ceiling checkpoints directly from `ops/targets.yaml`, and define what happens if a channel breaches them (pause and reallocate, per step 6).
6. Monitor and reallocate: pause underperforming channel/creative combinations against the CPI ceiling, and log every reallocation decision to `ops/decision-log.md`.

## Output

Write to `ops/campaigns/<title>-<date>.md`:

```markdown
# UA Campaign — <title> — <date>

## Channel Mix & Rationale
| Channel | Rationale | Allocation % |
|---|---|---|

## Creative Matrix
| Concept | Format | Channel | Hook source |
|---|---|---|---|

## Budget Pacing
| Week | Planned spend | Rolling 7-day check vs spend_limit_usd |
|---|---|---|

## Performance Gates
- CPI ceiling (ops/targets.yaml):
- Payback-days ceiling (ops/targets.yaml):

## Gate Status
[Any request routed to real_money_spend, and its resolution]
```

## Pass/Fail Criteria

Pass: no planned or actual rolling-7-day spend exceeds `spend_limit_usd` without a logged, resolved human-gate approval; CPI/ROAS checkpoints reference `ops/targets.yaml`, not invented numbers. Fail: any spend projection that silently exceeds the limit, or a CPI ceiling not traceable to `ops/targets.yaml`.

## Handoff

Hands off performance data to `kpi-review` and `analytics-engineer` for attribution, and to `publishing-director` for scale/hold/cut decisions on the channel mix.
