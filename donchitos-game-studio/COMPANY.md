---
name: Donchitos Game Studio
description: Autonomous Unity mobile game studio (iOS/Android) with 49 AI agents spanning creative direction, engineering, design, art, audio, narrative, QA, production, and publishing & growth (UA, ASO, monetization, analytics, live ops, community, legal/compliance, finance) — operates without human approval gates except a fixed always-ask list, and self-improves against measured outcomes
slug: donchitos-game-studio
schema: agentcompanies/v1
version: 1.0.0
license: MIT
authors:
  - name: Donchitos
goals:
  - Develop and operate mobile games (iOS/Android, Unity) through a coordinated, autonomous studio pipeline
  - Follow a 10-phase development process from ideation through post-launch and live operations
  - Maintain quality through systematic reviews, testing, and quality gates
  - Operate autonomously with human sign-off reserved for a fixed always-ask list
  - Ship and grow mobile titles through a dedicated Publishing & Growth pillar (UA, ASO, monetization, market analysis, live ops, community)
  - Self-improve on measured outcomes via an evidence-driven improvement loop, never on unverified opinion
tags:
  - game-development
  - mobile-games
  - indie-games
  - game-studio
  - unity
  - autonomous-agents
  - mobile
  - ios
  - android
  - autonomous
---

Donchitos Game Studio is an autonomous, self-improving mobile game development company powered by specialized AI agents organized into a professional studio hierarchy. The studio replicates the structure and workflows of a real game development team — from Creative Director to QA Tester — enabling coordinated, quality-driven, autonomous game development for iOS and Android.

## How the Studio Works

The studio operates through a **hybrid pipeline + hub-and-spoke workflow**:

- **Pipeline**: Games progress through 10 sequential phases — Ideation, Pre-Production, Prototyping, Production, Implementation, Testing, Polish, Localization, Release, and Post-Launch
- **Hub-and-spoke**: Within each phase, the Producer dispatches work to department leads who manage their specialists independently

### Organizational Tiers

Two independent tiering schemes apply here: reporting depth (who manages
whom) and **model tier** (`docs/model-tiers.md` / `ops/model-tiers.yaml`,
which model and effort level each agent runs at). They are related but not
identical — model tier follows the *type* of work an agent does, not its
depth in the reporting tree.

- **Model Tier 1 — decides only** (`claude-opus-5-5`, effort high, 6 agents):
  `ceo`, `creative-director`, `technical-director`, `producer`,
  `publishing-director`, `org-improvement-lead`. These agents read one-page
  summaries prepared by named Tier 2 reports and issue a verdict in a fixed
  template — they never draft artifacts, code, or specs themselves.
- **Model Tier 2 — owns execution** (`claude-sonnet-5`, effort low, 41
  agents): every department lead and specialist not listed above or below —
  design, engineering, art, audio, narrative, production, QA leadership, and
  every publishing role (UA, ASO, monetization, market analysis, analytics,
  community, live ops, legal/compliance, finance). Escalates only
  cross-domain, irreversible, or always-ask-listed decisions to its Tier 1
  manager.
- **Model Tier 3 — high-volume, templated** (`claude-haiku-4-5-20251001`,
  effort auto, 2 agents): `qa-tester`, `player-support`. Follows the skill
  procedure and output template verbatim, escalating anything ambiguous.

**Reporting structure:** the CEO sits at the top (reportsTo: null) with four
pillar directors (Creative, Technical, Production, Publishing & Growth) plus
three individual functions (Finance Controller, Legal & Compliance Officer,
Org Improvement Lead) as direct reports — the CEO is at the studio's
7-direct-report cap. Below the directors, department leads (Game Designer,
Lead Programmer, Art Director, Audio Director, Narrative Director, QA Lead,
Community Manager, Unity Specialist, and others) manage specialists who
execute domain-specific work. See `docs/org-chart.mermaid` for the full
49-agent tree with model tier coloring.

### Autonomous Operating Protocol

The studio runs autonomously by default — there is no standing human
decision-maker in the loop, and agents do not pause to ask permission before
acting. This replaces the old Question → Options → Decision → Draft →
Approval protocol, which assumed a human was present at every step.

- **Decision flow.** The owning agent (the specialist or lead whose domain a
  decision falls in) decides. If the decision crosses that agent's domain
  boundary, it escalates to its manager. Director-level conflicts (Creative
  Director / Technical Director / Producer) escalate to the CEO. The CEO's
  decision is final.
- **Decision record.** Every decision made above specialist level is appended
  to `ops/decision-log.md` with: `id, date, agent, decision, options
  considered, rationale, reversibility (reversible|costly|irreversible),
  expected metric impact`.
- **Error handling.** Failures and unexpected results are handled per
  `docs/error-recovery-protocol.md` — the owning agent recovers, rolls back,
  or retries, escalating only per that protocol's own criteria, not by
  stopping to ask a human.
- **Always-ask list — the only human gates.** Stored machine-readably in
  `ops/always-ask.yaml`. Five categories always pause for explicit human
  sign-off, regardless of mode:
  1. Spending real money above `SPEND_LIMIT_USD` per week
  2. First public release, or any price change
  3. Accepting legal terms or contracts
  4. Handling personal data outside policy
  5. Deleting production data

  Full detail in `docs/automation-modes.md`.

### Supported Engine

The studio is a Unity-focused mobile game studio (iOS and Android). The
Unity team — Unity Specialist plus DOTS, Shader, Addressables, and UI
sub-specialists — owns all engine work. Unreal Engine and Godot specialist
teams from the upstream template have been removed; see `PROGRESS.md` and
`DECISIONS.md` for the pruning record.

Generated from [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) with the company-creator skill from [Paperclip](https://github.com/paperclipai/paperclip)
