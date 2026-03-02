document.addEventListener('DOMContentLoaded', function () {
    var textarea = document.getElementById('code-editor');
    if (!textarea) return;

    // Dynamic CodeMirror theme based on current site theme
    function getCodeMirrorTheme() {
        return document.documentElement.getAttribute('data-bs-theme') === 'dark' ? 'monokai' : 'eclipse';
    }

    var editor = CodeMirror.fromTextArea(textarea, {
        mode: 'python',
        theme: getCodeMirrorTheme(),
        lineNumbers: true,
        indentUnit: 4,
        tabSize: 4,
        indentWithTabs: false,
        autofocus: true,
        matchBrackets: true,
        autoCloseBrackets: true,
        lineWrapping: true,
        extraKeys: {
            'Tab': function (cm) {
                cm.replaceSelection('    ', 'end');
            }
        }
    });

    editor.setSize(null, '400px');

    // Listen for theme changes and update editor
    window.addEventListener('themechange', function () {
        editor.setOption('theme', getCodeMirrorTheme());
    });

    var form = document.getElementById('submit-form');
    if (form) {
        form.addEventListener('submit', function () {
            textarea.value = editor.getValue();
            var btn = document.getElementById('submit-btn');
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span> Running...';
            }
        });
    }

    window.codeEditor = editor;
});
