import re
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db, limiter
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

VALID_PYTHON_LEVELS = ['complete_beginner', 'some_experience', 'python_beginner', 'intermediate']


@auth_bp.route('/register', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.overview'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        python_level = request.form.get('python_level', 'complete_beginner')

        errors = []
        if not username or len(username) < 3 or len(username) > 30:
            errors.append('Username must be 3-30 characters.')
        if username and not re.match(r'^[a-zA-Z0-9_]+$', username):
            errors.append('Username can only contain letters, numbers, and underscores.')
        if not email or not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            errors.append('Please enter a valid email address.')
        if len(password) < 8:
            errors.append('Password must be at least 8 characters.')
        if not re.search(r'[a-zA-Z]', password) or not re.search(r'[0-9]', password):
            errors.append('Password must contain at least one letter and one number.')
        if password != confirm_password:
            errors.append('Passwords do not match.')
        if python_level not in VALID_PYTHON_LEVELS:
            python_level = 'complete_beginner'

        if User.query.filter_by(username=username).first():
            errors.append('Username already taken.')
        if User.query.filter_by(email=email).first():
            errors.append('Email already registered.')

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('auth/register.html',
                                   username=username, email=email,
                                   python_level=python_level)

        user = User(username=username, email=email, python_level=python_level)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.overview'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            flash('Welcome back!', 'success')
            return redirect(next_page or url_for('dashboard.overview'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
