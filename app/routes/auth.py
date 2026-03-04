import re
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from app.extensions import db, limiter, mail
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

VALID_PYTHON_LEVELS = ['complete_beginner', 'some_experience', 'python_beginner', 'intermediate']
VALID_AGE_GROUPS = ['under_12', '12_to_17', '18_plus']


# ──────────────────────────────────────
# Token helpers (itsdangerous)
# ──────────────────────────────────────

def generate_reset_token(email):
    """Generate a secure, time-limited password-reset token."""
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return s.dumps(email, salt='password-reset')


def verify_reset_token(token, max_age=3600):
    """Verify a password-reset token. Returns email or None."""
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = s.loads(token, salt='password-reset', max_age=max_age)
        return email
    except (SignatureExpired, BadSignature):
        return None


# ──────────────────────────────────────
# Registration
# ──────────────────────────────────────

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
        age_group = request.form.get('age_group', '18_plus')

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
        if age_group not in VALID_AGE_GROUPS:
            age_group = '18_plus'

        if User.query.filter_by(username=username).first():
            errors.append('Username already taken.')
        if User.query.filter_by(email=email).first():
            errors.append('Email already registered.')

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('auth/register.html',
                                   username=username, email=email,
                                   python_level=python_level,
                                   age_group=age_group)

        user = User(username=username, email=email, python_level=python_level, age_group=age_group)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        # Send welcome email (non-blocking)
        try:
            from app.growth.engagement_rules import send_welcome_email
            send_welcome_email(user)
        except Exception:
            import logging
            logging.getLogger(__name__).warning('Welcome email failed', exc_info=True)

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


# ──────────────────────────────────────
# Login / Logout
# ──────────────────────────────────────

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


# ──────────────────────────────────────
# Forgot Password / Reset Password
# ──────────────────────────────────────

@auth_bp.route('/forgot-password', methods=['GET', 'POST'])
@limiter.limit("3 per minute")
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.overview'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()

        # Check if mail is configured
        if not current_app.config.get('MAIL_USERNAME'):
            current_app.logger.warning('Password reset attempted but MAIL_USERNAME is not configured.')
            flash('Password reset is currently unavailable. Please contact an administrator.', 'warning')
            return redirect(url_for('auth.forgot_password'))

        # Always show the same message to prevent email enumeration
        user = User.query.filter_by(email=email).first()

        if user:
            try:
                token = generate_reset_token(user.email)
                reset_url = url_for('auth.reset_password', token=token, _external=True)

                msg = Message(
                    subject='Reset Your Password - Python Learning Tool',
                    recipients=[user.email],
                )
                msg.html = render_template('emails/reset_password.html',
                                           user=user, reset_url=reset_url)
                msg.body = render_template('emails/reset_password.txt',
                                           user=user, reset_url=reset_url)
                mail.send(msg)
                current_app.logger.info(f'Password reset email sent to {user.email}')
            except Exception as e:
                current_app.logger.error(f'Failed to send password reset email: {e}')
                flash('An error occurred while sending the email. Please try again later.', 'danger')
                return redirect(url_for('auth.forgot_password'))
        else:
            current_app.logger.info(f'Password reset requested for non-existent email: {email}')

        # Same message whether user exists or not (security)
        flash('If an account with that email exists, we\'ve sent a password reset link. Please check your inbox.', 'info')
        return redirect(url_for('auth.login'))

    return render_template('auth/forgot_password.html')


@auth_bp.route('/reset-password/<token>', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.overview'))

    email = verify_reset_token(token)
    if not email:
        flash('The password reset link is invalid or has expired. Please request a new one.', 'danger')
        return redirect(url_for('auth.forgot_password'))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash('The password reset link is invalid. Please request a new one.', 'danger')
        return redirect(url_for('auth.forgot_password'))

    if request.method == 'POST':
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        errors = []
        if len(password) < 8:
            errors.append('Password must be at least 8 characters.')
        if not re.search(r'[a-zA-Z]', password) or not re.search(r'[0-9]', password):
            errors.append('Password must contain at least one letter and one number.')
        if password != confirm_password:
            errors.append('Passwords do not match.')

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('auth/reset_password.html', token=token)

        user.set_password(password)
        db.session.commit()
        current_app.logger.info(f'Password reset completed for user: {user.username}')

        flash('Your password has been reset successfully! You can now log in with your new password.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/reset_password.html', token=token)
