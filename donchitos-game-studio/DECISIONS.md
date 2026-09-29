# Decisions Log — Autonomous Mobile Studio Conversion

This file records judgment calls made while converting `donchitos-game-studio`
into an autonomous, self-improving mobile game company, per the assigning
issue's instruction to record decisions where the spec required a choice and
continue without stopping to ask.

## Parameters as fixed by the issue

- ENGINE = unity
- PLATFORMS = ios, android
- BUSINESS_MODEL = f2p-hybrid (IAP + rewarded ads) — chosen over the
  alternative `f2p-ads` because it is the superset business model (a hybrid
  studio can always choose to run ads-only per title later; skills/docs will
  be written to support both IAP and rewarded ads rather than assuming ads
  are the only revenue path). This affects monetization-related agents/skills
  added in a later phase (Work Items 4+), not this phase.
- TIER1_MODEL = claude-opus-5-5, effort high
- TIER2_MODEL = claude-sonnet-5, effort low
- TIER3_MODEL = claude-haiku-4-5-20251001, effort auto (omitted param)

## Pinned upstream commits

- UPSTREAM_STUDIO = https://github.com/Donchitos/Claude-Code-Game-Studios
  pinned at commit `7ed2c3e9c46c880c9780fbce49266e7edfa15141` (HEAD at time
  of cloning, 2026-09-29).
- UPSTREAM_AGENCY = https://github.com/msitarzewski/agency-agents
  pinned at commit `68f01534ef30805ed3764f2d302ad03fe443707a` (HEAD at time
  of cloning, 2026-09-29). Cloned and pinned now per the issue's instruction
  to save time for the phase that consumes it; not otherwise used this phase.

Both were cloned fresh into `$PAPERCLIP_RUN_SCRATCH_DIR/work/upstream-studio`
and `$PAPERCLIP_RUN_SCRATCH_DIR/work/upstream-agency` respectively (outside
the `companies` repo, per instructions — these scratch clones are not part of
this git history).

## Phase 1 scope and judgment calls (Work Items 1-3 only)

