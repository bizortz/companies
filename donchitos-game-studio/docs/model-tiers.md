# Model Tier Assignment

This document is the human-readable description of the studio's model-tier
system. The machine-readable single source of truth is
`ops/model-tiers.yaml`, which every agent's `AGENTS.md`
`metadata.modelTier`/`metadata.model`/`metadata.effort` frontmatter fields
must agree with exactly — `scripts/validate.sh` enforces this.

This replaces the Phase 1 upstream-inherited version of this file entirely.
Phase 1's version declared tiers **per skill** (`model:` in `SKILL.md`
frontmatter) and noted that Claude Code did not actually honor that
mechanism. This package now assigns tiers **per agent only** — a skill runs
on the model of the agent invoking it, never its own declared model. Every
`model:` frontmatter key has been stripped from every `SKILL.md` file (see
`DECISIONS.md`).

## Tier Definitions

| Tier | Model | Effort | Role |
|---|---|---|---|
| 1 | `claude-opus-5-5` | high | Decides only. Reads summaries, rules on options, issues verdicts. Produces no drafts, code, assets, or specs. |
| 2 | `claude-sonnet-5` | low | Thinking work: design, code, creative, analysis, problem solving, department-level review. |
| 3 | `claude-haiku-4-5-20251001` | auto (no effort param; runtime default) | High-volume, repetitive, rule-following work with fixed templates. |

## Behavioral Contracts

- **Tier 1** must NOT draft artifacts or perform execution work. Input is
  summaries of one page or less, prepared by Tier 2 reports. Output is a
  decision in the fixed template only. Delegates everything else.
- **Tier 2** owns execution in its domain. Escalates to its Tier 1 manager
  only decisions that are cross-domain, irreversible, or listed in
  `ops/always-ask.yaml`. Delegates mechanical volume to a Tier 3 agent where
  one exists.
- **Tier 3** follows the skill procedure exactly, uses output templates
  verbatim, makes no judgment calls. Anything ambiguous or outside the
  template escalates to its manager.

## Assignment (49 agents)

**Tier 1 (6):** `ceo`, `creative-director`, `technical-director`, `producer`,
`publishing-director`, `org-improvement-lead`.

**Tier 3 (2):** `qa-tester`, `player-support`.

**Tier 2 (41):** every other agent — the full breakdown lives in
`ops/model-tiers.yaml` and is reflected into every agent's own `AGENTS.md`
`## Model Tier` section, not maintained by hand in two places.

## Pre-Decision Summary Pairings

Before a Tier 1 agent issues a verdict, a named Tier 2 agent prepares the
summary that verdict is based on:

- `producer` ← `qa-lead` & `lead-programmer`
- `creative-director` ← `game-designer`
- `technical-director` ← `lead-programmer`
- `publishing-director` ← `market-analyst` & `analytics-engineer`
- `ceo` ← `finance-controller` & the four directors (`creative-director`,
  `technical-director`, `producer`, `publishing-director`)
- `org-improvement-lead` ← `analytics-engineer`

These pairings are also stated in the relevant agents' own `AGENTS.md`
bodies.

## Tier 1 Skills Are Tier-1-Only

`gate-check`, `milestone-review`, `portfolio-review`, and `improvement-cycle`
are decision-verdict skills and may only be invoked by Tier 1 agents. No
Tier 2 or Tier 3 agent lists any of these four in its `skills:` frontmatter;
a Tier 2 agent that needs one of these verdicts requests it from its Tier 1
manager instead of running the skill itself.

## Enforcement

This is a prompt-driven package with no runtime permission mechanism, so
tiering is enforced the same way every other guardrail here is: stated
explicitly in this file, in `ops/model-tiers.yaml`, in every agent's own
`## Model Tier` section, and checked structurally by `scripts/validate.sh`.
Runtime application of `metadata.model`/`metadata.effort` is the
responsibility of whatever system imports this package (see
`MODIFICATION_REPORT.md`'s "Known gaps" section) — these fields are
declarative intent, not a guarantee the import target actually runs the
named model.

## Changing a Tier

Only the CEO decides to change an agent's tier, logged to
`ops/decision-log.md`. `org-improvement-lead` may propose a tier change as
part of an improvement-cycle finding but must never self-apply one — see
its `AGENTS.md` Must-NOT list.
