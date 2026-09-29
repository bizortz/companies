---
name: team-combat
description: Orchestrate the combat team — game-designer, gameplay-programmer, ai-programmer,
  technical-artist, sound-designer, qa-tester — design through implement and validate.
metadata:
  sources:
  - kind: github-file
    repo: Donchitos/Claude-Code-Game-Studios
    path: .claude/skills/team-combat/SKILL.md
    commit: 7ed2c3e9c46c880c9780fbce49266e7edfa15141
    attribution: Donchitos
    license: MIT
    usage: adapted
---

**Argument check:** If no combat feature description is provided, output:
> "Usage: `/team-combat [combat feature description]` — Provide a description of the combat feature to design and implement (e.g., `melee parry system`, `ranged weapon spread`)."
Then stop immediately without spawning any subagents or reading any files.

When this skill is invoked with a valid argument, orchestrate the combat team through a structured pipeline.

**Decision Points:** At each phase transition, the orchestrating agent reviews the subagent's proposals directly, records the decision with concise labels in `ops/decision-log.md`, and advances to the next phase — the pipeline runs end to end without pausing for approval. Only decisions matching `ops/always-ask.yaml` pause regardless of how far the pipeline has run. See `docs/automation-modes.md`.

## Phase 0: Resolve Config

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
Resolved above — use as-is; `--review` overrides `review_mode`. No block →
defaults in `docs/config-resolution.md`.

`review_mode` sets gate depth:
- `full` — spawn all director and lead gates as described
- `lean` — skip director gates unless they are PHASE-GATE type (CD-PHASE-GATE, TD-PHASE-GATE, PR-PHASE-GATE, AD-PHASE-GATE)
- `solo` — skip all director gate spawning entirely; run the skill without any agent gates

`automation` drives the Decision Points note above. See the Decision Points note above and
`docs/automation-modes.md` for how each mode changes pipeline behavior.

**`team.size`**: which agents are active (orthogonal to review_mode gate-depth and workflow docs).
- **`individual`** (default): `gameplay-programmer` runs the pipeline; escalate `ai-programmer` only if the feature flags AI work. Other Team Composition agents are consulted via the gameplay-programmer, not spawned separately.
- **`small`**: the full Team Composition pipeline below, as documented.
- **`studio`**: full pipeline + engine sub-specialists + an adversarial review pass.
Directors (CD/TD/PR) still spawn at phase gates regardless of size; a non-core agent needed at `individual` routes through the nearest active core agent with an informational note. **"Phase gate" means any phase that ends in an autonomous decision (logged to `ops/decision-log.md` per `docs/automation-modes.md`) decision point before the pipeline advances** — not every phase. Apply the test literally: if the phase below has no decision point, it is not a gate, and an agent restricted to "phase gates only" is not spawned for it. This active-set scoping applies throughout the pipeline below: any phase that names an agent outside the active set routes through the nearest core agent rather than spawning it.

**Announce the active set before Phase 1 — never let the collapse be silent.**
Before spawning anything, state in one line which agents this run will actually
spawn, and which the pipeline below names but will **not** spawn at the resolved
`team.size`. For example:

> `Active set (team.size: <resolved>): <the agents listed for that size above>.`
> `Not spawned this run: <every other agent this pipeline names> — consulted`
> `through <nearest active core agent>. Raise team.size (or modes.rigor) to widen.`

Fill it from the `team.size` list directly above and the agents this file's own
pipeline names — not from an example. Both sets differ per orchestrator.

The pipeline below reads as a multi-agent fan-out and at the shipped default it
is one or two agents — `team-release` names eight and runs one, `team-narrative`
names six across five phases and runs `writer` alone. **The collapse is correct**:
`team.size` is rigor-fronted and the narrow default is the token lever, measured
at roughly 10x. What was wrong is that nothing said so, so a reader could not
distinguish a correctly-collapsed run from a broken pipeline, and the per-agent
"routes through the nearest core agent with an informational note" rule above
fires at routing time and never states the shape of the run as a whole.

This is the same rule as the skipped-check reporting elsewhere in this file: **a constraint that is enforced but never surfaced is
indistinguishable, to the person reading the output, from one that was never
enforced.**

