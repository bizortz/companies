# Progress — Phase 1 (Work Items 1-3)

This file tracks progress on converting `donchitos-game-studio` into an
autonomous, self-improving mobile game company. Phase 1 covered Work Items
1-3 only. Work Items 4-11 are explicitly out of scope for this phase and are
listed in full at the bottom.

## Pinned upstream commits

- **UPSTREAM_STUDIO** — `https://github.com/Donchitos/Claude-Code-Game-Studios`
  pinned at commit `7ed2c3e9c46c880c9780fbce49266e7edfa15141` (HEAD at clone
  time, 2026-09-29). Cloned into
  `$PAPERCLIP_RUN_SCRATCH_DIR/work/upstream-studio`.
- **UPSTREAM_AGENCY** — `https://github.com/msitarzewski/agency-agents`
  pinned at commit `68f01534ef30805ed3764f2d302ad03fe443707a` (HEAD at clone
  time, 2026-09-29). Cloned into
  `$PAPERCLIP_RUN_SCRATCH_DIR/work/upstream-agency`. Not consumed this phase
  — cloned and pinned early per the issue's instruction, for the phase that
  needs it.

Both clones live outside this git repository (in the run's scratch dir) and
are not part of this history; only the pinned SHAs matter going forward.

## Work Item 1 — Inline upstream content (COMPLETE)

- All 37 previously-stub `skills/*/SKILL.md` files replaced with the full,
  adapted upstream content (procedure, checks, output format, etc.), with
  Claude-Code-specific syntax stripped: `!`inline command execution``,
  `allowed-tools`, `AskUserQuestion`, `${CLAUDE_SKILL_DIR}` /
  `${CLAUDE_PROJECT_DIR}`, and `.claude/...` paths were all rewritten to
  package-relative equivalents or plain autonomous-decision language.
- 16 additional upstream skills imported and adapted: `skill-improve`,
  `skill-test`, `team-live-ops`, `soak-test`, `smoke-check`, `day-one-patch`,
  `security-audit`, `bug-triage`, `qa-plan`, `regression-suite`,
  `sprint-status`, `story-readiness`, `story-done`, `vertical-slice`,
  `consistency-check`, `propagate-design-change`. Total skills: **53** (37 +
  16), all with `usage: adapted` + the pinned commit SHA, all with `##
  Procedure` and `## Output` sections, all ≥150 words (verified
  programmatically — see below).
- Docs copied and adapted into `docs/`: `automation-modes.md` (further
  rewritten per Work Item 2, see below), `director-gates.md`,
  `coordination-rules.md`, `error-recovery-protocol.md`, `model-tiers.md`
  (left largely as-is per instructions — flagged for a later phase rewrite),
  `workflow-catalog.yaml`.
- Upstream `agents/*.md` bodies merged into the package's 39
  applicable`AGENTS.md` files (all except `ceo`, which has no upstream
  counterpart) as a `## Additional Procedures (Merged from Upstream)`
  section — existing frontmatter (`name`, `title`, `reportsTo`, `skills`)
  and existing body sections were never overwritten, only added to. The
  upstream `Collaboration Protocol` section (and its Claude-Code-specific
  ask-before-write instructions) was stripped out entirely during the merge
  rather than carried over, since Work Item 2 removes that pattern anyway.
- Added a `skills:` frontmatter field to the 33 agents that were missing it
  (pre-existing gap, not caused by this phase's work, but required by the
  hard constraint that every agent have `name/title/reportsTo/skills`) —
  mapped each to 2 existing, relevant skills.

## Work Item 2 — Autonomy (COMPLETE)

- `COMPANY.md`'s "Collaboration Protocol" section replaced with an
  "Autonomous Operating Protocol" section covering: decision flow (owning
  agent decides → escalates on domain-boundary conflict → director conflicts
  escalate to CEO → CEO is final), the decision-record requirement, error
  handling via `docs/error-recovery-protocol.md`, and the always-ask list.
- `ops/always-ask.yaml` created with the five fixed human gates from the
  issue (real-money spend above `SPEND_LIMIT_USD`/week — defaults to
  `spend_limit_usd: 0` until Finance sets it in a later phase; first public
  release or price change; legal terms/contracts; personal data outside
  policy; deleting production data).
- `ops/decision-log.md` created with the required format (`id, date, agent,
  decision, options considered, rationale, reversibility, expected metric
  impact`) and a seed entry (`D-0000`) recording the decision to adopt this
  operating model.
- `docs/automation-modes.md` rewritten (not just adapted) so the default —
  and, in normal operation, the *only* — mode is `autonomous`; the upstream
  `collaborative`/`guided` modes are documented solely as legacy vocabulary
  to interpret if it surfaces in older inlined skill text, never as an
  active runtime path. `automation_always_ask` now equals the five-item list
  above, replacing upstream's `scope_changes / file_deletions /
  schema_changes` categories.
- Removed human-in-the-loop gate language from all 49 originally-affected
  `AGENTS.md` files and from the 53 skills, plus the affected `docs/*.md`
  files, via a combination of scripted bulk fixes and targeted manual edits.
  This was a large, multi-pass effort — see **Deviations** below for how
  thorough this pass was and where the residual risk is.
- `skill-improve`/`skill-test` were updated so their own structural checks
  match this package's reality: Check 1 now validates this package's actual
  frontmatter shape (`name`, `description`, `metadata.sources[...]` with
  `usage: adapted`) instead of upstream's Claude-Code fields
  (`argument-hint`, `user-invocable`, `allowed-tools`), and Check 4 now
  fails on human-gate language instead of requiring "ask before write"
  language (the inverse of the upstream check, matching this studio's
  autonomous default).

## Work Item 3 — Prune to Unity (COMPLETE)

- Deleted agent directories: `unreal-specialist`, `ue-blueprint-specialist`,
  `ue-gas-specialist`, `ue-replication-specialist`, `ue-umg-specialist`,
  `godot-specialist`, `godot-gdscript-specialist`, `godot-shader-specialist`,
  `godot-gdextension-specialist` (9 total). Deleted `teams/unreal/` and
  `teams/godot/`. All `unity-*` agents and `teams/unity/` kept.
- Agent count: **49 → 40**.
- Removed every literal reference to the deleted agent IDs anywhere in the
  package (`reportsTo`, delegation lists, routing tables, README, skill
  bodies) — verified by grep with zero remaining live references (two
  intentional exceptions: `DECISIONS.md`'s own record of the removal, and
  one explanatory sentence in `skills/setup-engine/SKILL.md` naming what was
  removed and pointing to `DECISIONS.md`).
  `skills/setup-engine/SKILL.md` retains general Godot/Unreal *prose*
  (engine trade-off narrative, e.g. "mobile means Unity is strongly
  preferred") inherited from the upstream multi-engine wizard — this does
  not reference any deleted agent and is now framed by an added "Studio
  scope" banner at the top of the skill stating the studio is Unity-only and
  those branches are inert/unreachable.
- `README.md` and `COMPANY.md` regenerated/rewritten to reflect the current
  40-agent/53-skill, Unity-only, autonomous state (agent table and skill
  table both regenerated programmatically from the actual frontmatter on
  disk, not hand-maintained).
- Added a substantial `## Mobile Platform Scope (iOS & Android)` section
  (touch input, screen sizes/safe areas, thermal/battery limits, per-device-
  tier memory budgets, build size limits, iOS/Android build pipelines and
  signing, AAB/IPA store formats) to all 12 named agents: `unity-specialist`,
  `unity-dots-specialist`, `unity-shader-specialist`,
  `unity-addressables-specialist`, `unity-ui-specialist`,
  `engine-programmer`, `performance-analyst`, `technical-artist`,
  `ui-programmer`, `ux-designer`, `devops-engineer`, `release-manager`. Each
  section is genuinely tailored to that agent's role (different emphasis
  bullets per agent), not a copy-pasted boilerplate. No fabricated policy
  numbers — every section instructs fetching current official limits at
  decision time instead of hardcoding a number.
- **Incidental hard-constraint fix**: discovered `producer` had 9 direct
  reports (pre-existing, not caused by this phase's edits) — over the
  max-7 limit. Moved `devops-engineer` and `security-engineer` to report to
  `technical-director` instead (build infrastructure and security are
  engineering-quality concerns, and `technical-director` already referenced
  `devops-engineer` for infra decisions) — `producer` now has 7,
  `technical-director` has 5. Updated `teams/production/TEAM.md`,
  `teams/engineering/TEAM.md`, both agents' own files, and
  `producer`/`technical-director`'s delegation text to match. Recorded in
  `DECISIONS.md`.

## Verification performed

- All 40 `AGENTS.md` bodies ≥150 words (programmatic check, none failed).
- All 53 `SKILL.md` files: `usage: adapted` (zero `usage: referenced`
  remaining), `## Procedure` and `## Output` present, ≥150 words.
- `reportsTo` resolves to an existing agent for all 40 agents; `ceo` is the
  only `reportsTo: null`.
- Every `skills:` entry in every agent's frontmatter exists in `skills/`.
- No manager has more than 7 direct reports (verified after the producer/
  technical-director rebalance above).
- No remaining literal references to the 9 deleted agent IDs outside
  intentional citations in `DECISIONS.md` and one explanatory sentence in
  `setup-engine/SKILL.md`.

## Deviations / judgment calls

All recorded in detail in `DECISIONS.md`. Summary:

1. Business model parameter resolved to `f2p-hybrid` (superset of
   `f2p-ads`) per the issue's instruction to pick the option most consistent
   with the spec when a choice is required.
2. Agent-body merge used an additive "Additional Procedures (Merged from
   Upstream)" section rather than a line-by-line diff/merge, to guarantee no
   accidental loss of the hand-tuned existing frontmatter/body.
3. Skill adaptation used mechanical regex-based transformation of
   Claude-Code-specific syntax rather than hand-rewriting each of the 53
   files from scratch — this is faithful to the source material's structure
   and intent, but the removal of human-gate language in particular required
   **several follow-up passes** (an initial bulk regex pass, then a second
   pass fixing grammar artifacts it introduced, then a third manual pass
   working through the exact `grep -rniE "user (decides|approv)|approval|
   before any files are written|ask the user"` pattern file-by-file) before
   converging on a state with zero matches against that pattern outside
   legitimate peer/manager-approval language and this document's own
   citations. **Residual risk**: with 53 large skill files (some 600+
   lines) and 40 agent files, it is possible a stylistic variant of
   human-gate language (not matching the literal grep patterns used) was
   missed in a low-traffic corner of a large file. The verification grep
   above should be re-run after any future edit to these files.
4. `docs/model-tiers.md` was left largely as-is (only path adaptation, no
   content rewrite) per the issue's explicit instruction that it will be
   rewritten further in a later phase.
5. `skills/setup-engine/SKILL.md` was not fully rewritten to remove all
   Godot/Unreal *prose* (only literal deleted-agent-ID references and
   specialist-routing tables were removed/replaced) — see the note above.

## What remains — Work Items 4-11 (explicitly NOT done this phase)

Per the assigning issue, these are reserved for later phases:

- **Work Item 4** (implied by ground truth #5): add marketing/UA/ASO/
  monetization/finance/legal/support roles — none exist yet.
- **Work Item 5**: add mobile store/KPI skills (App Store/Play policy
  fetch-at-runtime skills, ASO, UA, KPI tracking, etc.) — none exist yet
  beyond the general skills imported in Work Item 1.
- **Work Item 6+**: rewrite `skill-improve` to measure *outcomes*, not just
  `skill-test static` structural checks (ground truth #4 — currently
  `skill-improve` still only drives the structural linter).
- **Work Item 7+**: full rewrite of `docs/model-tiers.md` for the
  TIER1/TIER2/TIER3 model names specified in this issue
  (`claude-opus-5-5` / `claude-sonnet-5` / `claude-haiku-4-5-20251001`) —
  currently still references the older `claude-opus-5` naming inherited
  from upstream.
- **Work Item 8+**: consume `UPSTREAM_AGENCY` (`msitarzewski/agency-agents`,
  pinned commit `68f01534ef30805ed3764f2d302ad03fe443707a`) — cloned and
  pinned this phase, not yet used.
- **Work Item 9+**: BUSINESS_MODEL-specific monetization skill/agent
  content (IAP + rewarded ads workflows) beyond the `economy-designer`
  agent that already exists.
- **Work Item 10+**: COPPA/GDPR/ATT/Play Data Safety runtime-fetch skills
  for the new legal/privacy-adjacent roles once they exist.
- **Work Item 11+**: any additional validation/CI script the assigning
  issue references as "a later validation script" — none was written this
  phase; the checks in "Verification performed" above were done ad hoc with
  inline Python, not committed as a reusable script.

Any of the above that turns out to already be partially covered by this
phase's work (e.g. some general QA/release skills already touch on store
readiness) should be treated as a head start, not as already complete.

---

# Progress — Phase 2 (Work Items 4-5)

Phase 2 covers Work Items 4 (rewrite the CEO) and 5 (add the Publishing &
Growth pillar) only. Work Items 6-11 remain out of scope — see "What remains"
at the bottom, updated for the current state.

## Work Item 4 — Rewrite the CEO (COMPLETE)

- `agents/ceo/AGENTS.md` rewritten: explicit direct-report list
  (`creative-director`, `technical-director`, `producer`,
  `publishing-director`, plus `finance-controller` and
  `legal-compliance-officer` added during Work Item 5 — see below), the four
  required pre-greenlight inputs (`market-scan` output, `kpi-review` output,
  `ops/metrics/` dashboard, finance runway report), explicit numeric
  greenlight/kill criteria read from a new `ops/targets.yaml` (CPI ceiling,
  D1/D7/D30 retention floors, ARPDAU floor, payback-days ceiling, budget-burn
  ceiling), and four fixed output templates (Portfolio Decision, Cross-Pillar
  Ruling, Resource Reallocation, Quarterly Strategy Note) written out
  literally in the body.
- `ops/targets.yaml` created, seeded with `TODO` for every threshold — no
  fabricated numbers. The CEO's AGENTS.md documents that setting real values
  is its first-operating-cycle action, logged to `ops/decision-log.md`.
  `ceo/AGENTS.md`'s Must-NOT list now explicitly includes inventing
  thresholds outside this file, editing metric definitions, and editing
  `ops/always-ask.yaml`.
- `ceo/AGENTS.md`'s `skills:` frontmatter now includes `market-scan`,
  `kpi-review`, and `portfolio-review` — none of these exist under `skills/`
  yet; Phase 3 must create them (see "What remains").

## Work Item 5 — Publishing & Growth pillar (COMPLETE)

- 8 new agents created under `agents/<slug>/AGENTS.md`, each with full
  upstream-derived or structurally-derived bodies (≥150 words, real
  procedural content, no stubs):
  - `publishing-director` (reports to `ceo`) — merged from
    `UPSTREAM_AGENCY`'s `product/product-manager.md` and
    `marketing/marketing-growth-hacker.md` (no literal `cmo`/`vp-product` file
    exists in this fork at the pinned commit — see `DECISIONS.md` #10 for the
    substitution rationale).
  - `ua-manager` (reports to `publishing-director`) — merged from
    `paid-media/paid-media-paid-social-strategist.md` and
    `paid-media/paid-media-tracking-specialist.md`.
  - `aso-specialist` (reports to `publishing-director`) — from
    `marketing/marketing-app-store-optimizer.md`.
  - `monetization-designer` (reports to `publishing-director`) — structurally
    based on `agents/economy-designer/AGENTS.md` per the issue's own
    instruction, not sourced from `UPSTREAM_AGENCY`.
  - `market-analyst` (reports to `publishing-director`) — from
    `product/product-trend-researcher.md`.
  - `legal-compliance-officer` (reports to `ceo`, **not**
    `publishing-director` — see max-7-cap fix below) — from
    `support/support-legal-compliance-checker.md`.
  - `finance-controller` (reports to `ceo`) — from
    `support/support-finance-tracker.md`.
  - `player-support` (reports to `community-manager`) — from
    `support/support-support-responder.md`.
  - All 8 were rewritten to remove B2B/SaaS/enterprise/regional-social-platform
    content and speak entirely to a mobile f2p game studio; all fabricated
    "success metric" benchmarks from the upstream files (e.g. specific
    CAC:LTV ratios, retention percentages) were dropped in favor of
    referencing `ops/targets.yaml` and the studio's own `kpi-review`/
    `market-scan` output instead of hardcoded numbers.
- `teams/publishing/TEAM.md` created, manager `publishing-director`, includes
  the 5 new reports plus the 3 moved agents (`analytics-engineer`,
  `community-manager`, `live-ops-designer`) and `player-support`.
  `legal-compliance-officer` is deliberately **not** in this team's includes
  since it reports to `ceo`, not `publishing-director` — see below.
- `analytics-engineer`, `community-manager`, and `live-ops-designer` moved to
  `reportsTo: publishing-director`. `teams/production/TEAM.md` updated to
  remove them and its description/prose rewritten accordingly.
  `producer/AGENTS.md`'s delegation list and prose updated to match. Every
  internal "producer approval"/"reports to producer" reference inside these
  three agents' own AGENTS.md bodies was also updated so body text matches
  the new frontmatter, not just the frontmatter field itself.
- `player-support` added as `community-manager`'s only direct report;
  `community-manager`'s "Who Reports To You" and "Coordination" sections
  updated; all internal "producer" references in `community-manager`'s body
  updated to `publishing-director` to match its new `reportsTo`.
- `teams/leadership/TEAM.md` updated to include `publishing-director` and its
  prose rewritten to describe all four CEO-report pillars.
- **Max-7-direct-reports cap violation found and fixed**: the issue's literal
  instructions would have given `publishing-director` 8 direct reports.
  `legal-compliance-officer` was moved to report to `ceo` instead — see
  `DECISIONS.md` #11 for the full rationale (loosest coupling to the
  publishing pillar specifically, plus the independence argument for a
  compliance function). Full detail and rationale in `DECISIONS.md`.
- `README.md` and `COMPANY.md` updated: agent count 40 → 48, full agent
  table regenerated, org-tier description updated to four pillars plus two
  CEO-direct individual functions (Finance Controller, Legal & Compliance
  Officer), and a note added that 8 new skill names are referenced but not
  yet created (Phase 3's job).
- `ops/always-ask.yaml`'s `applies_to` lists updated to include the new
  relevant agents (`ua-manager`, `finance-controller`, `monetization-designer`,
  `publishing-director`, `legal-compliance-officer`) on the always-ask
  categories their new roles actually touch (real-money spend,
  first-release/price-change, legal terms, personal-data-outside-policy).
  The five always-ask categories themselves were not changed — only which
  agents they apply to.

## Full agent list (48) and reportsTo tree, current state

```
ceo (reportsTo: null)
├── creative-director
│   ├── art-director
│   │   ├── technical-artist
│   │   └── ux-designer
│   ├── audio-director
│   │   └── sound-designer
│   ├── game-designer
│   │   ├── systems-designer
│   │   ├── level-designer
│   │   └── economy-designer
│   └── narrative-director
│       ├── writer
│       └── world-builder
├── technical-director
│   ├── lead-programmer
│   │   ├── ai-programmer
│   │   ├── engine-programmer
│   │   ├── gameplay-programmer
│   │   ├── network-programmer
│   │   ├── tools-programmer
│   │   ├── ui-programmer
│   │   └── unity-specialist
│   │       ├── unity-addressables-specialist
│   │       ├── unity-dots-specialist
│   │       ├── unity-shader-specialist
│   │       └── unity-ui-specialist
│   ├── qa-lead
│   │   └── qa-tester
│   ├── performance-analyst
│   ├── devops-engineer
│   └── security-engineer
├── producer
│   ├── release-manager
│   ├── localization-lead
│   ├── prototyper
│   └── accessibility-specialist
├── publishing-director
│   ├── ua-manager
│   ├── aso-specialist
│   ├── monetization-designer
│   ├── market-analyst
│   ├── analytics-engineer
│   ├── community-manager
│   │   └── player-support
│   └── live-ops-designer
├── finance-controller
└── legal-compliance-officer
```

## 7-report-cap check (run programmatically after all Work Item 5 edits)

```
Total agents: 48
lead-programmer: 7
publishing-director: 7
ceo: 6
technical-director: 5
producer: 4
creative-director: 4
unity-specialist: 4
game-designer: 3
art-director: 2
narrative-director: 2
community-manager: 1
qa-lead: 1
audio-director: 1

Max reports for any manager: 7   <-- PASS (cap is 7, none exceed it)
```

Also verified programmatically after all Work Item 4-5 edits: every
`reportsTo` resolves to an existing agent (only `ceo` has `null`); every
agent has `name`/`title`/`reportsTo`/`skills`; every `AGENTS.md` body is
≥150 words; every `skills:` entry either exists under `skills/` or is one of
the 8 explicitly-flagged not-yet-created Phase 3 skills (see below) — no
other unexpected missing skill references.

## What remains — Work Items 6-11 (Phase 3 and Phase 4)

### Phase 3 (Work Items 6, 7, 8)

- **New skills to create** (referenced in frontmatter across this phase's
  work, none exist under `skills/` yet):
  - `market-scan` — used by `ceo`, `publishing-director`, `market-analyst`.
  - `kpi-review` — used by `ceo`, `publishing-director`.
  - `portfolio-review` — used by `ceo`.
  - `concept-validation` — used by `market-analyst`.
  - `monetization-setup` — used by `monetization-designer`.
  - `privacy-compliance` — used by `legal-compliance-officer`.
  - `aso-update` — used by `aso-specialist`.
  - `ua-campaign` — used by `ua-manager`.
  - Each must ship with real `## Procedure`/`## Output` sections (≥150
    words), `usage` metadata consistent with this package's existing skill
    shape, and — per the hard constraint against fabricating store/platform
    policy facts — any store-policy-adjacent skill (`aso-update`,
    `privacy-compliance`) must instruct fetching the current official source
    at runtime rather than hardcoding App Store/Google Play/COPPA/GDPR/ATT/
    Play Data Safety specifics.
- **Work Item 6+**: rewrite `skill-improve` to measure outcomes, not just
  `skill-test static` structural checks (ground truth #4) — still open,
  untouched by Phase 2.
- **Work Item 7+**: full rewrite of `docs/model-tiers.md` for
  `claude-opus-5-5` / `claude-sonnet-5` / `claude-haiku-4-5-20251001` — still
  open, untouched by Phase 2.
- **Work Item 8+**: `UPSTREAM_AGENCY` has now been substantially consumed by
  Work Item 5 (8 new agents sourced from it), but any remaining
  agency-agents content the later phases want (e.g. additional paid-media
  specialists, more marketing-channel agents) is still available at the
  pinned commit `68f01534ef30805ed3764f2d302ad03fe443707a`.

### Phase 4 (Work Items 9, 10, 11 + final PR)

- **Work Item 9+**: BUSINESS_MODEL-specific monetization skill/agent content
  (IAP + rewarded ads workflows) — partially addressed by this phase's
  `monetization-designer` agent and `ops/always-ask.yaml` price-change gate,
  but the `monetization-setup` skill itself (the executable workflow) is
  still a Phase 3 deliverable, not yet written.
- **Work Item 10+**: COPPA/GDPR/ATT/Play Data Safety runtime-fetch skills —
  the `legal-compliance-officer` agent now exists and its AGENTS.md
  establishes the "fetch current official source, never hardcode" rule, but
  the actual `privacy-compliance` skill implementing that workflow is a
  Phase 3 deliverable, not yet written.
- **Work Item 11+**: a reusable, committed validation/CI script — still not
  written. All verification in Phase 1 and Phase 2 (word counts, reportsTo
  resolution, 7-report cap, skill-existence) was done with ad hoc inline
  Python, not committed to the repo as a script. This remains open for
  whichever later phase the issue designates for it.
- Final PR against `agentcompanies/v1` upstream is not yet opened — reserved
  for the end of Phase 4 per the issue's structure.
