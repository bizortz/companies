---
name: privacy-compliance
description: Draft privacy policy, ATT prompt spec, Data safety form answers, and
  age-rating questionnaire answers. Fetches current policy sources at runtime.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `legal-compliance-officer` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`. Accepting any legal terms and any personal-data handling outside the written policy are always subject to the `legal_terms_or_contracts` and `personal_data_outside_policy` gates in `ops/always-ask.yaml`.

# Privacy Compliance

## Purpose

Produce the studio's privacy and compliance artifacts for a title before it can be submitted to any store: a plain-language privacy policy, an App Tracking Transparency (ATT) prompt spec (iOS), Google Play Data safety form answers, and age-rating questionnaire answers (e.g. IARC). This skill must never hardcode a specific COPPA, GDPR, ATT, or Play Data Safety numeric threshold, required-disclosure list, or policy clause from memory — every such fact is fetched from the current official source (Apple/Google developer documentation, the relevant regulator's published text) at the time this skill runs, cited by URL and fetch date, because these policies change and a stale hardcoded fact is worse than admitting it must be looked up.

## Trigger / Owner Agent

Owner: `legal-compliance-officer`. Runs as the first task in the `mobile-launch` project (before monetization or ASO, since the SDK/data-collection footprint those depend on must be known and disclosed first), and re-runs whenever a new SDK, analytics event, or ad network is added.

## Inputs

- The actual list of SDKs, analytics events, and third-party services the title uses (from `analytics-engineer`, `monetization-designer`, `devops-engineer`).
- The target audience / age rating intent from `creative-director` / `market-analyst`.
- Current official policy sources for App Store (ATT, App Privacy "nutrition label"), Google Play (Data safety section), COPPA, and GDPR — fetched at runtime, not assumed.

## Procedure

1. Enumerate every SDK, analytics event, and third-party integration that touches user data, with what data each one collects and why.
2. Fetch the current official Apple ATT and App Privacy documentation and the current Google Play Data safety documentation; do not rely on remembered specifics — cite the fetched source and date in the output.
3. Determine whether the title's audience or content triggers COPPA (US) or equivalent child-directed-app obligations elsewhere, and GDPR obligations for EU users, again fetching current official guidance rather than asserting thresholds from memory.
4. Draft the privacy policy in plain language covering: what is collected, why, who it's shared with, retention, and user rights/controls — matching what was actually enumerated in step 1, not a generic template.
5. Draft the ATT prompt spec: the pre-permission context screen (if used) and the system prompt copy, consistent with current Apple guidance fetched in step 2.
6. Complete the Data safety form answers and age-rating questionnaire answers to match the actual data practices from step 1.
7. Any data practice not already covered by the existing written policy triggers the `personal_data_outside_policy` human gate before it ships. Accepting the platform's own terms/agreements triggers `legal_terms_or_contracts`.
8. Log the full pass to `ops/decision-log.md`.

## Output

Write to `design/compliance/<title>-privacy.md`:

```markdown
# Privacy & Compliance — <title>

## Data Inventory
| SDK/Feature | Data collected | Purpose | Shared with |
|---|---|---|---|

## Privacy Policy
[Full plain-language text]

## ATT Prompt Spec (iOS)
[Pre-permission context + system prompt copy]

## Play Data Safety Form Answers
[Section-by-section answers]

## Age Rating Questionnaire Answers
[Question-by-question answers]

## Sources Cited
[Every official source fetched, with URL and fetch date]

## Gate Status
[Any item routed to personal_data_outside_policy or legal_terms_or_contracts, and its resolution]
```

## Pass/Fail Criteria

Pass: every policy-specific claim cites a source fetched at runtime with a date; the data inventory matches what's actually implemented; every new-data-practice item is routed through the correct human gate before ship. Fail: any hardcoded policy percentage/threshold/clause presented as current fact, or a data practice shipped without gate sign-off.

## Handoff

Hands off to `release-manager` for `store-submission` (privacy artifacts are a required submission input) and to `monetization-designer`/`analytics-engineer` if the data inventory reveals an undisclosed practice that must be fixed before proceeding.
