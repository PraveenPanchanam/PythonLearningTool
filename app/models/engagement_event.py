from datetime import datetime
from app.extensions import db


class EngagementEvent(db.Model):
    """Log engagement actions taken by the growth engine."""
    __tablename__ = 'engagement_events'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    event_type = db.Column(db.String(50), nullable=False, index=True)
    event_data = db.Column(db.Text, nullable=True)  # JSON string for extra context
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    user = db.relationship('User', backref=db.backref('engagement_events', lazy='dynamic'))

    # Event types
    WELCOME_EMAIL = 'welcome_email'
    INACTIVE_NUDGE = 'inactive_nudge'
    CHAPTER_MILESTONE = 'chapter_milestone'
    FIRST_ASSIGNMENT_NUDGE = 'first_assignment_nudge'
    STREAK_CELEBRATION = 'streak_celebration'
    STUCK_NUDGE = 'stuck_nudge'
    RETURNING_USER = 'returning_user'

    def __repr__(self):
        return f'<EngagementEvent {self.event_type} user={self.user_id}>'
