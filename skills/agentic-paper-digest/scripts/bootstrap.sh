#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="${PROJECT_DIR:-$HOME/agentic_paper_digest}"
REPO_URL="https://github.com/matanle51/agentic_paper_digest"

# Clone or update
if [ -d "$PROJECT_DIR/.git" ]; then
  echo ">> Updating repo in $PROJECT_DIR"
  git -C "$PROJECT_DIR" pull --ff-only
else
  echo ">> Cloning repo into $PROJECT_DIR"
  git clone "$REPO_URL" "$PROJECT_DIR"
fi

cd "$PROJECT_DIR"

# Use uv for dependency management (Tommy's standard)
if ! command -v uv >/dev/null 2>&1; then
  echo "Error: uv not found. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
  exit 1
fi

if [ ! -d ".venv" ]; then
  echo ">> Creating virtualenv with uv"
  uv venv
fi

echo ">> Installing Python deps with uv"
if [ -f "pyproject.toml" ]; then
  uv sync
elif [ -f "requirements.txt" ]; then
  uv pip install -r requirements.txt
else
  echo "Error: No pyproject.toml or requirements.txt found"
  exit 1
fi

if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  cp .env.example .env
  echo ">> Created .env from .env.example"
fi

echo ">> Done. Edit .env, then run scripts/run_cli.sh"
