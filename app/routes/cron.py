"""
Cron endpoints — secret-protected HTTP endpoints for GitHub Actions to trigger.

All endpoints require ?secret=CRON_SECRET query parameter for authentication.
"""

import logging
from flask import Blueprint, request, jsonify, current_app
from app.extensions import csrf

logger = logging.getLogger(__name__)

cron_bp = Blueprint('cron', __name__)

# Exempt all cron endpoints from CSRF — they use secret-based authentication
csrf.exempt(cron_bp)


def _check_secret():
    """Validate the cron secret. Returns error response or None."""
    expected = current_app.config.get('CRON_SECRET')
    if not expected:
        return jsonify({'error': 'CRON_SECRET not configured'}), 503

    provided = request.args.get('secret', '')
    if provided != expected:
        return jsonify({'error': 'Invalid secret'}), 403

    return None


@cron_bp.route('/publish', methods=['POST'])
def cron_publish():
    """Publish scheduled blog posts."""
    error = _check_secret()
    if error:
        return error

    from app.growth.content_pipeline import publish_scheduled_posts, publish_next_post
    from app.models.user import User

    # First, publish any posts that are past their scheduled_at time
    scheduled_count = publish_scheduled_posts()

    # Also publish the next pre-written post if none were scheduled
    next_post = None
    if scheduled_count == 0:
        admin = User.query.filter_by(is_admin=True).first()
        author_id = admin.id if admin else None
        next_post = publish_next_post(author_id=author_id)

    result = {
        'status': 'ok',
        'scheduled_published': scheduled_count,
        'next_post_published': next_post.title if next_post else None,
    }
    logger.info(f'Cron publish: {result}')
    return jsonify(result)


@cron_bp.route('/engage', methods=['POST'])
def cron_engage():
    """Run all engagement rules."""
    error = _check_secret()
    if error:
        return error

    from app.growth.engagement_rules import run_all_rules

    app = current_app._get_current_object()
    results = run_all_rules(app)

    logger.info(f'Cron engagement: {results}')
    return jsonify({'status': 'ok', 'results': {
        k: v if isinstance(v, int) else str(v) for k, v in results.items()
    }})


@cron_bp.route('/analytics', methods=['POST'])
def cron_analytics():
    """Refresh view counts and analytics data."""
    error = _check_secret()
    if error:
        return error

    from app.growth.seo_optimizer import refresh_view_counts

    updated = refresh_view_counts()

    result = {'status': 'ok', 'view_counts_refreshed': updated}
    logger.info(f'Cron analytics: {result}')
    return jsonify(result)


@cron_bp.route('/health', methods=['GET'])
def cron_health():
    """Health check for the cron system."""
    error = _check_secret()
    if error:
        return error

    from app.growth.analytics import get_growth_kpis
    from app.growth.content_pipeline import get_pending_posts
    from app.models.blog_post import BlogPost

    kpis = get_growth_kpis(days=7)
    pending = len(get_pending_posts())
    scheduled = BlogPost.query.filter(
        BlogPost.scheduled_at != None,  # noqa: E711
        BlogPost.is_published == False,  # noqa: E712
    ).count()

    return jsonify({
        'status': 'healthy',
        'kpis_7d': kpis,
        'content_queue': {
            'pending_in_code': pending,
            'scheduled_in_db': scheduled,
        },
    })
