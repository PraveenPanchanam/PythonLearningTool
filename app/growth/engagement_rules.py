"""
Engagement rules engine — rule-based user engagement automation.

Each rule is a function that checks conditions in the database and triggers
actions (usually emails). All rules are idempotent and have cooldown checks
to avoid spamming users.
"""

import json
import logging
from datetime import datetime, timedelta

from app.extensions import db
from app.models.user import User
from app.models.submission import Submission
from app.models.assignment import Assignment
from app.models.lesson import Lesson
from app.models.lesson_completion import LessonCompletion
from app.models.chapter import Chapter
from app.models.certificate import Certificate
from app.models.engagement_event import EngagementEvent

logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────

def _has_recent_event(user_id, event_type, cooldown_days=7):
    """Check if a user already received this event type within cooldown period."""
    cutoff = datetime.utcnow() - timedelta(days=cooldown_days)
    return EngagementEvent.query.filter(
        EngagementEvent.user_id == user_id,
        EngagementEvent.event_type == event_type,
        EngagementEvent.created_at >= cutoff,
    ).first() is not None


def _log_event(user_id, event_type, data=None):
    """Log an engagement event."""
    event = EngagementEvent(
        user_id=user_id,
        event_type=event_type,
        event_data=json.dumps(data) if data else None,
    )
    db.session.add(event)
    return event


def _send_email(app, recipient_email, subject, html_body, text_body=None):
    """Send an email using Flask-Mail. Returns True on success."""
    try:
        from flask_mail import Message
        from app.extensions import mail

        msg = Message(
            subject=subject,
            recipients=[recipient_email],
            html=html_body,
            body=text_body or subject,
        )
        mail.send(msg)
        return True
    except Exception as e:
        logger.warning(f'Email send failed to {recipient_email}: {e}')
        return False


# ──────────────────────────────────────────────────────────
# Individual Rules
# ──────────────────────────────────────────────────────────

def rule_welcome_email(app):
    """Send welcome email to new users who haven't received one."""
    from app.growth.email_templates import render_welcome_email

    users = User.query.filter_by(welcome_email_sent=False).all()
    count = 0

    for user in users:
        if _has_recent_event(user.id, EngagementEvent.WELCOME_EMAIL, cooldown_days=365):
            continue

        subject, html, text = render_welcome_email(user, app)
        if _send_email(app, user.email, subject, html, text):
            user.welcome_email_sent = True
            _log_event(user.id, EngagementEvent.WELCOME_EMAIL)
            count += 1
            logger.info(f'Welcome email sent to {user.username}')

    if count:
        db.session.commit()
    return count


def send_welcome_email(user):
    """Immediate welcome email send — called from registration route."""
    from flask import current_app
    from app.growth.email_templates import render_welcome_email

    app = current_app._get_current_object()
    subject, html, text = render_welcome_email(user, app)
    if _send_email(app, user.email, subject, html, text):
        user.welcome_email_sent = True
        _log_event(user.id, EngagementEvent.WELCOME_EMAIL)
        db.session.commit()
        logger.info(f'Welcome email sent to {user.username} (on registration)')


def rule_inactive_nudge(app):
    """Nudge users who haven't been active for 7+ days."""
    from app.growth.email_templates import render_nudge_email

    cutoff = datetime.utcnow() - timedelta(days=7)
    min_age = datetime.utcnow() - timedelta(days=3)

    users = User.query.filter(
        User.created_at <= min_age,  # Registered > 3 days ago
        User.is_admin == False,  # noqa: E712
        db.or_(
            User.last_active_at <= cutoff,
            User.last_active_at == None,  # noqa: E711
        )
    ).all()

    count = 0
    for user in users:
        if _has_recent_event(user.id, EngagementEvent.INACTIVE_NUDGE, cooldown_days=14):
            continue

        # Calculate days inactive
        if user.last_active_at:
            days_inactive = (datetime.utcnow() - user.last_active_at).days
        else:
            days_inactive = (datetime.utcnow() - user.created_at).days

        subject, html, text = render_nudge_email(user, days_inactive, app)
        if _send_email(app, user.email, subject, html, text):
            _log_event(user.id, EngagementEvent.INACTIVE_NUDGE,
                       {'days_inactive': days_inactive})
            count += 1
            logger.info(f'Inactive nudge sent to {user.username} ({days_inactive}d)')

    if count:
        db.session.commit()
    return count


