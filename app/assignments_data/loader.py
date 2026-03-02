import json
from app.extensions import db
from app.models.chapter import Chapter
from app.models.assignment import Assignment


def load_all_assignments():
    """Load all chapter and assignment data into the database."""
    from app.assignments_data import (
        chapter1_data_types,
        chapter2_conditionals,
        chapter3_loops,
        chapter4_functions,
        chapter5_data_structures,
        chapter6_file_io,
        chapter7_oop,
        chapter8_advanced,
        chapter9_numpy,
        chapter10_pandas,
        chapter11_sklearn,
    )

    chapter_modules = [
        chapter1_data_types,
        chapter2_conditionals,
        chapter3_loops,
        chapter4_functions,
        chapter5_data_structures,
        chapter6_file_io,
        chapter7_oop,
        chapter8_advanced,
        chapter9_numpy,
        chapter10_pandas,
        chapter11_sklearn,
    ]

    for module in chapter_modules:
        info = module.CHAPTER_INFO

        existing = Chapter.query.filter_by(order=info['order']).first()
        if existing:
            print(f"  Skipping chapter {info['order']}: {info['title']} (already exists)")
            continue

        chapter = Chapter(
            title=info['title'],
            description=info['description'],
            difficulty_level=info['difficulty_level'],
            order=info['order'],
            learning_objectives=json.dumps(info.get('learning_objectives', [])),
            estimated_time_minutes=info.get('estimated_time_minutes', 60),
        )
        db.session.add(chapter)
        db.session.flush()

        for assgn_data in module.ASSIGNMENTS:
            assignment = Assignment(
                chapter_id=chapter.id,
                title=assgn_data['title'],
                description=assgn_data['description'],
                difficulty=assgn_data['difficulty'],
                order=assgn_data['order'],
                item_order=assgn_data.get('item_order', assgn_data['order']),
                starter_code=assgn_data.get('starter_code', ''),
                hints=json.dumps(assgn_data.get('hints', [])),
                test_cases_code=assgn_data['test_cases_code'],
                input_output_pairs=json.dumps(assgn_data['input_output_pairs']),
                max_score=assgn_data.get('max_score', 100),
                test_weight=assgn_data.get('test_weight', 0.6),
                output_weight=assgn_data.get('output_weight', 0.4),
                allow_file_io=assgn_data.get('allow_file_io', False),
            )
            db.session.add(assignment)

        print(f"  Loaded chapter {info['order']}: {info['title']} ({len(module.ASSIGNMENTS)} assignments)")

    db.session.commit()
    print("All chapters and assignments loaded successfully!")
