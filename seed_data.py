"""Seed the database with chapters and assignments."""
import os

from app import create_app
from app.extensions import db
from app.assignments_data.loader import load_all_assignments
from app.lessons_data.loader import load_all_lessons

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
    print("Done!")
