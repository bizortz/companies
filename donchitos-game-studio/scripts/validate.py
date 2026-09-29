#!/usr/bin/env python3
"""
Structural validator for donchitos-game-studio (agentcompanies/v1).

Run from the package root (donchitos-game-studio/) or from anywhere — paths
are resolved relative to this script's location. Exits 0 and prints
"VALIDATION PASSED" only if every check below passes; otherwise prints every
failure found and exits 1. Intended to be re-run after any future edit to
this package, not just during this phase.

Checks (numbered to match the assigning issue's Work Item 11 list):
  1. Every reportsTo target resolves to an existing agent (ceo: null exempt).
  2. Every skill in an agent's frontmatter exists under skills/.
  3. Every SKILL.md / AGENTS.md body is >= 150 words.
  4. No remaining `usage: referenced` anywhere.
  5. No human-in-the-loop gate language in agents/, skills/, docs/.
  6. No reference to a deleted engine agent slug.
  7. No manager has more than 7 direct reports.
  8. Every SKILL.md has a Procedure and an Output section.
  9. Every TEAM.md includes path exists on disk.
  10. Every agent is in ops/model-tiers.yaml and its frontmatter agrees.
  11. Tier counts are exactly 6 / 41 / 2 (Tier 1 / Tier 2 / Tier 3).
  12. No Tier-1-only skill is listed by a non-Tier-1 agent.
  13. No `model:` key remains in any SKILL.md frontmatter.
"""
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML is required: pip install pyyaml\n")
    sys.exit(2)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)

failures = []


def fail(check, msg):
    failures.append(f"[Check {check}] {msg}")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text, path):
    if not text.startswith("---\n"):
        fail("frontmatter", f"{path}: does not start with '---' frontmatter fence")
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("frontmatter", f"{path}: unterminated frontmatter fence")
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5:]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        fail("frontmatter", f"{path}: invalid YAML frontmatter: {e}")
        return {}, body
    return fm, body


def word_count(text):
    return len(re.findall(r"\S+", text))


# ---------------------------------------------------------------------------
# Load all agents
# ---------------------------------------------------------------------------
agent_slugs = sorted(
    d for d in os.listdir("agents")
    if os.path.isdir(os.path.join("agents", d)) and os.path.exists(f"agents/{d}/AGENTS.md")
)
agents = {}
for slug in agent_slugs:
    path = f"agents/{slug}/AGENTS.md"
    fm, body = split_frontmatter(read(path), path)
    agents[slug] = {"fm": fm, "body": body, "path": path}

skill_slugs = sorted(
    d for d in os.listdir("skills")
    if os.path.isdir(os.path.join("skills", d)) and os.path.exists(f"skills/{d}/SKILL.md")
)
skills = {}
for slug in skill_slugs:
    path = f"skills/{slug}/SKILL.md"
    fm, body = split_frontmatter(read(path), path)
    skills[slug] = {"fm": fm, "body": body, "path": path}

# ---------------------------------------------------------------------------
# Check 1: reportsTo resolves
# ---------------------------------------------------------------------------
for slug, a in agents.items():
    rt = a["fm"].get("reportsTo")
    if rt is None:
        if slug != "ceo":
            fail(1, f"{slug}: reportsTo is null but only 'ceo' is allowed to have a null reportsTo")
        continue
    if rt not in agents:
        fail(1, f"{slug}: reportsTo '{rt}' does not resolve to an existing agent")

# ---------------------------------------------------------------------------
# Check 2: skills referenced exist
# ---------------------------------------------------------------------------
for slug, a in agents.items():
    for s in a["fm"].get("skills") or []:
        if s not in skills:
            fail(2, f"{slug}: skills entry '{s}' does not exist under skills/")

# ---------------------------------------------------------------------------
# Check 3: body word counts >= 150
# ---------------------------------------------------------------------------
for slug, a in agents.items():
    n = word_count(a["body"])
    if n < 150:
        fail(3, f"agents/{slug}/AGENTS.md: body is {n} words, below the 150-word minimum")
for slug, s in skills.items():
    n = word_count(s["body"])
    if n < 150:
        fail(3, f"skills/{slug}/SKILL.md: body is {n} words, below the 150-word minimum")

