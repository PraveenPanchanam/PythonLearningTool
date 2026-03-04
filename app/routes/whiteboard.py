import json
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.extensions import db, limiter
from app.models.diagram_note import DiagramNote
from app.models.lesson import Lesson

whiteboard_bp = Blueprint('whiteboard', __name__)


@whiteboard_bp.route('/')
@login_required
def whiteboard_index():
    """Main whiteboard page — blank editor with saved diagrams sidebar."""
    diagrams = DiagramNote.query.filter_by(
        user_id=current_user.id
    ).order_by(DiagramNote.updated_at.desc()).all()

    return render_template(
        'whiteboard/editor.html',
        diagrams=diagrams,
        lesson=None,
        template_diagrams=[],
    )


@whiteboard_bp.route('/lesson/<int:lesson_id>')
@login_required
def whiteboard_for_lesson(lesson_id):
    """Whiteboard pre-loaded with lesson diagram templates."""
    lesson = db.session.get(Lesson, lesson_id)
    if not lesson:
        return render_template('errors/404.html'), 404

    sections = json.loads(lesson.content)
    template_diagrams = [
        s['diagram'] for s in sections if s.get('diagram')
    ]

    diagrams = DiagramNote.query.filter_by(
        user_id=current_user.id
    ).order_by(DiagramNote.updated_at.desc()).all()

    return render_template(
        'whiteboard/editor.html',
        lesson=lesson,
        template_diagrams=template_diagrams,
        diagrams=diagrams,
    )


@whiteboard_bp.route('/save', methods=['POST'])
@login_required
@limiter.limit("30 per minute")
def save_diagram():
    """Save or update a diagram note (AJAX)."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    diagram_id = data.get('id')
    title = (data.get('title') or 'Untitled Diagram')[:200]
    scene_data = data.get('data', '{}')
    lesson_id = data.get('lesson_id')

    # Convert dict to JSON string if needed
    if isinstance(scene_data, dict):
        scene_data = json.dumps(scene_data)

    if diagram_id:
        # Update existing
        note = DiagramNote.query.filter_by(
            id=diagram_id, user_id=current_user.id
        ).first()
        if not note:
            return jsonify({'error': 'Not found'}), 404
        note.title = title
        note.data = scene_data
    else:
        # Create new
        note = DiagramNote(
            user_id=current_user.id,
            lesson_id=lesson_id,
            title=title,
            data=scene_data,
        )
        db.session.add(note)

    db.session.commit()
    return jsonify({
        'status': 'ok',
        'id': note.id,
        'title': note.title,
        'updated_at': note.updated_at.isoformat(),
    })


@whiteboard_bp.route('/load/<int:diagram_id>')
@login_required
def load_diagram(diagram_id):
    """Load a saved diagram (AJAX)."""
    note = DiagramNote.query.filter_by(
        id=diagram_id, user_id=current_user.id
    ).first()
    if not note:
        return jsonify({'error': 'Not found'}), 404

    return jsonify({
        'id': note.id,
        'title': note.title,
        'data': json.loads(note.data),
        'lesson_id': note.lesson_id,
        'updated_at': note.updated_at.isoformat(),
    })


@whiteboard_bp.route('/delete/<int:diagram_id>', methods=['POST'])
@login_required
def delete_diagram(diagram_id):
    """Delete a saved diagram (AJAX)."""
    note = DiagramNote.query.filter_by(
        id=diagram_id, user_id=current_user.id
    ).first()
    if not note:
        return jsonify({'error': 'Not found'}), 404

    db.session.delete(note)
    db.session.commit()
    return jsonify({'status': 'ok'})


@whiteboard_bp.route('/list')
@login_required
def list_diagrams():
    """List all saved diagrams for current user (AJAX)."""
    diagrams = DiagramNote.query.filter_by(
        user_id=current_user.id
    ).order_by(DiagramNote.updated_at.desc()).all()

    return jsonify([{
        'id': d.id,
        'title': d.title,
        'lesson_id': d.lesson_id,
        'updated_at': d.updated_at.isoformat(),
    } for d in diagrams])
