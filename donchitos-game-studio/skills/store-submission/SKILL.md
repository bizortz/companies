---
name: store-submission
description: iOS and Android submission checklist, fetching current review guidelines
  at runtime rather than relying on hardcoded rules.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `release-manager` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`. Any first public release is always subject to the `first_release_or_price_change` gate in `ops/always-ask.yaml`.

# Store Submission

## Purpose

Produce a submission-ready checklist and package for both the Apple App Store and Google Play Store. Because store review guidelines, required metadata fields, and technical requirements change frequently and a stale hardcoded checklist causes real rejections, this skill's procedure requires fetching the current official Apple App Store Review Guidelines and Google Play Developer Policy/Console requirements at the time of each submission, rather than reusing a remembered checklist.

## Trigger / Owner Agent

Owner: `release-manager`. Runs before every store submission — soft-launch build, global launch, and any subsequent binary update that touches store metadata or permissions. Part of `mobile-launch`'s task sequence (step 4, after ASO and monetization/compliance artifacts exist).

## Inputs

- `design/compliance/<title>-privacy.md` (from `privacy-compliance`) — required for App Privacy / Data safety fields.
- `design/monetization/catalog.md` (from `monetization-setup`) — required for IAP product configuration.
- ASO listing assets (from `aso-update`).
- Current official Apple App Store Review Guidelines and Google Play Console requirements, fetched at runtime.
- Build artifacts (IPA / AAB) and their version/build numbers from `devops-engineer`.

## Procedure

1. Fetch the current official Apple App Store Review Guidelines and Google Play Developer Program Policies; do not reuse a remembered list — guidelines and required fields change between submissions.
2. Build the iOS checklist from the fetched guidelines: app metadata, screenshots/previews per required device sizes, App Privacy answers (from `privacy-compliance`), age rating, IAP configuration in App Store Connect, and any category-specific requirement the fetched guidelines flag for this title's content.
3. Build the Android checklist from the fetched policy: store listing content, Data safety section (from `privacy-compliance`), content rating (IARC), target API level and other technical requirements current at submission time, and Play Console release track configuration (internal/closed/open/production as appropriate to this submission's purpose).
4. Verify every checklist item against the actual build and artifacts before marking it complete — do not mark an item done because it was done for a previous title; each submission is re-verified against current requirements.
5. Route the submission through the `first_release_or_price_change` gate if this is the title's first public release on either store.
6. Submit (or stage for the human-gated go-ahead) and log the submission and outcome to `ops/decision-log.md`.

## Output

Write to `ops/releases/<title>-submission-<date>.md`:

```markdown
# Store Submission — <title> — <date>

## Guidelines Fetched
[Apple guideline source + date, Google policy source + date]

## iOS Checklist
| Item | Status | Note |
|---|---|---|

## Android Checklist
| Item | Status | Note |
|---|---|---|

## Gate Status
[first_release_or_price_change status if applicable]

## Submission Result
[Accepted / pending review / rejected, with reviewer feedback if rejected]
```

## Pass/Fail Criteria

Pass: both checklists are built from guidelines fetched at submission time (dated citation present), every item is verified against the actual build, and the first-release gate is honored. Fail: any checklist item marked complete without verification against the current build, or a first release submitted without the human gate.

## Handoff

On rejection, hands off to `incident-response` (store rejection runbook) and back to whichever agent owns the flagged issue (e.g. `legal-compliance-officer` for a privacy flag, `monetization-designer` for an IAP flag). On acceptance, hands off to `soft-launch` or the live-launch task, as applicable.