1. **Skill body adaptation strategy.** Upstream SKILL.md files are large
   (100-600+ lines) and contain Claude-Code-specific execution syntax
   (`!\`bash ...\``inline command execution, `allowed-tools:` frontmatter,
   `AskUserQuestion` tool calls, `${CLAUDE_SKILL_DIR}`/`${CLAUDE_PROJECT_DIR}`
   variables, and `.claude/...` paths). These were mechanically transformed:
   - `!\`...\`` inline command-execution lines were replaced with a plain
     prose instruction describing the same intent (resolve config, run a
     check, etc.) rather than an executable directive.
   - `AskUserQuestion`-driven branches were rewritten to autonomous decision
     language: the owning agent decides and records the decision in
     `ops/decision-log.md` per `docs/automation-modes.md`, escalating only if
     the decision crosses a domain boundary or matches `ops/always-ask.yaml`.
   - `.claude/skills/`, `.claude/docs/`, `.claude/agents/`, `.claude/hooks/`,
     `.claude/rules/` paths were rewritten to this package's equivalent
     relative locations (`skills/`, `docs/`, `agents/`, `docs/` for former
     hooks content, `docs/` for former rules content).
   - `allowed-tools`, `argument-hint`, `user-invocable`, and `model` frontmatter
     keys from upstream were dropped; this package's frontmatter shape
     (`name`, `description`, `metadata.sources[...]`) was retained and the
     `usage` field changed from `referenced` to `adapted` with the pinned
     commit SHA recorded.
   - Every adapted skill got explicit `## Procedure` and `## Output` headers
     appended if the upstream structure did not already use those exact
     headings, so the later validation script's structural check passes
     without discarding the richer upstream section structure that already
     existed under other headings (e.g. "Run the Gate Check", "Output the
     Verdict"). This is intentionally additive, not a rewrite of the
     already-good procedural content.

2. **Agent-body merge strategy (Work Item 1.5).** Rather than a line-by-line
   diff/merge (49 files, upstream bodies restructured non-trivially since the
   package snapshot was taken), each package `AGENTS.md` got a new
   `## Additional Procedures (Merged from Upstream)` section appended,
   carrying over upstream body content not already covered, with the same
   CC-specific-syntax stripping applied as for skills. The existing
   package frontmatter (`name`, `title`, `reportsTo`, `skills`) and existing
   body sections were left untouched except for the autonomy-language cleanup
   required by Work Item 2. This guarantees no genuine upstream detail is
   silently dropped while never overwriting the hand-tuned frontmatter/body
   this package already had.

3. **Always-ask list wording.** Used the five bullets from the issue verbatim
   in `ops/always-ask.yaml`, plus a `spend_limit_usd` placeholder field the
   Finance function (added in a later phase) is expected to set; until then
   it defaults to `0` (i.e., no real-money spend is pre-approved) so the gate
   is fail-safe rather than silently permissive.

4. **Godot C# specialist.** Upstream has a `godot-csharp-specialist.md` agent
   that does not exist in this package's 49 agents. Since ENGINE=unity and
   all godot-* agents are being deleted in Work Item 3 anyway, this upstream
   agent was not imported — importing then immediately deleting it would be
   wasted work with no lasting effect.

5. **Mobile-scope additions (Work Item 3.3).** Added as a new, clearly
   labeled `## Mobile Platform Scope (iOS & Android)` section in each of the
   12 named agents, covering: touch input, screen sizes/safe areas, thermal
   and battery limits, memory budgets per device tier, build size limits,
   iOS/Android build pipelines and signing, and store build formats (AAB /
   IPA). Content is written as engineering practice guidance, not as
   fabricated numeric budgets/policy facts — where a concrete limit matters
   (e.g. exact store size caps) the section instructs the agent to fetch the
   current official limit at runtime rather than hardcoding a number that
   could go stale or be wrong.

6. **Team files for deleted engines.** `teams/unreal/` and `teams/godot/`
   are deleted per Work Item 3.1. `teams/unity/TEAM.md` is kept as-is (it
   only ever referenced unity-* agents, so no reference cleanup was needed
   there).

Deviations, if any come up while executing, will be appended below this line.

## Deviations recorded during execution

7. **Max-7-direct-reports fix (Work Item 3).** Discovered mid-phase that
   `producer` had 9 direct reports — a pre-existing violation of the
   max-7-direct-reports hard constraint, not introduced by this phase's
   deletions. Fixed by moving `devops-engineer` and `security-engineer` to
   report to `technical-director` instead of `producer`: build
   infrastructure and security are engineering-quality concerns, and
   `technical-director` already referenced `devops-engineer` for
   infrastructure architecture decisions in its own AGENTS.md before this
   change. `producer` now has 7 direct reports, `technical-director` has 5.
   Updated `teams/production/TEAM.md`, `teams/engineering/TEAM.md`, both
   agents' own AGENTS.md files, `producer`/`technical-director`'s delegation
   text, and `README.md`'s agent table to match.

## Phase 2 scope and judgment calls (Work Items 4-5 only)

8. **`ops/targets.yaml` seeded with TODO placeholders, not fabricated numbers.**
   Work Item 4 requires the CEO's greenlight/kill criteria to be explicit
   numeric thresholds (CPI ceiling, D1/D7/D30 retention floors, ARPDAU floor,
   payback-days ceiling, budget-burn ceiling) read from a config file rather
   than invented ad hoc. Per the hard constraint against fabricating
   metrics/benchmarks, every field in the new `ops/targets.yaml` is a `TODO`
   placeholder rather than a plausible-looking number pulled from training
   data. The CEO's AGENTS.md documents that setting real values is its first
   operating-cycle action, informed by `market-scan` output and logged to
   `ops/decision-log.md` with cited sources — not something this phase's
   authoring should pre-empt with a guessed number.

9. **CEO skills reference three not-yet-created skills.** Per the issue's own
   instruction, `market-scan`, `kpi-review`, and `portfolio-review` were added
   to `ceo/AGENTS.md`'s `skills:` frontmatter even though no `skills/` directory
   exists for them yet. This is a known, explicitly flagged gap — a structural
   skill-existence validator will fail on these three (and on the five more
   listed below) until Phase 3 creates them. Recorded in `PROGRESS.md` so
   Phase 3 does not treat the failure as a regression.

10. **No literal "CMO" or "VP Product" file exists in `UPSTREAM_AGENCY`.**
    The issue's Work Item 5 table names `cmo + vp-product (merge both)` as the
    source for `publishing-director`, but at the pinned commit
    `68f01534ef30805ed3764f2d302ad03fe443707a` there is no agent literally
    named CMO or VP Product anywhere in the fork (checked `marketing/`,
    `product/`, `strategy/`, and `divisions.json`). The closest analogs were
    used instead: `product/product-manager.md` (a holistic product-lifecycle
    owner — the closest VP-Product equivalent: discovery, roadmap, GTM,
    outcome measurement) and `marketing/marketing-growth-hacker.md` (the
    closest CMO-equivalent for a growth-stage company: acquisition, funnel
    optimization, channel strategy) were both read in full and merged into
    `publishing-director/AGENTS.md`, rewritten entirely for a mobile f2p game
    studio context (removed all B2B SaaS/enterprise examples, PRD/RICE
    templates written for software features, and generic SaaS success
    metrics; replaced with mobile game market positioning, launch strategy,
    monetization strategy, and growth-KPI content, and cross-referenced to
    this package's own CEO/`ops/targets.yaml` vocabulary).

11. **Publishing Director's direct-report count required a max-7-cap fix.**
    Following the issue's literal instructions produced 8 direct reports
    under `publishing-director`: the five new agents it manages
    (`ua-manager`, `aso-specialist`, `monetization-designer`, `market-analyst`,
    `legal-compliance-officer`) plus the three moved agents
    (`analytics-engineer`, `community-manager`, `live-ops-designer`) — a
    violation of the max-7-direct-reports hard constraint that the issue
    itself requires checking for and fixing by "moving the most
    loosely-coupled report to a sibling director." `legal-compliance-officer`
    was moved to report directly to `ceo` instead of `publishing-director`,
    for two reasons: (1) it is the most loosely coupled of the eight — its
    work (privacy policy, age ratings, COPPA/GDPR/ATT/Play Data Safety,
    loot-box regulation) is a cross-cutting compliance function touched by
    engineering (analytics, SDKs), production (release certification), and
    publishing (monetization, UA) alike, not exclusively a publishing/growth
    concern; and (2) compliance review is more credible when it is
    organizationally independent of the pillar whose growth and monetization
    decisions it is meant to check — a compliance officer reporting to the
    director whose KPIs it can block has an obvious incentive conflict.
    `publishing-director` now has 7 direct reports; `ceo` now has 6
    (`creative-director`, `technical-director`, `producer`,
    `publishing-director`, `finance-controller`, `legal-compliance-officer`)
    instead of the 5 the issue's Work Item 4 note projected — this is a
    direct, documented consequence of the cap fix, not scope creep. Updated
    `ceo/AGENTS.md`, `publishing-director/AGENTS.md`,
    `legal-compliance-officer/AGENTS.md`, and `teams/publishing/TEAM.md` to
    match. The full report-count table is in `PROGRESS.md`.

12. **`monetization-designer` sourced from `economy-designer`, not
    `UPSTREAM_AGENCY`, per the issue's own instruction.** No upstream file was
    inlined for this agent; its AGENTS.md was authored using
    `agents/economy-designer/AGENTS.md`'s structure (mathematical-rigor
    framing, ethical-guidelines section, handoff process) as a template, then
    written to own the real-money/ad-revenue surface specifically, with an
    explicit "coordinates with, does not edit" relationship to
    `economy-designer`'s in-game currency model to avoid the two roles
    silently duplicating or contradicting each other's resource-flow math.

13. **`analytics-engineer`, `community-manager`, `live-ops-designer` moved to
    `publishing-director`.** Per the issue's explicit instruction. Updated
    `teams/production/TEAM.md` (removed these three, updated its description
    and manager-note prose), created `teams/publishing/TEAM.md` (added these
    three plus the five new agents), updated `producer/AGENTS.md`'s
    delegation list and delegation prose, and fixed every internal
    `producer`-approval reference inside the three moved agents' own AGENTS.md
    bodies (e.g. "approved by producer" -> "approved by publishing-director")
    so the body text matches the new frontmatter `reportsTo`, not just the
    frontmatter field itself.

14. **`player-support` added under `community-manager`.** Sourced from
    `support/support-support-responder.md`, rewritten to drop all
    generic-SaaS/enterprise-tier support content (phone queues, ABM,
    multi-tier enterprise escalation) and focus on mobile f2p support: ticket
    triage, refunds per platform policy, and bug intake routed to `qa-lead`.
    This is `community-manager`'s only direct report, well under the max-7
    cap, and does not change `community-manager`'s own `reportsTo`
    (`publishing-director`, set in the same reorganization).

15. **`teams/leadership/TEAM.md` updated to include `publishing-director`.**
    Not explicitly required by the issue, but consistent with the existing
    pattern of that team listing the CEO's pillar-director-level direct
    reports (`creative-director`, `technical-director`, `producer`). Its
    prose was rewritten to describe all four pillars and to note that all
    four report to the CEO. `finance-controller` and `legal-compliance-officer`
    were deliberately *not* added to any team, matching the pre-existing
    pattern that `ceo` itself belongs to no team — both are individual
    CEO-direct functions without a department of their own to lead, not
    omissions.

16. **Eight new skill names referenced but not yet created.** Per the issue's
    explicit instruction, `market-scan`, `kpi-review`, `portfolio-review`,
    `concept-validation`, `monetization-setup`, `privacy-compliance`,
    `aso-update`, and `ua-campaign` appear in various new/modified agents'
    `skills:` frontmatter without a corresponding `skills/<name>/SKILL.md` on
    disk. This is expected and is Phase 3's responsibility — see
    `PROGRESS.md`'s "What remains" section. A skill-existence validator run
    today will report exactly these eight as missing and nothing else.
