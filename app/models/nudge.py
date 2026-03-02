from datetime import datetime
from app.extensions import db


class Nudge(db.Model):
    """Motivational nudge sent by admin to a student."""
    __tablename__ = 'nudges'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    nudge_type = db.Column(db.String(30), default='encouragement')
    # Types: 'encouragement', 'reminder', 'milestone', 'custom'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    read_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', backref=db.backref('nudges', lazy='dynamic'))

    @property
    def is_read(self):
        return self.read_at is not None

    def __repr__(self):
        return f'<Nudge {self.id} for user {self.user_id}>'
