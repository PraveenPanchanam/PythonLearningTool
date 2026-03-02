import logging
from logging.handlers import RotatingFileHandler
import os

from datetime import datetime

from flask import Flask, render_template, request
from flask_login import current_user
from markupsafe import Markup
import markdown as md

from config import config
from app.extensions import db, login_manager, csrf, limiter, migrate, mail


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'default')
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    csrf.init_app(app)
    limiter.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Security headers via Flask-Talisman (production only)
    if not app.debug and not app.testing:
        from flask_talisman import Talisman

        csp = {
            'default-src': "'self'",
            'script-src': [
                "'self'",
                "'unsafe-inline'",
                'cdn.jsdelivr.net',
                'cdnjs.cloudflare.com',
            ],
            'style-src': [
                "'self'",
                "'unsafe-inline'",
                'cdn.jsdelivr.net',
                'cdnjs.cloudflare.com',
            ],
            'font-src': [
                "'self'",
                'cdn.jsdelivr.net',
            ],
            'img-src': "'self' data:",
        }
        force_https = os.environ.get('FORCE_HTTPS', 'false').lower() == 'true'
        Talisman(
            app,
            content_security_policy=csp,
            force_https=force_https,
            session_cookie_secure=force_https,
            session_cookie_http_only=True,
            session_cookie_samesite='Lax',
        )

    # Configure logging
    log_level = getattr(logging, app.config.get('LOG_LEVEL', 'INFO'))

    # Stream handler (stdout) for Docker and development
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s'
    ))
    app.logger.addHandler(stream_handler)

    # File handler for production
    if not app.debug and not app.testing:
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, 'app.log'),
            maxBytes=10_240_000,
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(log_level)
        app.logger.addHandler(file_handler)

    app.logger.setLevel(log_level)
    app.logger.info('Python Learning Tool startup')

    # Register custom Jinja2 filter for Markdown rendering
    @app.template_filter('markdown')
    def markdown_filter(text):
        if not text:
            return ''
        html = md.markdown(
            text,
            extensions=['fenced_code', 'tables', 'nl2br', 'sane_lists']
        )
        return Markup(html)

    # Timeago filter for relative timestamps
    @app.template_filter('timeago')
    def timeago_filter(dt):
        if not dt:
            return 'Never'
        diff = datetime.utcnow() - dt
        seconds = diff.total_seconds()
        if seconds < 60:
            return 'Just now'
        if seconds < 3600:
            return f'{int(seconds // 60)}m ago'
        if seconds < 86400:
            return f'{int(seconds // 3600)}h ago'
        if seconds < 604800:
            return f'{int(seconds // 86400)}d ago'
        return dt.strftime('%b %d, %Y')

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.chapters import chapters_bp
    from app.routes.assignments import assignments_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.lessons import lessons_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(chapters_bp, url_prefix='/chapters')
    app.register_blueprint(assignments_bp, url_prefix='/assignments')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(lessons_bp, url_prefix='/lessons')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Track user activity (last active time + IP)
    @app.before_request
    def update_last_active():
        try:
            if current_user.is_authenticated:
                now = datetime.utcnow()
                # Throttle: only write every 5 minutes
                if not current_user.last_active_at or \
                   (now - current_user.last_active_at).total_seconds() > 300:
                    current_user.last_active_at = now
                    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
                    if ip:
                        ip = ip.split(',')[0].strip()
                    current_user.last_ip = ip
                    db.session.commit()
        except Exception:
            # Gracefully handle missing columns during migration transition
            db.session.rollback()

    # Import models (for Flask-Migrate to detect them)
    with app.app_context():
        from app.models import User, Chapter, Assignment, Submission, Lesson, LessonCompletion, Nudge, Feedback  # noqa: F401
        # In development, auto-create tables. In production, use: flask db upgrade
        if app.debug:
            db.create_all()

    # User loader for Flask-Login
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(429)
    def ratelimit_handler(error):
        return render_template('errors/429.html'), 429

    return app
