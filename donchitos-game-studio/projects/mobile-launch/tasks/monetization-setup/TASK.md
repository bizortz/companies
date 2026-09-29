---
name: Monetization Setup
assignee: monetization-designer
project: mobile-launch
---

Run the `monetization-setup` skill: build the IAP catalog, ad placement spec, and store product ID map for this title, consistent with `economy-designer`'s in-game currency model and the data-collection footprint already documented in the `privacy-compliance` task.

## Owner
`monetization-designer`

## Inputs
- `design/compliance/<title>-privacy.md` (from the `privacy-compliance` task) — confirms what SDK data collection is already disclosed before adding more via ad/IAP SDKs.
- `economy-designer`'s in-game currency/economy model.
- `ops/targets.yaml` (ARPDAU floor) and the `f2p-hybrid` business model designation.

## Done Criteria
- `design/monetization/catalog.md` written per the `monetization-setup` skill's Output template.
- Every proposed price point is routed through the `first_release_or_price_change` gate in `ops/always-ask.yaml`.
- Ad placement pacing has a stated retention-risk rationale tied to `ops/targets.yaml`.

## Next Task
`aso-update`
