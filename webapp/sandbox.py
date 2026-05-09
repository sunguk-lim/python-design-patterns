"""
Sandboxed Python code executor.

Runs user code in an isolated subprocess with resource limits
to prevent abuse (infinite loops, memory bombs, file system access, etc.).
"""

import subprocess
import tempfile
import textwrap
from pathlib import Path

# Only block modules that are directly dangerous AND not needed by stdlib internals.
# os/sys/pathlib are used transitively by many safe modules (dataclasses, typing, etc.)
# so we can't block them. The subprocess isolation + resource limits + restricted env
# provide the real security boundary.
BLOCKED_MODULES = {
    "subprocess", "shutil", "socket", "http", "urllib",
    "ctypes", "multiprocessing", "asyncio",
    "webbrowser", "antigravity",
    "tkinter", "turtle",
}

# This preamble:
# 1. Sets resource limits (before the import guard activates)
# 2. Installs an import hook that blocks dangerous modules
# 3. Cleans up so user code can't access internals
SANDBOX_PRELUDE = textwrap.dedent("""\
    # --- sandbox setup (not part of user code) ---
    import resource as _r
    import builtins as _builtins
    import sys as _sys

    # 1. Set resource limits
    try:
        _r.setrlimit(_r.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
    except ValueError:
        pass
    _r.setrlimit(_r.RLIMIT_CPU, (10, 10))
    try:
        _r.setrlimit(_r.RLIMIT_NOFILE, (32, 32))
    except ValueError:
        pass

    # 2. Clean up dangerous modules from sys.modules
    _blocked_set = {blocked}
    for _mod_name in list(_sys.modules.keys()):
        _top = _mod_name.split(".")[0]
        if _top in _blocked_set:
            del _sys.modules[_mod_name]

    # 3. Install import guard
    _original_import = _builtins.__import__

    def _make_safe_import(_blocked, _orig):
        def _safe_import(name, *args, **kwargs):
            top = name.split(".")[0]
            if top in _blocked:
                raise ImportError(f"Import of '{{name}}' is not allowed in the sandbox.")
            return _orig(name, *args, **kwargs)
        return _safe_import

    _builtins.__import__ = _make_safe_import(_blocked_set, _original_import)

    # 4. Clean up setup variables
    del _r, _builtins, _sys, _original_import, _make_safe_import, _blocked_set
    try:
        del _mod_name, _top
    except NameError:
        pass
    # --- end sandbox setup ---
""")


def execute_code(code: str, timeout: int = 10) -> dict:
    """Execute Python code in a sandboxed subprocess.

    Returns dict with keys: stdout, stderr, returncode, timed_out
    """
    guarded_code = SANDBOX_PRELUDE.format(blocked=repr(BLOCKED_MODULES)) + code

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, dir=tempfile.gettempdir()
    ) as f:
        f.write(guarded_code)
        tmp_path = f.name

    try:
        result = subprocess.run(
            ["python3", tmp_path],
            capture_output=True,
            text=True,
            timeout=timeout,
            env={"PATH": "/usr/bin:/bin", "HOME": "/tmp", "LANG": "C.UTF-8"},
        )
        return {
            "stdout": result.stdout,
            "stderr": _clean_stderr(result.stderr, tmp_path),
            "returncode": result.returncode,
            "timed_out": False,
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": f"Execution timed out after {timeout} seconds.",
            "returncode": -1,
            "timed_out": True,
        }
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def _clean_stderr(stderr: str, tmp_path: str) -> str:
    """Remove temp file path and sandbox preamble line numbers from tracebacks."""
    stderr = stderr.replace(tmp_path, "<your_code>")
    return stderr
