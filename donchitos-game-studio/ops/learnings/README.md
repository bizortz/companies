# ops/learnings/

This directory holds structured evidence entries written by any skill's
evidence-capture step — currently `retrospective`, `playtest-report`,
`kpi-review`, `bug-triage`, and `gate-check` (see each SKILL.md's Procedure
for the exact step), and by `incident-response`. It is the raw input to the
`improvement-cycle` skill (owner: `org-improvement-lead`), which clusters
these entries and ranks them by metric impact x frequency to decide what to
propose changing next.

## File naming

`ops/learnings/<date>-<source>.md`, one file per skill run that produced at
least one finding (e.g. `ops/learnings/2026-10-03-kpi-review.md`). A single
skill run may contain multiple findings in one file.

## Required fields per finding

Each finding is a single entry with exactly these fields:

```markdown
### <short finding title>

- **finding:** <what was observed, stated as a fact, not a fix>
- **affected agent/skill:** <the agent or skill whose output/process this reflects on>
- **evidence:** <file paths / report references that support this finding>
- **metric affected:** <id from ops/metrics-registry.yaml, or "none — qualitative">
- **severity:** S1 | S2 | S3 | S4 (same scale as bug-triage's severity definitions)
```

## What this directory is not

- It is not a place to write fixes or proposals — those go in
  `ops/improvements/<id>.md`, written by `improvement-cycle` after clustering.
- It is not editable by `improvement-cycle` or `org-improvement-lead` except
  to append new entries as a byproduct of running a skill's own evidence-
  capture step — the improvement loop reads this directory, it does not
  curate or delete from it.
- Entries are never deleted. A superseded finding is closed by a new entry
  referencing it, not by editing the old one.
