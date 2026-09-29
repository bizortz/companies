---
name: ASO Listing Package
assignee: aso-specialist
project: mobile-launch
---

Run the `aso-update` skill: produce the App Store and Google Play listing copy, target keywords, and asset specification, grounded in the title's actual pillars and the monetization value proposition set in the previous task.

## Owner
`aso-specialist`

## Inputs
- `design/monetization/catalog.md` (from `monetization-setup`) — value-proposition copy accuracy.
- `market-scan` output for competitor listing/keyword intelligence.
- Current official App Store Connect / Google Play Console field constraints, fetched at runtime.

## Done Criteria
- `design/aso/<title>-listing-<date>.md` written per the `aso-update` skill's Output template.
- Field-length/format constraints cite a runtime-fetched source.
- Asset spec handed to `art-director`/`ux-designer` for production.

## Next Task
`store-submission-soft-launch`
