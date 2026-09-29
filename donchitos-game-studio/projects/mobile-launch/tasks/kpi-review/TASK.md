---
name: Post-Soft-Launch KPI Review
assignee: analytics-engineer
project: mobile-launch
---

Run the `kpi-review` skill against the concluded (or concluding) soft launch: pull D1/D7/D30 retention, ARPDAU, CPI, ROAS, LTV, and crash-free session rate using the exact definitions in `ops/metrics-registry.yaml`, and compute the delta versus `ops/targets.yaml`. This review is the evidentiary basis for both the `soft-launch` exit verdict and the CEO's global go/no-go ruling in the next task.

## Owner
`analytics-engineer`

## Inputs
- Raw analytics/telemetry from the soft-launch markets.
- `ops/targets.yaml` and `ops/metrics-registry.yaml`.
- Prior `ops/metrics/` reports for trend computation.

## Done Criteria
- `ops/metrics/<date>.md` written with every required metric, its sample size, and its delta vs `ops/targets.yaml`.
- Any metric below `min_sample` is labeled "insufficient sample," not presented as final.
- Any threshold-breach or trend-reversal finding logged to `ops/learnings/<date>-kpi-review.md`.

## Next Task
`go-no-go-global-launch`
