from flask import Blueprint, Response, render_template, url_for

seo_bp = Blueprint('seo', __name__)


@seo_bp.route('/sitemap.xml')
def sitemap():
    """Dynamic sitemap.xml listing all public pages."""
    pages = []

    # Static public pages
    pages.append({'loc': url_for('main.index', _external=True), 'changefreq': 'weekly', 'priority': '1.0'})
    pages.append({'loc': url_for('auth.login', _external=True), 'changefreq': 'monthly', 'priority': '0.5'})
    pages.append({'loc': url_for('auth.register', _external=True), 'changefreq': 'monthly', 'priority': '0.7'})
    pages.append({'loc': url_for('blog.blog_list', _external=True), 'changefreq': 'weekly', 'priority': '0.8'})

    # Published blog posts
    try:
        from app.models.blog_post import BlogPost
        posts = BlogPost.query.filter_by(is_published=True).all()
        for post in posts:
            pages.append({
                'loc': url_for('blog.blog_detail', slug=post.slug, _external=True),
                'lastmod': post.published_at.strftime('%Y-%m-%d') if post.published_at else None,
                'changefreq': 'monthly',
                'priority': '0.6',
            })
    except Exception:
        pass

    # Public certificates
    try:
        from app.models.certificate import Certificate
        certs = Certificate.query.all()
        for cert in certs:
            pages.append({
                'loc': url_for('certificates.view_certificate', token=cert.token, _external=True),
                'lastmod': cert.issued_at.strftime('%Y-%m-%d') if cert.issued_at else None,
                'changefreq': 'yearly',
                'priority': '0.4',
            })
    except Exception:
        pass

    xml = render_template('seo/sitemap.xml', pages=pages)
    return Response(xml, mimetype='application/xml')


@seo_bp.route('/robots.txt')
def robots():
    """Serve robots.txt."""
    content = f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /dashboard/
Disallow: /assignments/
Disallow: /lessons/

Sitemap: {url_for('seo.sitemap', _external=True)}
"""
    return Response(content, mimetype='text/plain')