## Team Composition
- **game-designer** — Design the mechanic, define formulas and edge cases
- **gameplay-programmer** — Implement the core gameplay code
- **ai-programmer** — Implement NPC/enemy AI behavior for the feature
- **technical-artist** — Create VFX, shader effects, and visual feedback
- **sound-designer** — Define audio events, impact sounds, and ambient combat audio
- **engine specialist** (primary) — Validate architecture and implementation patterns are idiomatic for the engine (the primary specialist is `<engine>-specialist` from `engine.name` — Godot→`godot-specialist`, Unity→`unity-specialist`, Unreal→`unreal-specialist`; fall back to the Primary line of `## Engine Specialists` in `technical-preferences.md`)
- **qa-tester** — Write test cases and validate the implementation

## How to Delegate

Use the `Agent` tool to spawn each team member as a subagent:
- `subagent_type: game-designer` — Design the mechanic, define formulas and edge cases
- `subagent_type: gameplay-programmer` — Implement the core gameplay code
- `subagent_type: ai-programmer` — Implement NPC/enemy AI behavior
- `subagent_type: technical-artist` — Create VFX, shader effects, visual feedback
- `subagent_type: sound-designer` — Define audio events, impact sounds, ambient audio
- `subagent_type: [primary engine specialist]` — Engine idiom validation for architecture and implementation
- `subagent_type: qa-tester` — Write test cases and validate implementation

**Brief each agent — do not dump context.** Read the shared inputs **once** and pass a distilled brief inline: the lines each agent actually needs, never a file path for a document you have already read (an agent handed a path re-reads the whole file). Pass a path only for a document you have not read and only that agent needs.

**End every agent prompt with a return contract:** "Write your full output to `[path]` — that named path is your write authorisation under the bounded exception below, so write it without a separate approval prompt. Return **only** (1) the path written, (2) a ≤5-bullet summary of decisions, (3) any BLOCKED/CONCERNS items, one line each. Do not restate the documents you read." Without it, an agent returns everything it read back into this session.

**Substitute a real path for `[path]`.** Every phase that produces an artifact
names one; most are fixed by the skill that already reads them:

| Phase / agent | Writes to | Destination fixed by |
|---|---|---|
| 1 game-designer | `design/gdd/[feature].md` | the GDD convention |
| 2 gameplay-programmer | `docs/architecture/[feature]-sketch.md` | see note below |
| 2 engine specialist | `docs/architecture/[feature]-engine-notes.md` | see note below |
| 5 qa-tester (test cases) | `production/qa/test-cases/[feature]-cases.md` | `/team-qa` Phase 4 |
| 5 qa-tester (bugs) | `production/qa/bugs/BUG-[NNN]-[slug].md` | `/team-qa` Phase 5 |

Phase 6 is a spoken status report, not an artifact — no path, and none needed.

> **Every phase above names a concrete destination, deliberately.** The Error
> Recovery Protocol below says "a named artifact that is not on disk is a failed
> phase" — a check that cannot run when no path was named.
>
> **The two `docs/architecture/` entries are a judgement call, not a convention.**
> That directory holds ADRs (`adr-NNNN-*.md`); a sketch is a precursor to one, not
> one itself, and **nothing in the repo reads either file**. Say so when
> reporting, so the sketch is understood as a record rather than an input to a
> later gate.

> **Autonomous write.** This subagent writes the artifact directly, without asking for approval — this studio runs `autonomous` by default (see `docs/automation-modes.md`). The write is logged to `ops/decision-log.md` as part of the phase's decision record.

Launch independent agents in parallel where the pipeline allows it (e.g., Phase 3 agents can run simultaneously).

## Pipeline

### Phase 1: Design
Delegate to **game-designer**:
- Create or update the design document in `design/gdd/` covering: mechanic overview, player fantasy, detailed rules, formulas with variable definitions, edge cases, dependencies, tuning knobs with safe ranges, and acceptance criteria
- Output: completed design document

