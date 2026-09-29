---
name: bug-report
description: Structured bug report from a description, or analyze code for potential
  bugs. Reproduction steps, severity.
metadata:
  sources:
  - kind: github-file
    repo: Donchitos/Claude-Code-Game-Studios
    path: .claude/skills/bug-report/SKILL.md
    commit: 7ed2c3e9c46c880c9780fbce49266e7edfa15141
    attribution: Donchitos
    license: MIT
    usage: adapted
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
**Automation mode**: Resolve `modes.automation` (`project.local.yaml` →
`project.yaml` → default `collaborative`). This skill runs autonomously. Every decision it would previously have surfaced as a question is made by the owning agent and logged to `ops/decision-log.md`, per the operating rules in `docs/automation-modes.md` (the studio default mode is `autonomous`). The only exceptions are the fixed human gates listed in `ops/always-ask.yaml`, which always pause for explicit sign-off.

## Phase 1: Parse Arguments

Determine the mode from the argument:

- No keyword → **Description Mode**: generate a structured bug report from the provided description
- `analyze [path]` → **Analyze Mode**: read the target file(s) and identify potential bugs
- `verify [BUG-ID]` → **Verify Mode**: confirm a reported fix actually resolved the bug
- `close [BUG-ID]` → **Close Mode**: mark a verified bug as closed with resolution record

If no argument is provided, If not already specified in project files, decide autonomously (using the most reasonable default given current project state) for a bug description before proceeding, and record the assumption in `ops/decision-log.md`.

---

## Phase 2A: Description Mode

1. **Parse the description** for key information: what broke, when, how to reproduce it, and what the expected behavior is.

2. **Search the codebase** for related files using Grep/Glob to add context (affected system, likely files).

3. **Draft the bug report**:

```markdown
# Bug Report

## Summary
**Title**: [Concise, descriptive title]
**ID**: BUG-[NNNN]
**Severity**: [S1-Critical / S2-Major / S3-Minor / S4-Trivial]
**Priority**: [P1-Fix this sprint / P2-Fix soon / P3-Backlog / P4-Won't fix]

> **These labels must match `/bug-triage`'s priority table exactly** — it parses
> this field out of the file you are writing. P4 is the easiest to get wrong:
> `P4-Wishlist` ("would be nice someday") and `P4 — Won't fix / Deferred`
> ("accepted risk, not doing it") mean opposite things, and nothing at runtime
> surfaces a disagreement between the producer and consumer of the field. If you change this ladder, change
> `skills/bug-triage/SKILL.md` in the same commit.
**Status**: Open
**Reported**: [Date]
**Reporter**: [Name]

## Classification
- **Category**: [Gameplay / UI / Audio / Visual / Performance / Crash / Network]
- **System**: [Which game system is affected]
- **Frequency**: [Always / Often (>50%) / Sometimes (10-50%) / Rare (<10%)]
- **Regression**: [Yes/No/Unknown -- was this working before?]

## Environment
- **Build**: [Version or commit hash]
- **Platform**: [OS, hardware if relevant]
- **Scene/Level**: [Where in the game]
- **Game State**: [Relevant state -- inventory, quest progress, etc.]

## Reproduction Steps
**Preconditions**: [Required state before starting]

1. [Exact step 1]
2. [Exact step 2]
3. [Exact step 3]

**Expected Result**: [What should happen]
**Actual Result**: [What actually happens]

## Technical Context
- **Likely affected files**: [List of files based on codebase search]
- **Related systems**: [What other systems might be involved]
- **Possible root cause**: [If identifiable from the description]

## Evidence
- **Logs**: [Relevant log output if available]
- **Visual**: [Description of visual evidence]

## Related Issues
- [Links to related bugs or design documents]

## Notes
[Any additional context or observations]
```

---

## Phase 2B: Analyze Mode

1. **Read the target file(s)** specified in the argument.

2. **Identify potential bugs**: null references, off-by-one errors, race conditions, unhandled edge cases, resource leaks, incorrect state transitions.

3. **For each potential bug**, generate a bug report using the template above, with the likely trigger scenario and recommended fix filled in.

---

## Phase 2C: Verify Mode

Read `production/qa/bugs/[BUG-ID].md`. Extract the reproduction steps and expected result.

1. **Re-run reproduction steps** — use Grep/Glob to check whether the root cause code path still exists as described. If the fix removed or changed it, note the change.
2. **Run the related test** — if the bug's system has a test file in `tests/`, run it via Bash and report pass/fail.
3. **Check for regression** — grep the codebase for any new occurrence of the pattern that caused the bug.

Produce a verification verdict:

- **VERIFIED FIXED** — reproduction steps no longer produce the bug; related tests pass
- **STILL PRESENT** — bug reproduces as described; fix did not resolve the issue
- **CANNOT VERIFY** — automated checks inconclusive; manual playtest required

Ask: "May I update `production/qa/bugs/[BUG-ID].md` to set Status: Verified Fixed / Still Present / Cannot Verify?"

If STILL PRESENT: reopen the bug, set Status back to Open, and suggest re-running `/hotfix [BUG-ID]`.

---

## Phase 2D: Close Mode

Read `production/qa/bugs/[BUG-ID].md`. Confirm Status is `Verified Fixed` before closing. If status is anything else, stop: "Bug [ID] must be Verified Fixed before it can be closed. Run `/bug-report verify [BUG-ID]` first."

Append a closure record to the bug file:

```markdown
## Closure Record
**Closed**: [date]
**Resolution**: Fixed — [one-line description of what was changed]
**Fix commit / PR**: [if known]
**Verified by**: qa-tester
**Closed by**: [user]
**Regression test**: [test file path, or "Manual verification"]
**Status**: Closed
```

Update the top-level `**Status**: Open` field to `**Status**: Closed`.

Ask: "May I update `production/qa/bugs/[BUG-ID].md` to mark it Closed?"

After closing, check `production/qa/bug-triage-*.md` — if the bug appears in an open triage report, note: "Bug [ID] is referenced in the triage report. Run `/bug-triage` to refresh the open bug count."

---

## Phase 3: Save Report

Present the completed bug report(s) to the user.

Write directly to `production/qa/bugs/BUG-[NNNN].md` and log the write to `ops/decision-log.md`.

If yes, write the file, creating the directory if needed. Verdict: **COMPLETE** — bug report filed.

If no, stop here. 

---

## Phase 4: Next Steps

After saving, suggest based on mode:

**After filing (Description/Analyze mode):**
- Run `/bug-triage` to prioritize alongside existing open bugs
- If S1 or S2: run `/hotfix [BUG-ID]` for emergency fix workflow

**After fixing the bug (developer confirms fix is in):**
- Run `/bug-report verify [BUG-ID]` — confirm the fix actually works before closing
- Never mark a bug closed without verification — a fix that doesn't verify is still Open

**After verify returns VERIFIED FIXED:**
- Run `/bug-report close [BUG-ID]` — write the closure record and update status
- Run `/bug-triage` to refresh the open bug count and remove it from the active list

## Procedure

Follow the numbered/staged steps described above in order. Each step runs autonomously: resolve configuration and current project state first, perform the check or artifact generation described, and record any decision above specialist level in `ops/decision-log.md`. If a step would normally have asked the user a question, instead apply the autonomous decision rule in `docs/automation-modes.md` and proceed, escalating only per `ops/always-ask.yaml`.

## Output

Produce the artifact(s) described above (report, verdict, updated project file, or log entry) and write them to the appropriate location in the project (e.g. `production/`, `docs/`, or the relevant tracked file). Summarize the result back to the calling agent/team in a short status block, and append a decision-log entry if the output changed project state or direction.