def rule_chapter_milestone(app):
    """Congratulate users who just completed a chapter."""
    from app.growth.email_templates import render_milestone_email

    chapters = Chapter.query.order_by(Chapter.order).all()
    count = 0

    for chapter in chapters:
        assignments = Assignment.query.filter_by(chapter_id=chapter.id).all()
        lessons = Lesson.query.filter_by(chapter_id=chapter.id).all()

        if not assignments and not lessons:
            continue

        # Find users who have a passing submission for ALL assignments in this chapter
        # and have completed ALL lessons
        for user in User.query.filter_by(is_admin=False).all():
            # Skip if already has certificate for this chapter
            if Certificate.query.filter_by(user_id=user.id, chapter_id=chapter.id).first():
                continue

            if _has_recent_event(user.id, EngagementEvent.CHAPTER_MILESTONE, cooldown_days=1):
                continue

            # Check all assignments passed
            all_assignments_passed = True
            for assignment in assignments:
                passing = Submission.query.filter(
                    Submission.user_id == user.id,
                    Submission.assignment_id == assignment.id,
                    Submission.score > 0,
                ).first()
                if not passing:
                    all_assignments_passed = False
                    break

            if not all_assignments_passed:
                continue

            # Check all lessons completed
            all_lessons_done = True
            for lesson in lessons:
                completion = LessonCompletion.query.filter_by(
                    user_id=user.id, lesson_id=lesson.id
                ).first()
                if not completion:
                    all_lessons_done = False
                    break

            if not all_lessons_done:
                continue

            # User completed this chapter!
            subject, html, text = render_milestone_email(user, chapter, app)
            if _send_email(app, user.email, subject, html, text):
                _log_event(user.id, EngagementEvent.CHAPTER_MILESTONE,
                           {'chapter_id': chapter.id, 'chapter_title': chapter.title})
                count += 1
                logger.info(f'Milestone email sent to {user.username} for {chapter.title}')

    if count:
        db.session.commit()
    return count


def rule_first_assignment_nudge(app):
    """Encourage users who registered 2+ days ago but have zero submissions."""
    from app.growth.email_templates import render_first_assignment_email

    cutoff = datetime.utcnow() - timedelta(days=2)

    users = User.query.filter(
        User.created_at <= cutoff,
        User.is_admin == False,  # noqa: E712
    ).all()

    count = 0
    for user in users:
        # Skip if they have any submissions
        if Submission.query.filter_by(user_id=user.id).first():
            continue

        if _has_recent_event(user.id, EngagementEvent.FIRST_ASSIGNMENT_NUDGE, cooldown_days=7):
            continue

        subject, html, text = render_first_assignment_email(user, app)
        if _send_email(app, user.email, subject, html, text):
            _log_event(user.id, EngagementEvent.FIRST_ASSIGNMENT_NUDGE)
            count += 1
            logger.info(f'First assignment nudge sent to {user.username}')

    if count:
        db.session.commit()
    return count


def rule_streak_celebration(app):
    """Celebrate users who have been active 5+ consecutive days."""
    count = 0
    now = datetime.utcnow()

    users = User.query.filter(
        User.last_active_at >= now - timedelta(days=1),
        User.is_admin == False,  # noqa: E712
    ).all()

    for user in users:
        if _has_recent_event(user.id, EngagementEvent.STREAK_CELEBRATION, cooldown_days=7):
            continue

        # Check if user was active each of the last 5 days
        # We use engagement events and last_active_at as proxies
        if not user.last_active_at:
            continue

        # Simple heuristic: if user's created_at is > 5 days ago
        # and last_active_at is within 24h, log a streak event
        # (A full streak check would need daily activity tracking)
        if (now - user.created_at).days >= 5:
            submissions_last_5_days = Submission.query.filter(
                Submission.user_id == user.id,
                Submission.submitted_at >= now - timedelta(days=5),
            ).count()

            if submissions_last_5_days >= 3:  # Active enough
                _log_event(user.id, EngagementEvent.STREAK_CELEBRATION,
                           {'submissions_5d': submissions_last_5_days})
                count += 1
                logger.info(f'Streak celebration for {user.username}')

    if count:
        db.session.commit()
    return count