# ---------------------------------------------------------------------------
# Check 4: no `usage: referenced` anywhere
# ---------------------------------------------------------------------------
# PROGRESS.md/DECISIONS.md legitimately describe, in prose, that this
# string no longer appears anywhere live ("zero `usage: referenced`
# remaining") — that is a historical record, not a live occurrence.
# skills/skill-test/SKILL.md legitimately quotes this exact string as part
# of its own Check 1 definition (what to fail on) — self-referential, same
# as this validator's own DELETED_AGENTS list and GATE_RE pattern below.
CHECK4_EXCLUDE = {"./PROGRESS.md", "./DECISIONS.md", "./skills/skill-test/SKILL.md"}
for dirpath, _, filenames in os.walk("."):
    if "/.git" in dirpath or dirpath.startswith("./.git"):
        continue
    for fn in filenames:
        if fn.endswith((".md", ".yaml", ".yml")):
            fp = os.path.join(dirpath, fn)
            if fp in CHECK4_EXCLUDE:
                continue
            try:
                content = read(fp)
            except (UnicodeDecodeError, OSError):
                continue
            if "usage: referenced" in content:
                fail(4, f"{fp}: contains 'usage: referenced'")

# ---------------------------------------------------------------------------
# Check 5: no human-in-the-loop gate language in agents/, skills/, docs/
# ---------------------------------------------------------------------------
GATE_RE = re.compile(r"user (decides|approv)|before any files are written|AskUserQuestion", re.I)
this_script_name = os.path.basename(__file__)
# skills/skill-test/SKILL.md's own Check 4 quotes these exact phrases in
# backticks to define what its structural check fails on (see DECISIONS.md
# #Work Item 2's skill-improve/skill-test note) — this is the check's own
# definition, not an instance of human-gate language governing behavior.
CHECK5_EXCLUDE = {"skills/skill-test/SKILL.md"}
for scandir in ("agents", "skills", "docs"):
    for dirpath, _, filenames in os.walk(scandir):
        for fn in filenames:
            if fn == this_script_name:
                continue
            p = os.path.join(dirpath, fn)
            if p in CHECK5_EXCLUDE:
                continue
            try:
                content = read(p)
            except (UnicodeDecodeError, OSError):
                continue
            for i, line in enumerate(content.splitlines(), 1):
                if GATE_RE.search(line):
                    fail(5, f"{p}:{i}: matches human-gate pattern: {line.strip()[:140]}")

# ---------------------------------------------------------------------------
# Check 6: no reference to deleted engine agents
# ---------------------------------------------------------------------------
DELETED_AGENTS = [
    "unreal-specialist", "ue-blueprint-specialist", "ue-gas-specialist",
    "ue-replication-specialist", "ue-umg-specialist", "godot-specialist",
    "godot-gdscript-specialist", "godot-shader-specialist",
    "godot-gdextension-specialist",
]
# DECISIONS.md and PROGRESS.md legitimately record the removal; exclude those
# two files, and this script itself (which lists the slugs to check for).
EXCLUDE_FILES = {"DECISIONS.md", "PROGRESS.md", this_script_name}
# setup-engine/SKILL.md retains one explanatory sentence naming the removed
# unreal-specialist/ue-*-specialist agents and pointing to DECISIONS.md —
# an intentional, documented exception from Work Item 3 (see PROGRESS.md's
# Phase 1 "Work Item 3" section and DECISIONS.md #6), not a live reference.
EXCLUDE_PATHS = {"./skills/setup-engine/SKILL.md"}
for dirpath, _, filenames in os.walk("."):
    if "/.git" in dirpath or dirpath.startswith("./.git"):
        continue
    for fn in filenames:
        if fn in EXCLUDE_FILES:
            continue
        if not fn.endswith((".md", ".yaml", ".yml")):
            continue
        p = os.path.join(dirpath, fn)
        if p in EXCLUDE_PATHS:
            continue
        try:
            content = read(p)
        except (UnicodeDecodeError, OSError):
            continue
        for slug in DELETED_AGENTS:
            if slug in content:
                fail(6, f"{p}: references deleted engine agent '{slug}'")

# ---------------------------------------------------------------------------
# Check 7: max 7 direct reports per manager
# ---------------------------------------------------------------------------
report_counts = {}
for slug, a in agents.items():
    rt = a["fm"].get("reportsTo")
    if rt:
        report_counts[rt] = report_counts.get(rt, 0) + 1
for mgr, n in report_counts.items():
    if n > 7:
        fail(7, f"{mgr}: has {n} direct reports, exceeding the max of 7")

# ---------------------------------------------------------------------------
# Check 8: SKILL.md Procedure + Output sections
# ---------------------------------------------------------------------------
for slug, s in skills.items():
    if not re.search(r"^##\s+Procedure\s*$", s["body"], re.M):
        fail(8, f"skills/{slug}/SKILL.md: missing '## Procedure' section")
    if not re.search(r"^##\s+Output\s*$", s["body"], re.M):
        fail(8, f"skills/{slug}/SKILL.md: missing '## Output' section")

