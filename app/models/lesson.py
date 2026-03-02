from app.extensions import db


class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)        # Lesson-specific order (1, 2, 3)
    item_order = db.Column(db.Integer, nullable=False)    # Unified timeline position
    content = db.Column(db.Text, nullable=False)          # JSON list of sections
    estimated_time_minutes = db.Column(db.Integer, default=15)

    completions = db.relationship('LessonCompletion', backref='lesson', lazy='dynamic')

    __table_args__ = (
        db.UniqueConstraint('chapter_id', 'order', name='uq_chapter_lesson_order'),
        db.UniqueConstraint('chapter_id', 'item_order', name='uq_chapter_lesson_item_order'),
    )

    def __repr__(self):
        return f'<Lesson {self.title}>'
