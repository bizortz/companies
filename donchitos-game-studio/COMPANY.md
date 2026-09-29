---
name: Donchitos Game Studio
description: Autonomous Unity mobile game studio (iOS/Android) with AI agents spanning creative direction, engineering, design, art, audio, narrative, QA, production, and live operations
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
tags:
  - game-development
  - mobile-games
  - indie-games
  - game-studio
  - unity
  - autonomous-agents
---

Donchitos Game Studio is an autonomous, self-improving mobile game development company powered by specialized AI agents organized into a professional studio hierarchy. The studio replicates the structure and workflows of a real game development team — from Creative Director to QA Tester — enabling coordinated, quality-driven, autonomous game development for iOS and Android.

## How the Studio Works

The studio operates through a **hybrid pipeline + hub-and-spoke workflow**:

- **Pipeline**: Games progress through 10 sequential phases — Ideation, Pre-Production, Prototyping, Production, Implementation, Testing, Polish, Localization, Release, and Post-Launch
- **Hub-and-spoke**: Within each phase, the Producer dispatches work to department leads who manage their specialists independently

### Organizational Tiers

- **CEO** (Opus-tier): Studio Head aligns creative, technical, production, and publishing/growth pillars and makes portfolio greenlight/kill decisions against explicit thresholds in `ops/targets.yaml`. Finance Controller, Legal & Compliance Officer, and Org Improvement Lead also report directly to the CEO, kept independent of any single pillar — the CEO is at the studio's 7-direct-report cap with these three plus the four pillar directors.
- **Directors** (Opus-tier): Creative Director, Technical Director, Producer, and Publishing Director set vision, architecture, schedule, and go-to-market/monetization strategy — all report to the CEO.
- **Department Leads** (Sonnet-tier): Game Designer, Lead Programmer, Art Director, Audio Director, Narrative Director, QA Lead, Community Manager, and others translate direction into actionable work.
- **Specialists** (Sonnet/Haiku-tier): 35+ specialists execute domain-specific tasks — from Gameplay Programmers to Sound Designers to Engine Specialists to User Acquisition Manager and ASO Specialist.

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
