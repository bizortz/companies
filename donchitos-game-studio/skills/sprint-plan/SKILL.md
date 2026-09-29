---
name: sprint-plan
description: New or updated sprint plan from the current milestone, completed work,
  and available capacity.
metadata:
  sources:
  - kind: github-file
    repo: Donchitos/Claude-Code-Game-Studios
    path: .claude/skills/sprint-plan/SKILL.md
    commit: 7ed2c3e9c46c880c9780fbce49266e7edfa15141
    attribution: Donchitos
    license: MIT
    usage: adapted
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
Resolved above — use as-is; `--review` overrides `review_mode`. No block →
defaults in `docs/config-resolution.md`.

## Existing Sprints

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
Resolved before this skill runs — use it to identify the previous sprint in
Phase 1 rather than re-globbing.

---

## Phase 0: Parse Arguments

Extract the mode argument (`new`, `update`, or `status`).

See `docs/director-gates.md` for the full check pattern. Individual gate definitions live in `docs/director-gates/[gate-id].md` — the spawned agent reads its own gate file; do not read it in the parent session.

This skill runs autonomously. Every decision it would previously have surfaced as a question is made by the owning agent and logged to `ops/decision-log.md`, per the operating rules in `docs/automation-modes.md` (the studio default mode is `autonomous`). The only exceptions are the fixed human gates listed in `ops/always-ask.yaml`, which always pause for explicit sign-off.

**`story_granularity`** — it sets how
many stories to allocate per sprint, scaled by velocity: **2–4** at `coarse`,
**6–10** at `balanced` (default), **15–25** at `fine`.

**Review mode check** (before gates run):
- The review mode was already resolved in steps 1–4 above — do not re-resolve it.
- **Special case:** if steps 1–3 all found nothing configured (no `--review`
  flag, no `modes.review_mode` in `project.yaml`, no `production/review-mode.txt`)
  **and** this is a `new` sprint, do not silently take the step-4 `lean` default
  — instead use an autonomous decision (logged to `ops/decision-log.md` per `docs/automation-modes.md`):
  - Prompt: "No review mode is set. Which review depth would you like for this sprint?"
  - Options:
    - `[A] full — spawn all director and lead gates`
    - `[B] lean — skip non-phase-gate director reviews (recommended for most sprints)`
    - `[C] solo — skip all gate spawning`
  - After selection: dual-write the chosen mode — set `modes.review_mode` in `project.yaml` (primary; add the `modes:` block if absent) AND write `production/review-mode.txt` (legacy fallback). Say: "Review mode set to [mode] and saved to project.yaml (and production/review-mode.txt)."
- In every other case the value resolved in steps 1–4 stands (for a non-`new`
  sprint with nothing configured, that is the `lean` default).

> **Do not write until Phase 1 confirms the sprint can be planned.** This write
> lands in Phase 0, before the Phase 1 backlog check that aborts the run —
> observed live: the run correctly BLOCKED on "No stories found under
> `production/epics/`" and `project.yaml` had *already* gained
> `review_mode: lean`. A skill that decides it cannot run must not have edited
> config on the way to deciding. Hold the selection in memory, complete Phase 1,
> and write only if planning proceeds.
> **Confirm the destination before writing.** The question above asks for review
> depth "for this sprint"; the write is permanent project config on a
> rigor-fronted knob. Ask explicitly: "Set `modes.review_mode: [mode]` in
> `project.yaml` (persists beyond this sprint), or use it for this sprint only?"

---

## Phase 1: Gather Context

1. **Read the current milestone** from `production/milestones/` **if it exists**.
   No skill writes this directory — it is authored by hand from
   `docs/templates/milestone-definition.md`. On the majority of projects
   it is absent, which is the normal state, not a gap: note "no milestone
   defined — planning against the story backlog alone" and continue. Never block
   sprint planning on it, and never infer a milestone from the sprint files.

2. **Read the previous sprint** (if any) from `production/sprints/` to
   understand velocity and carryover.

