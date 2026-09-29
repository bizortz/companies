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
