---
name: Set Device Performance Budget
assignee: performance-analyst
project: new-game-kickoff
---

Run the `device-perf-budget` skill during Pre-Production, alongside
`select-engine` and `decompose-systems`, to set per-device-tier FPS, memory,
build-size, and load-time targets before any production art or engineering
work commits to a specific fidelity level. This budget is a required input
to `build-prototype` (the prototype should be built and measured against
these targets, not against an assumed high-end device) and to every
subsequent art/engineering decision in production.

## Deliverables
- `design/perf-budget.md` with per-tier FPS, memory, build size, and load
  time targets, and a stated basis for each (or a flag that it is
  provisional pending real device testing)

## Next Task
`build-prototype` (perf budget is consumed by the prototype build and its
findings report)
