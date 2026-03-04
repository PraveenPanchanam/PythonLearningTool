import hashlib
from datetime import datetime
from app.extensions import db


class BlogPostView(db.Model):
    """Track individual blog post views for analytics."""
    __tablename__ = 'blog_post_views'

    id = db.Column(db.Integer, primary_key=True)
    blog_post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'), nullable=False, index=True)
    viewer_ip_hash = db.Column(db.String(64), nullable=True)  # SHA-256 hash for privacy
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    viewed_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    referrer = db.Column(db.String(500), nullable=True)

    blog_post = db.relationship('BlogPost', backref=db.backref('views', lazy='dynamic'))

    @staticmethod
    def hash_ip(ip_address):
        """Hash an IP address for privacy-preserving analytics."""
        if not ip_address:
            return None
        return hashlib.sha256(ip_address.encode()).hexdigest()

    def __repr__(self):
        return f'<BlogPostView post={self.blog_post_id} at={self.viewed_at}>'
