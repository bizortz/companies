---
name: device-perf-budget
description: Set per-device-tier FPS, memory, build size, and load time budgets
  before production. Anchors every subsequent performance decision.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; `performance-analyst` decides and logs to `ops/decision-log.md` per `docs/automation-modes.md`, escalating only per `ops/always-ask.yaml`.

# Device Performance Budget

## Purpose

Establish explicit, written performance budgets per device tier before Pre-Production ends, so every engineering and art decision downstream (poly counts, texture resolution, shader complexity, addressables bundle sizes) has a concrete target instead of being discovered as a crisis during optimization passes late in production. This skill never hardcodes a specific numeric budget from memory — every number is derived from this studio's own device-tier definitions and the target markets' actual device mix, fetched or profiled at decision time, or explicitly marked provisional pending real device testing.

## Trigger / Owner Agent

Owner: `performance-analyst`. Runs once as a task inside `new-game-kickoff`'s Pre-Production phase, and is revisited whenever the target device tier range changes or a milestone review shows the game trending over budget.

## Inputs

- The game concept and target markets (from `creative-director` / `publishing-director` / `market-scan` output) — determines which device tiers matter.
- `agents/unity-specialist/AGENTS.md`, `agents/performance-analyst/AGENTS.md`, and other agents' Mobile Platform Scope sections for the studio's existing device-tier and thermal/memory framing.
- Any available real-device test data from prior titles, if this is not the studio's first release.

## Procedure

1. Define the device tier bands relevant to the target markets (e.g. low/mid/high, described qualitatively — RAM class, GPU class, release-year band — rather than a hardcoded model list that goes stale).
2. For each tier, set a target sustained frame rate, appropriate to genre (a twitch action game needs a higher floor than a puzzle game) — state the reasoning, not just a number.
3. Set a memory budget per tier (peak RSS ceiling), informed by the platform's actual OOM-kill behavior for that tier, fetched or tested at decision time rather than assumed.
4. Set a build/install size budget per platform (iOS IPA, Android AAB), informed by the current store's actual download-size warnings/thresholds fetched at runtime — never a hardcoded figure that may be outdated.
5. Set a cold-start load-time target per tier.
6. Write the budget file, and flag any budget that is provisional pending real device profiling.
7. Log the decision to `ops/decision-log.md` and notify `technical-director`, `art-director`, and `producer`.

## Output

Write to `design/perf-budget.md`:

```markdown
# Device Performance Budget

| Tier | Target FPS | Memory ceiling | Notes |
|---|---|---|---|
| Low | | | |
| Mid | | | |
| High | | | |

## Build Size
- iOS IPA target: 
- Android AAB target: 

## Load Time
| Tier | Cold start target |
|---|---|

## Basis / Provisional Flags
[What each number is derived from; which are provisional pending device testing]
```

## Pass/Fail Criteria

Pass: every tier has a stated FPS, memory, and load-time target with a stated basis; build-size targets reference the current store limits fetched at decision time. Fail: any number presented as final without a stated basis, or omission of a tier the target markets actually use.

## Handoff

Hands off to `engine-programmer`, `technical-artist`, and `unity-specialist` as the binding target for all subsequent optimization work, and to `perf-profile`/`soak-test` skills as the pass/fail bar during QA.
