---
name: concept-validation
description: Fake-door or CPI test plan and result for a new concept, before Concept
  Lock. Cheap external signal ahead of production spend.
metadata:
  sources:
  - kind: original
    usage: original
    authored_for: donchitos-game-studio
    phase: 3
---

*(Autonomous step: resolve the relevant configuration/state described below before proceeding — no interactive prompt is required; use current project files and `docs/config-resolution.md` as the source of defaults.)*
This skill runs autonomously; decisions are made by `market-analyst` and logged to `ops/decision-log.md` per `docs/automation-modes.md`, except the fixed gates in `ops/always-ask.yaml` (note: any real-money ad spend used to run a CPI test is itself subject to the `real_money_spend` always-ask gate if it would exceed `ops/targets.yaml`/`ops/always-ask.yaml`'s `spend_limit_usd`).

# Concept Validation

## Purpose

Get cheap, real, external signal on whether a proposed game concept has an audience before the studio commits production budget to it. This runs before Concept Lock in `projects/new-game-kickoff`, between concept pitch and pillar-definition, so a concept that fails validation is killed or reshaped before any art, code, or design-doc investment.

## Trigger / Owner Agent

Owner: `market-analyst`. Triggered by `creative-director` or `publishing-director` whenever a new concept is proposed, before `new-game-kickoff`'s "Define Game Pillars" task begins.

## Inputs

- The concept pitch (genre, core mechanic, core fantasy, target audience) from `creative-director`.
- Latest relevant `market-scan` output, if one exists for this genre.
- `ops/targets.yaml` and `ops/always-ask.yaml` for spend limits, if a paid CPI test is chosen.

## Procedure

1. Choose the test type based on what's fastest and cheapest to get a real signal: **fake-door test** (a landing page, store-listing mock, or ad creative describing the concept, measuring click-through / pre-register / wishlist rate with no real product behind it) or **CPI test** (a small paid-traffic test — install ads pointed at a minimal build or prototype — measuring actual install cost and early engagement). Default to fake-door first; escalate to CPI only if fake-door signal is ambiguous and the CEO/publishing-director agrees the concept is worth the spend.
2. Define the test's hypothesis and pass/fail thresholds *before* running it (e.g., "click-through rate above X in this test's control group means proceed" — set thresholds from comparable prior tests or `ops/targets.yaml`, never a number invented on the spot; if no comparable exists, state that the threshold is provisional and will be recalibrated after the first few tests).
3. If the test requires real-money ad spend, check the amount against `spend_limit_usd` in `ops/always-ask.yaml` before proceeding; if it would exceed the limit, stop and route to the human gate.
4. Run the test for a defined, short duration (days, not weeks) sufficient to reach the sample size needed for statistical relevance given expected traffic.
5. Record the result against the pre-set thresholds and write the verdict.
6. Log the decision and result to `ops/decision-log.md`.

## Output

Write to `ops/reports/validation/<date>-<concept-slug>.md`:

```markdown
# Concept Validation — <concept name>

**Test type:** fake-door | CPI
**Hypothesis:** <stated before the test>
**Pass threshold:** <stated before the test, with source>
**Duration / sample:** <dates, traffic volume>
**Result:** <measured metric vs threshold>
**Verdict:** PROCEED | RESHAPE | KILL
**Rationale:** <why>
```

## Pass/Fail Criteria

Pass: threshold was set before the result was known; result is measured, not estimated; verdict is unambiguous. Fail: post-hoc threshold-setting, or a verdict issued without a completed test.

## Handoff

PROCEED hands off to `new-game-kickoff`'s "Define Game Pillars" task with the validated concept and evidence attached. RESHAPE returns to `creative-director` with specific feedback on what to change. KILL is logged and the concept is closed out.
