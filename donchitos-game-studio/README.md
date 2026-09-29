# Donchitos Game Studio

> Autonomous Unity mobile game studio (iOS/Android) — AI agents spanning creative direction, engineering, design, art, audio, narrative, QA, production, publishing & growth (UA, ASO, monetization, analytics, live ops, community, legal/compliance, finance), operating without human approval gates except a fixed always-ask list

> An [Agent Company](https://agentcompanies.io) based on [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) (pinned at commit `7ed2c3e9c46c880c9780fbce49266e7edfa15141`) — game studio workflows and skills for design documents, sprint planning, team coordination, balancing, QA, release management, and live operations, fully inlined and adapted for autonomous operation

![Org Chart](images/org-chart.png)

## What's Inside

> This is an [Agent Company](https://agentcompanies.io) package from [Paperclip](https://paperclip.ing)

| Content | Count |
|---------|-------|
| Agents | 48 |
| Skills | 53 |

This studio runs `autonomous` by default (see `docs/automation-modes.md`):
agents decide and log rather than asking for approval, except for the five
categories in `ops/always-ask.yaml` (real-money spend above a weekly limit,
first public release or price changes, legal terms, personal data handling
outside policy, and deleting production data). Every decision above
specialist level is recorded in `ops/decision-log.md`.

The studio has four pillars reporting to the CEO: Creative (Creative
Director), Engineering (Technical Director), Production (Producer), and
Publishing & Growth (Publishing Director) — plus two individual CEO reports,
Finance Controller and Legal & Compliance Officer, kept independent of any
single pillar. See `PROGRESS.md` for the record of the Publishing & Growth
pillar's addition and `ops/targets.yaml` for the greenlight/kill thresholds
the CEO uses at every portfolio decision.

Note: eight new skills referenced in this reorganization's agent frontmatter
(`market-scan`, `kpi-review`, `portfolio-review`, `concept-validation`,
`monetization-setup`, `privacy-compliance`, `aso-update`, `ua-campaign`) do
not exist under `skills/` yet — they are reserved for Phase 3. The skill
count above (53) reflects only skills that currently exist on disk.

The studio is Unity-only (iOS and Android) — Unreal Engine and Godot
specialist teams from the upstream template were removed; see
`DECISIONS.md` and `PROGRESS.md` for the record of that change.

### Agents

| Agent | Reports To |
|-------|------------|
| Accessibility Specialist | producer |
| AI Programmer | lead-programmer |
| Analytics Engineer | publishing-director |
| App Store Optimization Specialist | publishing-director |
| Art Director | creative-director |
| Audio Director | creative-director |
| Studio Head & CEO | — |
| Community Manager | publishing-director |
| Creative Director | ceo |
| DevOps Engineer | technical-director |
| Economy Designer | game-designer |
| Engine Programmer | lead-programmer |
| Finance Controller | ceo |
| Lead Game Designer | creative-director |
| Gameplay Programmer | lead-programmer |
| Lead Programmer | technical-director |
| Legal & Compliance Officer | ceo |
| Level Designer | game-designer |
| Live Operations Designer | publishing-director |
| Localization Lead | producer |
| Market Analyst | publishing-director |
| Monetization Designer | publishing-director |
| Narrative Director | creative-director |
| Network Programmer | lead-programmer |
| Performance Analyst | technical-director |
| Player Support Specialist | community-manager |
| Producer | ceo |
| Prototyper | producer |
| Publishing Director | ceo |
| QA Lead | technical-director |
| QA Tester | qa-lead |
| Release Manager | producer |
| Security Engineer | technical-director |
| Sound Designer | audio-director |
| Systems Designer | game-designer |
| Technical Artist | art-director |
| Technical Director | ceo |
| Tools Programmer | lead-programmer |
| UI Programmer | lead-programmer |
| Unity Addressables Specialist | unity-specialist |
| DOTS/ECS Specialist | unity-specialist |
| Unity Shader/VFX Specialist | unity-specialist |
| Unity Engine Lead | lead-programmer |
| Unity UI Specialist | unity-specialist |
| User Acquisition Manager | publishing-director |
| UX Designer | art-director |
| World Builder | narrative-director |
| Writer | narrative-director |

### Skills

| Skill | Description | Source |
|-------|-------------|--------|
| architecture-decision | Create an ADR documenting a technical decision: context, alternatives considered, consequences. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/architecture-decision/SKILL.md) |
| asset-audit | Audit assets against naming conventions, file size budgets, format standards. Finds orphaned assets,... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/asset-audit/SKILL.md) |
| balance-check | Find balance outliers, broken progressions, degenerate strategies, economy imbalances in formulas an... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/balance-check/SKILL.md) |
| brainstorm | Guided concept ideation using professional studio techniques, player psychology, creative exploratio... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/brainstorm/SKILL.md) |
| bug-report | Structured bug report from a description, or analyze code for potential bugs. Reproduction steps, se... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/bug-report/SKILL.md) |
| bug-triage | Re-evaluate open bugs — priority vs severity, assign to sprints, surface systemic trends. Run when t... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/bug-triage/SKILL.md) |
| changelog | Auto-generate a changelog from git commits and sprint data. Internal and player-facing versions. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/changelog/SKILL.md) |
| code-review | Architectural code review — coding standards, SOLID, testability, performance concerns. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/code-review/SKILL.md) |
| consistency-check | Scan GDDs against the entity registry for cross-document conflicts. Grep-first approach targets conf... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/consistency-check/SKILL.md) |
| day-one-patch | Day-one launch patch — focused fix for known issues found after gold master. Mini-sprint with QA gat... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/day-one-patch/SKILL.md) |
| design-review | Reviews one design document for completeness, internal consistency, implementability, and design sta... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/design-review/SKILL.md) |
| design-system | Section-by-section GDD authoring for one system — walks through each required section, cross-referen... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/design-system/SKILL.md) |
| estimate | Estimate task effort from complexity, dependencies, velocity, risk. Structured estimate with confide... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/estimate/SKILL.md) |
| gate-check | Ready to advance between development phases? PASS/CONCERNS/NOT ASSESSED/FAIL with blockers and requi... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/gate-check/SKILL.md) |
| hotfix | Emergency fix bypassing normal sprint process — hotfix branch, approvals tracked, backport verified,... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/hotfix/SKILL.md) |
| launch-checklist | Launch readiness across every department: code, content, store, marketing, community, infrastructure... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/launch-checklist/SKILL.md) |
| localize | Localization pipeline — find hardcoded strings, extract string tables, cultural review, VO, RTL, enf... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/localize/SKILL.md) |
| map-systems | Decompose a concept into individual systems, map dependencies, prioritize design order, create the s... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/map-systems/SKILL.md) |
| milestone-review | Milestone progress review — completeness, quality metrics, risk, go/no-go recommendation. At checkpo... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/milestone-review/SKILL.md) |
| onboard | Onboarding doc for a new contributor or agent — project state, conventions, priorities relevant to t... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/onboard/SKILL.md) |
| patch-notes | Player-facing patch notes from git history and changelogs. Translates developer language into player... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/patch-notes/SKILL.md) |
| perf-profile | Performance profiling — find bottlenecks, measure against budgets, produce ranked optimization recom... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/perf-profile/SKILL.md) |
| playtest-report | Structured playtest report template, or turn existing playtest notes into structured feedback. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/playtest-report/SKILL.md) |
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
| sprint-plan | New or updated sprint plan from the current milestone, completed work, and available capacity. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/sprint-plan/SKILL.md) |
| sprint-status | Fast, concise sprint snapshot — burndown and emerging risks for situational awareness. 'How is the s... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/sprint-status/SKILL.md) |
| start | First-time onboarding — asks where you are, then guides you to the right workflow. | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/start/SKILL.md) |
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
| vertical-slice | Pre-production validation — end-to-end build to confirm the full loop is achievable before committin... | [github](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/7ed2c3e9c46c880c9780fbce49266e7edfa15141/.claude/skills/vertical-slice/SKILL.md) |

## Getting Started

```bash
npx paperclipai company import this-github-url-or-folder
```

See [Paperclip](https://paperclip.ing) for more information.

---
Exported from [Paperclip](https://paperclip.ing) on 2026-03-23
