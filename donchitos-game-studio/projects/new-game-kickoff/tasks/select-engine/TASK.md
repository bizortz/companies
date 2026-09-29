---
name: Confirm Engine and Platform Setup
assignee: technical-director
project: new-game-kickoff
---

This studio is Unity-only, targeting iOS and Android (see `COMPANY.md`). This
task confirms Unity project setup fits the new game's requirements rather
than re-evaluating engine choice: Unity version/LTS track, render pipeline
(URP for mobile), target device tier range, and any platform-specific
constraints (thermal/battery/memory budgets — see the Mobile Platform Scope
sections in `agents/unity-specialist/AGENTS.md` and related agents). Decide
directly and log the decision to `ops/decision-log.md`; escalate to the CEO
only if a genuine platform change (e.g. adding a third platform) is being
considered, since that is a scope decision, not a routine setup step.

## Deliverables
- Unity project setup confirmation (version, render pipeline, device tier targets)
- Initial project setup plan