# ---------------------------------------------------------------------------
# Check 9: TEAM.md includes paths exist
# ---------------------------------------------------------------------------
team_dirs = sorted(
    d for d in os.listdir("teams")
    if os.path.isdir(os.path.join("teams", d)) and os.path.exists(f"teams/{d}/TEAM.md")
)
for slug in team_dirs:
    path = f"teams/{slug}/TEAM.md"
    fm, _ = split_frontmatter(read(path), path)
    mgr = fm.get("manager")
    if mgr and not os.path.exists(os.path.normpath(os.path.join("teams", slug, mgr))):
        fail(9, f"{path}: manager path '{mgr}' does not exist")
    for inc in fm.get("includes") or []:
        target = os.path.normpath(os.path.join("teams", slug, inc))
        if not os.path.exists(target):
            fail(9, f"{path}: includes path '{inc}' does not exist")

# ---------------------------------------------------------------------------
# Checks 10 & 11: model-tiers.yaml consistency + tier counts
# ---------------------------------------------------------------------------
tiers_yaml_path = "ops/model-tiers.yaml"
tier_map = {}
if not os.path.exists(tiers_yaml_path):
    fail(10, f"{tiers_yaml_path} does not exist")
else:
    tiers_doc = yaml.safe_load(read(tiers_yaml_path)) or {}
    tier_map = tiers_doc.get("tiers") or {}
    for slug in agent_slugs:
        if slug not in tier_map:
            fail(10, f"{slug}: missing from {tiers_yaml_path}")
            continue
        expected = tier_map[slug]
        fm = agents[slug]["fm"]
        meta = fm.get("metadata") or {}
        actual_tier = meta.get("modelTier")
        actual_model = meta.get("model")
        actual_effort = meta.get("effort")
        if actual_tier != expected.get("tier"):
            fail(10, f"{slug}: frontmatter modelTier={actual_tier!r} disagrees with {tiers_yaml_path} tier={expected.get('tier')!r}")
        if actual_model != expected.get("model"):
            fail(10, f"{slug}: frontmatter model={actual_model!r} disagrees with {tiers_yaml_path} model={expected.get('model')!r}")
        if actual_effort != expected.get("effort"):
            fail(10, f"{slug}: frontmatter effort={actual_effort!r} disagrees with {tiers_yaml_path} effort={expected.get('effort')!r}")
    for slug in tier_map:
        if slug not in agents:
            fail(10, f"{tiers_yaml_path}: lists '{slug}' which is not an agent on disk")

    tier_counts = {1: 0, 2: 0, 3: 0}
    for slug, entry in tier_map.items():
        t = entry.get("tier")
        if t in tier_counts:
            tier_counts[t] += 1
    expected_counts = {1: 6, 2: 41, 3: 2}
    if tier_counts != expected_counts:
        fail(11, f"tier counts are {tier_counts}, expected {expected_counts} (total {sum(tier_counts.values())})")

# ---------------------------------------------------------------------------
# Check 12: Tier-1-only skills not listed by non-Tier-1 agents
# ---------------------------------------------------------------------------
TIER1_SKILLS = {"gate-check", "milestone-review", "portfolio-review", "improvement-cycle"}
for slug, a in agents.items():
    tier = (a["fm"].get("metadata") or {}).get("modelTier")
    agent_skills = set(a["fm"].get("skills") or [])
    bad = agent_skills & TIER1_SKILLS
    if bad and tier != 1:
        fail(12, f"{slug} (tier {tier}): lists Tier-1-only skill(s) {sorted(bad)} in its skills: frontmatter")

# ---------------------------------------------------------------------------
# Check 13: no `model:` key in any SKILL.md frontmatter
# ---------------------------------------------------------------------------
for slug, s in skills.items():
    if "model" in s["fm"]:
        fail(13, f"skills/{slug}/SKILL.md: frontmatter still declares a 'model:' key")

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
if failures:
    print(f"VALIDATION FAILED — {len(failures)} failure(s):\n")
    for f in failures:
        print(f" - {f}")
    sys.exit(1)
else:
    print(f"VALIDATION PASSED — {len(agent_slugs)} agents, {len(skill_slugs)} skills, "
          f"{len(team_dirs)} teams checked, 0 failures across all 13 checks.")
    sys.exit(0)
