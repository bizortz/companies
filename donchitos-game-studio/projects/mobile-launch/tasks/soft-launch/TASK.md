---
name: Soft Launch
assignee: publishing-director
project: mobile-launch
---

Run the `soft-launch` skill: select markets, set the duration and KPI gates from `ops/targets.yaml`, monitor through the duration via `kpi-review`, and issue the exit verdict once `min_sample` (per `ops/metrics-registry.yaml`) is reached.

## Owner
`publishing-director`

## Inputs
- `ops/releases/<title>-submission-<date>.md` (from `store-submission-soft-launch`) — confirms the build is live in the chosen markets.
- `ops/targets.yaml` — the KPI gates.
- `market-scan` output — market selection rationale.

## Done Criteria
- `ops/reports/soft-launch/<title>.md` written with the plan and, once the duration elapses, an exit verdict (PASS / EXTEND / KILL-RESHAPE).
- Verdict issued only once `min_sample` is met for the relevant metrics.

## Next Task
`kpi-review` (the KPI review that determines the verdict is the same review consumed by the next task's go/no-go decision)
