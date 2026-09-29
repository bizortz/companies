---
name: Privacy & Compliance Setup
assignee: legal-compliance-officer
project: mobile-launch
---

Run the `privacy-compliance` skill for this title: enumerate every SDK/analytics event/third-party integration touching user data, fetch current official Apple ATT/App Privacy and Google Play Data safety guidance at runtime, and produce the privacy policy, ATT prompt spec, Data safety form answers, and age-rating questionnaire answers. This is the first task in the project because the data-collection footprint it documents is a required input to monetization SDKs (task 2) and store submission (task 4).

## Owner
`legal-compliance-officer`

## Inputs
- Actual SDK/analytics/third-party integration list from `analytics-engineer` and `devops-engineer`.
- Target audience/age-rating intent from `creative-director` / `market-analyst`.
- Current official Apple and Google policy sources, fetched at runtime.

## Done Criteria
- `design/compliance/<title>-privacy.md` written per the `privacy-compliance` skill's Output template.
- Every policy claim cites a runtime-fetched source and date.
- Any data practice not already covered by the existing written policy has been routed through the `personal_data_outside_policy` gate in `ops/always-ask.yaml` and resolved.

## Next Task
`monetization-setup`
