#!/usr/bin/env bash
# Structural validator entry point for donchitos-game-studio.
# The actual checks are implemented in validate.py (13 checks — see its
# module docstring); this wrapper just resolves python3 and forwards exit
# status so `./scripts/validate.sh` works from any working directory.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "${SCRIPT_DIR}/validate.py" "$@"
