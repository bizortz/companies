---
name: Go/No-Go — Global Launch
assignee: ceo
project: mobile-launch
---

Issue the CEO's portfolio ruling on whether this title proceeds to global (full-market, full-scale) launch, using the CEO's standard Portfolio Decision output template and the four required pre-greenlight inputs (latest `market-scan`, latest `kpi-review`, `ops/metrics/` dashboard, finance runway report from `finance-controller`), judged against `ops/targets.yaml`.

## Owner
`ceo`

## Inputs
- `ops/reports/soft-launch/<title>.md` (from `soft-launch`) — exit verdict and evidence.
- `ops/metrics/<date>.md` (from `kpi-review`) — the metric basis for the decision.
- Current `market-scan` output.
- Finance runway report from `finance-controller`.

## Done Criteria
- A Portfolio Decision issued (GO / CONDITIONAL GO / NO-GO), per the CEO's AGENTS.md output template, logged to `ops/decision-log.md`.
- The first public global release of the title (if GO) is routed through the `first_release_or_price_change` gate in `ops/always-ask.yaml` before going live.

## Next Task
`ua-campaign-scale-up` (only on GO or CONDITIONAL GO — a NO-GO routes back to `publishing-director`/`producer` for reshape-or-sunset via `portfolio-review` instead)
