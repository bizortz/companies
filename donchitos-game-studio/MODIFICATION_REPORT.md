# Modification Report — Donchitos Game Studio → Autonomous Mobile Studio

This report summarizes the full four-phase conversion of `donchitos-game-studio`
from a Claude-Code-Game-Studios-derived, human-in-the-loop, multi-engine
template into an autonomous, self-improving, Unity-only mobile game studio
package (`agentcompanies/v1`). Full narrative detail for every phase lives in
`PROGRESS.md`; every judgment call is recorded in `DECISIONS.md`. This file
is the single entry point for reviewing the whole change set.

## Pinned Upstream Commits

- **UPSTREAM_STUDIO** — `https://github.com/Donchitos/Claude-Code-Game-Studios`
  pinned at `7ed2c3e9c46c880c9780fbce49266e7edfa15141` (HEAD at clone time,
  2026-09-29). Source for the 53 originally-inlined skills and the merged
  agent-body content.
- **UPSTREAM_AGENCY** — `https://github.com/msitarzewski/agency-agents`
  pinned at `68f01534ef30805ed3764f2d302ad03fe443707a` (HEAD at clone time,
  2026-09-29). Source for the 8 Publishing & Growth pillar agents added in
  Phase 2.

## Agents — Added / Removed / Moved

### Removed (Phase 1, Work Item 3) — 9 agents

| Slug | Reason |
|---|---|
| `unreal-specialist`, `ue-blueprint-specialist`, `ue-gas-specialist`, `ue-replication-specialist`, `ue-umg-specialist` | ENGINE=unity — Unreal team pruned |
| `godot-specialist`, `godot-gdscript-specialist`, `godot-shader-specialist`, `godot-gdextension-specialist` | ENGINE=unity — Godot team pruned |

### Added (Phase 2, Work Item 5) — 8 agents

| Slug | Reports To | Upstream Source |
|---|---|---|
| `publishing-director` | `ceo` | `product/product-manager.md` + `marketing/marketing-growth-hacker.md` (merged) |
| `ua-manager` | `publishing-director` | `paid-media/paid-media-paid-social-strategist.md` + `paid-media/paid-media-tracking-specialist.md` |
| `aso-specialist` | `publishing-director` | `marketing/marketing-app-store-optimizer.md` |
| `monetization-designer` | `publishing-director` | structural template from `agents/economy-designer` (no upstream file, per issue) |
| `market-analyst` | `publishing-director` | `product/product-trend-researcher.md` |
| `legal-compliance-officer` | `ceo` | `support/support-legal-compliance-checker.md` |
| `finance-controller` | `ceo` | `support/support-finance-tracker.md` |
| `player-support` | `community-manager` | `support/support-support-responder.md` |

Plus `org-improvement-lead` (Phase 3, Work Item 7), reports to `ceo`, original
content (no upstream source — owns the outcome-based self-improvement loop).

### Moved

| Slug | From | To | Phase |
|---|---|---|---|
| `devops-engineer` | `producer` | `technical-director` | 1 (7-report-cap fix) |
| `security-engineer` | `producer` | `technical-director` | 1 (7-report-cap fix) |
| `analytics-engineer` | `producer` | `publishing-director` | 2 |
| `community-manager` | `producer` | `publishing-director` | 2 |
| `live-ops-designer` | `producer` | `publishing-director` | 2 |

**Net result:** 49 → 40 (Phase 1 pruning) → 48 (Phase 2 additions) → 49
(Phase 3, `org-improvement-lead`) = **49 agents**, final.

## Skills — Added / Inlined

- **53 skills inlined and adapted** from `UPSTREAM_STUDIO` in Phase 1 (37
  previously-stub files fully adapted + 16 additional upstream skills
  imported), all Claude-Code-specific syntax stripped, all with `##
  Procedure`/`## Output` sections and `usage: adapted` provenance.
- **12 original mobile skills** authored in Phase 3 (Work Item 6):
  `market-scan`, `concept-validation`, `device-perf-budget`,
  `monetization-setup`, `privacy-compliance`, `store-submission`,
  `aso-update`, `soft-launch`, `ua-campaign`, `kpi-review`,
  `portfolio-review`, `incident-response`.
- **1 original skill** authored in Phase 3 (Work Item 7): `improvement-cycle`.

