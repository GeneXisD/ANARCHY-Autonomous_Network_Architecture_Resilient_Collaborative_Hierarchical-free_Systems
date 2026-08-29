#!/bin/bash
set -euo pipefail

echo "=== ANARCHY verification ==="
echo

echo "Git root:"
git rev-parse --show-toplevel

echo
echo "Branch:"
git branch --show-current

echo
echo "Status:"
git status --short

echo
echo "Research directories:"
find research -maxdepth 2 -type d | sort

echo
echo "Files:"
find . -type f ! -path './.git/*' | sort

echo
echo "Recent commits:"
git log --oneline --decorate -5
