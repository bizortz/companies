---
name: Store Submission — Soft-Launch Build
assignee: release-manager
project: mobile-launch
---

Run the `store-submission` skill for the soft-launch build specifically (not the global-launch build): fetch current official Apple/Google guidelines, build the iOS and Android checklists using the compliance and monetization artifacts from the earlier tasks, and submit to the soft-launch markets only.

## Owner
`release-manager`

## Inputs
- `design/compliance/<title>-privacy.md` (from `privacy-compliance`).
- `design/monetization/catalog.md` (from `monetization-setup`) — store product ID configuration.
- `design/aso/<title>-listing-<date>.md` (from `aso-update`) — store listing content.
- Build artifacts (IPA/AAB) from `devops-engineer`.

## Done Criteria
- `ops/releases/<title>-submission-<date>.md` written with both checklists complete and verified against the actual build.
- Build accepted by both stores for the soft-launch markets (release track set to a limited/soft-launch configuration, not full production).
- Any rejection routed through `incident-response` and resolved before proceeding.

## Next Task
`soft-launch`
