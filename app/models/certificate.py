import uuid
from datetime import datetime
from app.extensions import db


class Certificate(db.Model):
    """Completion certificate for a chapter or full course."""
    __tablename__ = 'certificates'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=True)

    token = db.Column(db.String(64), unique=True, nullable=False, index=True,
                      default=lambda: uuid.uuid4().hex)
    certificate_type = db.Column(db.String(20), nullable=False, default='chapter')

    issued_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('certificates', lazy='dynamic'))
    chapter = db.relationship('Chapter', backref=db.backref('certificates', lazy='dynamic'))

    __table_args__ = (
        db.UniqueConstraint('user_id', 'chapter_id', name='uq_user_chapter_certificate'),
    )

    def __repr__(self):
        return f'<Certificate {self.token[:12]} user={self.user_id} chapter={self.chapter_id}>'
