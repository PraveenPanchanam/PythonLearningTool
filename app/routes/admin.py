from functools import wraps
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from app.extensions import db
from app.models.user import User
from app.models.chapter import Chapter
from app.models.assignment import Assignment
from app.models.submission import Submission
from app.models.lesson import Lesson
from app.models.lesson_completion import LessonCompletion

admin_bp = Blueprint('admin', __name__)


def admin_required(f):
    """Decorator that requires the current user to be an admin."""
    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/')
@admin_required
def admin_dashboard():
    total_students = User.query.filter_by(is_admin=False).count()
    total_submissions = Submission.query.count()
    total_lessons_completed = LessonCompletion.query.count()

    chapters = Chapter.query.order_by(Chapter.order).all()
    chapter_stats = []
    for chapter in chapters:
        assignments = chapter.assignments.all()
        lessons = chapter.lessons.all()
        sub_count = 0
        for a in assignments:
            sub_count += Submission.query.filter_by(assignment_id=a.id).count()

        chapter_stats.append({
            'chapter': chapter,
            'assignment_count': len(assignments),
            'lesson_count': len(lessons),
            'submission_count': sub_count,
        })

    return render_template(
        'admin/dashboard.html',
        total_students=total_students,
        total_submissions=total_submissions,
        total_lessons_completed=total_lessons_completed,
        chapter_stats=chapter_stats,
    )


@admin_bp.route('/students')
@admin_required
def student_list():
    students = User.query.filter_by(is_admin=False).order_by(User.created_at.desc()).all()
    student_data = []
    for student in students:
        sub_count = Submission.query.filter_by(user_id=student.id).count()
        lesson_count = LessonCompletion.query.filter_by(user_id=student.id).count()
        # Calculate average score
        from sqlalchemy import func
        avg_score = db.session.query(func.avg(Submission.score)).filter_by(
            user_id=student.id
        ).scalar() or 0

        student_data.append({
            'user': student,
            'submission_count': sub_count,
            'lesson_count': lesson_count,
            'avg_score': round(avg_score, 1),
        })
    return render_template('admin/students.html', students=student_data)


@admin_bp.route('/students/<int:user_id>')
@admin_required
def student_detail(user_id):
    student = db.session.get(User, user_id)
    if not student:
        abort(404)

    chapters = Chapter.query.order_by(Chapter.order).all()
    chapter_progress = []
    for chapter in chapters:
        assignments = chapter.assignments.all()
        lessons = chapter.lessons.all()

        # Assignment progress
        completed_assignments = 0
        total_score = 0
        for assignment in assignments:
            best = Submission.query.filter_by(
                user_id=user_id, assignment_id=assignment.id
            ).order_by(Submission.score.desc()).first()
            if best and best.score > 0:
                completed_assignments += 1
                total_score += best.score

        # Lesson progress
        completed_lessons = LessonCompletion.query.filter_by(
            user_id=user_id
        ).join(Lesson).filter(
            Lesson.chapter_id == chapter.id
        ).count()

        chapter_progress.append({
            'chapter': chapter,
            'total_assignments': len(assignments),
            'completed_assignments': completed_assignments,
            'avg_score': round(total_score / completed_assignments, 1) if completed_assignments > 0 else 0,
            'total_lessons': len(lessons),
            'completed_lessons': completed_lessons,
        })

    recent_submissions = Submission.query.filter_by(user_id=user_id).order_by(
        Submission.submitted_at.desc()
    ).limit(20).all()

    return render_template(
        'admin/student_detail.html',
        student=student,
        chapter_progress=chapter_progress,
        recent_submissions=recent_submissions,
    )
