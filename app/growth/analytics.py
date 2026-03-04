"""
Growth analytics — KPIs, funnels, and trend data for the admin dashboard.
"""

from datetime import datetime, timedelta
from collections import defaultdict

from sqlalchemy import func

from app.extensions import db
from app.models.user import User
from app.models.submission import Submission
from app.models.chapter import Chapter
from app.models.assignment import Assignment
from app.models.lesson import Lesson
from app.models.lesson_completion import LessonCompletion
from app.models.certificate import Certificate
from app.models.blog_post import BlogPost
from app.models.blog_post_view import BlogPostView
from app.models.engagement_event import EngagementEvent


def get_growth_kpis(days=30):
    """Return key performance indicators for the growth dashboard."""
    cutoff = datetime.utcnow() - timedelta(days=days)

    new_registrations = User.query.filter(
        User.created_at >= cutoff,
        User.is_admin == False,  # noqa: E712
    ).count()

    active_users = User.query.filter(
        User.last_active_at >= cutoff,
        User.is_admin == False,  # noqa: E712
    ).count()

    total_submissions = Submission.query.filter(
        Submission.submitted_at >= cutoff
    ).count()

    passing_submissions = Submission.query.filter(
        Submission.submitted_at >= cutoff,
        Submission.score > 0,
    ).count()

    pass_rate = (passing_submissions / total_submissions * 100) if total_submissions > 0 else 0

    blog_views = BlogPostView.query.filter(
        BlogPostView.viewed_at >= cutoff
    ).count()

    certificates_issued = Certificate.query.filter(
        Certificate.issued_at >= cutoff
    ).count()

    total_users = User.query.filter_by(is_admin=False).count()

    return {
        'new_registrations': new_registrations,
        'active_users': active_users,
        'total_users': total_users,
        'total_submissions': total_submissions,
        'passing_submissions': passing_submissions,
        'pass_rate': round(pass_rate, 1),
        'blog_views': blog_views,
        'certificates_issued': certificates_issued,
        'period_days': days,
    }


def get_registration_trend(days=30):
    """Return daily registration counts for the last N days."""
    cutoff = datetime.utcnow() - timedelta(days=days)

    results = db.session.query(
        func.date(User.created_at).label('date'),
        func.count(User.id).label('count'),
    ).filter(
        User.created_at >= cutoff,
        User.is_admin == False,  # noqa: E712
    ).group_by(
        func.date(User.created_at)
    ).order_by(
        func.date(User.created_at)
    ).all()

    # Fill in missing days with 0
    trend = {}
    for i in range(days):
        day = (datetime.utcnow() - timedelta(days=days - 1 - i)).strftime('%Y-%m-%d')
        trend[day] = 0

    for row in results:
        day_str = str(row.date)
        if day_str in trend:
            trend[day_str] = row.count

    return trend


def get_chapter_completion_funnel():
    """Return users who started vs completed each chapter."""
    chapters = Chapter.query.order_by(Chapter.order).all()
    funnel = []

    for chapter in chapters:
        assignments = Assignment.query.filter_by(chapter_id=chapter.id).all()
        assignment_ids = [a.id for a in assignments]

        lessons = Lesson.query.filter_by(chapter_id=chapter.id).all()
        lesson_ids = [l.id for l in lessons]

        # Users who attempted at least one assignment
        started = 0
        if assignment_ids:
            started = db.session.query(
                func.count(func.distinct(Submission.user_id))
            ).filter(
                Submission.assignment_id.in_(assignment_ids)
            ).scalar() or 0

        # Users who passed all assignments AND completed all lessons
        completed = 0
        if assignment_ids or lesson_ids:
            all_users = User.query.filter_by(is_admin=False).all()
            for user in all_users:
                # Check assignments
                all_passed = True
                for a_id in assignment_ids:
                    passed = Submission.query.filter(
                        Submission.user_id == user.id,
                        Submission.assignment_id == a_id,
                        Submission.score > 0,
                    ).first()
                    if not passed:
                        all_passed = False
                        break

                if not all_passed:
                    continue

                # Check lessons
                all_lessons = True
                for l_id in lesson_ids:
                    done = LessonCompletion.query.filter_by(
                        user_id=user.id, lesson_id=l_id
                    ).first()
                    if not done:
                        all_lessons = False
                        break

                if all_passed and all_lessons:
                    completed += 1

        funnel.append({
            'chapter_id': chapter.id,
            'chapter_title': chapter.title,
            'order': chapter.order,
            'started': started,
            'completed': completed,
            'completion_rate': round(completed / started * 100, 1) if started > 0 else 0,
        })

    return funnel


def get_drop_off_points():
    """Identify chapters where users stop progressing."""
    funnel = get_chapter_completion_funnel()
    drop_offs = []

    for i in range(1, len(funnel)):
        prev_completed = funnel[i - 1]['completed']
        curr_started = funnel[i]['started']

        if prev_completed > 0:
            retention = (curr_started / prev_completed * 100) if prev_completed > 0 else 0
            drop_offs.append({
                'from_chapter': funnel[i - 1]['chapter_title'],
                'to_chapter': funnel[i]['chapter_title'],
                'prev_completed': prev_completed,
                'next_started': curr_started,
                'retention_pct': round(retention, 1),
                'drop_off_pct': round(100 - retention, 1),
            })

    return drop_offs


def get_blog_analytics():
    """Return analytics for blog posts."""
    posts = BlogPost.query.filter_by(is_published=True).order_by(
        BlogPost.view_count.desc()
    ).all()

    return [{
        'id': post.id,
        'title': post.title,
        'slug': post.slug,
        'view_count': post.view_count,
        'category': post.category,
        'published_at': post.published_at,
        'tags': post.tag_list,
    } for post in posts]


def get_engagement_summary(days=30):
    """Return counts of each engagement event type."""
    cutoff = datetime.utcnow() - timedelta(days=days)

    results = db.session.query(
        EngagementEvent.event_type,
        func.count(EngagementEvent.id).label('count'),
    ).filter(
        EngagementEvent.created_at >= cutoff
    ).group_by(
        EngagementEvent.event_type
    ).all()

    summary = {r.event_type: r.count for r in results}

    # Recent events log
    recent = EngagementEvent.query.filter(
        EngagementEvent.created_at >= cutoff
    ).order_by(
        EngagementEvent.created_at.desc()
    ).limit(50).all()

    return {
        'counts': summary,
        'total': sum(summary.values()),
        'recent_events': recent,
    }
