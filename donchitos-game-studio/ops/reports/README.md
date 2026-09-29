# ops/reports/

This directory holds evidence-based reports produced by the two market-facing
research skills, kept separate from `ops/metrics/` (the studio's own live
telemetry) because these reports are about the external market and about
early, cheap validation signal for concepts that do not have live telemetry
yet.

- **`market/`** — written by `market-scan` (run by `market-analyst`,
  commissioned by `publishing-director` or `creative-director`). One file per
  scan: `ops/reports/market/<date>.md`. Every claim in a market-scan report
  cites its source (a named store listing observed at a point in time, a
  named public report, or the studio's own `ops/metrics/` data) or is
  explicitly marked as an estimate with its basis stated — no fabricated
  chart positions, download estimates, or revenue figures.

- **`validation/`** — written by `concept-validation` (run by
  `market-analyst`, gating the `validate-concept` task ahead of Concept
  Lock). One file per concept validated: `ops/reports/validation/
  <date>-<concept-slug>.md`, containing the fake-door or CPI test plan and
  result, and a PROCEED/PIVOT/KILL recommendation.

Both subdirectories start empty. Neither is a place for fixes or proposals —
those belong in `ops/improvements/`. Entries are never deleted; a superseded
report is superseded by a new dated file, not an edit to the old one.