def rule_stuck_on_assignment(app):
    """Nudge users who have 3+ failed attempts on the same assignment."""
    from app.growth.email_templates import render_stuck_email

    count = 0

    # Find users with multiple failed attempts (score=0) and no passing attempt
    from sqlalchemy import func

    stuck_users = db.session.query(
        Submission.user_id,
        Submission.assignment_id,
        func.count(Submission.id).label('attempts')
    ).filter(
        Submission.score == 0
    ).group_by(
        Submission.user_id, Submission.assignment_id
    ).having(
        func.count(Submission.id) >= 3
    ).all()

    for user_id, assignment_id, attempts in stuck_users:
        # Skip if they eventually passed
        passed = Submission.query.filter(
            Submission.user_id == user_id,
            Submission.assignment_id == assignment_id,
            Submission.score > 0,
        ).first()
        if passed:
            continue

        if _has_recent_event(user_id, EngagementEvent.STUCK_NUDGE, cooldown_days=7):
            continue

        user = User.query.get(user_id)
        assignment = Assignment.query.get(assignment_id)
        if not user or not assignment:
            continue

        subject, html, text = render_stuck_email(user, assignment, attempts, app)
        if _send_email(app, user.email, subject, html, text):
            _log_event(user.id, EngagementEvent.STUCK_NUDGE,
                       {'assignment_id': assignment_id, 'attempts': attempts})
            count += 1
            logger.info(f'Stuck nudge sent to {user.username} on {assignment.title}')

    if count:
        db.session.commit()
    return count


def rule_returning_user(app):
    """Welcome back users who were inactive 14+ days and returned today."""
    from app.growth.email_templates import render_reengagement_email

    now = datetime.utcnow()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    users = User.query.filter(
        User.last_active_at >= today_start,
        User.is_admin == False,  # noqa: E712
    ).all()

    count = 0
    for user in users:
        if _has_recent_event(user.id, EngagementEvent.RETURNING_USER, cooldown_days=30):
            continue

        # Check if there's an inactive_nudge event (meaning they were inactive)
        nudge = EngagementEvent.query.filter(
            EngagementEvent.user_id == user.id,
            EngagementEvent.event_type == EngagementEvent.INACTIVE_NUDGE,
        ).order_by(EngagementEvent.created_at.desc()).first()

        if not nudge:
            continue

        # They were nudged for inactivity and are now back
        subject, html, text = render_reengagement_email(user, app)
        if _send_email(app, user.email, subject, html, text):
            _log_event(user.id, EngagementEvent.RETURNING_USER)
            count += 1
            logger.info(f'Returning user email sent to {user.username}')

    if count:
        db.session.commit()
    return count


# ──────────────────────────────────────────────────────────
# Run All Rules
# ──────────────────────────────────────────────────────────

ALL_RULES = [
    ('welcome_email', rule_welcome_email),
    ('inactive_nudge', rule_inactive_nudge),
    ('chapter_milestone', rule_chapter_milestone),
    ('first_assignment_nudge', rule_first_assignment_nudge),
    ('streak_celebration', rule_streak_celebration),
    ('stuck_on_assignment', rule_stuck_on_assignment),
    ('returning_user', rule_returning_user),
]


def run_all_rules(app):
    """Run all engagement rules and return summary dict."""
    results = {}
    for name, rule_fn in ALL_RULES:
        try:
            count = rule_fn(app)
            results[name] = count
            logger.info(f'Rule {name}: {count} actions')
        except Exception as e:
            results[name] = f'ERROR: {e}'
            logger.error(f'Rule {name} failed: {e}', exc_info=True)
    return results
