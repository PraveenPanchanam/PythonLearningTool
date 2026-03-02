from app.extensions import db


class Chapter(db.Model):
    __tablename__ = 'chapters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty_level = db.Column(db.String(20), nullable=False)
    order = db.Column(db.Integer, nullable=False, unique=True)
    learning_objectives = db.Column(db.Text)
    estimated_time_minutes = db.Column(db.Integer, default=60)

    assignments = db.relationship(
        'Assignment', backref='chapter', lazy='dynamic',
        order_by='Assignment.order'
    )
    lessons = db.relationship(
        'Lesson', backref='chapter', lazy='dynamic',
        order_by='Lesson.order'
    )

    def __repr__(self):
        return f'<Chapter {self.order}: {self.title}>'
