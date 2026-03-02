from datetime import datetime
from app.extensions import db


class LessonCompletion(db.Model):
    __tablename__ = 'lesson_completions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    exercises_completed = db.Column(db.Integer, default=0)
    exercises_total = db.Column(db.Integer, default=0)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'lesson_id', name='uq_user_lesson_completion'),
        db.Index('idx_user_lesson', 'user_id', 'lesson_id'),
    )

    def __repr__(self):
        return f'<LessonCompletion user={self.user_id} lesson={self.lesson_id}>'
