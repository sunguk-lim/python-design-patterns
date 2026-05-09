# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational repository teaching 25 design patterns in Python (GoF + 3 bonus architectural patterns). Includes an interactive web app for browsing and running the examples.

## Repository Structure

- **`01_strategy/` through `25_event_sourcing/`** — Each numbered folder is one pattern lesson containing:
  - `bad_example.py` — demonstrates the problem (anti-pattern)
  - `<pattern_name>.py` — clean solution using the pattern
  - `HANDOUT.md` — summary with diagrams and key takeaways
- **`webapp/`** — FastAPI web app for interactive browsing/running of pattern examples
- **`SYLLABUS.md`** — Course outline with pattern categories and completion status
- **`TEXTBOOK.md` / `TEXTBOOK.pdf`** — Full textbook covering all 25 patterns

### Pattern Categories

| Range  | Category    | Description                    |
|--------|-------------|--------------------------------|
| 01–10  | Behavioral  | How objects communicate         |
| 11–15  | Creational  | How objects are created          |
| 16–22  | Structural  | How objects are composed         |
| 23–25  | Beyond GoF  | Repository, DI, Event Sourcing   |

## Running Examples

```bash
# Run any pattern example directly
python 01_strategy/strategy.py
python 01_strategy/bad_example.py

# Run the web app (from webapp/ directory, uses .venv)
cd webapp && source .venv/bin/activate
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## Web App Architecture

- **`webapp/app.py`** — FastAPI app that auto-discovers pattern folders via glob, renders HANDOUT.md as HTML (using `markdown` lib), syntax-highlights Python files (using `pygments`), and serves a code execution API.
- **`webapp/sandbox.py`** — Sandboxed subprocess executor for user code. Blocks dangerous modules, sets resource limits (256MB RAM, 10s CPU), and runs in a restricted environment.
- **`webapp/templates/`** — Jinja2 templates (`base.html`, `index.html`, `pattern.html`).
- **Dependencies**: FastAPI, Uvicorn, Jinja2, Markdown, Pygments, Pydantic (installed in `webapp/.venv`).

## Pattern File Conventions

- Each pattern file starts with a docstring block explaining: category, intent, real-world analogy, and when to use.
- Examples use `if __name__ == "__main__":` blocks with demo output and key takeaways.
- Patterns use `abc.ABC` / `@abstractmethod` for interfaces.
- All examples are self-contained single files with no cross-pattern dependencies.
