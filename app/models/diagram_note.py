from datetime import datetime
from app.extensions import db


class DiagramNote(db.Model):
    """User-created diagram notes from the Whiteboard feature."""

    __tablename__ = 'diagram_notes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=True)
    title = db.Column(db.String(200), nullable=False, default='Untitled Diagram')
    data = db.Column(db.Text, nullable=False)  # Excalidraw scene JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('diagram_notes', lazy='dynamic'))
    lesson = db.relationship('Lesson', backref=db.backref('diagram_notes', lazy='dynamic'))

    __table_args__ = (
        db.Index('idx_diagram_user', 'user_id'),
        db.Index('idx_diagram_lesson', 'lesson_id'),
    )

    def __repr__(self):
        return f'<DiagramNote {self.id}: {self.title}>'
