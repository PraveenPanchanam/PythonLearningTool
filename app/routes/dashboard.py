from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import func
from app.extensions import db
from app.models.chapter import Chapter
from app.models.assignment import Assignment
from app.models.submission import Submission
from app.models.lesson import Lesson
from app.models.lesson_completion import LessonCompletion
from app.models.nudge import Nudge
from app.utils.learning_plan import get_learning_plan, get_level_display_name, get_start_chapter

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@login_required
def overview():
    chapters = Chapter.query.order_by(Chapter.order).all()

    total_assignments = Assignment.query.count()
    completed_assignments = 0
    total_score = 0
    scored_count = 0

    total_lessons = Lesson.query.count()
    completed_lessons = LessonCompletion.query.filter_by(user_id=current_user.id).count()

    chapter_stats = []
    for chapter in chapters:
        assignments = chapter.assignments.all()
        lessons = chapter.lessons.all()
        ch_total = len(assignments)
        ch_completed = 0
        ch_score_sum = 0

        for assignment in assignments:
            best = Submission.query.filter_by(
                user_id=current_user.id,
                assignment_id=assignment.id
            ).order_by(Submission.score.desc()).first()
            if best and best.score > 0:
                ch_completed += 1
                completed_assignments += 1
                ch_score_sum += best.score
                total_score += best.score
                scored_count += 1

        # Lesson progress for this chapter
        ch_lesson_total = len(lessons)
        ch_lesson_completed = LessonCompletion.query.filter_by(
            user_id=current_user.id
        ).join(Lesson).filter(
            Lesson.chapter_id == chapter.id
        ).count()

        chapter_stats.append({
            'chapter': chapter,
            'total': ch_total,
            'completed': ch_completed,
            'percentage': int(ch_completed / ch_total * 100) if ch_total > 0 else 0,
            'avg_score': round(ch_score_sum / ch_completed, 1) if ch_completed > 0 else 0,
            'lesson_total': ch_lesson_total,
            'lesson_completed': ch_lesson_completed,
        })

    avg_score = round(total_score / scored_count, 1) if scored_count > 0 else 0

    recent_submissions = Submission.query.filter_by(
        user_id=current_user.id
    ).order_by(Submission.submitted_at.desc()).limit(10).all()

    for sub in recent_submissions:
        sub.assignment_obj = db.session.get(Assignment, sub.assignment_id)

    # Get unread nudges for this student
    unread_nudges = Nudge.query.filter_by(
        user_id=current_user.id, read_at=None
    ).order_by(Nudge.created_at.desc()).all()

    return render_template(
        'dashboard/overview.html',
        chapter_stats=chapter_stats,
        total_assignments=total_assignments,
        completed_assignments=completed_assignments,
        overall_percentage=int(completed_assignments / total_assignments * 100) if total_assignments > 0 else 0,
        avg_score=avg_score,
        recent_submissions=recent_submissions,
        total_lessons=total_lessons,
        completed_lessons=completed_lessons,
        user_level=current_user.python_level or 'complete_beginner',
        level_display_name=get_level_display_name(current_user.python_level or 'complete_beginner'),
        learning_plan=get_learning_plan(current_user.python_level or 'complete_beginner'),
        start_chapter=get_start_chapter(current_user.python_level or 'complete_beginner'),
        unread_nudges=unread_nudges,
    )


@dashboard_bp.route('/dismiss-nudge/<int:nudge_id>', methods=['POST'])
@login_required
def dismiss_nudge(nudge_id):
    """Mark a nudge as read."""
    nudge = db.session.get(Nudge, nudge_id)
    if nudge and nudge.user_id == current_user.id:
        nudge.read_at = datetime.utcnow()
        db.session.commit()
    return redirect(url_for('dashboard.overview'))