3. **Find the stories to plan** — this is the actual backlog, and it is the one
   input this phase cannot do without:
   ```
   Glob production/epics/**/story-*.md
   Grep pattern="^> \*\*Status\*\*" glob="production/epics/**/story-*.md" output_mode="content"
   ```
   Stories live at `production/epics/[epic-slug]/story-NNN-[slug].md` — that is
   where `/create-stories` writes them and where `/dev-story` looks for them. Plan
   from the ones marked `Ready`. Use the grep rather than reading each story: at
   this stage you need status and title, not the body.

   If the glob returns nothing: "No stories found under `production/epics/`. Run
   `/create-stories` first (at `standard`/`full`, `/create-epics` before it)."
   Do not proceed to invent work items — a sprint plan that references stories
   which do not exist cannot be implemented.

4. **Scan design documents** in `design/gdd/` for additional context on the
   features those stories implement. At `workflow: minimal` there are no
   per-system GDDs — use `design/game-brief.md` instead, and do not treat the
   absent GDDs as missing work. (Note: `/sprint-plan` is **optional** at
   `minimal` — the brief's Build order already is the plan.)

5. **Check the risk register** at `production/risk-register/` **if it exists**.
   Like the milestone above, no skill writes it — entries are authored by hand
   from `docs/templates/risk-register-entry.md`. If the directory is
   absent, say so once ("no risk register — risks assessed from the sprint
   contents only") rather than skipping risk assessment silently.

---

## Phase 2: Generate Output

For `new`:

**Generate a sprint plan** following this format and present it to the user. Do NOT ask to write yet — the gate phases run first and may require revisions before the file is written: the producer feasibility gate (Phase 4, spawned only in `full` review mode — skipped in `lean`/`solo`) and the QA plan check (Phase 5, all modes).

```markdown
# Sprint [N] — [Start Date] to [End Date]

## Sprint Goal
[One sentence describing what this sprint achieves toward the milestone]

## Capacity
- Total days: [X]
- Buffer (20%): [Y days reserved for unplanned work]
- Available: [Z days]

## Tasks

### Must Have (Critical Path)
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|

### Should Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|

### Nice to Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|

## Carryover from Previous Sprint
| Task | Reason | New Estimate |
|------|--------|-------------|

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|

## Dependencies on External Factors
- [List any external dependencies]

## Definition of Done for this Sprint
- [ ] All Must Have tasks completed
- [ ] All tasks pass acceptance criteria
- [ ] QA plan exists (`production/qa/qa-plan-sprint-[N].md`)
- [ ] All Logic/Integration stories have passing unit/integration tests
- [ ] Smoke check passed (`/smoke-check sprint`)
- [ ] QA sign-off report: APPROVED or APPROVED WITH CONDITIONS (`/team-qa sprint`)
- [ ] No S1 or S2 bugs in delivered features
- [ ] Design documents updated for any deviations
- [ ] Code reviewed and merged
```

For `update`:

**Update an existing sprint plan**:

1. Read the most recent sprint plan from `production/sprints/`.
2. Present the current story list with their current statuses from `production/sprint-status.yaml`.
3. If not already specified in project files, decide autonomously (using the most reasonable default given current project state) what to change: stories to add, remove, reprioritize, or re-estimate, and record the assumption in `ops/decision-log.md`. Decide autonomously and record the decision in `ops/decision-log.md`; escalate to your manager only if it crosses your domain boundary or matches an entry in `ops/always-ask.yaml` (see `docs/automation-modes.md`).
4. Apply the changes and re-present the full revised plan for review.
5. Re-run the producer feasibility gate (Phase 4) on the revised plan.
6. Write the updated markdown plan and yaml together directly (same write flow as `new` mode).

Note: `update` mode does not reset story statuses. Stories already marked `in-progress` or `done` keep their status. Only `backlog` and `ready-for-dev` stories can be removed or reprioritized freely.

For `status`:

**Generate a status report**:

```markdown
# Sprint [N] Status -- [Date]

## Progress: [X/Y tasks complete] ([Z%])

### Completed
| Task | Completed By | Notes |
|------|-------------|-------|

### In Progress
| Task | Owner | % Done | Blockers |
|------|-------|--------|----------|

### Not Started
| Task | Owner | At Risk? | Notes |
|------|-------|----------|-------|

### Blocked
| Task | Blocker | Owner of Blocker | ETA |
|------|---------|-----------------|-----|

## Burndown Assessment
[On track / Behind / Ahead]
[If behind: What is being cut or deferred]

## Emerging Risks
- [Any new risks identified this sprint]
```

---

## Phase 3: Prepare Sprint Status File

After generating a new sprint plan, also prepare the `production/sprint-status.yaml` content.
This is the machine-readable source of truth for story status — read by
`/sprint-status`, `/story-done`, and `/help` without markdown parsing.

**Do not write the yaml yet** — hold it in context. The producer feasibility gate (Phase 4, `full` review mode only) may revise the story list; the QA plan check (Phase 5) runs in every mode. Both files are written together directly after Phase 5.

Format:

```yaml
# Auto-generated by /sprint-plan. Updated by /story-done and /dev-story.
# DO NOT edit manually — use /story-done to update story status.
#
# Status value mapping (yaml ↔ story file Status field):
#   backlog        ↔  Not Started
#   ready-for-dev  ↔  Ready
#   in-progress    ↔  In Progress
#   review         ↔  In Review
#   done           ↔  Complete
#   blocked        ↔  Blocked

sprint: [N]
goal: "[sprint goal]"
start: "[YYYY-MM-DD]"
end: "[YYYY-MM-DD]"
generated: "[YYYY-MM-DD]"
updated: "[YYYY-MM-DD]"

stories:
  - id: "[epic-story, e.g. 1-1]"
    name: "[story name]"
    file: "[production/epics/[epic-slug]/story-NNN-[slug].md]"   # the real path, verbatim from the Glob above
    priority: must-have        # must-have | should-have | nice-to-have
    status: ready-for-dev      # backlog | ready-for-dev | in-progress | review | done | blocked
    owner: ""
    estimate_days: 0
    blocker: ""
    completed: ""
```

Initialize each story from the sprint plan's task tables:
- Must Have tasks → `priority: must-have`, `status: ready-for-dev`
- Should Have tasks → `priority: should-have`, `status: backlog`
- Nice to Have tasks → `priority: nice-to-have`, `status: backlog`

For `update`: read the existing `sprint-status.yaml`, carry over statuses for
stories that haven't changed, add new stories, remove dropped ones.

---

## Phase 4: Producer Feasibility Gate

**Review mode check** — apply before spawning PR-SPRINT:
- `solo` → skip. Note: "PR-SPRINT skipped — Solo mode." Proceed to Phase 5 (QA plan gate).
- `lean` → skip (not a PHASE-GATE). Note: "PR-SPRINT skipped — Lean mode." Proceed to Phase 5 (QA plan gate).
- `full` → spawn as normal.

Before finalising the sprint plan, spawn `producer` via `Agent` using gate **PR-SPRINT** (`docs/director-gates/pr-sprint.md`).

Pass: proposed story list (titles, estimates, dependencies), total team capacity in hours/days, any carryover from the previous sprint, milestone constraints and deadline.

Present the producer's assessment.

If UNREALISTIC: revise the story selection (defer stories to Should Have or Nice to Have) and re-present the updated plan before writing.

If CONCERNS, use an autonomous decision (logged to `ops/decision-log.md` per `docs/automation-modes.md`):
- Prompt: "Producer flagged concerns with this sprint plan. How do you want to proceed?"
- Options:
  - `[A] Proceed as planned — I accept the risk`
  - `[B] Adjust scope — defer some Should Have stories`
  - `[C] Extend the sprint timeline`

If [A]: proceed to write directly.
If [B]: revise the story list, re-present the updated plan, then write directly.
If [C]: adjust sprint dates and capacity, re-present the updated plan, then write directly.

After handling the producer's verdict, write `production/sprints/sprint-[N].md` and `production/sprint-status.yaml` directly (creating directories as needed) and log the write to `ops/decision-log.md`. Verdict: **COMPLETE** — sprint plan and status file created.

After writing, add:

> **Scope check:** If this sprint includes stories added beyond the original epic scope, run `/scope-check [epic]` to detect scope creep before implementation begins.

---

## Phase 5: QA Plan Gate

Before closing the sprint plan, check whether a QA plan exists for this sprint.

Use `Glob` to look for `production/qa/qa-plan-sprint-[N].md` or any file in `production/qa/` referencing this sprint number.

**If a QA plan is found**: note it in the sprint plan output — "QA Plan: `[path]`" — and proceed.

**If no QA plan exists**: do not silently proceed. Surface this explicitly:

> "This sprint has no QA plan. A sprint plan without a QA plan means test requirements are undefined — developers won't know what 'done' looks like from a QA perspective, and the sprint cannot pass the Production → Polish gate without one.
>
> Run `/qa-plan sprint` now, before starting any implementation. It takes one session and produces the test case requirements each story needs."

Use an autonomous decision (logged to `ops/decision-log.md` per `docs/automation-modes.md`):
- Prompt: "No QA plan found for this sprint. How do you want to proceed?"
- Options:
  - `[A] Run /qa-plan sprint now — I'll do that before starting implementation (Recommended)`
  - `[B] Skip for now — I understand QA sign-off will be blocked at the Production → Polish gate`

If [A]: close with "Sprint plan written. Run `/qa-plan sprint` next — then begin implementation."
If [B]: add a warning block to the sprint plan document:

```markdown
> ⚠️ **No QA Plan**: This sprint was started without a QA plan. Run `/qa-plan sprint`
> before the last story is implemented. The Production → Polish gate requires a QA
> sign-off report, which requires a QA plan.
```

---

## Phase 6: Next Steps

After the sprint plan is written and QA plan status is resolved:

- `/qa-plan sprint` — **required before implementation begins** — defines test cases per story so developers implement against QA specs, not a blank slate
- `/story-readiness [story-file]` — validate a story is ready before starting it
- `/dev-story [story-file]` — begin implementing the first story
- `/sprint-status` — check progress mid-sprint
- `/scope-check [epic]` — verify no scope creep before implementation begins

**Review mode configuration:** All director gates (producer feasibility, QA review, code review) respect the project review mode, resolved by the Phase 0 chain (`--review` flag → `modes.review_mode` in `project.yaml` → `production/review-mode.txt` → the `modes.rigor` expansion, which yields `lean` at standard rigor and `solo` at minimal). For a `new` sprint with nothing configured, Phase 0 prompts for it and dual-writes the choice. The mode is one of:
- `lean` — skip non-phase-gate director gates (default — fastest for solo dev)
- `full` — run all director gates as spawned sub-agents
- `solo` — skip all gate spawning unconditionally (single developer, no review)

`modes.review_mode` in `project.yaml` is the primary source; `production/review-mode.txt` is the legacy fallback. Both are read by `/sprint-plan`, `/story-readiness`, `/story-done`, and other gate-using skills at startup.

## Procedure

Follow the numbered/staged steps described above in order. Each step runs autonomously: resolve configuration and current project state first, perform the check or artifact generation described, and record any decision above specialist level in `ops/decision-log.md`. If a step would normally have asked the user a question, instead apply the autonomous decision rule in `docs/automation-modes.md` and proceed, escalating only per `ops/always-ask.yaml`.

## Output

Produce the artifact(s) described above (report, verdict, updated project file, or log entry) and write them to the appropriate location in the project (e.g. `production/`, `docs/`, or the relevant tracked file). Summarize the result back to the calling agent/team in a short status block, and append a decision-log entry if the output changed project state or direction.
