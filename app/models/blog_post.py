import re
from datetime import datetime
from app.extensions import db


class BlogPost(db.Model):
    """Blog post for content marketing."""
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(250), unique=True, nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    meta_description = db.Column(db.String(300), nullable=True)
    tags = db.Column(db.String(500), nullable=True)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    is_published = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = db.Column(db.DateTime, nullable=True)

    author = db.relationship('User', backref=db.backref('blog_posts', lazy='dynamic'))

    @staticmethod
    def generate_slug(title):
        """Generate a URL-friendly slug from title."""
        slug = title.lower().strip()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[\s_]+', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        return slug.strip('-')

    @property
    def tag_list(self):
        """Return tags as a list."""
        if not self.tags:
            return []
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    @property
    def excerpt(self):
        """Return first 200 characters of content as plain text excerpt."""
        text = re.sub(r'[#*_`\[\]()]', '', self.content or '')
        text = re.sub(r'\n+', ' ', text).strip()
        return text[:200] + '...' if len(text) > 200 else text

    def __repr__(self):
        return f'<BlogPost {self.slug}>'
