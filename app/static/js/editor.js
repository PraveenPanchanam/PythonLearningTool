document.addEventListener('DOMContentLoaded', function () {
    var textarea = document.getElementById('code-editor');
    if (!textarea) return;

    var editor = CodeMirror.fromTextArea(textarea, {
        mode: 'python',
        theme: 'monokai',
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
