import json
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.extensions import db, limiter
from app.models.lesson import Lesson
from app.models.lesson_completion import LessonCompletion
from app.utils.code_runner import run_student_code, check_blocked_patterns

lessons_bp = Blueprint('lessons', __name__)


@lessons_bp.route('/<int:lesson_id>')
@login_required
def view_lesson(lesson_id):
    lesson = db.session.get(Lesson, lesson_id)
    if not lesson:
        return render_template('errors/404.html'), 404

    sections = json.loads(lesson.content)
    completion = LessonCompletion.query.filter_by(
        user_id=current_user.id, lesson_id=lesson_id
    ).first()

    # Check if previous lesson in chapter has been viewed (soft gating)
    show_reminder = False
    if lesson.order > 1:
        prev_lesson = Lesson.query.filter_by(
            chapter_id=lesson.chapter_id, order=lesson.order - 1
        ).first()
        if prev_lesson:
            prev_completion = LessonCompletion.query.filter_by(
                user_id=current_user.id, lesson_id=prev_lesson.id
            ).first()
            if not prev_completion:
                show_reminder = True

    # Count exercises for progress tracking
    exercise_count = sum(1 for s in sections if s.get('exercise'))

    return render_template(
        'lessons/view.html',
        lesson=lesson,
        chapter=lesson.chapter,
        sections=sections,
        completion=completion,
        show_reminder=show_reminder,
        exercise_count=exercise_count,
    )


@lessons_bp.route('/<int:lesson_id>/check-exercise', methods=['POST'])
@login_required
@limiter.limit("30 per minute")
def check_exercise(lesson_id):
    """AJAX endpoint: run student code and check output match."""
    lesson = db.session.get(Lesson, lesson_id)
    if not lesson:
        return jsonify({'error': 'Lesson not found'}), 404

    data = request.get_json()
    code = data.get('code', '').strip()
    expected_output = data.get('expected_output', '').strip()

    if not code:
        return jsonify({'error': 'No code provided'}), 400

    # Check for blocked patterns first
    blocked = check_blocked_patterns(code)
    if blocked:
        return jsonify({
            'passed': False,
            'error': f'Blocked pattern detected: {blocked}',
            'output': '',
        })

    # Run student code using existing code runner
    result = run_student_code(code)

    if result['status'] == 'error':
        return jsonify({
            'passed': False,
            'error': result.get('stderr', result.get('error', 'Unknown error')),
            'output': result.get('stdout', ''),
        })

    if result['status'] == 'timeout':
        return jsonify({
            'passed': False,
            'error': 'Code execution timed out (10 second limit).',
            'output': '',
        })

    actual_output = result.get('stdout', '').strip()
    passed = actual_output == expected_output

    return jsonify({
        'passed': passed,
        'output': actual_output,
        'expected': expected_output,
        'error': result.get('stderr', '') if result.get('returncode', 0) != 0 else '',
    })


@lessons_bp.route('/<int:lesson_id>/complete', methods=['POST'])
@login_required
def mark_complete(lesson_id):
    """Mark a lesson as complete (or update completion)."""
    lesson = db.session.get(Lesson, lesson_id)
    if not lesson:
        return jsonify({'error': 'Lesson not found'}), 404

    data = request.get_json() or {}
    exercises_completed = data.get('exercises_completed', 0)

    sections = json.loads(lesson.content)
    exercises_total = sum(1 for s in sections if s.get('exercise'))

    completion = LessonCompletion.query.filter_by(
        user_id=current_user.id, lesson_id=lesson_id
    ).first()

    if completion:
        completion.exercises_completed = max(completion.exercises_completed, exercises_completed)
        completion.exercises_total = exercises_total
    else:
        completion = LessonCompletion(
            user_id=current_user.id,
            lesson_id=lesson_id,
            exercises_completed=exercises_completed,
            exercises_total=exercises_total,
        )
        db.session.add(completion)

    db.session.commit()
    return jsonify({
        'status': 'ok',
        'exercises_completed': completion.exercises_completed,
        'exercises_total': exercises_total,
    })
