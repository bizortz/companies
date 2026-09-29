# Donchitos Game Studio

> Autonomous Unity mobile game studio (iOS/Android) — AI agents spanning creative direction, engineering, design, art, audio, narrative, QA, production, publishing & growth (UA, ASO, monetization, analytics, live ops, community, legal/compliance, finance), operating without human approval gates except a fixed always-ask list

> An [Agent Company](https://agentcompanies.io) based on [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) (pinned at commit `7ed2c3e9c46c880c9780fbce49266e7edfa15141`) — game studio workflows and skills for design documents, sprint planning, team coordination, balancing, QA, release management, and live operations, fully inlined and adapted for autonomous operation

![Org Chart](images/org-chart.png)

(`images/org-chart.png` predates this phase and was not regenerated — no
generation tooling exists in this repo. `docs/org-chart.mermaid` is the
current, authoritative 49-agent tree with model-tier coloring.)

## What's Inside

> This is an [Agent Company](https://agentcompanies.io) package from [Paperclip](https://paperclip.ing)

| Content | Count |
|---------|-------|
| Agents | 49 |
| Skills | 66 |

This studio runs `autonomous` by default (see `docs/automation-modes.md`):
agents decide and log rather than asking for approval, except for the five
categories in `ops/always-ask.yaml` (real-money spend above a weekly limit,
first public release or price changes, legal terms, personal data handling
outside policy, and deleting production data). Every decision above
specialist level is recorded in `ops/decision-log.md`.

The studio has four pillars reporting to the CEO: Creative (Creative
Director), Engineering (Technical Director), Production (Producer), and
Publishing & Growth (Publishing Director) — plus three individual CEO
reports, Finance Controller, Legal & Compliance Officer, and Org Improvement
Lead (the outcome-based self-improvement loop, added in Phase 3), each kept
independent of any single pillar. The CEO is now at the studio's 7-direct-
report cap — see `PROGRESS.md`. `ops/targets.yaml` holds the greenlight/kill
thresholds the CEO uses at every portfolio decision, and
`ops/metrics-registry.yaml` holds the canonical metric definitions the
improvement loop and every KPI-facing skill read from.

All 12 mobile skills flagged missing at the end of Phase 2 (`market-scan`,
`kpi-review`, `portfolio-review`, `concept-validation`, `monetization-setup`,
`privacy-compliance`, `aso-update`, `ua-campaign`, `device-perf-budget`,
`store-submission`, `soft-launch`, `incident-response`) plus `improvement-cycle`
now exist under `skills/` — the skill count above (66) reflects every skill
on disk, verified programmatically to have zero dangling `skills:` references
from any agent.

The studio is Unity-only (iOS and Android) — Unreal Engine and Godot
specialist teams from the upstream template were removed; see
`DECISIONS.md` and `PROGRESS.md` for the record of that change.

Every agent is assigned a model tier (`docs/model-tiers.md` /
`ops/model-tiers.yaml`): 6 Tier 1 decision-only agents (`claude-opus-5-5`),
41 Tier 2 execution agents (`claude-sonnet-5`), and 2 Tier 3 high-volume
templated agents (`claude-haiku-4-5-20251001`). See `docs/org-chart.mermaid`
for the full tree with tier coloring.

### Agents

| Agent | Reports To | Model Tier |
|-------|------------|------------|
| AI Programmer | lead-programmer | 2 |
| Accessibility Specialist | producer | 2 |
| Analytics Engineer | publishing-director | 2 |
| App Store Optimization Specialist | publishing-director | 2 |
| Art Director | creative-director | 2 |
| Audio Director | creative-director | 2 |
| Community Manager | publishing-director | 2 |
| Creative Director | ceo | 1 |
| DOTS/ECS Specialist | unity-specialist | 2 |
| DevOps Engineer | technical-director | 2 |
| Economy Designer | game-designer | 2 |
| Engine Programmer | lead-programmer | 2 |
| Finance Controller | ceo | 2 |
| Gameplay Programmer | lead-programmer | 2 |
| Lead Game Designer | creative-director | 2 |
| Lead Programmer | technical-director | 2 |
| Legal & Compliance Officer | ceo | 2 |
| Level Designer | game-designer | 2 |
| Live Operations Designer | publishing-director | 2 |
| Localization Lead | producer | 2 |
| Market Analyst | publishing-director | 2 |
| Monetization Designer | publishing-director | 2 |
| Narrative Director | creative-director | 2 |
| Network Programmer | lead-programmer | 2 |
| Organizational Improvement Lead | ceo | 1 |
| Performance Analyst | technical-director | 2 |
| Player Support Specialist | community-manager | 3 |
| Producer | ceo | 1 |
| Prototyper | producer | 2 |
| Publishing Director | ceo | 1 |
| QA Lead | technical-director | 2 |
| QA Tester | qa-lead | 3 |
| Release Manager | producer | 2 |
| Security Engineer | technical-director | 2 |
| Sound Designer | audio-director | 2 |
| Studio Head & CEO | null | 1 |
| Systems Designer | game-designer | 2 |
| Technical Artist | art-director | 2 |
| Technical Director | ceo | 1 |
| Tools Programmer | lead-programmer | 2 |
| UI Programmer | lead-programmer | 2 |
| UX Designer | art-director | 2 |
| Unity Addressables Specialist | unity-specialist | 2 |
| Unity Engine Lead | lead-programmer | 2 |
| Unity Shader/VFX Specialist | unity-specialist | 2 |
| Unity UI Specialist | unity-specialist | 2 |
| User Acquisition Manager | publishing-director | 2 |
| World Builder | narrative-director | 2 |
| Writer | narrative-director | 2 |

### Skills

| Skill | Description | Source |
|-------|--------------|--------|
| architecture-decision | Create an ADR documenting a technical decision: context, alternatives considered, consequences. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/architecture-decision/SKILL.md) |
| aso-update | App store optimization pass — listing copy, keywords, and asset spec per store, refreshed on a caden... | original (Phase 3) |
| asset-audit | Audit assets against naming conventions, file size budgets, format standards. Finds orphaned assets,... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/asset-audit/SKILL.md) |
| balance-check | Find balance outliers, broken progressions, degenerate strategies, economy imbalances in formulas an... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/balance-check/SKILL.md) |
| brainstorm | Guided concept ideation using professional studio techniques, player psychology, creative exploratio... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/brainstorm/SKILL.md) |
| bug-report | Structured bug report from a description, or analyze code for potential bugs. Reproduction steps, se... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/bug-report/SKILL.md) |
| bug-triage | Re-evaluate open bugs — priority vs severity, assign to sprints, surface systemic trends. Run when t... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/bug-triage/SKILL.md) |
| changelog | Auto-generate a changelog from git commits and sprint data. Internal and player-facing versions. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/changelog/SKILL.md) |
| code-review | Architectural code review — coding standards, SOLID, testability, performance concerns. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/code-review/SKILL.md) |
| concept-validation | Fake-door or CPI test plan and result for a new concept, before Concept Lock. Cheap external signal ... | original (Phase 3) |
| consistency-check | Scan GDDs against the entity registry for cross-document conflicts. Grep-first approach targets conf... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/consistency-check/SKILL.md) |
| day-one-patch | Day-one launch patch — focused fix for known issues found after gold master. Mini-sprint with QA gat... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/day-one-patch/SKILL.md) |
| design-review | Reviews one design document for completeness, internal consistency, implementability, and design sta... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/design-review/SKILL.md) |
| design-system | Section-by-section GDD authoring for one system — walks through each required section, cross-referen... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/design-system/SKILL.md) |
| device-perf-budget | Set per-device-tier FPS, memory, build size, and load time budgets before production. Anchors every ... | original (Phase 3) |
| estimate | Estimate task effort from complexity, dependencies, velocity, risk. Structured estimate with confide... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/estimate/SKILL.md) |
| gate-check | Ready to advance between development phases? PASS/CONCERNS/NOT ASSESSED/FAIL with blockers and requi... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/gate-check/SKILL.md) |
| hotfix | Emergency fix bypassing normal sprint process — hotfix branch, approvals tracked, backport verified,... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/hotfix/SKILL.md) |
| improvement-cycle | Cluster ops/learnings/, propose and evaluate targeted AGENTS.md/SKILL.md changes against ops/metrics... | original (Phase 3) |
| incident-response | Runbook for a crash spike or store rejection — triage, mitigate, root-cause, and report. | original (Phase 3) |
| kpi-review | Standing KPI report — D1/D7/D30, ARPDAU, CPI, ROAS, LTV, crash-free rate — with delta vs ops/targets... | original (Phase 3) |
| launch-checklist | Launch readiness across every department: code, content, store, marketing, community, infrastructure... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/launch-checklist/SKILL.md) |
| localize | Localization pipeline — find hardcoded strings, extract string tables, cultural review, VO, RTL, enf... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/localize/SKILL.md) |
| map-systems | Decompose a concept into individual systems, map dependencies, prioritize design order, create the s... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/map-systems/SKILL.md) |
| market-scan | Genre, competitor, and trend scan for the mobile games market. Feeds concept decisions, greenlights,... | original (Phase 3) |
| milestone-review | Milestone progress review — completeness, quality metrics, risk, go/no-go recommendation. At checkpo... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/milestone-review/SKILL.md) |
| monetization-setup | Build the IAP catalog, ad placement spec, and store product ID map for a title's real-money monetiza... | original (Phase 3) |
| onboard | Onboarding doc for a new contributor or agent — project state, conventions, priorities relevant to t... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/onboard/SKILL.md) |
| patch-notes | Player-facing patch notes from git history and changelogs. Translates developer language into player... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/patch-notes/SKILL.md) |
| perf-profile | Performance profiling — find bottlenecks, measure against budgets, produce ranked optimization recom... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/perf-profile/SKILL.md) |
| playtest-report | Structured playtest report template, or turn existing playtest notes into structured feedback. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/playtest-report/SKILL.md) |
| portfolio-review | Continue / scale / sunset ruling per title across the studio's full portfolio, against ops/targets.y... | original (Phase 3) |
| privacy-compliance | Draft privacy policy, ATT prompt spec, Data safety form answers, and age-rating questionnaire answer... | original (Phase 3) |
| project-stage-detect | Analyze project state, detect stage, identify gaps, recommend next steps. 'Where are we in developme... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/project-stage-detect/SKILL.md) |
| propagate-design-change | A GDD changed — scan ADRs and the traceability index for now-stale architectural decisions. Impact r... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/propagate-design-change/SKILL.md) |
| prototype | Concept prototype before GDDs — throwaway HTML, Engine or Paper build, PROCEED/PIVOT/KILL. After /br... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/prototype/SKILL.md) |
| qa-plan | QA test plan for a sprint — classifies stories by Logic/Integration/Visual/UI, covers automated test... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/qa-plan/SKILL.md) |
| regression-suite | Map test coverage to GDD critical paths, find fixed bugs lacking regression tests, flag drift from n... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/regression-suite/SKILL.md) |
| release-checklist | Pre-release checklist — build verification, certification requirements, store metadata, launch readi... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/release-checklist/SKILL.md) |
| retrospective | Sprint or milestone retrospective from completed work, velocity, blockers. Actionable insights for t... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/retrospective/SKILL.md) |
| reverse-document | Generate missing design or architecture docs from existing implementation — works backwards from cod... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/reverse-document/SKILL.md) |
| scope-check | Scope creep check — current scope versus the original plan. Flags additions, quantifies bloat, recom... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/scope-check/SKILL.md) |
| security-audit | Security audit — save tampering, cheat vectors, network exploits, data exposure, input validation. B... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/security-audit/SKILL.md) |
| setup-engine | Configure engine and version. Pins it in CLAUDE.md; WebSearch fills reference docs when the version ... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/setup-engine/SKILL.md) |
| skill-improve | Improve a skill via a test-fix-retest loop — static checks, targeted fixes, keep or revert on score ... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/skill-improve/SKILL.md) |
| skill-test | Validate skill files for structural compliance and behavioral correctness. Four modes: static linter... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/skill-test/SKILL.md) |
| smoke-check | Critical-path smoke gate before QA hand-off — runs the automated suite. A failed check means the bui... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/smoke-check/SKILL.md) |
| soak-test | Soak test protocol for extended play — what to observe and log for slow leaks, fatigue, late-appeari... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/soak-test/SKILL.md) |
| soft-launch | Plan and adjudicate a soft launch — markets, duration, KPI gates, and the exit verdict against ops/t... | original (Phase 3) |
| sprint-plan | New or updated sprint plan from the current milestone, completed work, and available capacity. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/sprint-plan/SKILL.md) |
| sprint-status | Fast, concise sprint snapshot — burndown and emerging risks for situational awareness. 'How is the s... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/sprint-status/SKILL.md) |
| start | First-time onboarding — asks where you are, then guides you to the right workflow. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/start/SKILL.md) |
| store-submission | iOS and Android submission checklist, fetching current review guidelines at runtime rather than rely... | original (Phase 3) |
| story-done | End-of-story completion review — verifies each acceptance criterion, checks GDD/ADR deviations, prom... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/story-done/SKILL.md) |
| story-readiness | Is a story implementation-ready? Checks clear acceptance criteria, open questions, ADR refs. READY/N... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/story-readiness/SKILL.md) |
| team-audio | Orchestrate the audio team — audio-director, sound-designer, technical-artist, gameplay-programmer —... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/team-audio/SKILL.md) |
| team-combat | Orchestrate the combat team — game-designer, gameplay-programmer, ai-programmer, technical-artist, s... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/team-combat/SKILL.md) |
| team-level | Orchestrate the level team — level-designer, narrative-director, world-builder, art-director, system... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/team-level/SKILL.md) |
| team-live-ops | Orchestrate the live-ops team — live-ops-designer, economy-designer, analytics-engineer, community-m... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/team-live-ops/SKILL.md) |
| team-narrative | Orchestrate the narrative team — narrative-director, writer, world-builder, level-designer — for sto... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/team-narrative/SKILL.md) |
| team-polish | Orchestrate the polish team — performance-analyst, technical-artist, sound-designer, qa-tester — to ... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/team-polish/SKILL.md) |
| team-release | Orchestrate the release team — release-manager, qa-lead, devops-engineer, producer — to execute a re... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/team-release/SKILL.md) |
| team-ui | Orchestrate the UI team through the UX pipeline — authoring, visual design, implementation, review, ... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/team-ui/SKILL.md) |
| tech-debt | Track, categorize and prioritize technical debt across the codebase — scans for debt indicators, mai... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/tech-debt/SKILL.md) |
| ua-campaign | Build a user-acquisition campaign plan, creative matrix, and budget pacing schedule, bounded by SPEN... | original (Phase 3) |
| vertical-slice | Pre-production validation — end-to-end build to confirm the full loop is achievable before committin... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/vertical-slice/SKILL.md) |

## Getting Started

```bash
npx paperclipai company import this-github-url-or-folder
```

See [Paperclip](https://paperclip.ing) for more information.

---
Exported from [Paperclip](https://paperclip.ing) on 2026-03-23
