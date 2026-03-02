#!/bin/bash
set -e

echo "Ensuring database tables exist..."
python -c "
from app import create_app
from app.extensions import db
app = create_app('production')
with app.app_context():
    db.create_all()
    print('Database tables ready.')
"

echo "Running database migrations..."
flask db upgrade 2>/dev/null || echo "No pending migrations."

echo "Seeding data if needed..."
python -c "
from app import create_app
from app.extensions import db
from app.models.chapter import Chapter
app = create_app('production')
with app.app_context():
    if Chapter.query.count() == 0:
        print('No data found. Seeding chapters, assignments, and lessons...')
        from app.assignments_data.loader import load_all_assignments
        from app.lessons_data.loader import load_all_lessons
        load_all_assignments()
        load_all_lessons()
        print('Seed complete.')
    else:
        print('Data already exists. Skipping seed.')
        # Check if lessons need loading (upgrade from pre-lesson version)
        from app.models.lesson import Lesson
        if Lesson.query.count() == 0:
            print('Loading lessons for existing database...')
            from app.lessons_data.loader import load_all_lessons
            load_all_lessons()
            print('Lessons loaded.')
"

echo "Starting Gunicorn..."
exec gunicorn --config gunicorn.conf.py run:app
