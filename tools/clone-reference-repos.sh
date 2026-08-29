#!/bin/bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
DEST="$ROOT/evidence/source-repos"

mkdir -p "$DEST"

echo "This script intentionally clones only repositories explicitly listed"
echo "below. Do not turn ANARCHY into an indiscriminate mirror."

# Add verified repositories here as research progresses.
#
# Example:
# git clone --filter=blob:none https://github.com/example/project.git "$DEST/project"

echo "No additional repositories configured."
