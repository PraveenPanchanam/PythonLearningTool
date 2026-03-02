import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db, limiter
from app.models.assignment import Assignment
from app.models.submission import Submission
from app.utils.code_runner import validate_submission

assignments_bp = Blueprint('assignments', __name__)


@assignments_bp.route('/<int:assignment_id>')
@login_required
def view_assignment(assignment_id):
    assignment = db.session.get(Assignment, assignment_id)
    if not assignment:
        return render_template('404.html'), 404

    hints = json.loads(assignment.hints) if assignment.hints else []

    best_submission = Submission.query.filter_by(
        user_id=current_user.id,
        assignment_id=assignment.id
    ).order_by(Submission.score.desc()).first()

    attempt_count = Submission.query.filter_by(
        user_id=current_user.id,
        assignment_id=assignment.id
    ).count()

    last_submission = Submission.query.filter_by(
        user_id=current_user.id,
        assignment_id=assignment.id
    ).order_by(Submission.submitted_at.desc()).first()

    starter = last_submission.code if last_submission else assignment.starter_code

    return render_template(
        'assignments/view.html',
        assignment=assignment,
        chapter=assignment.chapter,
        hints=hints,
        best_score=best_submission.score if best_submission else None,
        attempt_count=attempt_count,
        starter_code=starter,
    )


@assignments_bp.route('/<int:assignment_id>/submit', methods=['POST'])
@login_required
@limiter.limit("20 per minute")
def submit_assignment(assignment_id):
    assignment = db.session.get(Assignment, assignment_id)
    if not assignment:
        flash('Assignment not found.', 'danger')
        return redirect(url_for('chapters.chapter_list'))

    code = request.form.get('code', '').strip()
    if not code:
        flash('Please write some code before submitting.', 'warning')
        return redirect(url_for('assignments.view_assignment', assignment_id=assignment_id))

    result = validate_submission(code, assignment)

    submission = Submission(
        user_id=current_user.id,
        assignment_id=assignment.id,
        code=code,
        score=result['score'],
        passed_tests=result['passed_tests'],
        total_tests=result['total_tests'],
        test_details=json.dumps(result['test_details']),
        output_match=result['output_match'],
        output_matches_count=result['output_matches_count'],
        output_total_count=result['output_total_count'],
        actual_output=result['actual_output'],
        execution_time_ms=result['execution_time_ms'],
        error_message=result['error_message'],
        status=result['status'],
    )
    db.session.add(submission)
    db.session.commit()

    return redirect(url_for(
        'assignments.view_result',
        assignment_id=assignment_id,
        submission_id=submission.id
    ))


@assignments_bp.route('/<int:assignment_id>/result/<int:submission_id>')
@login_required
def view_result(assignment_id, submission_id):
    submission = db.session.get(Submission, submission_id)
    if not submission or submission.user_id != current_user.id:
        flash('Submission not found.', 'danger')
        return redirect(url_for('chapters.chapter_list'))

    assignment = db.session.get(Assignment, assignment_id)
    test_details = json.loads(submission.test_details) if submission.test_details else []

    io_pairs = json.loads(assignment.input_output_pairs) if assignment.input_output_pairs else []
    actual_outputs = submission.actual_output.split('\n---\n') if submission.actual_output else []

    output_comparison = []
    for i, pair in enumerate(io_pairs):
        output_comparison.append({
            'input': pair.get('input', ''),
            'expected': pair.get('expected_output', ''),
            'actual': actual_outputs[i] if i < len(actual_outputs) else 'N/A',
            'match': (
                actual_outputs[i].strip() == pair.get('expected_output', '').strip()
                if i < len(actual_outputs) else False
            ),
        })

    return render_template(
        'assignments/result.html',
        assignment=assignment,
        submission=submission,
        test_details=test_details,
        output_comparison=output_comparison,
    )


@assignments_bp.route('/<int:assignment_id>/history')
@login_required
def submission_history(assignment_id):
    assignment = db.session.get(Assignment, assignment_id)
    if not assignment:
        return render_template('404.html'), 404

    submissions = Submission.query.filter_by(
        user_id=current_user.id,
        assignment_id=assignment_id
    ).order_by(Submission.submitted_at.desc()).all()

    return render_template(
        'assignments/history.html',
        assignment=assignment,
        submissions=submissions,
    )