### Phase 2: Architecture
Delegate to **gameplay-programmer** (with **ai-programmer** if AI is involved):
- Review the design document
- Design the code architecture: class structure, interfaces, data flow
- Identify integration points with existing systems
- Output: architecture sketch with file list and interface definitions

Then spawn the **primary engine specialist** to validate the proposed architecture:
- Is the class/node/component structure idiomatic for the pinned engine? (e.g., Godot node hierarchy, Unity MonoBehaviour vs DOTS, Unreal Actor/Component design)
- Are there engine-native systems that should be used instead of custom implementations?
- Any proposed APIs that are deprecated or changed in the pinned engine version?
- Output: engine architecture notes — incorporate into the architecture before Phase 3 begins

Review the architecture sketch directly: proceed to spawn implementation
agents (gameplay-programmer, ai-programmer, technical-artist, sound-designer)
unless the sketch came back BLOCKED, in which case revise it first. Log the
decision via `ops/decision-log.md`. This gate is not release-critical or
irreversible, so it follows the standard autonomous pipeline rule — no human
approval required.

### Phase 3: Implementation (parallel where possible)
Delegate in parallel:
- **gameplay-programmer**: Implement core combat mechanic code
- **ai-programmer**: Implement AI behaviors (if the feature involves NPC reactions)
- **technical-artist**: Create VFX and shader effects
- **sound-designer**: Define audio event list and mixing notes

### Phase 4: Integration
- Wire together gameplay code, AI, VFX, and audio
- Ensure all tuning knobs are exposed and data-driven
- Verify the feature works with existing combat systems

### Phase 5: Validation
Delegate to **qa-tester**:
- Write test cases from the acceptance criteria
- Test all edge cases documented in the design
- Verify performance impact is within budget
- File bug reports for any issues found

### Phase 6: Sign-off
- Collect results from all team members
- Report feature status: COMPLETE / NEEDS WORK / BLOCKED
- List any outstanding issues and their assigned owners

## Error Recovery Protocol

**First, verify the artifact.** If the return contract named a path, check the
path exists before treating the phase as done — **a named artifact that is not
on disk is a failed phase, however fluent the response reads.** An agent can
burn a full phase and return a plausible preamble having written nothing, which
is neither BLOCKED nor an error nor "cannot complete", so the trigger below
never fires. Resume it naming the unmet contract; the context is
usually still there.

If any spawned agent returns BLOCKED, errors, or cannot complete: **surface it
immediately, don't proceed past a dependency it blocks, and always produce a
partial report.** Full procedure: `docs/error-recovery-protocol.md`.

Common blockers:
- Input file missing (story not found, GDD absent) → redirect to the skill that creates it
- ADR status is Proposed → do not implement; run `/architecture-decision` first
- Scope too large → split into two stories via `/create-stories`
- Conflicting instructions between ADR and story → surface the conflict, do not guess

## File Write Protocol

All file writes (design documents, implementation files, test cases) are
delegated to sub-agents spawned via `Agent`. Those writes follow the **bounded
exception** documented above under "Why this does not violate the Collaboration
Protocol" — the path is one you named, the artifact is new under `production/`,
`docs/` or `tests/`, and the phase is gated by an autonomous decision (logged to `ops/decision-log.md` per `docs/automation-modes.md`). A sub-agent
does **not** prompt per write inside those bounds; outside them it must ask.
This orchestrator does not write files directly.

## Output

A summary report covering: design completion status, implementation status per team member, test results, and any open issues.

Verdict: **COMPLETE** — combat feature designed, implemented, and validated.
Verdict: **BLOCKED** — one or more phases could not complete; partial report produced with unresolved items listed.

## Next Steps

- Run `/code-review` on the implemented combat code before closing stories.
- Run `/balance-check` to validate combat formulas and tuning values.
- Run `/team-polish` if VFX, audio, or performance polish is needed.

## Procedure

Follow the numbered/staged steps described above in order. Each step runs autonomously: resolve configuration and current project state first, perform the check or artifact generation described, and record any decision above specialist level in `ops/decision-log.md`. If a step would normally have asked the user a question, instead apply the autonomous decision rule in `docs/automation-modes.md` and proceed, escalating only per `ops/always-ask.yaml`.
