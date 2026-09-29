# Improvement Ledger

Every experiment run by the `improvement-cycle` skill (owner: `org-improvement-lead`)
is logged here, in full, whether it is kept or reverted. This is the
permanent audit trail of the self-improvement loop — an entry is never
deleted, only appended to (a reverted experiment gets a closing entry, not a
removed one).

Schema per entry:

```markdown
## <id> — <date opened>

- **Target file:** <AGENTS.md or SKILL.md path>
- **Cluster:** <link/reference to the ops/learnings/ entries this experiment addresses>
- **Proposal:** ops/improvements/<id>.md
- **Hypothesis:**
- **Target metric(s)** (per ops/metrics-registry.yaml id):
- **Baseline value(s):** <value, date, sample size>
- **Evaluation window:** <N sprints | N days>
- **Rollback condition:**
- **skill-test static result (pre-apply):** PASS | FAIL (no regression required to proceed)
- **Applied:** <date, branch or versioned-copy reference>
- **Outcome (filled at end of window):**
  - Final metric value(s) vs baseline:
  - Guardrail metrics checked (no regression beyond tolerance):
  - **Decision:** KEEP | REVERT
  - **Rationale:**
- **Status:** OPEN | KEPT | REVERTED
```

## Concurrency limits (enforced by improvement-cycle)

- At most **one active experiment per target file** at any time.
- At most **3 concurrent experiments company-wide** at any time.

## Entries

_No entries yet — this ledger is seeded empty. The first entry is created the
first time `improvement-cycle` runs at a sprint end with enough `ops/learnings/`
volume to cluster and rank a top-3._
