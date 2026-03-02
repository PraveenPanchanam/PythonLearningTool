"""Seed the database with chapters, assignments, lessons, and admin user."""
import os

from app import create_app
from app.extensions import db
from app.assignments_data.loader import load_all_assignments
from app.lessons_data.loader import load_all_lessons
from app.models.user import User

config_name = os.environ.get('FLASK_CONFIG', 'default')
app = create_app(config_name)

with app.app_context():
    # Create all tables (works for both SQLite and PostgreSQL)
    db.create_all()
    print("Database tables created.")
    print("Loading chapters and assignments...")
    load_all_assignments()
    print("Loading lessons...")
    load_all_lessons()

    # Create admin user from environment variables (if provided)
    admin_username = os.environ.get('ADMIN_USERNAME')
    admin_email = os.environ.get('ADMIN_EMAIL')
    admin_password = os.environ.get('ADMIN_PASSWORD')

    if admin_username and admin_email and admin_password:
        if not User.query.filter_by(username=admin_username).first():
            admin = User(
                username=admin_username,
                email=admin_email,
                is_admin=True,
                python_level='intermediate',
            )
            admin.set_password(admin_password)
            db.session.add(admin)
            db.session.commit()
            print(f"Admin user '{admin_username}' created.")
        else:
            print(f"Admin user '{admin_username}' already exists.")
    else:
        print("No ADMIN_USERNAME/ADMIN_EMAIL/ADMIN_PASSWORD env vars set. Skipping admin creation.")

    print("Done!")
