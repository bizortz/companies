---
name: monetization-setup
description: Build the IAP catalog, ad placement spec, and store product ID map
  for a title's real-money monetization surface.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `monetization-designer` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`. Any first-time price setting or price change is subject to the `first_release_or_price_change` gate in `ops/always-ask.yaml`.

# Monetization Setup

## Purpose

Produce the concrete, implementable monetization surface for a title: the IAP catalog (SKUs, contents, price points), the ad placement spec (which ad formats appear where and under what frequency/pacing rules), and the mapping from internal product identifiers to each store's product ID scheme. This is the executable counterpart to `economy-designer`'s in-game currency/economy model — this skill owns the real-money and ad-revenue surface and coordinates with, but never edits, `economy-designer`'s currency balancing.

## Trigger / Owner Agent

Owner: `monetization-designer`. Runs as a `mobile-launch` project task (after `privacy-compliance`, since ad SDKs and IAP both touch data-collection and consent), and is revisited whenever a live-ops event or `kpi-review` finding suggests the monetization mix needs adjustment.

## Inputs

- `economy-designer`'s in-game currency/economy model, for consistency (no duplicated or contradictory currency math).
- `ops/targets.yaml` (ARPDAU floor and other monetization-relevant targets).
- Business model designation (`f2p-hybrid`, per `DECISIONS.md`) — informs the IAP/ad mix.
- `ops/always-ask.yaml` for the price-change gate.

## Procedure

1. Confirm the business model (`f2p-hybrid`) and design an IAP catalog: consumables (currency packs, boosts), non-consumables (remove-ads, cosmetics), and any subscription tier, each mapped to a specific player value proposition — never invent a specific price point from memory; propose a price informed by the segment's `market-scan` comparables and this studio's own `ops/targets.yaml`, and flag it as a first-time price requiring the `first_release_or_price_change` human gate.
2. Design the ad placement spec: which formats (interstitial, rewarded video, banner) appear at which game moments, with explicit frequency-capping and pacing rules that protect the retention floor in `ops/targets.yaml` — ad load should never be set by revenue-maximization alone without a stated retention-risk tradeoff.
3. Map each internal product ID to the corresponding store product ID (App Store Connect, Google Play Console) — do not hardcode store-specific technical requirements (receipt validation specifics, product-ID character limits, etc.) from memory; fetch and cite the current official source at runtime for any such detail.
4. Route the full catalog and price points through the `first_release_or_price_change` gate before anything goes live.
5. Log the setup and any price decisions to `ops/decision-log.md`.

## Output

Write to `design/monetization/catalog.md`:

```markdown
# Monetization Setup — <title>

## IAP Catalog
| SKU | Type | Contents | Price (proposed) | Store product ID (iOS) | Store product ID (Android) |
|---|---|---|---|---|---|

## Ad Placement Spec
| Placement | Format | Trigger moment | Frequency cap | Retention-risk note |
|---|---|---|---|---|

## Human Gate Status
[Which items are pending first_release_or_price_change sign-off]
```

## Pass/Fail Criteria

Pass: catalog is internally consistent with `economy-designer`'s model, every price is routed through the human gate before going live, ad pacing has a stated retention rationale. Fail: any price point live without gate sign-off, or ad frequency set without a retention-tradeoff note.

## Handoff

Hands off to `release-manager` (store product ID map needed for `store-submission`) and to `analytics-engineer` (event instrumentation for each SKU/placement, subject to `personal_data_outside_policy` if new SDK data collection is introduced).
