from app.extensions import db


class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    item_order = db.Column(db.Integer, nullable=True)     # Unified timeline position
    starter_code = db.Column(db.Text, default='')
    hints = db.Column(db.Text, default='[]')

    test_cases_code = db.Column(db.Text, nullable=False)
    input_output_pairs = db.Column(db.Text, nullable=False)

    max_score = db.Column(db.Integer, nullable=False, default=100)
    test_weight = db.Column(db.Float, default=0.6)
    output_weight = db.Column(db.Float, default=0.4)
    allow_file_io = db.Column(db.Boolean, default=False)

    submissions = db.relationship('Submission', backref='assignment', lazy='dynamic')

    __table_args__ = (
        db.UniqueConstraint('chapter_id', 'order', name='uq_chapter_assignment_order'),
    )

    def __repr__(self):
        return f'<Assignment {self.title}>'
