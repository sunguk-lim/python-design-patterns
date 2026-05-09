// ===== Tab switching =====
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
        tab.classList.add('active');
        document.getElementById('panel-' + tab.dataset.tab).classList.add('active');
    });
});

// ===== Wait for CodeMirror to be ready =====
function initConsole() {
    const editor = window.cmEditor;
    if (!editor) return;

    const output = document.getElementById('console-output');
    const runBtn = document.getElementById('run-btn');
    const verifyBtn = document.getElementById('verify-btn');
    const status = document.getElementById('output-status');
    const loadGood = document.getElementById('load-good');
    const loadBad = document.getElementById('load-bad');
    const loadChallenge = document.getElementById('load-challenge');

    // Helper: set editor content
    function setCode(text) {
        editor.dispatch({
            changes: { from: 0, to: editor.state.doc.length, insert: text },
        });
    }

    // Helper: get editor content
    function getCode() {
        return editor.state.doc.toString();
    }

    // Load example buttons
    loadGood.addEventListener('click', () => setCode(GOOD_SOURCE));
    loadBad.addEventListener('click', () => setCode(BAD_SOURCE));

    // Load Challenge button
    loadChallenge.addEventListener('click', async () => {
        loadChallenge.disabled = true;
        loadChallenge.textContent = 'Loading...';
        try {
            const resp = await fetch('/api/exercise/' + SLUG);
            const data = await resp.json();
            if (data.source) {
                setCode(data.source);
                output.textContent = 'Challenge loaded! Implement the TODO methods, then click "Verify".';
                output.className = 'console-output';
                status.textContent = 'Challenge';
                status.className = 'output-status';
                status.style.color = 'var(--orange)';
            } else {
                output.textContent = 'Could not load challenge.';
                output.className = 'console-output error';
            }
        } catch (err) {
            output.textContent = 'Error loading challenge: ' + err.message;
            output.className = 'console-output error';
        } finally {
            loadChallenge.disabled = false;
            loadChallenge.textContent = 'Load Challenge';
        }
    });

    // Run code
    async function runCode() {
        const code = getCode();
        if (!code.trim()) {
            output.textContent = 'No code to run.';
            return;
        }

        runBtn.disabled = true;
        runBtn.innerHTML = '<span class="spinner"></span> Running...';
        status.textContent = '';
        output.textContent = 'Executing...';
        output.className = 'console-output';

        try {
            const resp = await fetch('/api/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code }),
            });
            const data = await resp.json();

            let text = '';
            if (data.stdout) text += data.stdout;
            if (data.stderr) text += (text ? '\n' : '') + data.stderr;
            if (!text) text = '(no output)';

            output.textContent = text;

            if (data.timed_out) {
                output.classList.add('error');
                status.textContent = 'Timed out';
                status.className = 'output-status error';
            } else if (data.returncode !== 0) {
                output.classList.add('error');
                status.textContent = 'Error (exit ' + data.returncode + ')';
                status.className = 'output-status error';
            } else {
                status.textContent = 'Success';
                status.className = 'output-status success';
            }
        } catch (err) {
            output.textContent = 'Network error: ' + err.message;
            output.classList.add('error');
            status.textContent = 'Failed';
            status.className = 'output-status error';
        } finally {
            runBtn.disabled = false;
            runBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5,3 19,12 5,21"/></svg> Run';
        }
    }

    runBtn.addEventListener('click', runCode);

    // Verify code against reference
    async function verifyCode() {
        const code = getCode();
        if (!code.trim()) {
            output.textContent = 'No code to verify.';
            return;
        }

        verifyBtn.disabled = true;
        runBtn.disabled = true;
        verifyBtn.innerHTML = '<span class="spinner"></span> Verifying...';
        status.textContent = '';
        output.textContent = 'Running verification...';
        output.className = 'console-output';

        try {
            const resp = await fetch('/api/verify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code, slug: SLUG }),
            });
            const data = await resp.json();

            if (data.error) {
                output.textContent = 'Error: ' + data.error;
                output.className = 'console-output error';
                status.textContent = 'Error';
                status.className = 'output-status error';
                return;
            }

            // Build result display
            let html = '';

            if (data.match) {
                html += '<div class="verify-pass">PASS — Your output matches the expected answer!</div>';
                status.textContent = 'PASS';
                status.className = 'output-status success';
            } else {
                html += '<div class="verify-fail">FAIL — Your output does not match the expected answer.</div>';
                status.textContent = 'FAIL';
                status.className = 'output-status error';
            }

            if (data.actual_stderr) {
                html += '<div class="verify-section"><div class="verify-label">Errors</div>';
                html += '<pre style="color:var(--red);margin:0">' + escapeHtml(data.actual_stderr) + '</pre></div>';
            }

            html += '<div class="verify-section"><div class="verify-label">Your Output</div>';
            html += '<pre style="margin:0">' + escapeHtml(data.actual_stdout || '(no output)') + '</pre></div>';

            html += '<div class="verify-section"><div class="verify-label">Expected Output</div>';
            html += '<pre style="margin:0;color:var(--text-dim)">' + escapeHtml(data.expected_stdout || '(no output)') + '</pre></div>';

            output.innerHTML = html;

        } catch (err) {
            output.textContent = 'Network error: ' + err.message;
            output.className = 'console-output error';
            status.textContent = 'Failed';
            status.className = 'output-status error';
        } finally {
            verifyBtn.disabled = false;
            runBtn.disabled = false;
            verifyBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20,6 9,17 4,12"/></svg> Verify';
        }
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    verifyBtn.addEventListener('click', verifyCode);

    // ===== Draggable resize handle =====
    const resizeHandle = document.getElementById('resize-handle');
    const editorMount = document.getElementById('code-editor-mount');
    let isDragging = false;
    let startY = 0;
    let startHeight = 0;

    function onResizeStart(e) {
        isDragging = true;
        startY = e.type.startsWith('touch') ? e.touches[0].clientY : e.clientY;
        startHeight = editorMount.offsetHeight;
        resizeHandle.classList.add('active');
        document.body.style.cursor = 'row-resize';
        document.body.style.userSelect = 'none';
        e.preventDefault();
    }

    function onResizeMove(e) {
        if (!isDragging) return;
        const clientY = e.type.startsWith('touch') ? e.touches[0].clientY : e.clientY;
        const dy = clientY - startY;
        const newHeight = Math.max(150, startHeight + dy);
        editorMount.style.height = newHeight + 'px';
        editorMount.style.maxHeight = newHeight + 'px';
    }

    function onResizeEnd() {
        if (!isDragging) return;
        isDragging = false;
        resizeHandle.classList.remove('active');
        document.body.style.cursor = '';
        document.body.style.userSelect = '';
    }

    resizeHandle.addEventListener('mousedown', onResizeStart);
    document.addEventListener('mousemove', onResizeMove);
    document.addEventListener('mouseup', onResizeEnd);
    resizeHandle.addEventListener('touchstart', onResizeStart, { passive: false });
    document.addEventListener('touchmove', onResizeMove, { passive: true });
    document.addEventListener('touchend', onResizeEnd);
}

// Init when CodeMirror is ready (it loads async as a module)
if (window.cmEditor) {
    initConsole();
} else {
    window.addEventListener('cm-ready', initConsole);
}
