/**
 * Interactive Code Sandbox Execution Controller
 */
document.addEventListener('DOMContentLoaded', () => {
    const runBtn = document.getElementById('runCodeBtn');
    const editor = document.getElementById('codeEditor');
    const consoleBox = document.getElementById('outputConsole');

    if (runBtn && editor && consoleBox) {
        runBtn.addEventListener('click', () => {
            const code = editor.value;
            consoleBox.innerHTML = '<span class="text-warning">&gt; Executing in Python sandbox...</span>';

            fetch('/assessments/api/run-code/', {
                method: 'POST',
                headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken')},
                body: JSON.stringify({code: code})
            })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    consoleBox.innerHTML = `<span class="text-danger">Error:
${data.error}</span>`;
                } else {
                    consoleBox.innerHTML = `<span class="text-success">&gt; Execution Succeeded (${data.execution_time_ms}ms):
</span><pre class="text-white mt-2">${data.output || '(No output)'}</pre>`;
                }
            })
            .catch(err => {
                consoleBox.innerHTML = `<span class="text-danger">&gt; Network Error: ${err}</span>`;
            });
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
