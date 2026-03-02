#!/bin/bash
set -e

echo "========================================="
echo " Python Learning Tool - Startup Sequence"
echo "========================================="

# ─── Step 1: Ensure base tables exist ───
echo ""
echo "[1/5] Ensuring database tables exist..."
python -c "
from app import create_app
from app.extensions import db
app = create_app('production')
with app.app_context():
    db.create_all()
    print('  ✓ Database tables ready.')
"

# ─── Step 2: Run Alembic migrations ───
echo ""
echo "[2/5] Running database migrations..."
flask db upgrade 2>&1 || echo "  ⚠ Migration returned non-zero (may be first run or already current)."

# ─── Step 3: Comprehensive schema sync ───
# Compares every SQLAlchemy model column to the actual database
# and adds any missing columns via ALTER TABLE.
# This is a safety net that works regardless of whether Alembic succeeds.
echo ""
echo "[3/5] Schema sync — checking all models against database..."
python -c "
from app import create_app
from app.extensions import db
from sqlalchemy import inspect, text

app = create_app('production')
with app.app_context():
    inspector = inspect(db.engine)
    existing_tables = inspector.get_table_names()

    # Map SQLAlchemy types to PostgreSQL types
    type_map = {
        'INTEGER': 'INTEGER',
        'SMALLINT': 'SMALLINT',
        'BIGINT': 'BIGINT',
        'VARCHAR': 'VARCHAR',
        'TEXT': 'TEXT',
        'BOOLEAN': 'BOOLEAN',
        'FLOAT': 'FLOAT',
        'DOUBLE_PRECISION': 'DOUBLE PRECISION',
        'DATETIME': 'TIMESTAMP',
        'DATE': 'DATE',
        'NUMERIC': 'NUMERIC',
    }

    def sa_type_to_pg(col):
        \"\"\"Convert a SQLAlchemy column type to PostgreSQL DDL type.\"\"\"
        sa_type = type(col.type).__name__.upper()
        if sa_type == 'VARCHAR':
            length = getattr(col.type, 'length', None)
            return f'VARCHAR({length})' if length else 'VARCHAR'
        if sa_type == 'STRING':
            length = getattr(col.type, 'length', None)
            return f'VARCHAR({length})' if length else 'VARCHAR'
        return type_map.get(sa_type, 'TEXT')

    total_added = 0

    for table in db.metadata.sorted_tables:
        tname = table.name
        if tname not in existing_tables:
            # Table doesn't exist — db.create_all() should have made it
            print(f'  ⚠ Table {tname} missing! Running db.create_all()...')
            db.create_all()
            continue

        # Get existing columns
        db_columns = {c['name'] for c in inspector.get_columns(tname)}

        for col in table.columns:
            if col.name not in db_columns:
                pg_type = sa_type_to_pg(col)
                sql = f'ALTER TABLE {tname} ADD COLUMN \"{col.name}\" {pg_type}'

                # Add DEFAULT for non-nullable columns or columns with defaults
                if col.default is not None:
                    default_val = col.default.arg
                    if callable(default_val):
                        pass  # Skip callable defaults (e.g., datetime.utcnow)
                    elif isinstance(default_val, bool):
                        sql += f\" DEFAULT {'TRUE' if default_val else 'FALSE'}\"
                    elif isinstance(default_val, (int, float)):
                        sql += f' DEFAULT {default_val}'
                    elif isinstance(default_val, str):
                        escaped = default_val.replace(\"'\", \"''\")
                        sql += f\" DEFAULT '{escaped}'\"

                db.session.execute(text(sql))
                total_added += 1
                print(f'  + Added column {tname}.{col.name} ({pg_type})')

    if total_added > 0:
        db.session.commit()
        print(f'  ✓ Schema sync complete — added {total_added} missing column(s).')
    else:
        print('  ✓ All model columns present in database.')
"

# ─── Step 4: Pre-flight verification ───
# BLOCK startup if any model query fails
echo ""
echo "[4/5] Pre-flight verification — testing all model queries..."
python -c "
from app import create_app
from app.extensions import db
app = create_app('production')

with app.app_context():
    errors = []

    # Test every model with a real query
    from app.models.user import User
    from app.models.chapter import Chapter
    from app.models.assignment import Assignment
    from app.models.submission import Submission
    from app.models.lesson import Lesson
    from app.models.lesson_completion import LessonCompletion
    from app.models.nudge import Nudge
    from app.models.feedback import Feedback

    models = [
        ('User', User),
        ('Chapter', Chapter),
        ('Assignment', Assignment),
        ('Submission', Submission),
        ('Lesson', Lesson),
        ('LessonCompletion', LessonCompletion),
        ('Nudge', Nudge),
        ('Feedback', Feedback),
    ]

    for name, model in models:
        try:
            model.query.limit(1).all()
            print(f'  ✓ {name} query OK')
        except Exception as ex:
            errors.append(f'{name}: {ex}')
            print(f'  ✗ {name} query FAILED: {ex}')

    if errors:
        print('')
        print('  ✗ FATAL — Pre-flight verification failed!')
        print('  The application will NOT start with broken queries.')
        import sys
        sys.exit(1)

    print('  ✓ All pre-flight checks passed.')
"

# ─── Step 5: Seed data + admin user ───
echo ""
echo "[5/5] Seeding data if needed..."
python -c "
from app import create_app
from app.extensions import db
from app.models.chapter import Chapter
app = create_app('production')
with app.app_context():
    if Chapter.query.count() == 0:
        print('  No data found. Seeding chapters, assignments, and lessons...')
        from app.assignments_data.loader import load_all_assignments
        from app.lessons_data.loader import load_all_lessons
        load_all_assignments()
        load_all_lessons()
        print('  Seed complete.')
    else:
        print('  Data already exists. Skipping seed.')
        # Check if lessons need loading (upgrade from pre-lesson version)
        from app.models.lesson import Lesson
        if Lesson.query.count() == 0:
            print('  Loading lessons for existing database...')
            from app.lessons_data.loader import load_all_lessons
            load_all_lessons()
            print('  Lessons loaded.')
"

echo ""
echo "Checking admin user..."
python -c "
import os
from app import create_app
from app.extensions import db
from app.models.user import User
app = create_app('production')
with app.app_context():
    admin_username = os.environ.get('ADMIN_USERNAME')
    admin_email = os.environ.get('ADMIN_EMAIL')
    admin_password = os.environ.get('ADMIN_PASSWORD')

    # Diagnostic logging (safe — only shows length and first/last char)
    print(f'  ENV ADMIN_USERNAME = {repr(admin_username)}')
    print(f'  ENV ADMIN_EMAIL    = {repr(admin_email)}')
    if admin_password:
        print(f'  ENV ADMIN_PASSWORD = ({len(admin_password)} chars) {admin_password[0]}...{admin_password[-1]}')
    else:
        print(f'  ENV ADMIN_PASSWORD = None')

    if admin_username and admin_email and admin_password:
        admin = User.query.filter_by(username=admin_username).first()
        if not admin:
            admin = User(
                username=admin_username,
                email=admin_email,
                is_admin=True,
                python_level='intermediate',
            )
            admin.set_password(admin_password)
            db.session.add(admin)
            db.session.commit()
            print(f'  Admin user created: {admin_username}')
        else:
            print(f'  Admin found: id={admin.id}, username={admin.username}, is_admin={admin.is_admin}')
            # Ensure password stays in sync with env var
            if not admin.check_password(admin_password):
                admin.set_password(admin_password)
                db.session.commit()
                print('  Admin password UPDATED from env var.')
            else:
                print('  Admin password matches env var. OK.')

            # Verify the password was set correctly by re-checking
            admin_recheck = User.query.filter_by(username=admin_username).first()
            verify = admin_recheck.check_password(admin_password)
            print(f'  Password verification after sync: {verify}')
    else:
        missing = []
        if not admin_username: missing.append('ADMIN_USERNAME')
        if not admin_email: missing.append('ADMIN_EMAIL')
        if not admin_password: missing.append('ADMIN_PASSWORD')
        print(f'  Missing env vars: {missing}. Skipping admin creation.')
"

echo ""
echo "========================================="
echo " Starting Gunicorn..."
echo "========================================="
exec gunicorn --config gunicorn.conf.py run:app
