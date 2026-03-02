import json
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.chapter import Chapter
from app.models.lesson import Lesson
from app.models.lesson_completion import LessonCompletion
from app.models.submission import Submission
from app.extensions import db
from app.utils.learning_plan import get_chapter_recommendation, get_learning_plan, get_level_display_name

chapters_bp = Blueprint('chapters', __name__)


@chapters_bp.route('/')
@login_required
def chapter_list():
    chapters = Chapter.query.order_by(Chapter.order).all()
    chapter_progress = {}
    for chapter in chapters:
        assignments = chapter.assignments.all()
        lessons = chapter.lessons.all()
        total_assignments = len(assignments)
        completed_assignments = 0
        for assignment in assignments:
            best = Submission.query.filter_by(
                user_id=current_user.id,
                assignment_id=assignment.id
            ).order_by(Submission.score.desc()).first()
            if best and best.score > 0:
                completed_assignments += 1

        total_lessons = len(lessons)
        completed_lessons = LessonCompletion.query.filter_by(
            user_id=current_user.id
        ).join(Lesson).filter(
            Lesson.chapter_id == chapter.id
        ).count()

        total_items = total_assignments + total_lessons
        completed_items = completed_assignments + completed_lessons

        chapter_progress[chapter.id] = {
            'total': total_items,
            'completed': completed_items,
            'percentage': int(completed_items / total_items * 100) if total_items > 0 else 0,
            'assignment_total': total_assignments,
            'assignment_completed': completed_assignments,
            'lesson_total': total_lessons,
            'lesson_completed': completed_lessons,
        }
    # Get personalized learning plan
    user_level = current_user.python_level or 'complete_beginner'
    learning_plan = get_learning_plan(user_level)
    chapter_recommendations = {}
    for chapter in chapters:
        chapter_recommendations[chapter.id] = get_chapter_recommendation(user_level, chapter.order)

    return render_template(
        'chapters/list.html',
        chapters=chapters,
        progress=chapter_progress,
        learning_plan=learning_plan,
        chapter_recommendations=chapter_recommendations,
        user_level=user_level,
        level_display_name=get_level_display_name(user_level),
    )


@chapters_bp.route('/<int:chapter_id>')
@login_required
def chapter_detail(chapter_id):
    chapter = db.session.get(Chapter, chapter_id)
    if not chapter:
        return render_template('errors/404.html'), 404

    objectives = json.loads(chapter.learning_objectives) if chapter.learning_objectives else []
    assignments = chapter.assignments.all()
    lessons = Lesson.query.filter_by(chapter_id=chapter_id).order_by(Lesson.item_order).all()

    # Assignment status
    assignment_status = {}
    for assignment in assignments:
        best = Submission.query.filter_by(
            user_id=current_user.id,
            assignment_id=assignment.id
        ).order_by(Submission.score.desc()).first()
        assignment_status[assignment.id] = {
            'best_score': best.score if best else None,
            'attempts': Submission.query.filter_by(
                user_id=current_user.id,
                assignment_id=assignment.id
            ).count()
        }

    # Lesson status
    lesson_status = {}
    for lesson in lessons:
        completion = LessonCompletion.query.filter_by(
            user_id=current_user.id, lesson_id=lesson.id
        ).first()
        lesson_status[lesson.id] = {
            'completed': completion is not None,
            'exercises_completed': completion.exercises_completed if completion else 0,
            'exercises_total': completion.exercises_total if completion else 0,
        }

    # Build unified list sorted by item_order
    unified_items = []
    for lesson in lessons:
        unified_items.append({
            'type': 'lesson',
            'item': lesson,
            'item_order': lesson.item_order,
        })
    for assignment in assignments:
        unified_items.append({
            'type': 'assignment',
            'item': assignment,
            'item_order': assignment.item_order if assignment.item_order else assignment.order,
        })
    unified_items.sort(key=lambda x: x['item_order'])

    return render_template(
        'chapters/detail.html',
        chapter=chapter,
        objectives=objectives,
        assignments=assignments,
        lessons=lessons,
        status=assignment_status,
        lesson_status=lesson_status,
        unified_items=unified_items,
    )
