"""
Growth admin dashboard — analytics, content calendar, and engagement monitoring.

All routes require admin login.
"""

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from app.extensions import db
from app.models.blog_post import BlogPost
from app.models.user import User
from app.growth.analytics import (
    get_growth_kpis,
    get_registration_trend,
    get_chapter_completion_funnel,
    get_drop_off_points,
    get_blog_analytics,
    get_engagement_summary,
)

growth_admin_bp = Blueprint('growth_admin', __name__)


def _admin_required(f):
    """Decorator to require admin access."""
    from functools import wraps

    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            flash('Admin access required.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated


@growth_admin_bp.route('/')
@_admin_required
def growth_dashboard():
    """Main growth analytics dashboard."""
    days = request.args.get('days', 30, type=int)

    kpis = get_growth_kpis(days=days)
    trend = get_registration_trend(days=days)
    funnel = get_chapter_completion_funnel()
    drop_offs = get_drop_off_points()
    blog_stats = get_blog_analytics()
    engagement = get_engagement_summary(days=days)

    return render_template('admin/growth_dashboard.html',
                           kpis=kpis,
                           trend=trend,
                           funnel=funnel,
                           drop_offs=drop_offs,
                           blog_stats=blog_stats[:10],
                           engagement=engagement,
                           selected_days=days)


@growth_admin_bp.route('/content')
@_admin_required
def content_calendar():
    """Content calendar — published, scheduled, and queued posts."""
    from app.growth.content_pipeline import get_pending_posts

    published = BlogPost.query.filter_by(is_published=True).order_by(
        BlogPost.published_at.desc()
    ).all()

    scheduled = BlogPost.query.filter(
        BlogPost.scheduled_at != None,  # noqa: E711
        BlogPost.is_published == False,  # noqa: E712
    ).order_by(BlogPost.scheduled_at.asc()).all()

    pending = get_pending_posts()

    return render_template('admin/content_calendar.html',
                           published=published,
                           scheduled=scheduled,
                           pending=pending)


@growth_admin_bp.route('/content/publish-next', methods=['POST'])
@_admin_required
def publish_next():
    """Manually publish the next queued post."""
    from app.growth.content_pipeline import publish_next_post

    admin = User.query.filter_by(is_admin=True).first()
    author_id = admin.id if admin else None

    post = publish_next_post(author_id=author_id)
    if post:
        flash(f'Published: "{post.title}"', 'success')
    else:
        flash('No pending posts to publish.', 'info')

    return redirect(url_for('growth_admin.content_calendar'))


@growth_admin_bp.route('/engagement')
@_admin_required
def engagement_rules():
    """Engagement rule monitoring and history."""
    days = request.args.get('days', 30, type=int)
    engagement = get_engagement_summary(days=days)

    # Rule descriptions for display
    rule_descriptions = {
        'welcome_email': 'Sends a welcome email with learning path overview to new registrations',
        'inactive_nudge': 'Emails users inactive for 7+ days with encouragement to return',
        'chapter_milestone': 'Congratulates users who complete all assignments and lessons in a chapter',
        'first_assignment_nudge': 'Encourages users who registered 2+ days ago but have zero submissions',
        'streak_celebration': 'Recognizes users active 5+ consecutive days',
        'stuck_nudge': 'Helps users with 3+ failed attempts on the same assignment',
        'returning_user': 'Welcomes back users who were inactive 14+ days and returned',
    }

    return render_template('admin/engagement_rules.html',
                           engagement=engagement,
                           rule_descriptions=rule_descriptions,
                           selected_days=days)


@growth_admin_bp.route('/engagement/run', methods=['POST'])
@_admin_required
def run_engagement_now():
    """Manually trigger all engagement rules."""
    from flask import current_app
    from app.growth.engagement_rules import run_all_rules

    app = current_app._get_current_object()
    results = run_all_rules(app)

    total = sum(v for v in results.values() if isinstance(v, int))
    flash(f'Engagement rules executed: {total} total actions taken.', 'success')
    return redirect(url_for('growth_admin.engagement_rules'))
