from datetime import datetime, timedelta
from functools import wraps

from flask import Blueprint, render_template, abort, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from sqlalchemy import func

from app.extensions import db
from app.models.user import User
from app.models.chapter import Chapter
from app.models.assignment import Assignment
from app.models.submission import Submission
from app.models.lesson import Lesson
from app.models.lesson_completion import LessonCompletion
from app.models.nudge import Nudge
from app.models.feedback import Feedback
from app.models.blog_post import BlogPost

admin_bp = Blueprint('admin', __name__)

# ── Predefined nudge templates ──────────────────────────────────
NUDGE_TEMPLATES = {
    'encouragement': [
        "🌟 Great start! Keep up the momentum — you're doing awesome!",
        "💪 You've got this! Every lesson brings you closer to mastering Python.",
        "🎉 Amazing progress so far! Don't stop now — the best is yet to come.",
    ],
    'reminder': [
        "👋 Hey! We miss you. Jump back in and pick up where you left off!",
        "📚 It's been a while! Your Python journey is waiting — come back and continue learning.",
        "⏰ Don't let your progress fade! A quick lesson today can make a big difference.",
    ],
    'milestone': [
        "🏆 You're so close to completing this chapter! Push through the finish line!",
        "🚀 Almost halfway through the course! Keep going — you're building real skills.",
        "⭐ You've completed multiple chapters! That's a huge achievement. What's next?",
    ],
}


def admin_required(f):
    """Decorator that requires the current user to be an admin."""
    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated


def geolocate_ip(ip):
    """Resolve IP to 'City, Country' using free ip-api.com."""
    if not ip or ip in ('127.0.0.1', '::1', 'localhost', '172.', '10.', '192.168.'):
        return 'Local'
    # Skip private IPs
    if ip.startswith(('172.', '10.', '192.168.')):
        return 'Local'
    try:
        import requests as http_requests
        resp = http_requests.get(
            f'http://ip-api.com/json/{ip}?fields=city,country',
            timeout=2
        )
        if resp.status_code == 200:
            data = resp.json()
            city = data.get('city', '')
            country = data.get('country', '')
            if city and country:
                return f'{city}, {country}'
            return country or 'Unknown'
    except Exception:
        pass
    return 'Unknown'


def get_activity_status(last_active_at):
    """Return activity status string based on last active time."""
    if not last_active_at:
        return 'away'
    diff = (datetime.utcnow() - last_active_at).total_seconds()
    if diff < 300:      # 5 minutes
        return 'online'
    if diff < 86400:    # 24 hours
        return 'today'
    return 'away'


@admin_bp.route('/')
@admin_required
def admin_dashboard():
    now = datetime.utcnow()
    total_students = User.query.filter_by(is_admin=False).count()
    total_submissions = Submission.query.count()
    total_lessons_completed = LessonCompletion.query.count()
    total_lessons = Lesson.query.count()

    # Activity counts
    active_now = User.query.filter(
        User.is_admin == False,
        User.last_active_at >= now - timedelta(minutes=5)
    ).count()
    active_today = User.query.filter(
        User.is_admin == False,
        User.last_active_at >= now - timedelta(hours=24)
    ).count()
    active_week = User.query.filter(
        User.is_admin == False,
        User.last_active_at >= now - timedelta(days=7)
    ).count()

    # Recently active users (last 10)
    recent_active_users = User.query.filter(
        User.is_admin == False,
        User.last_active_at.isnot(None)
    ).order_by(User.last_active_at.desc()).limit(10).all()

    recent_user_data = []
    for user in recent_active_users:
        # Resolve geolocation lazily
        if user.last_ip and not user.last_location:
            user.last_location = geolocate_ip(user.last_ip)
            db.session.commit()

        lesson_count = LessonCompletion.query.filter_by(user_id=user.id).count()
        progress = round(lesson_count / total_lessons * 100, 1) if total_lessons > 0 else 0

        recent_user_data.append({
            'user': user,
            'status': get_activity_status(user.last_active_at),
            'progress': progress,
            'lesson_count': lesson_count,
        })

    # Chapter stats
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
        total_lessons=total_lessons,
        active_now=active_now,
        active_today=active_today,
        active_week=active_week,
        recent_active_users=recent_user_data,
        chapter_stats=chapter_stats,
    )


