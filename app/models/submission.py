from datetime import datetime
from app.extensions import db


class Submission(db.Model):
    __tablename__ = 'submissions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'), nullable=False)
    code = db.Column(db.Text, nullable=False)

    score = db.Column(db.Float, default=0.0)
    passed_tests = db.Column(db.Integer, default=0)
    total_tests = db.Column(db.Integer, default=0)
    test_details = db.Column(db.Text, default='')

    output_match = db.Column(db.Boolean, default=False)
    output_matches_count = db.Column(db.Integer, default=0)
    output_total_count = db.Column(db.Integer, default=0)
    actual_output = db.Column(db.Text, default='')

    execution_time_ms = db.Column(db.Integer, default=0)
    error_message = db.Column(db.Text, default='')
    status = db.Column(db.String(20), default='pending')

    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.Index('idx_user_assignment', 'user_id', 'assignment_id'),
    )

    def __repr__(self):
        return f'<Submission {self.id} score={self.score}>'
