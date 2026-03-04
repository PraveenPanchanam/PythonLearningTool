"""
SEO optimizer — view count reconciliation, SEO audits, and internal link suggestions.
"""

import logging
from sqlalchemy import func

from app.extensions import db
from app.models.blog_post import BlogPost
from app.models.blog_post_view import BlogPostView

logger = logging.getLogger(__name__)


def refresh_view_counts():
    """Batch-update blog_post.view_count from BlogPostView aggregation.

    This reconciles the lightweight counter on BlogPost with the
    actual view records in BlogPostView.
    Returns the number of posts updated.
    """
    counts = db.session.query(
        BlogPostView.blog_post_id,
        func.count(BlogPostView.id).label('total'),
    ).group_by(
        BlogPostView.blog_post_id
    ).all()

    updated = 0
    for post_id, total in counts:
        post = BlogPost.query.get(post_id)
        if post and post.view_count != total:
            post.view_count = total
            updated += 1

    if updated:
        db.session.commit()
        logger.info(f'Refreshed view counts for {updated} posts')

    return updated


def get_seo_report():
    """Audit all published blog posts for SEO completeness.

    Returns a list of issues found.
    """
    posts = BlogPost.query.filter_by(is_published=True).all()
    issues = []

    for post in posts:
        post_issues = []

        if not post.meta_description:
            post_issues.append('Missing meta description')
        elif len(post.meta_description) > 160:
            post_issues.append(f'Meta description too long ({len(post.meta_description)} chars, max 160)')

        if not post.slug:
            post_issues.append('Missing slug')

        if not post.tags:
            post_issues.append('No tags')

        if not post.content or len(post.content) < 300:
            post_issues.append('Content too short (< 300 chars)')

        title_len = len(post.title) if post.title else 0
        if title_len > 60:
            post_issues.append(f'Title too long ({title_len} chars, recommended max 60)')

        if not post.category:
            post_issues.append('No category assigned')

        if post_issues:
            issues.append({
                'post_id': post.id,
                'title': post.title,
                'slug': post.slug,
                'issues': post_issues,
            })

    return {
        'total_posts': len(posts),
        'posts_with_issues': len(issues),
        'issues': issues,
    }


# Keywords associated with each category for internal linking
CATEGORY_KEYWORDS = {
    'numpy': ['numpy', 'array', 'ndarray', 'broadcasting', 'vectorized', 'linear algebra', 'matrix'],
    'pandas': ['pandas', 'dataframe', 'series', 'csv', 'data cleaning', 'groupby', 'merge'],
    'scikit-learn': ['scikit-learn', 'sklearn', 'machine learning', 'classification', 'regression',
                     'model', 'training', 'cross-validation', 'feature engineering'],
    'career': ['career', 'job', 'roadmap', 'interview', 'portfolio', 'resume', 'hired'],
    'python-tips': ['python', 'list comprehension', 'data types', 'functions', 'loops', 'tips'],
}


def generate_internal_links(post):
    """Suggest internal links for a blog post based on keyword overlap.

    Returns a list of {title, slug, reason} dicts for posts that could
    be linked from the given post's content.
    """
    if not post.content:
        return []

    content_lower = post.content.lower()
    other_posts = BlogPost.query.filter(
        BlogPost.id != post.id,
        BlogPost.is_published == True,  # noqa: E712
    ).all()

    suggestions = []
    for other in other_posts:
        # Check if any of the other post's category keywords appear in this post's content
        other_category = other.category or ''
        keywords = CATEGORY_KEYWORDS.get(other_category, [])

        # Also check for the other post's tags as keywords
        for tag in other.tag_list:
            if tag not in keywords:
                keywords.append(tag)

        matching_keywords = [kw for kw in keywords if kw.lower() in content_lower]

        if matching_keywords and other.slug != post.slug:
            suggestions.append({
                'title': other.title,
                'slug': other.slug,
                'matching_keywords': matching_keywords,
                'reason': f'Mentions: {", ".join(matching_keywords[:3])}',
            })

    # Sort by number of matching keywords (most relevant first)
    suggestions.sort(key=lambda x: len(x['matching_keywords']), reverse=True)
    return suggestions[:5]  # Top 5 suggestions
