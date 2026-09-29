---
name: UA Campaign — Scale-Up
assignee: ua-manager
project: mobile-launch
---

Run the `ua-campaign` skill to plan and pace the global-launch UA scale-up: channel mix, creative matrix, and a budget pacing schedule that never projects a rolling-7-day spend above `spend_limit_usd` in `ops/always-ask.yaml` without an explicit, resolved human-gate approval.

## Owner
`ua-manager`

## Inputs
- The CEO's GO/CONDITIONAL GO ruling (from `go-no-go-global-launch`).
- `ops/targets.yaml` (CPI ceiling, payback-days ceiling) and `ops/always-ask.yaml` (`spend_limit_usd`).
- Soft-launch channel/creative performance data, if available.
- `design/aso/<title>-listing-<date>.md` for creative/value-prop consistency.

## Done Criteria
- `ops/campaigns/<title>-<date>.md` written per the `ua-campaign` skill's Output template.
- No planned rolling-7-day spend exceeds `spend_limit_usd` without a logged, resolved `real_money_spend` gate approval.

## Next Task
`live-ops-cadence`
