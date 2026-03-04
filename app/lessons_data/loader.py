import json
from app.extensions import db
from app.models.chapter import Chapter
from app.models.lesson import Lesson


def load_all_lessons():
    """Load all lesson data into the database."""
    from app.lessons_data import (
        chapter1_lessons,
        chapter2_lessons,
        chapter3_lessons,
        chapter4_lessons,
        chapter5_lessons,
        chapter6_lessons,
        chapter7_lessons,
        chapter8_lessons,
        chapter9_lessons,
        chapter10_lessons,
        chapter11_lessons,
    )

    lesson_modules = [
        chapter1_lessons,
        chapter2_lessons,
        chapter3_lessons,
        chapter4_lessons,
        chapter5_lessons,
        chapter6_lessons,
        chapter7_lessons,
        chapter8_lessons,
        chapter9_lessons,
        chapter10_lessons,
        chapter11_lessons,
    ]

    for module in lesson_modules:
        chapter_order = module.CHAPTER_ORDER
        chapter = Chapter.query.filter_by(order=chapter_order).first()
        if not chapter:
            print(f"  Warning: Chapter order={chapter_order} not found. Skipping lessons.")
            continue

        existing_count = Lesson.query.filter_by(chapter_id=chapter.id).count()
        if existing_count > 0:
            print(f"  Skipping lessons for chapter {chapter_order}: {chapter.title} (already loaded)")
            continue

        for lesson_data in module.LESSONS:
            lesson = Lesson(
                chapter_id=chapter.id,
                title=lesson_data['title'],
                description=lesson_data['description'],
                order=lesson_data['order'],
                item_order=lesson_data['item_order'],
                content=json.dumps(lesson_data['sections']),
                estimated_time_minutes=lesson_data.get('estimated_time_minutes', 15),
            )
            db.session.add(lesson)

        print(f"  Loaded {len(module.LESSONS)} lessons for chapter {chapter_order}: {chapter.title}")

    db.session.commit()
    print("All lessons loaded successfully!")


def update_lesson_content():
    """Update existing lesson content from lesson data modules.

    This preserves lesson IDs and user completion records while
    refreshing the section content (e.g. adding diagram fields).
    """
    from app.lessons_data import (
        chapter1_lessons,
        chapter2_lessons,
        chapter3_lessons,
        chapter4_lessons,
        chapter5_lessons,
        chapter6_lessons,
        chapter7_lessons,
        chapter8_lessons,
        chapter9_lessons,
        chapter10_lessons,
        chapter11_lessons,
    )

    lesson_modules = [
        chapter1_lessons, chapter2_lessons, chapter3_lessons,
        chapter4_lessons, chapter5_lessons, chapter6_lessons,
        chapter7_lessons, chapter8_lessons, chapter9_lessons,
        chapter10_lessons, chapter11_lessons,
    ]

    updated = 0
    for module in lesson_modules:
        chapter_order = module.CHAPTER_ORDER
        chapter = Chapter.query.filter_by(order=chapter_order).first()
        if not chapter:
            continue

        for lesson_data in module.LESSONS:
            lesson = Lesson.query.filter_by(
                chapter_id=chapter.id, order=lesson_data['order']
            ).first()
            if lesson:
                new_content = json.dumps(lesson_data['sections'])
                if lesson.content != new_content:
                    lesson.content = new_content
                    updated += 1

    if updated:
        db.session.commit()
        print(f"  Updated content for {updated} lessons.")
    else:
        print("  Lesson content already up to date.")
