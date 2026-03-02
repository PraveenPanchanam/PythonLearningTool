from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models.certificate import Certificate
from app.models.chapter import Chapter
from app.models.assignment import Assignment
from app.models.submission import Submission
from app.models.lesson import Lesson
from app.models.lesson_completion import LessonCompletion

certificates_bp = Blueprint('certificates', __name__)


def check_chapter_complete(user_id, chapter_id):
    """Check if a user has completed all assignments and lessons in a chapter."""
    chapter = db.session.get(Chapter, chapter_id)
    if not chapter:
        return False

    assignments = chapter.assignments.all()
    lessons = chapter.lessons.all()

    if not assignments and not lessons:
        return False

    for assignment in assignments:
        best = Submission.query.filter_by(
            user_id=user_id, assignment_id=assignment.id
        ).order_by(Submission.score.desc()).first()
        if not best or best.score <= 0:
            return False

    for lesson in lessons:
        completion = LessonCompletion.query.filter_by(
            user_id=user_id, lesson_id=lesson.id
        ).first()
        if not completion:
            return False

    return True


def check_course_complete(user_id):
    """Check if a user has completed ALL chapters."""
    chapters = Chapter.query.all()
    if not chapters:
        return False
    return all(check_chapter_complete(user_id, ch.id) for ch in chapters)


@certificates_bp.route('/claim/chapter/<int:chapter_id>', methods=['POST'])
@login_required
def claim_chapter_certificate(chapter_id):
    """Claim a chapter completion certificate."""
    existing = Certificate.query.filter_by(
        user_id=current_user.id, chapter_id=chapter_id
    ).first()
    if existing:
        return redirect(url_for('certificates.view_certificate', token=existing.token))

    if not check_chapter_complete(current_user.id, chapter_id):
        flash('You have not yet completed all assignments and lessons in this chapter.', 'warning')
        return redirect(url_for('dashboard.overview'))

    cert = Certificate(
        user_id=current_user.id,
        chapter_id=chapter_id,
        certificate_type='chapter',
    )
    db.session.add(cert)
    db.session.commit()

    flash('Congratulations! Your certificate has been issued.', 'success')
    return redirect(url_for('certificates.view_certificate', token=cert.token))


@certificates_bp.route('/claim/course', methods=['POST'])
@login_required
def claim_course_certificate():
    """Claim the full course completion certificate."""
    existing = Certificate.query.filter_by(
        user_id=current_user.id, chapter_id=None, certificate_type='course'
    ).first()
    if existing:
        return redirect(url_for('certificates.view_certificate', token=existing.token))

    if not check_course_complete(current_user.id):
        flash('You have not yet completed all chapters.', 'warning')
        return redirect(url_for('dashboard.overview'))

    cert = Certificate(
        user_id=current_user.id,
        chapter_id=None,
        certificate_type='course',
    )
    db.session.add(cert)
    db.session.commit()

    flash('Congratulations! Your full course completion certificate has been issued.', 'success')
    return redirect(url_for('certificates.view_certificate', token=cert.token))


@certificates_bp.route('/<token>')
def view_certificate(token):
    """Public certificate view page — no login required."""
    cert = Certificate.query.filter_by(token=token).first_or_404()

    share_url = url_for('certificates.view_certificate', token=token, _external=True)

    if cert.certificate_type == 'chapter' and cert.chapter:
        title = f'Chapter {cert.chapter.order}: {cert.chapter.title} — Completion Certificate'
        description = f'{cert.user.username} completed Chapter {cert.chapter.order}: {cert.chapter.title} on the Python Learning Tool.'
    else:
        title = 'Python Learning Tool — Full Course Completion Certificate'
        description = f'{cert.user.username} completed the entire Python Learning Tool curriculum covering Python fundamentals through data science and machine learning.'

    return render_template(
        'certificates/view.html',
        cert=cert,
        cert_title=title,
        cert_description=description,
        share_url=share_url,
    )
