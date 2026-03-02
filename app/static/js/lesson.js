/**
 * Lesson page JavaScript
 * Handles CodeMirror editors for exercises, AJAX exercise checking, and lesson completion.
 */

document.addEventListener('DOMContentLoaded', function () {
    const editors = {};
    const passedExercises = new Set();
    let totalExercises = 0;

    // Initialize CodeMirror editors for each exercise
    document.querySelectorAll('.lesson-code-editor').forEach(function (textarea) {
        const sectionId = textarea.dataset.sectionId;
        const editor = CodeMirror.fromTextArea(textarea, {
            mode: 'python',
            theme: 'monokai',
            lineNumbers: true,
            indentUnit: 4,
            tabSize: 4,
            autoCloseBrackets: true,
            matchBrackets: true,
            indentWithTabs: false,
            extraKeys: {
                'Tab': function (cm) {
                    cm.replaceSelection('    ', 'end');
                },
            },
        });
        editor.setSize(null, 150);
        editors[sectionId] = editor;
        totalExercises++;
    });

    // Run & Check button handlers
    document.querySelectorAll('.run-exercise-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const sectionId = this.dataset.sectionId;
            const editor = editors[sectionId];
            if (!editor) return;

            const code = editor.getValue().trim();
            const expected = document.getElementById('editor-' + sectionId).dataset.expected;

            if (!code) {
                showResult(sectionId, false, '', 'Please write some code first.');
                return;
            }

            // Show loading state
            this.disabled = true;
            this.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Running...';

            fetch('/lessons/' + window.LESSON_ID + '/check-exercise', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.CSRF_TOKEN,
                },
                body: JSON.stringify({
                    code: code,
                    expected_output: expected,
                }),
            })
                .then(function (response) { return response.json(); })
                .then(function (data) {
                    showResult(sectionId, data.passed, data.output || '', data.error || '');

                    if (data.passed) {
                        passedExercises.add(sectionId);
                        markSectionDone(sectionId);
                    }
                    updateProgress();
                })
                .catch(function (err) {
                    showResult(sectionId, false, '', 'Network error. Please try again.');
                })
                .finally(function () {
                    btn.disabled = false;
                    btn.innerHTML = '<i class="bi bi-play-fill"></i> Run & Check';
                });
        });
    });

    // Reset button handlers
    document.querySelectorAll('.reset-exercise-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const sectionId = this.dataset.sectionId;
            const starter = this.dataset.starter;
            const editor = editors[sectionId];
            if (editor) {
                editor.setValue(starter);
            }
            // Hide result
            const resultDiv = document.getElementById('result-' + sectionId);
            if (resultDiv) {
                resultDiv.classList.remove('show');
                resultDiv.innerHTML = '';
            }
        });
    });

    // Hint toggle handlers
    document.querySelectorAll('.hint-toggle-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const target = document.getElementById(this.dataset.target);
            if (target) {
                target.style.display = target.style.display === 'none' ? 'block' : 'none';
            }
        });
    });

    // Complete lesson button
    var completeBtn = document.getElementById('complete-lesson-btn');
    if (completeBtn && !completeBtn.disabled) {
        completeBtn.addEventListener('click', function () {
            markLessonComplete();
        });
    }

    function showResult(sectionId, passed, output, error) {
        const resultDiv = document.getElementById('result-' + sectionId);
        if (!resultDiv) return;

        let html = '';
        if (passed) {
            html = '<div class="alert alert-success mb-0 py-2">' +
                '<i class="bi bi-check-circle-fill"></i> <strong>Correct!</strong> Output matches expected result.' +
                '</div>';
            if (output) {
                html += '<div class="exercise-output mt-2">' + escapeHtml(output) + '</div>';
            }
        } else {
            if (error) {
                html = '<div class="alert alert-danger mb-0 py-2">' +
                    '<i class="bi bi-x-circle-fill"></i> <strong>Error:</strong>' +
                    '<pre class="mb-0 mt-1" style="color: inherit; background: none; font-size: 0.85rem;">' + escapeHtml(error) + '</pre>' +
                    '</div>';
            } else {
                const expected = document.getElementById('editor-' + sectionId).dataset.expected;
                html = '<div class="alert alert-warning mb-0 py-2">' +
                    '<i class="bi bi-exclamation-triangle-fill"></i> <strong>Not quite right.</strong>' +
                    '</div>' +
                    '<div class="row mt-2">' +
                    '<div class="col-6">' +
                    '<small class="text-muted">Expected:</small>' +
                    '<div class="exercise-output">' + escapeHtml(expected) + '</div>' +
                    '</div>' +
                    '<div class="col-6">' +
                    '<small class="text-muted">Your output:</small>' +
                    '<div class="exercise-output">' + escapeHtml(output) + '</div>' +
                    '</div>' +
                    '</div>';
            }
        }

        resultDiv.innerHTML = html;
        resultDiv.classList.add('show');
    }

    function markSectionDone(sectionId) {
        const progressEl = document.getElementById('progress-' + sectionId);
        if (progressEl) {
            progressEl.classList.remove('pending');
            progressEl.classList.add('done');
            progressEl.innerHTML = '<i class="bi bi-check-lg"></i>';
        }
        const card = document.getElementById('section-' + sectionId);
        if (card) {
            card.classList.add('completed');
        }
    }

    function updateProgress() {
        const passedCount = passedExercises.size;
        const passedEl = document.getElementById('exercises-passed');
        if (passedEl) passedEl.textContent = passedCount;

        const progressBar = document.getElementById('exercise-progress-bar');
        if (progressBar && totalExercises > 0) {
            progressBar.style.width = Math.round((passedCount / totalExercises) * 100) + '%';
        }

        // Auto-complete when all exercises pass
        if (passedCount === totalExercises && totalExercises > 0) {
            markLessonComplete();
        }
    }

    function markLessonComplete() {
        var btn = document.getElementById('complete-lesson-btn');
        if (btn) {
            btn.disabled = true;
            btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Saving...';
        }

        fetch('/lessons/' + window.LESSON_ID + '/complete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': window.CSRF_TOKEN,
            },
            body: JSON.stringify({
                exercises_completed: passedExercises.size,
            }),
        })
            .then(function (response) { return response.json(); })
            .then(function (data) {
                if (data.status === 'ok') {
                    if (btn) {
                        btn.innerHTML = '<i class="bi bi-check-circle"></i> Lesson Completed <i class="bi bi-check-lg"></i>';
                        btn.classList.remove('btn-success');
                        btn.classList.add('btn-outline-success');
                    }
                }
            })
            .catch(function (err) {
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = '<i class="bi bi-check-circle"></i> Mark Lesson Complete';
                }
            });
    }

    function escapeHtml(text) {
        var div = document.createElement('div');
        div.appendChild(document.createTextNode(text));
        return div.innerHTML;
    }
});