**Total: 66 skills**, final. Zero skills declare a `model:` frontmatter key
(confirmed, not just stripped — see Decision #29).

## Model Tiers (Work Item 10) — All 49 Agents

Single source of truth: `ops/model-tiers.yaml`. Full contract text:
`docs/model-tiers.md`.

| Tier | Model | Effort | Count |
|---|---|---|---|
| 1 (decides only) | `claude-opus-5-5` | high | 6 |
| 2 (owns execution) | `claude-sonnet-5` | low | 41 |
| 3 (templated, high-volume) | `claude-haiku-4-5-20251001` | auto | 2 |

| Agent (slug) | Title | Tier | Model | Effort |
|---|---|---|---|---|
| `accessibility-specialist` | Accessibility Specialist | 2 | `claude-sonnet-5` | low |
| `ai-programmer` | AI Programmer | 2 | `claude-sonnet-5` | low |
| `analytics-engineer` | Analytics Engineer | 2 | `claude-sonnet-5` | low |
| `art-director` | Art Director | 2 | `claude-sonnet-5` | low |
| `aso-specialist` | App Store Optimization Specialist | 2 | `claude-sonnet-5` | low |
| `audio-director` | Audio Director | 2 | `claude-sonnet-5` | low |
| `ceo` | Studio Head & CEO | 1 | `claude-opus-5-5` | high |
| `community-manager` | Community Manager | 2 | `claude-sonnet-5` | low |
| `creative-director` | Creative Director | 1 | `claude-opus-5-5` | high |
| `devops-engineer` | DevOps Engineer | 2 | `claude-sonnet-5` | low |
| `economy-designer` | Economy Designer | 2 | `claude-sonnet-5` | low |
| `engine-programmer` | Engine Programmer | 2 | `claude-sonnet-5` | low |
| `finance-controller` | Finance Controller | 2 | `claude-sonnet-5` | low |
| `game-designer` | Lead Game Designer | 2 | `claude-sonnet-5` | low |
| `gameplay-programmer` | Gameplay Programmer | 2 | `claude-sonnet-5` | low |
| `lead-programmer` | Lead Programmer | 2 | `claude-sonnet-5` | low |
| `legal-compliance-officer` | Legal & Compliance Officer | 2 | `claude-sonnet-5` | low |
| `level-designer` | Level Designer | 2 | `claude-sonnet-5` | low |
| `live-ops-designer` | Live Operations Designer | 2 | `claude-sonnet-5` | low |
| `localization-lead` | Localization Lead | 2 | `claude-sonnet-5` | low |
| `market-analyst` | Market Analyst | 2 | `claude-sonnet-5` | low |
| `monetization-designer` | Monetization Designer | 2 | `claude-sonnet-5` | low |
| `narrative-director` | Narrative Director | 2 | `claude-sonnet-5` | low |
| `network-programmer` | Network Programmer | 2 | `claude-sonnet-5` | low |
| `org-improvement-lead` | Organizational Improvement Lead | 1 | `claude-opus-5-5` | high |
| `performance-analyst` | Performance Analyst | 2 | `claude-sonnet-5` | low |
| `player-support` | Player Support Specialist | 3 | `claude-haiku-4-5-20251001` | auto |
| `producer` | Producer | 1 | `claude-opus-5-5` | high |
| `prototyper` | Prototyper | 2 | `claude-sonnet-5` | low |
| `publishing-director` | Publishing Director | 1 | `claude-opus-5-5` | high |
| `qa-lead` | QA Lead | 2 | `claude-sonnet-5` | low |
| `qa-tester` | QA Tester | 3 | `claude-haiku-4-5-20251001` | auto |
| `release-manager` | Release Manager | 2 | `claude-sonnet-5` | low |
| `security-engineer` | Security Engineer | 2 | `claude-sonnet-5` | low |
| `sound-designer` | Sound Designer | 2 | `claude-sonnet-5` | low |
| `systems-designer` | Systems Designer | 2 | `claude-sonnet-5` | low |
| `technical-artist` | Technical Artist | 2 | `claude-sonnet-5` | low |
| `technical-director` | Technical Director | 1 | `claude-opus-5-5` | high |
| `tools-programmer` | Tools Programmer | 2 | `claude-sonnet-5` | low |
| `ua-manager` | User Acquisition Manager | 2 | `claude-sonnet-5` | low |
| `ui-programmer` | UI Programmer | 2 | `claude-sonnet-5` | low |
| `unity-addressables-specialist` | Unity Addressables Specialist | 2 | `claude-sonnet-5` | low |
| `unity-dots-specialist` | DOTS/ECS Specialist | 2 | `claude-sonnet-5` | low |
| `unity-shader-specialist` | Unity Shader/VFX Specialist | 2 | `claude-sonnet-5` | low |
| `unity-specialist` | Unity Engine Lead | 2 | `claude-sonnet-5` | low |
| `unity-ui-specialist` | Unity UI Specialist | 2 | `claude-sonnet-5` | low |
| `ux-designer` | UX Designer | 2 | `claude-sonnet-5` | low |
| `world-builder` | World Builder | 2 | `claude-sonnet-5` | low |
| `writer` | Writer | 2 | `claude-sonnet-5` | low |

## Decisions Log Summary (`DECISIONS.md`, 37 entries)

| # | Decision |
|---|---|
| 1 | Skill body adaptation strategy — mechanical CC-syntax stripping, additive `## Procedure`/`## Output` headers |
| 2 | Agent-body merge strategy — additive "Additional Procedures (Merged from Upstream)" section, never overwrite existing body |
| 3 | Always-ask list wording — issue's five bullets verbatim, fail-safe `spend_limit_usd: 0` default |
| 4 | Godot C# specialist not imported — would be deleted immediately anyway |
| 5 | Mobile-scope additions — new section per named agent, no fabricated numeric limits |
| 6 | Team files for deleted engines — `teams/unreal/`, `teams/godot/` deleted; `teams/unity/` kept as-is |
| 7 | Max-7-direct-reports fix — moved `devops-engineer`/`security-engineer` from `producer` to `technical-director` |
| 8 | `ops/targets.yaml` seeded with `TODO`, not fabricated thresholds |
| 9 | CEO skills reference 3 not-yet-created skills, flagged for Phase 3 |
| 10 | No literal CMO/VP-Product upstream file — closest analogs merged into `publishing-director` |
| 11 | Publishing Director 7-report cap fix — `legal-compliance-officer` moved to report to `ceo` |
| 12 | `monetization-designer` sourced from `economy-designer` template, not upstream |
| 13 | `analytics-engineer`/`community-manager`/`live-ops-designer` moved to `publishing-director` |
| 14 | `player-support` added under `community-manager` |
| 15 | `teams/leadership/TEAM.md` updated to include `publishing-director` |
| 16 | Eight new skill names referenced ahead of creation, flagged for Phase 3 |
| 17 | Original (non-upstream) skills use `metadata.sources: [{kind: original, ...}]` |
| 18 | Skill-existence validator confirmed all 8 flagged gaps resolved, no others |
| 19 | `org-improvement-lead` is CEO's 7th direct report — exactly at cap |
| 20 | `ops/metrics-registry.yaml` immutability enforced by convention (prompt text), not tooling |
| 21 | Evidence-capture step added to `bug-triage`, `gate-check`, `retrospective`, `playtest-report` |
| 22 | `improvement-cycle` trigger added to `retrospective`'s Handoff, not `sprint-plan`'s |
| 23 | `improvement-cycle` uses the same original-skill frontmatter convention as #17 |
| 24 | README tables regenerated programmatically from on-disk frontmatter, not hand-maintained |
| 25 | `new-game-kickoff` gained `validate-concept` and `set-perf-budget` tasks, not bolted-on appendices |
| 26 | `## Next Task` field added only to `mobile-launch`'s and 2 new `new-game-kickoff` tasks |
| 27 | `store-submission-soft-launch` / `go-no-go-global-launch` task slugs chosen (not specified by issue) |
| 28 | `continuous-improvement` project has one explicitly self-looping recurring task |
| 29 | Model tiers assigned per-agent, never per-skill (confirmed zero skills declare `model:`) |
| 30 | Tier assignment matched the issue's 6/41/2 list exactly against actual agent dirs, no defaults needed |
| 31 | `docs/model-tiers.md` fully replaced, not incrementally edited |
| 32 | Pre-decision summary pairings implemented as each agent's own `## Model Tier` body section |
| 33 | Tier-1-only-skill check found zero pre-existing violations |
| 34 | `teams/*/TEAM.md` includes lists required no changes — already matched reality |
| 35 | `images/org-chart.png` not regenerated (no tooling exists); added `docs/org-chart.mermaid` instead |
| 36 | `ops/` skeleton additions purely additive — 4 new READMEs, everything else pre-existing |
| 37 | `scripts/validate.sh` is a thin wrapper around `scripts/validate.py` (Python, not raw bash) |

## Validation — `scripts/validate.sh` Output

```
VALIDATION PASSED — 49 agents, 66 skills, 6 teams checked, 0 failures across all 13 checks.
```

All 13 checks pass: `reportsTo` resolution, skill-reference existence, 150-word
minimums, zero `usage: referenced`, zero human-in-the-loop gate language
(with narrowly-scoped, documented exceptions for `skill-test`'s own check
definition and `PROGRESS.md`/`DECISIONS.md`'s historical prose — see the
script's inline comments), zero references to deleted engine agents (with
`setup-engine/SKILL.md`'s one documented explanatory sentence excluded, per
Phase 1's own recorded exception), the 7-direct-reports cap, `## Procedure`/
`## Output` presence on every skill, `TEAM.md` includes-path existence,
`ops/model-tiers.yaml` agreement with every agent's frontmatter, the exact
6/41/2 tier split, zero Tier-1-only skills on non-Tier-1 agents, and zero
`model:` keys in any `SKILL.md`.

## Known Gaps

- **Runtime access:** the agents need live access to the store consoles, ad
  networks, and analytics SDKs to execute these skills. This package
  defines behavior only; it does not provide credentials or integrations.
- **Self-improvement preconditions:** the loop is inert until real metrics
  flow into `ops/metrics/`.
- **Model enforcement:** the `metadata.model` values are declarative. The
  Paperclip runtime adapter must be configured per agent at import to
  actually run the assigned model and effort. Verify this by checking which
  model the run logs attribute to each agent.

Additional, narrower known gaps carried from earlier phases (full detail in
`PROGRESS.md`/`DECISIONS.md`):

- `ops/targets.yaml` greenlight/kill thresholds are still `TODO` placeholders
  — setting real values is the CEO's first-operating-cycle action, not
  something this conversion could responsibly pre-fill with a plausible-
  looking but fabricated number.
- Every guardrail in this package (skill/tier boundaries, metrics-registry
  immutability, always-ask gates) is enforced by prompt text, not by a
  sandboxing or permission-checking runtime — this is a prompt-driven
  package, and `scripts/validate.sh` checks structure, not runtime behavior.
