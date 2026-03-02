from flask import Blueprint, render_template
from app.models.blog_post import BlogPost

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
    return render_template('blog/detail.html', post=post)
