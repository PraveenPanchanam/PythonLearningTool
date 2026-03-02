from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user
from app.extensions import db, limiter
from app.models.feedback import Feedback
from app.models.blog_post import BlogPost

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.overview'))
    # Latest 3 published blog posts for "Latest from Our Blog" section
    latest_posts = BlogPost.query.filter_by(is_published=True).order_by(
        BlogPost.published_at.desc()
    ).limit(3).all()
    return render_template('index.html', latest_posts=latest_posts)


@main_bp.route('/feedback', methods=['POST'])
@limiter.limit("3 per minute")
def submit_feedback():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    rating = request.form.get('rating', type=int)
    message = request.form.get('message', '').strip()

    # Validation
    errors = []
    if not name or len(name) < 2:
        errors.append('Please enter your name.')
    if not email or '@' not in email:
        errors.append('Please enter a valid email.')
    if not rating or rating not in range(1, 6):
        errors.append('Please select a rating (1-5).')
    if not message or len(message) < 10:
        errors.append('Please enter at least 10 characters of feedback.')

    if errors:
        for e in errors:
            flash(e, 'danger')
        return redirect(url_for('main.index') + '#feedback')

    feedback = Feedback(name=name, email=email, rating=rating, message=message)
    db.session.add(feedback)
    db.session.commit()
    flash('Thank you for your feedback! We appreciate your input.', 'success')
    return redirect(url_for('main.index'))