@admin_bp.route('/students')
@admin_required
def student_list():
    now = datetime.utcnow()
    filter_type = request.args.get('filter', 'all')
    total_lessons = Lesson.query.count()

    query = User.query.filter_by(is_admin=False)

    if filter_type == 'today':
        query = query.filter(User.last_active_at >= now - timedelta(hours=24))
    elif filter_type == 'week':
        query = query.filter(User.last_active_at >= now - timedelta(days=7))
    elif filter_type == 'inactive':
        query = query.filter(
            db.or_(
                User.last_active_at.is_(None),
                User.last_active_at < now - timedelta(days=7)
            )
        )

    # Sort by last_active_at (most recent first), nulls last
    students = query.order_by(
        db.case((User.last_active_at.is_(None), 1), else_=0),
        User.last_active_at.desc()
    ).all()

    student_data = []
    for student in students:
        # Resolve geolocation lazily
        if student.last_ip and not student.last_location:
            student.last_location = geolocate_ip(student.last_ip)
            db.session.commit()

        sub_count = Submission.query.filter_by(user_id=student.id).count()
        lesson_count = LessonCompletion.query.filter_by(user_id=student.id).count()
        avg_score = db.session.query(func.avg(Submission.score)).filter_by(
            user_id=student.id
        ).scalar() or 0
        progress = round(lesson_count / total_lessons * 100, 1) if total_lessons > 0 else 0

        # Count unread nudges for this student
        unread_nudges = Nudge.query.filter_by(user_id=student.id, read_at=None).count()

        student_data.append({
            'user': student,
            'submission_count': sub_count,
            'lesson_count': lesson_count,
            'avg_score': round(avg_score, 1),
            'progress': progress,
            'status': get_activity_status(student.last_active_at),
            'unread_nudges': unread_nudges,
        })

    return render_template(
        'admin/students.html',
        students=student_data,
        filter_type=filter_type,
        total_lessons=total_lessons,
    )


@admin_bp.route('/students/<int:user_id>')
@admin_required
def student_detail(user_id):
    student = db.session.get(User, user_id)
    if not student:
        abort(404)

    total_lessons = Lesson.query.count()

    # Resolve geolocation lazily
    if student.last_ip and not student.last_location:
        student.last_location = geolocate_ip(student.last_ip)
        db.session.commit()

    chapters = Chapter.query.order_by(Chapter.order).all()
    chapter_progress = []
    total_completed_lessons = 0
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
        total_completed_lessons += completed_lessons

        chapter_progress.append({
            'chapter': chapter,
            'total_assignments': len(assignments),
            'completed_assignments': completed_assignments,
            'avg_score': round(total_score / completed_assignments, 1) if completed_assignments > 0 else 0,
            'total_lessons': len(lessons),
            'completed_lessons': completed_lessons,
        })

    overall_progress = round(total_completed_lessons / total_lessons * 100, 1) if total_lessons > 0 else 0

    recent_submissions = Submission.query.filter_by(user_id=user_id).order_by(
        Submission.submitted_at.desc()
    ).limit(20).all()

    # Get nudge history for this student
    nudges = Nudge.query.filter_by(user_id=user_id).order_by(
        Nudge.created_at.desc()
    ).limit(10).all()

    return render_template(
        'admin/student_detail.html',
        student=student,
        chapter_progress=chapter_progress,
        recent_submissions=recent_submissions,
        overall_progress=overall_progress,
        total_completed_lessons=total_completed_lessons,
        total_lessons=total_lessons,
        status=get_activity_status(student.last_active_at),
        nudges=nudges,
        nudge_templates=NUDGE_TEMPLATES,
    )


@admin_bp.route('/nudge/<int:user_id>', methods=['POST'])
@admin_required
def send_nudge(user_id):
    """Send a motivational nudge to a student."""
    student = db.session.get(User, user_id)
    if not student:
        abort(404)

    message = request.form.get('message', '').strip()
    nudge_type = request.form.get('nudge_type', 'encouragement')

    if not message:
        flash('Please provide a message.', 'warning')
        return redirect(url_for('admin.student_detail', user_id=user_id))

    nudge = Nudge(
        user_id=user_id,
        message=message,
        nudge_type=nudge_type,
    )
    db.session.add(nudge)
    db.session.commit()

    flash(f'Nudge sent to {student.username}! 🎯', 'success')
    return redirect(url_for('admin.student_detail', user_id=user_id))


@admin_bp.route('/nudge/bulk', methods=['POST'])
@admin_required
def send_bulk_nudge():
    """Send a nudge to multiple students at once (e.g., all inactive)."""
    message = request.form.get('message', '').strip()
    nudge_type = request.form.get('nudge_type', 'reminder')
    target = request.form.get('target', 'inactive')  # 'inactive', 'all'

    if not message:
        flash('Please provide a message.', 'warning')
        return redirect(url_for('admin.student_list'))

    now = datetime.utcnow()
    if target == 'inactive':
        students = User.query.filter(
            User.is_admin == False,
            db.or_(
                User.last_active_at.is_(None),
                User.last_active_at < now - timedelta(days=7)
            )
        ).all()
    else:
        students = User.query.filter_by(is_admin=False).all()

    count = 0
    for student in students:
        nudge = Nudge(
            user_id=student.id,
            message=message,
            nudge_type=nudge_type,
        )
        db.session.add(nudge)
        count += 1

    db.session.commit()
    flash(f'Nudge sent to {count} students! 🎯', 'success')
    return redirect(url_for('admin.student_list'))


