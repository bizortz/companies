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


---

# Progress — Phase 3 (Work Items 6, 7, 8)

Phase 3 covers Work Items 6 (mobile skills), 7 (outcome-based self-improvement
loop), and 8 (projects) only. Work Items 9-11 remain out of scope — see "What
remains" at the bottom.

## Work Item 6 — Mobile skills (COMPLETE)

- 12 new skills created under `skills/<slug>/SKILL.md`, each with Purpose,
  Trigger/Owner Agent, Inputs, numbered Procedure, an Output template with an
  exact file path and structure, Pass/Fail Criteria, and a Handoff section,
  plus the package's standard `## Procedure`/`## Output` sections and
  ≥150-word bodies (all verified well over 500 words each): `market-scan`,
  `concept-validation`, `device-perf-budget`, `monetization-setup`,
  `privacy-compliance`, `store-submission`, `aso-update`, `soft-launch`,
  `ua-campaign`, `kpi-review`, `portfolio-review`, `incident-response`. This
  closes all 8 skill names flagged missing at the end of Phase 2 plus the 4
  more named in Work Item 6's table.
- Every store/platform-policy-adjacent skill (`privacy-compliance`,
  `store-submission`, `aso-update`) instructs fetching and citing the
  current official Apple/Google/COPPA/GDPR source at runtime — no App
  Store/Google Play/ATT/Play Data Safety/COPPA/GDPR numeric threshold or
  policy clause is hardcoded anywhere in these files.
