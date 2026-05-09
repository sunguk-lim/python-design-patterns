#!/usr/bin/env bash
# Auto-start the FastAPI webapp inside the codespace.
# Called from devcontainer.json postStartCommand on every container start.

WEBAPP=/workspaces/python-design-patterns/webapp
LOG=/tmp/uvicorn.log

# DEBUG: Prove the script ran. Marker file fetchable via the
# debug HTTP server below.
date '+%Y-%m-%d %H:%M:%S' > /tmp/poststart.marker
{
  echo "===== $(date) ====="
  echo "[start-server] script invoked"
  echo "[start-server] cwd=$(pwd) user=$(whoami) home=$HOME PATH=$PATH"
  echo "[start-server] webapp dir contents:"
  ls -la "$WEBAPP" 2>&1 || true
  echo "[start-server] .venv check:"
  ls -la "$WEBAPP/.venv/bin/uvicorn" 2>&1 || true
} >> "$LOG"

# DEBUG HTTP server on port 9999 serving /tmp so we can fetch logs
# from outside via `gh codespace ports forward 9999:19999` (no SSH needed).
# Launched BEFORE `set -e` so it always runs even if later steps fail.
if ! pgrep -f 'http.server 9999' >/dev/null; then
  nohup python3 -m http.server 9999 --directory /tmp >>/tmp/dbg.log 2>&1 &
  disown
  echo "[start-server] debug http server launched on :9999" >> "$LOG"
fi

set -euo pipefail
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
