import logging
from flask import Blueprint, render_template, request
from flask_login import current_user
from app.extensions import db
from app.models.blog_post import BlogPost
from app.models.blog_post_view import BlogPostView

logger = logging.getLogger(__name__)

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def blog_list():
    """Public blog listing — published posts only."""
    posts = BlogPost.query.filter_by(is_published=True) \
        .order_by(BlogPost.published_at.desc()).all()
    return render_template('blog/list.html', posts=posts)


@blog_bp.route('/<slug>')
def blog_detail(slug):
    """Public blog post detail page."""
    post = BlogPost.query.filter_by(slug=slug, is_published=True).first_or_404()

    # Track view
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        if ip:
            ip = ip.split(',')[0].strip()

        view = BlogPostView(
            blog_post_id=post.id,
            viewer_ip_hash=BlogPostView.hash_ip(ip),
            user_id=current_user.id if current_user.is_authenticated else None,
            referrer=request.referrer[:500] if request.referrer else None,
        )
        db.session.add(view)

        # Lightweight counter increment
        post.view_count = (post.view_count or 0) + 1
        db.session.commit()
    except Exception:
        db.session.rollback()
        logger.debug('Failed to track blog view', exc_info=True)

    return render_template('blog/detail.html', post=post)