- `gate-check`, `scope-check`, and `milestone-review` already existed in the
  original package (checked first, per the issue's own instruction) and were
  left unchanged — they reference only `creative-director`, `technical-
  director`, and `producer`, all still valid Tier-1-style directors in the
  current 49-agent org, so no consistency fix was needed.
- New skills use `metadata.sources: [{kind: original, usage: original,
  authored_for: donchitos-game-studio, phase: 3}]` instead of the `kind:
  github-file` shape used by the 53 upstream-sourced skills, since no
  upstream file exists for them — same `metadata.sources` list shape,
  honest about provenance (`DECISIONS.md` #17).

## Work Item 7 — Self-improvement loop, outcome-based (COMPLETE)

- `ops/metrics-registry.yaml` created: 12 required metrics (gate pass rate
  at first attempt, bug escape rate, sprint estimate accuracy, rework rate,
  decision reversal rate, crash-free sessions, D1/D7/D30 retention, CPI,
  ROAS, store rejection count), each with `id, definition, source, owner,
  direction, min_sample`. The file's header states, three times across the
  package (the file itself, `skills/improvement-cycle/SKILL.md`, and
  `agents/org-improvement-lead/AGENTS.md`'s Must-NOT list), that it is
  immutable to every agent except `analytics-engineer` and never editable by
  the improvement loop — enforced by convention/prompting, as is every other
  guardrail in this prompt-driven package (`DECISIONS.md` #20).
- Evidence-capture steps added to `bug-triage`, `gate-check`,
  `retrospective`, and `playtest-report` (each appends structured findings —
  `finding, affected agent/skill, evidence, metric affected, severity` — to
  `ops/learnings/<date>-<source>.md`, skipping the step when there's no
  systemic signal to log); `kpi-review` (new in Work Item 6) shipped with
  this step built in from the start.
- New agent `agents/org-improvement-lead/AGENTS.md` (reports to `ceo`, full
  ≥150-word body, 791 words) with explicit Must-NOT guardrails: no edits to
  `ops/metrics-registry.yaml`, `ops/targets.yaml`, `ops/always-ask.yaml`, the
  CEO's Must-NOT section, or its own AGENTS.md; no agent deletion; no
  `reportsTo` changes (structural org changes are proposed to the CEO, never
  self-applied); every change reversible via `ops/improvements/ledger.md`.
- New skill `skills/improvement-cycle/SKILL.md` (790 words) implementing the
  full 6-step procedure from the issue: cluster `ops/learnings/` by metric
  impact x frequency, propose top-3 with exact diffs/hypothesis/target
  metric/evaluation window/rollback condition, `skill-test static` gate
  before applying, apply on a branch/versioned copy with baseline capture,
  evaluate against `min_sample` and keep/revert, log every outcome to
  `ops/improvements/ledger.md`. Enforces 1 experiment per target file, 3
  concurrent company-wide.
- `ops/improvements/ledger.md` created (seeded with schema + concurrency
  limits, no entries yet). `ops/learnings/README.md` created (format spec,
  empty directory otherwise — tracked via this README rather than a bare
  `.gitkeep`, since the format needed documenting somewhere and this avoided
  adding a second file).
- `improvement-cycle`'s trigger added to `retrospective`'s new `## Handoff`
  section (placed after a new Phase 7 evidence-capture step and the existing
  Phase 6 "Next Steps"), per the issue's own preference for `retrospective`
  when both `sprint-plan` and `retrospective` exist (`DECISIONS.md` #22).
- **CEO direct-report count: 6 -> 7 — exactly at the studio's 7-report cap.**
  `org-improvement-lead` is the CEO's 7th direct report. Verified
  programmatically: 49 total agents (48 -> 49), `ceo` has 7 reports,
  `publishing-director` and `lead-programmer` also have 7 (pre-existing from
  Phases 1-2), no manager exceeds 7.

## Work Item 8 — Projects (COMPLETE)

- `projects/new-game-kickoff` kept, with two tasks inserted into its
  sequence: `validate-concept` (market-analyst, runs the `concept-validation`
  skill) as the new first task before `define-game-pillars`/Concept Lock,
  and `set-perf-budget` (performance-analyst, runs `device-perf-budget`)
  added to Pre-Production alongside `select-engine`/`decompose-systems`.
  `PROJECT.md`'s milestone descriptions and the `define-game-pillars` and
  `build-prototype` task bodies were updated to reflect the new sequence and
  cross-references (`build-prototype` now explicitly measures against
  `design/perf-budget.md` on the low-tier device band).
- New project `projects/mobile-launch` (owner `publishing-director`) with 9
  chained tasks, each with owner/inputs/done-criteria/`## Next Task`:
  `privacy-compliance` -> `monetization-setup` -> `aso-update` ->
  `store-submission-soft-launch` -> `soft-launch` -> `kpi-review` ->
  `go-no-go-global-launch` -> `ua-campaign-scale-up` -> `live-ops-cadence`.
- New project `projects/continuous-improvement` (owner `org-improvement-lead`)
  with a single recurring `improvement-cycle` task whose `## Next Task` is
  explicitly itself, run again at the next sprint end — no terminal state,
  matching the issue's "loops back to itself" instruction.

## Verification performed (Phase 3)

```
Total skills on disk: 66
Total agents: 49
Missing skill refs across all agents/*/AGENTS.md: NONE
Max reports for any manager: 7  <-- PASS (cap is 7)
  publishing-director: 7
  lead-programmer: 7
  ceo: 7
  technical-director: 5
  producer: 4
  unity-specialist: 4
  creative-director: 4
  game-designer: 3
  art-director: 2
  narrative-director: 2
  community-manager: 1
  qa-lead: 1
  audio-director: 1
```

Full skill list (66): architecture-decision, asset-audit, aso-update,
balance-check, brainstorm, bug-report, bug-triage, changelog, code-review,
concept-validation, consistency-check, day-one-patch, design-review,
design-system, device-perf-budget, estimate, gate-check, hotfix,
improvement-cycle, incident-response, kpi-review, launch-checklist,
localize, map-systems, market-scan, milestone-review, monetization-setup,
onboard, patch-notes, perf-profile, playtest-report, portfolio-review,
privacy-compliance, project-stage-detect, propagate-design-change,
prototype, qa-plan, regression-suite, release-checklist, retrospective,
reverse-document, scope-check, security-audit, setup-engine, skill-improve,
skill-test, smoke-check, soak-test, soft-launch, sprint-plan, sprint-status,
start, store-submission, story-done, story-readiness, team-audio,
team-combat, team-level, team-live-ops, team-narrative, team-polish,
team-release, team-ui, tech-debt, ua-campaign, vertical-slice.

`README.md`'s Agents and Skills tables regenerated programmatically from
on-disk frontmatter to match (49 agents, 66 skills); `COMPANY.md`'s
organizational-tiers paragraph updated for `org-improvement-lead`.

## What remains — Work Items 9-11 (Phase 4)

- **Work Item 9**: package metadata — not yet addressed.
- **Work Item 10**: model tiers — `docs/model-tiers.md` still needs the full
  rewrite for `claude-opus-5-5` / `claude-sonnet-5` /
  `claude-haiku-4-5-20251001` (flagged since Phase 1, still open — Phase 1's
  note that it was "left largely as-is... for a later phase" now resolves to
  Phase 4).
- **Work Item 11**: a reusable, committed validation/CI script, plus fixing
  whatever it finds, plus the final PR and `MODIFICATION_REPORT.md`. All
  verification across Phases 1-3 (word counts, `reportsTo` resolution,
  7-report cap, skill-existence) has been done with ad hoc inline Python,
  never committed to the repo as a script — Phase 4 should commit one (e.g.
  `scripts/validate.py`) covering all the checks demonstrated in this file
  and `PROGRESS.md`'s Phase 1/2 sections, run it, fix anything it surfaces,
  then open the final PR against `agentcompanies/v1` upstream with
  `MODIFICATION_REPORT.md` summarizing the full four-phase change set.
- `UPSTREAM_AGENCY` (pinned `68f01534ef30805ed3764f2d302ad03fe443707a`) has
  now been consumed by Work Item 5 only; any further agency-agents content
  Phase 4 wants remains available at that pinned commit.
