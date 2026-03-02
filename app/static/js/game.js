/**
 * Interactive Learning Games for Kids (Under 12)
 * Handles: drag-and-drop ordering, fill-in-the-blank, quiz, output prediction.
 * All games are client-side. Game completions dispatch 'gamepassed' events
 * for lesson.js to integrate with the progress tracker.
 */

document.addEventListener('DOMContentLoaded', function () {
    var passedGames = new Set();

    var SUCCESS_MESSAGES = [
        '\ud83c\udf89 Amazing job!',
        '\u2b50 You\'re a coding star!',
        '\ud83d\ude80 Brilliant!',
        '\ud83c\udfc6 You nailed it!',
        '\ud83d\udc4f Great work!',
        '\ud83c\udf1f Fantastic!'
    ];

    var TRY_AGAIN_MESSAGES = [
        '\ud83e\udd14 Almost there! Try again!',
        '\ud83d\udcaa You can do it!',
        '\ud83d\udd04 Not quite \u2014 give it another shot!',
        '\ud83c\udf31 Keep trying, you\'re learning!'
    ];

    function randomMessage(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    function showGameResult(sectionId, passed, message) {
        var resultDiv = document.getElementById('game-result-' + sectionId);
        if (!resultDiv) return;
        resultDiv.style.display = 'block';
        resultDiv.className = 'game-result mt-2 ' + (passed ? 'success' : 'try-again');
        resultDiv.textContent = message;
    }

    function showExplanation(sectionId) {
        var el = document.getElementById('game-explanation-' + sectionId);
        if (el) el.style.display = 'block';
    }

    function markGamePassed(sectionId) {
        if (passedGames.has(sectionId)) return;
        passedGames.add(sectionId);
        window.dispatchEvent(new CustomEvent('gamepassed', { detail: { sectionId: sectionId } }));
    }

    // ────────────────────────────────────────
    // Fisher-Yates shuffle (returns new array)
    // ────────────────────────────────────────
    function shuffleArray(arr) {
        var a = arr.slice();
        for (var i = a.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        }
        return a;
    }

    // ════════════════════════════════════════
    //  DRAG & DROP CODE ORDERING
    // ════════════════════════════════════════
    function initDragOrder(widget, sectionId) {
        var container = widget.querySelector('.drag-order-game');
        var correctOrder = JSON.parse(container.dataset.correct);
        var source = document.getElementById('drag-source-' + sectionId);
        var blocks = Array.from(source.querySelectorAll('.drag-block'));

        function shuffleBlocks() {
            // Reset classes
            blocks.forEach(function (b) { b.classList.remove('correct', 'wrong'); });
            var shuffled = shuffleArray(blocks);
            // Ensure shuffled is actually different from correct if possible
            if (shuffled.length > 1) {
                var same = shuffled.every(function (b, i) { return parseInt(b.dataset.index) === i; });
                if (same) {
                    var tmp = shuffled[0]; shuffled[0] = shuffled[1]; shuffled[1] = tmp;
                }
            }
            shuffled.forEach(function (b) { source.appendChild(b); });
        }

        shuffleBlocks();

        // Drag & drop event handlers
        var draggedEl = null;

        source.addEventListener('dragstart', function (e) {
            if (e.target.classList.contains('drag-block')) {
                draggedEl = e.target;
                e.target.classList.add('dragging');
                e.dataTransfer.effectAllowed = 'move';
            }
        });

        source.addEventListener('dragend', function (e) {
            if (e.target.classList.contains('drag-block')) {
                e.target.classList.remove('dragging');
                draggedEl = null;
            }
        });

        source.addEventListener('dragover', function (e) {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            var afterElement = getDragAfterElement(source, e.clientY);
            if (afterElement == null) {
                source.appendChild(draggedEl);
            } else {
                source.insertBefore(draggedEl, afterElement);
            }
        });

        function getDragAfterElement(container, y) {
            var elements = Array.from(container.querySelectorAll('.drag-block:not(.dragging)'));
            var result = null;
            var closest = Number.POSITIVE_INFINITY;
            elements.forEach(function (el) {
                var box = el.getBoundingClientRect();
                var offset = y - box.top - box.height / 2;
                if (offset < 0 && offset > -closest) {
                    closest = -offset;
                    result = el;
                }
            });
            return result;
        }

        // Check button
        widget.querySelector('.game-check-btn').addEventListener('click', function () {
            var current = Array.from(source.querySelectorAll('.drag-block'));
            var allCorrect = true;
            current.forEach(function (b, i) {
                var isCorrect = parseInt(b.dataset.index) === i;
                b.classList.toggle('correct', isCorrect);
                b.classList.toggle('wrong', !isCorrect);
                if (!isCorrect) allCorrect = false;
            });

            if (allCorrect) {
                showGameResult(sectionId, true, randomMessage(SUCCESS_MESSAGES));
                showExplanation(sectionId);
                markGamePassed(sectionId);
            } else {
                showGameResult(sectionId, false, randomMessage(TRY_AGAIN_MESSAGES));
            }
        });

        // Reset/shuffle button
        var resetBtn = widget.querySelector('.game-reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', function () {
                shuffleBlocks();
                var resultDiv = document.getElementById('game-result-' + sectionId);
                if (resultDiv) resultDiv.style.display = 'none';
                var expDiv = document.getElementById('game-explanation-' + sectionId);
                if (expDiv) expDiv.style.display = 'none';
            });
        }
    }

    // ════════════════════════════════════════
    //  FILL IN THE BLANK
    // ════════════════════════════════════════
    function initFillBlank(widget, sectionId) {
        var codeDiv = document.getElementById('fill-code-' + sectionId);
        var template = codeDiv.dataset.template;
        var blanks = JSON.parse(codeDiv.dataset.blanks);

        // Render code with input fields
        var html = escapeHtml(template);
        blanks.forEach(function (blank) {
            var placeholder = '{' + blank.id + '}';
            var inputHtml = '<input type="text" class="blank-input" ' +
                'data-blank-id="' + blank.id + '" ' +
                'data-answer="' + escapeAttr(blank.answer) + '" ' +
                'placeholder="???" ' +
                'autocomplete="off" ' +
                'size="' + Math.max(blank.answer.length + 2, 6) + '">';
            html = html.replace(escapeHtml(placeholder), inputHtml);
        });
        codeDiv.innerHTML = html;

        // Hint button
        var hintBtn = widget.querySelector('.game-hint-btn');

        // Check button
        widget.querySelector('.game-check-btn').addEventListener('click', function () {
            var inputs = codeDiv.querySelectorAll('.blank-input');
            var allCorrect = true;

            inputs.forEach(function (input) {
                var answer = input.dataset.answer;
                var userVal = input.value.trim();
                if (userVal.toLowerCase() === answer.toLowerCase()) {
                    input.classList.add('correct');
                    input.classList.remove('wrong');
                } else {
                    input.classList.add('wrong');
                    input.classList.remove('correct');
                    allCorrect = false;
                }
            });

            if (allCorrect) {
                showGameResult(sectionId, true, randomMessage(SUCCESS_MESSAGES));
                showExplanation(sectionId);
                markGamePassed(sectionId);
                if (hintBtn) hintBtn.style.display = 'none';
            } else {
                showGameResult(sectionId, false, randomMessage(TRY_AGAIN_MESSAGES));
                if (hintBtn) hintBtn.style.display = 'inline-block';
            }
        });

        // Hint button handler
        if (hintBtn) {
            hintBtn.addEventListener('click', function () {
                var inputs = codeDiv.querySelectorAll('.blank-input');
                inputs.forEach(function (input) {
                    if (!input.classList.contains('correct')) {
                        var blankId = parseInt(input.dataset.blankId);
                        var blankInfo = blanks.find(function (b) { return b.id === blankId; });
                        if (blankInfo && blankInfo.hint) {
                            input.setAttribute('placeholder', blankInfo.hint);
                        }
                    }
                });
            });
        }
    }

    // ════════════════════════════════════════
    //  MULTIPLE CHOICE QUIZ
    // ════════════════════════════════════════
    function initQuiz(widget, sectionId) {
        var optionsContainer = document.getElementById('quiz-options-' + sectionId);
        var options = JSON.parse(optionsContainer.dataset.options);
        var labels = optionsContainer.querySelectorAll('.quiz-option');
        var checked = false;

        // Click to select
        labels.forEach(function (label) {
            label.addEventListener('click', function () {
                if (checked) return;
                labels.forEach(function (l) { l.classList.remove('selected'); });
                label.classList.add('selected');
                var radio = label.querySelector('input[type="radio"]');
                if (radio) radio.checked = true;
            });
        });

        // Check button
        widget.querySelector('.game-check-btn').addEventListener('click', function () {
            if (checked) return;
            var selected = optionsContainer.querySelector('input[type="radio"]:checked');
            if (!selected) {
                showGameResult(sectionId, false, '\ud83d\udc46 Pick an answer first!');
                return;
            }

            checked = true;
            var selectedIdx = parseInt(selected.value);
            var isCorrect = options[selectedIdx] && options[selectedIdx].correct;

            labels.forEach(function (label, idx) {
                if (options[idx].correct) {
                    label.classList.add('correct');
                } else if (idx === selectedIdx) {
                    label.classList.add('wrong');
                }
            });

            if (isCorrect) {
                showGameResult(sectionId, true, randomMessage(SUCCESS_MESSAGES));
                markGamePassed(sectionId);
            } else {
                showGameResult(sectionId, false, '\u274c Not quite! The correct answer is highlighted in green.');
            }
            showExplanation(sectionId);
        });
    }

    // ════════════════════════════════════════
    //  OUTPUT PREDICTION
    // ════════════════════════════════════════
    function initPredictOutput(widget, sectionId) {
        var container = widget.querySelector('.predict-output-game');
        var expected = container.dataset.expected;
        var input = document.getElementById('predict-input-' + sectionId);
        var revealed = false;

        widget.querySelector('.game-check-btn').addEventListener('click', function () {
            if (revealed) return;
            revealed = true;

            var guess = input.value.trim();
            var isCorrect = guess === expected ||
                            guess.toLowerCase() === expected.toLowerCase();

            if (isCorrect) {
                showGameResult(sectionId, true,
                    randomMessage(SUCCESS_MESSAGES) + ' The output is: ' + expected);
                markGamePassed(sectionId);
            } else {
                showGameResult(sectionId, false,
                    'The output is: ' + expected + (guess ? ' (you guessed: ' + guess + ')' : ''));
                // Still mark as passed after reveal — they learned the answer
                markGamePassed(sectionId);
            }
            showExplanation(sectionId);
            input.disabled = true;
            this.disabled = true;
        });
    }

    // ────────────────────────────────────────
    // Utility functions
    // ────────────────────────────────────────
    function escapeHtml(text) {
        var div = document.createElement('div');
        div.appendChild(document.createTextNode(text));
        return div.innerHTML;
    }

    function escapeAttr(text) {
        return text.replace(/&/g, '&amp;').replace(/"/g, '&quot;')
                   .replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    // ────────────────────────────────────────
    // Initialize all game widgets on the page
    // ────────────────────────────────────────
    document.querySelectorAll('.game-widget').forEach(function (widget) {
        var type = widget.dataset.gameType;
        var sectionId = widget.id.replace('game-', '');

        if (type === 'drag_order') initDragOrder(widget, sectionId);
        else if (type === 'fill_blank') initFillBlank(widget, sectionId);
        else if (type === 'quiz') initQuiz(widget, sectionId);
        else if (type === 'predict_output') initPredictOutput(widget, sectionId);
    });
});