@admin_bp.route('/api/nudge-templates')
@admin_required
def get_nudge_templates():
    """API endpoint to get nudge templates by type."""
    nudge_type = request.args.get('type', 'encouragement')
    templates = NUDGE_TEMPLATES.get(nudge_type, NUDGE_TEMPLATES['encouragement'])
    return jsonify(templates)


# ── Feedback Management ────────────────────────────────────────
@admin_bp.route('/feedback')
@admin_required
def feedback_list():
    """View all user feedback."""
    feedback_items = Feedback.query.order_by(Feedback.created_at.desc()).all()
    avg_rating = db.session.query(func.avg(Feedback.rating)).scalar()
    total_count = len(feedback_items)
    return render_template(
        'admin/feedback.html',
        feedback=feedback_items,
        avg_rating=round(avg_rating, 1) if avg_rating else 0,
        total_count=total_count,
    )


# ── Blog Management ────────────────────────────────────────

@admin_bp.route('/blog')
@admin_required
def blog_list():
    """Admin view of all blog posts (published and drafts)."""
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('admin/blog_list.html', posts=posts)


@admin_bp.route('/blog/new', methods=['GET', 'POST'])
@admin_required
def blog_create():
    """Create a new blog post."""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        meta_description = request.form.get('meta_description', '').strip()
        tags = request.form.get('tags', '').strip()
        is_published = request.form.get('is_published') == 'on'

        errors = []
        if not title or len(title) < 5:
            errors.append('Title must be at least 5 characters.')
        if not content or len(content) < 50:
            errors.append('Content must be at least 50 characters.')

        slug = BlogPost.generate_slug(title)
        if BlogPost.query.filter_by(slug=slug).first():
            errors.append('A post with a similar title already exists.')

        if errors:
            for e in errors:
                flash(e, 'danger')
            return render_template('admin/blog_form.html',
                                   post=None, form_title=title, form_content=content,
                                   form_meta=meta_description, form_tags=tags)

        post = BlogPost(
            title=title,
            slug=slug,
            content=content,
            meta_description=meta_description or title,
            tags=tags,
            author_id=current_user.id,
            is_published=is_published,
            published_at=datetime.utcnow() if is_published else None,
        )
        db.session.add(post)
        db.session.commit()

        flash('Blog post created successfully!', 'success')
        return redirect(url_for('admin.blog_list'))

    return render_template('admin/blog_form.html', post=None)


@admin_bp.route('/blog/<int:post_id>/edit', methods=['GET', 'POST'])
@admin_required
def blog_edit(post_id):
    """Edit an existing blog post."""
    post = db.session.get(BlogPost, post_id)
    if not post:
        abort(404)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        meta_description = request.form.get('meta_description', '').strip()
        tags = request.form.get('tags', '').strip()
        is_published = request.form.get('is_published') == 'on'

        errors = []
        if not title or len(title) < 5:
            errors.append('Title must be at least 5 characters.')
        if not content or len(content) < 50:
            errors.append('Content must be at least 50 characters.')

        new_slug = BlogPost.generate_slug(title)
        existing = BlogPost.query.filter_by(slug=new_slug).first()
        if existing and existing.id != post.id:
            errors.append('A post with a similar title already exists.')

        if errors:
            for e in errors:
                flash(e, 'danger')
            return render_template('admin/blog_form.html', post=post)

        post.title = title
        post.slug = new_slug
        post.content = content
        post.meta_description = meta_description or title
        post.tags = tags

        was_published = post.is_published
        post.is_published = is_published
        if is_published and not was_published:
            post.published_at = datetime.utcnow()

        db.session.commit()
        flash('Blog post updated successfully!', 'success')
        return redirect(url_for('admin.blog_list'))

    return render_template('admin/blog_form.html', post=post)


@admin_bp.route('/blog/<int:post_id>/delete', methods=['POST'])
@admin_required
def blog_delete(post_id):
    """Delete a blog post."""
    post = db.session.get(BlogPost, post_id)
    if not post:
        abort(404)
    db.session.delete(post)
    db.session.commit()
    flash('Blog post deleted.', 'info')
    return redirect(url_for('admin.blog_list'))
