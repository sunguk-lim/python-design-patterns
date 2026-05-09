#!/usr/bin/env bash
# Auto-start the FastAPI webapp inside the codespace.
# Called from devcontainer.json postStartCommand on every container start.
set -euo pipefail

WEBAPP=/workspaces/python-design-patterns/webapp
LOG=/tmp/uvicorn.log

cd "$WEBAPP"

# Self-heal: if deps weren't installed (postCreate failed silently),
# install uv and re-sync the venv from uv.lock before launching.
if [ ! -x .venv/bin/uvicorn ]; then
  echo "[start-server] .venv/bin/uvicorn missing — running uv sync" >> "$LOG"
  pip install --user uv
  export PATH="$HOME/.local/bin:$PATH"
  uv sync
fi

# Don't start a second instance if one is already running.
if pgrep -f 'uvicorn app:app' >/dev/null; then
  echo "[start-server] uvicorn already running, skipping" >> "$LOG"
  exit 0
fi

# Launch uvicorn fully detached so it outlives this shell.
# nohup → ignore SIGHUP; & → background; disown → drop from job table;
# stdout/stderr → log file we can inspect later via `gh codespace cp`.
nohup .venv/bin/uvicorn app:app \
  --host 0.0.0.0 --port 8000 \
  >> "$LOG" 2>&1 &
disown

echo "[start-server] launched uvicorn (pid $!)" >> "$LOG"
