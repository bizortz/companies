---
name: market-scan
description: Genre, competitor, and trend scan for the mobile games market. Feeds
  concept decisions, greenlights, and quarterly strategy.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously. Any decision it would previously have surfaced as a question is made by the owning agent (`market-analyst`) and logged to `ops/decision-log.md`, per `docs/automation-modes.md`. The only exceptions are the fixed human gates in `ops/always-ask.yaml`.

# Market Scan

## Purpose

Produce a current, evidence-based read of the mobile games market segment relevant to a specific decision: a new concept under consideration, a competitive threat to a live title, or the CEO's quarterly strategy review. This skill never fabricates chart positions, download estimates, or revenue figures — every claim in the output must cite where it came from (a named store listing observed at a point in time, a named public report, or the studio's own `ops/metrics/` data), or be explicitly marked as an estimate with its basis stated.

## Trigger / Owner Agent

Owner: `market-analyst`. Triggered by: `publishing-director` before a concept decision; `ceo` before any greenlight (per the CEO's "must consume market-scan before any greenlight" rule); on a standing cadence (default quarterly, adjustable by `publishing-director`); or ad hoc when a competitor makes a significant move (major update, price change, sudden chart movement).

## Inputs

- `ops/targets.yaml` — current greenlight/kill thresholds, for framing whether a genre/segment looks viable against this studio's own bar.
- `ops/metrics/` — the studio's own live-title KPI history, if any exists, for comparison against market movement.
- The requesting agent's specific question (concept genre/mechanic, a named competitor, or "general quarterly scan").
- Public store listings and public market-data sources, fetched at runtime — never cached numbers from training data.

## Procedure

1. Parse the request: identify scope (genre scan, competitor scan, or general quarterly scan) and the specific decision it will feed.
2. For a genre/concept scan: identify 5-10 comparable titles currently live in the target genre; note their store category rank movement, apparent update cadence, and monetization model (IAP, ads, subscription, hybrid) from their live store listings, fetched at the time of the scan.
3. For a competitor scan: pull the named competitor's current store listing (screenshots, description, listed IAPs, rating trend, review themes) and recent update history.
4. Cross-reference findings against `ops/targets.yaml` thresholds and the studio's own `ops/metrics/` history to state, explicitly, whether the segment looks more or less attractive than the studio's current portfolio.
5. Separate observed facts (with source and date) from analyst judgment (labeled as such).
6. Write the report per the Output template below and log the write to `ops/decision-log.md`.

## Output

Write to `ops/reports/market/<date>.md`:

```markdown
# Market Scan — <date>

**Requested by:** <agent>
**Scope:** <genre scan | competitor scan | quarterly scan>

## Findings
| Title | Genre | Rank/trend | Monetization | Source | Observed date |
|---|---|---|---|---|---|

## Segment Read
[Growing / saturating / declining, with the evidence above cited]

## Comparison to Studio Targets
[How this segment compares to ops/targets.yaml thresholds and current portfolio KPIs]

## Recommendation
[What the requesting agent should do with this — pursue, pass, monitor]

## Sources
[Every source cited above, with date fetched]
```

## Pass/Fail Criteria

Pass: every factual claim has a cited source and date; judgment is clearly separated from fact; the report directly answers the requesting agent's question. Fail: any unsourced numeric claim, or a report that doesn't connect to the decision that triggered it.

## Handoff

Hands off to whichever agent requested it — `market-analyst` notifies `publishing-director` or `ceo` directly with the file path and a one-line summary. If the scan surfaces a threat to a live title, also notify `live-ops-designer` and `ua-manager`.
