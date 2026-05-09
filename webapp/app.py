"""
Design Patterns Interactive Web App
"""

from pathlib import Path

import markdown
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

from exercise import generate_exercise_stub
from sandbox import execute_code

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
WEBAPP_DIR = Path(__file__).resolve().parent

CATEGORIES = {
    range(1, 11): ("Behavioral", "How objects communicate"),
    range(11, 16): ("Creational", "How objects are created"),
    range(16, 23): ("Structural", "How objects are composed"),
    range(23, 26): ("Beyond GoF", "Patterns beyond the Gang of Four"),
}

# ---------------------------------------------------------------------------
# Pattern discovery
# ---------------------------------------------------------------------------

def _category_for(num: int) -> tuple[str, str]:
    for rng, cat in CATEGORIES.items():
        if num in rng:
            return cat
    return ("Other", "")


def _discover_patterns() -> list[dict]:
    patterns = []
    for d in sorted(REPO_ROOT.glob("[0-9][0-9]_*")):
        if not d.is_dir():
            continue
        num_str = d.name[:2]
        num = int(num_str)
        slug = d.name
        name = " ".join(w.capitalize() for w in d.name[3:].split("_"))
        category, category_desc = _category_for(num)

        # Find the "good" python file (not bad_example.py)
        py_files = [f for f in d.glob("*.py") if f.name != "bad_example.py"]
        good_file = py_files[0].name if py_files else None
        bad_file = "bad_example.py" if (d / "bad_example.py").exists() else None
        handout = "HANDOUT.md" if (d / "HANDOUT.md").exists() else None

        patterns.append({
            "number": num_str,
            "num": num,
            "slug": slug,
            "name": name,
            "category": category,
            "category_desc": category_desc,
            "dir": d,
            "good_file": good_file,
            "bad_file": bad_file,
            "handout": handout,
        })
    return patterns


PATTERNS = _discover_patterns()
PATTERN_MAP = {p["slug"]: p for p in PATTERNS}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
_md = markdown.Markdown(extensions=["fenced_code", "tables", "codehilite", "toc"],
                        extension_configs={"codehilite": {"guess_lang": False}})
_py_lexer = PythonLexer()
_html_formatter = HtmlFormatter(linenos=True, cssclass="source", style="monokai")
PYGMENTS_CSS = _html_formatter.get_style_defs(".source")


def render_handout(pattern: dict) -> str:
    path = pattern["dir"] / pattern["handout"]
    _md.reset()
    return _md.convert(path.read_text(encoding="utf-8"))


def highlight_python(pattern: dict, which: str = "good") -> str:
    fname = pattern["good_file"] if which == "good" else pattern["bad_file"]
    if not fname:
        return "<p>File not available.</p>"
    path = pattern["dir"] / fname
    code = path.read_text(encoding="utf-8")
    return highlight(code, _py_lexer, _html_formatter)


def get_source(pattern: dict, which: str = "good") -> str:
    fname = pattern["good_file"] if which == "good" else pattern["bad_file"]
    if not fname:
        return ""
    return (pattern["dir"] / fname).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------
app = FastAPI(title="Design Patterns in Python")
app.mount("/static", StaticFiles(directory=WEBAPP_DIR / "static"), name="static")
templates = Jinja2Templates(directory=WEBAPP_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    grouped: dict[str, list] = {}
    for p in PATTERNS:
        grouped.setdefault(p["category"], []).append(p)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "grouped": grouped,
        "patterns": PATTERNS,
        "pygments_css": PYGMENTS_CSS,
    })


@app.get("/pattern/{slug}", response_class=HTMLResponse)
async def pattern_page(request: Request, slug: str):
    p = PATTERN_MAP.get(slug)
    if not p:
        return HTMLResponse("<h1>Pattern not found</h1>", status_code=404)

    idx = next(i for i, pp in enumerate(PATTERNS) if pp["slug"] == slug)
    prev_pattern = PATTERNS[idx - 1] if idx > 0 else None
    next_pattern = PATTERNS[idx + 1] if idx < len(PATTERNS) - 1 else None

    return templates.TemplateResponse("pattern.html", {
        "request": request,
        "pattern": p,
        "handout_html": render_handout(p),
        "good_html": highlight_python(p, "good"),
        "bad_html": highlight_python(p, "bad"),
        "good_source": get_source(p, "good"),
        "bad_source": get_source(p, "bad"),
        "prev": prev_pattern,
        "next": next_pattern,
        "patterns": PATTERNS,
        "pygments_css": PYGMENTS_CSS,
    })


class RunRequest(BaseModel):
    code: str


@app.post("/api/run")
async def run_code(req: RunRequest):
    result = execute_code(req.code, timeout=10)
    return JSONResponse(result)


@app.get("/api/source/{slug}/{which}")
async def source(slug: str, which: str):
    p = PATTERN_MAP.get(slug)
    if not p:
        return JSONResponse({"error": "not found"}, status_code=404)
    return JSONResponse({"source": get_source(p, which)})


@app.get("/api/exercise/{slug}")
async def exercise_stub(slug: str):
    p = PATTERN_MAP.get(slug)
    if not p:
        return JSONResponse({"error": "not found"}, status_code=404)
    good_source = get_source(p, "good")
    if not good_source:
        return JSONResponse({"error": "source not available"}, status_code=404)
    stub = generate_exercise_stub(good_source)
    return JSONResponse({"source": stub})


class VerifyRequest(BaseModel):
    code: str
    slug: str


@app.post("/api/verify")
async def verify_code(req: VerifyRequest):
    p = PATTERN_MAP.get(req.slug)
    if not p:
        return JSONResponse({"error": "not found"}, status_code=404)

    good_source = get_source(p, "good")
    if not good_source:
        return JSONResponse({"error": "source not available"}, status_code=404)

    # Run both in parallel-ish (sequential here, but fast)
    expected = execute_code(good_source, timeout=10)
    actual = execute_code(req.code, timeout=10)

    # Normalize for comparison: strip trailing whitespace per line, strip trailing newlines
    def normalize(text: str) -> str:
        return "\n".join(line.rstrip() for line in text.strip().splitlines())

    match = normalize(actual["stdout"]) == normalize(expected["stdout"])

    return JSONResponse({
        "match": match,
        "actual_stdout": actual["stdout"],
        "actual_stderr": actual["stderr"],
        "actual_returncode": actual["returncode"],
        "actual_timed_out": actual["timed_out"],
        "expected_stdout": expected["stdout"],
    })


def main():
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
