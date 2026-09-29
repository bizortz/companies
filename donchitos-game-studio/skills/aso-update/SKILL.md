---
name: aso-update
description: App store optimization pass — listing copy, keywords, and asset spec
  per store, refreshed on a cadence or after a KPI signal.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `aso-specialist` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`, escalating only per `ops/always-ask.yaml`.

# ASO Update

## Purpose

Produce or refresh a title's store listing optimization package — copy, keyword targeting, and creative asset specification — for both the App Store and Google Play. This skill never hardcodes a store's current character limits, keyword-field mechanics, or algorithm behavior from memory; those change, so the procedure requires fetching and citing the current official App Store Connect / Google Play Console documentation for any structural constraint before finalizing copy.

## Trigger / Owner Agent

Owner: `aso-specialist`. Runs as a `mobile-launch` task (step 3, after monetization is defined so IAP/value-prop copy is accurate), on a standing refresh cadence (default quarterly, adjustable by `publishing-director`), and ad hoc whenever `kpi-review` shows a conversion-rate or impression-to-install drop that points at listing fatigue.

## Inputs

- `market-scan` output for competitor listing/keyword intelligence.
- `design/monetization/catalog.md` for accurate value-proposition copy.
- Current official App Store Connect metadata field specs and Google Play Console listing requirements, fetched at runtime.
- Latest `ops/metrics/<date>.md` conversion-rate data, if this is a refresh rather than an initial listing.

## Procedure

1. Fetch current official field-length/format constraints for both stores (title, subtitle/short description, description, keyword field where applicable) rather than assuming remembered limits.
2. Draft or revise listing copy: title, subtitle, full description, and (App Store) keyword field, each grounded in the title's actual pillars and monetization value proposition, not generic genre boilerplate.
3. Select target keywords informed by `market-scan` competitor data and the game's actual feature set — do not invent search-volume numbers; if volume data isn't available to this skill, state that keyword priority is qualitative (relevance + competitor usage) rather than fabricating a number.
4. Specify the icon, screenshot, and preview-video asset requirements per store (count, dimensions per the fetched current spec, and the narrative/order each asset should tell), and hand the spec to `art-director`/`ux-designer` for production.
5. If this is a refresh, compare against the prior listing's `ops/metrics/` conversion data to state what specifically is being changed and why.
6. Log the update to `ops/decision-log.md`.

## Output

Write to `design/aso/<title>-listing-<date>.md`:

```markdown
# ASO Update — <title> — <date>

## Constraints Fetched
[Store, field, limit, source, date]

## App Store Listing
- Title:
- Subtitle:
- Keyword field:
- Description:

## Google Play Listing
- Title:
- Short description:
- Full description:

## Target Keywords
| Keyword | Relevance rationale | Competitor usage (from market-scan) |
|---|---|---|

## Asset Spec
| Asset | Store | Spec (from fetched constraints) | Narrative role |
|---|---|---|---|

## Prior Performance (if refresh)
[Conversion delta being targeted]
```

## Pass/Fail Criteria

Pass: field constraints cite a runtime-fetched source; copy is specific to this title, not generic; asset spec matches current store requirements. Fail: any hardcoded character limit presented without a citation, or copy reused verbatim from another title without adaptation.

## Handoff

Hands off asset spec to `art-director`/`ux-designer` for production, and the finished package to `release-manager` for inclusion in `store-submission`.
