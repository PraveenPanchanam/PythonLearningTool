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
    from app.models.certificate import Certificate
    from app.models.blog_post import BlogPost
    from app.models.blog_post_view import BlogPostView
    from app.models.engagement_event import EngagementEvent
    from app.models.diagram_note import DiagramNote

    models = [
        ('User', User),
        ('Chapter', Chapter),
        ('Assignment', Assignment),
        ('Submission', Submission),
        ('Lesson', Lesson),
        ('LessonCompletion', LessonCompletion),
        ('Nudge', Nudge),
        ('Feedback', Feedback),
        ('Certificate', Certificate),
        ('BlogPost', BlogPost),
        ('BlogPostView', BlogPostView),
        ('EngagementEvent', EngagementEvent),
        ('DiagramNote', DiagramNote),
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
echo "Seeding blog posts if needed..."
python -c "
from app import create_app
from app.extensions import db
from app.models.blog_post import BlogPost
from app.models.user import User
from datetime import datetime

app = create_app('production')
with app.app_context():
    if BlogPost.query.count() == 0:
        # Find admin user for authorship
        admin = User.query.filter_by(is_admin=True).first()
        author_id = admin.id if admin else None

        posts = [
            {
                'title': 'Why Every Data Analyst Needs to Know Pandas',
                'slug': 'why-every-data-analyst-needs-pandas',
                'tags': 'pandas, data-analysis, python',
                'meta_description': 'Discover why Pandas is the must-have Python library for data analysts and how it transforms raw data into actionable insights.',
                'content': '''Pandas is the backbone of data analysis in Python, and for good reason. If you are pursuing a career as a Data Analyst, mastering Pandas is not optional — it is essential.

## What Makes Pandas So Powerful?

Pandas provides two core data structures — **Series** and **DataFrame** — that make working with structured data intuitive and fast. Whether you are cleaning messy CSV files, aggregating sales reports, or merging datasets from multiple sources, Pandas has you covered.

## Real-World Applications

- **Data Cleaning:** Handle missing values, duplicates, and inconsistent formats in minutes
- **Aggregation:** Group data by categories and compute statistics with a single line of code
- **Merging:** Combine data from multiple tables just like SQL JOINs
- **Time Series:** Analyze trends, resample data, and compute rolling averages effortlessly

## Why Employers Care

Job postings for Data Analysts consistently list Pandas as a required skill. Companies like Google, Amazon, and Netflix rely on Pandas-powered workflows for daily analytics. Learning Pandas is one of the highest-ROI investments you can make in your data career.

## Get Started Today

Our **Chapter 10: Pandas for Data Analysis** covers everything from basic DataFrame operations to advanced groupby, merge, and pivot techniques — all with hands-on assignments that mirror real-world scenarios.

Ready to level up your data skills? [Start learning now](/register).
''',
            },
            {
                'title': 'From Zero to Machine Learning: Your Python Learning Path',
                'slug': 'zero-to-machine-learning-python-path',
                'tags': 'machine-learning, scikit-learn, career',
                'meta_description': 'A clear roadmap from Python beginner to building your first machine learning models with Scikit-Learn.',
                'content': '''Machine learning might sound intimidating, but with the right learning path, anyone can go from zero to building real ML models. Here is exactly how to get there using Python.

## The Learning Path

### Stage 1: Python Fundamentals (Chapters 1-6)
Start with the basics — variables, loops, functions, and data structures. These are the building blocks that everything else rests on. You cannot skip this step.

### Stage 2: Advanced Python (Chapters 7-8)
Object-oriented programming and modules give you the tools to write clean, reusable code — exactly what ML projects demand.

### Stage 3: NumPy (Chapter 9)
NumPy is the mathematical engine behind every ML library. Understanding arrays, vectorized operations, and linear algebra fundamentals is critical.

### Stage 4: Pandas (Chapter 10)
Real ML projects start with data preparation. Pandas teaches you to load, clean, and transform data — the step that takes 80% of a data scientist's time.

### Stage 5: Scikit-Learn (Chapter 11)
Now you are ready. Scikit-Learn makes building classification, regression, and clustering models accessible. You will learn model selection, evaluation, and best practices.

## Why This Path Works

Each stage builds on the previous one. By the time you reach Scikit-Learn, you will have the Python fluency, numerical computing skills, and data manipulation expertise needed to succeed.

## Start Your ML Journey

Our structured curriculum takes you through all five stages with hands-on assignments at every step. [Create your free account](/register) and start building toward your ML career today.
''',
            },
            {
                'title': 'NumPy vs Python Lists: Why Scientists Choose NumPy',
                'slug': 'numpy-vs-python-lists-performance',
                'tags': 'numpy, performance, python',
                'meta_description': 'Learn why NumPy arrays dramatically outperform Python lists for numerical computing and data science workloads.',
                'content': '''If you have worked with Python lists, you might wonder why data scientists insist on using NumPy arrays instead. The answer comes down to three things: speed, memory, and functionality.

## Speed: 10x to 100x Faster

NumPy operations are implemented in optimized C code and operate on contiguous memory blocks. A simple element-wise addition on a million numbers can be **50-100x faster** with NumPy compared to a Python list comprehension.

## Memory Efficiency

A Python list of 1 million integers uses roughly 28 MB of memory. The same data in a NumPy array uses just 8 MB — **3.5x less memory**. This matters when working with large datasets.

## Built-in Math

NumPy provides hundreds of mathematical functions out of the box:

- **Linear Algebra:** matrix multiplication, eigenvalues, SVD
- **Statistics:** mean, median, standard deviation, correlation
- **Random:** generate random numbers, sample distributions
- **Broadcasting:** perform operations on arrays of different shapes automatically

## When to Use Which

Use **Python lists** when you need a general-purpose container for mixed data types. Use **NumPy arrays** whenever you are doing numerical computation, scientific analysis, or preparing data for machine learning.

## Learn NumPy Hands-On

Our **Chapter 9: NumPy Fundamentals** teaches you array creation, indexing, broadcasting, and real-world numerical computing — complete with auto-graded assignments. [Start learning](/register) today.
''',
            },
        ]

        for p in posts:
            post = BlogPost(
                title=p['title'],
                slug=p['slug'],
                content=p['content'],
                meta_description=p['meta_description'],
                tags=p['tags'],
                author_id=author_id,
                is_published=True,
                published_at=datetime.utcnow(),
            )
            db.session.add(post)

        db.session.commit()
        print(f'  ✓ Seeded {len(posts)} blog posts.')
    else:
        print(f'  Blog posts already exist ({BlogPost.query.count()} posts). Skipping seed.')
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
echo "Seeding growth engine content if needed..."
python -c "
from app import create_app
from app.extensions import db
from app.growth.content_pipeline import get_pending_posts, seed_scheduled_posts
from app.models.user import User

app = create_app('production')
with app.app_context():
    pending = get_pending_posts()
    if pending:
        admin = User.query.filter_by(is_admin=True).first()
        author_id = admin.id if admin else None
        count = seed_scheduled_posts(author_id=author_id, interval_days=3)
        print(f'  Seeded {count} growth blog posts as scheduled drafts.')
    else:
        print('  All growth blog posts already in database. Skipping.')
"

echo ""
echo "Updating lesson content with latest diagram data..."
python -c "
from app import create_app
from app.lessons_data.loader import update_lesson_content
app = create_app('production')
with app.app_context():
    update_lesson_content()
"

echo ""
echo "========================================="
echo " Starting Gunicorn..."
echo "========================================="
exec gunicorn --config gunicorn.conf.py run:app
