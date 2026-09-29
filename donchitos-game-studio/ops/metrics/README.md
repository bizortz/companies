# ops/metrics/

This directory holds the studio's own live-telemetry history, written by
`kpi-review` (owner: `analytics-engineer` prepares the summary;
`publishing-director` rules on it) and read by `market-scan`, the CEO's
portfolio decisions, and the `improvement-cycle` loop.

It starts empty. The self-improvement loop and every KPI-facing skill are
inert until real metric data lands here — see `MODIFICATION_REPORT.md`'s
"Known gaps" section.

## File naming

`ops/metrics/<date>.md`, one file per `kpi-review` run (e.g.
`ops/metrics/2026-10-03.md`).

## Required content per file

Each report pulls every metric using the exact definition, source, and
`min_sample` recorded in `ops/metrics-registry.yaml` — never an ad hoc
variant. At minimum:

```markdown
# KPI Review — <date>

## Metrics

| Metric | Value | Sample size | vs. ops/targets.yaml | Direction (2-review trend) |
|---|---|---|---|---|
| d1_retention | ... | ... | ... | ... |
| ... | | | | |

## Insufficient-sample metrics

<any metric below its registry `min_sample`, reported as "insufficient
sample" rather than as a final number>

## Threshold flags

<any metric that has crossed its target in the wrong `direction` for two
consecutive reviews>
```

A metric reported without meeting `min_sample`, and without the
insufficient-sample label, is a `kpi-review` failure per that skill's own
Pass/Fail criteria — never write one that way.
