"""
Learning Plan Generator

Maps a user's Python experience level to a personalized learning plan
that recommends which chapters to focus on, skip, or review.
"""

# Chapter order → metadata
CHAPTER_META = {
    1: {'title': 'Data Types & Variables', 'category': 'basics'},
    2: {'title': 'Conditional Statements', 'category': 'basics'},
    3: {'title': 'Loops', 'category': 'basics'},
    4: {'title': 'Functions', 'category': 'basics'},
    5: {'title': 'Data Structures', 'category': 'intermediate'},
    6: {'title': 'File I/O', 'category': 'intermediate'},
    7: {'title': 'Object-Oriented Programming', 'category': 'intermediate'},
    8: {'title': 'Advanced Python', 'category': 'advanced'},
    9: {'title': 'NumPy', 'category': 'data_science'},
    10: {'title': 'Pandas', 'category': 'data_science'},
    11: {'title': 'Scikit-learn', 'category': 'data_science'},
}

# Learning plan definitions per level
# status: 'focus' (recommended, start here), 'recommended', 'review' (quick review), 'optional'
LEARNING_PLANS = {
    'complete_beginner': {
        'description': 'Start from the very beginning and build a strong Python foundation.',
        'start_chapter': 1,
        'chapters': {
            1: {'status': 'focus', 'note': 'Start here! Learn the building blocks of Python.'},
            2: {'status': 'focus', 'note': 'Learn to make decisions in your code.'},
            3: {'status': 'focus', 'note': 'Master repetition and iteration.'},
            4: {'status': 'focus', 'note': 'Write reusable code with functions.'},
            5: {'status': 'recommended', 'note': 'Organize data with lists, dicts, and sets.'},
            6: {'status': 'recommended', 'note': 'Read and write files.'},
            7: {'status': 'recommended', 'note': 'Learn object-oriented design.'},
            8: {'status': 'optional', 'note': 'Advanced topics - tackle after mastering basics.'},
            9: {'status': 'optional', 'note': 'Data science with NumPy - after chapters 1-7.'},
            10: {'status': 'optional', 'note': 'Data analysis with Pandas - after NumPy.'},
            11: {'status': 'optional', 'note': 'Machine learning - after Pandas.'},
        },
    },
    'some_experience': {
        'description': 'You know another language. Focus on Python-specific features and syntax.',
        'start_chapter': 1,
        'chapters': {
            1: {'status': 'review', 'note': 'Quick review - Python syntax for variables and types.'},
            2: {'status': 'review', 'note': 'Quick review - Python conditionals (similar to other languages).'},
            3: {'status': 'review', 'note': 'Quick review - Python loops and iterables.'},
            4: {'status': 'focus', 'note': 'Python functions have unique features - focus here.'},
            5: {'status': 'focus', 'note': 'Python data structures are powerful - key chapter!'},
            6: {'status': 'recommended', 'note': 'Python file handling with context managers.'},
            7: {'status': 'focus', 'note': 'Python OOP has differences from other languages.'},
            8: {'status': 'recommended', 'note': 'Decorators, generators - Python-specific power tools.'},
            9: {'status': 'recommended', 'note': 'NumPy for numerical computing.'},
            10: {'status': 'recommended', 'note': 'Pandas for data analysis.'},
            11: {'status': 'optional', 'note': 'Machine learning with scikit-learn.'},
        },
    },
    'python_beginner': {
        'description': 'You know Python basics. Deepen your skills and explore advanced topics.',
        'start_chapter': 4,
        'chapters': {
            1: {'status': 'review', 'note': 'Skip or skim - you likely know this.'},
            2: {'status': 'review', 'note': 'Skip or skim - you likely know this.'},
            3: {'status': 'review', 'note': 'Skip or skim - you likely know this.'},
            4: {'status': 'review', 'note': 'Review advanced function concepts (*args, **kwargs).'},
            5: {'status': 'focus', 'note': 'Master comprehensions and nested structures.'},
            6: {'status': 'focus', 'note': 'File I/O patterns and context managers.'},
            7: {'status': 'focus', 'note': 'Deep dive into OOP - inheritance, special methods.'},
            8: {'status': 'focus', 'note': 'Decorators, generators, error handling.'},
            9: {'status': 'recommended', 'note': 'Start your data science journey with NumPy.'},
            10: {'status': 'recommended', 'note': 'Data analysis with Pandas.'},
            11: {'status': 'recommended', 'note': 'Machine learning fundamentals.'},
        },
    },
    'intermediate': {
        'description': 'You\'re comfortable with Python. Jump into advanced and data science topics.',
        'start_chapter': 7,
        'chapters': {
            1: {'status': 'optional', 'note': 'Skip - review only if needed.'},
            2: {'status': 'optional', 'note': 'Skip - review only if needed.'},
            3: {'status': 'optional', 'note': 'Skip - review only if needed.'},
            4: {'status': 'optional', 'note': 'Skip - review only if needed.'},
            5: {'status': 'review', 'note': 'Quick review of comprehensions and sets.'},
            6: {'status': 'review', 'note': 'Quick review of file handling patterns.'},
            7: {'status': 'review', 'note': 'Review special methods and advanced OOP.'},
            8: {'status': 'focus', 'note': 'Master decorators, generators, and advanced patterns.'},
            9: {'status': 'focus', 'note': 'NumPy - essential for data science.'},
            10: {'status': 'focus', 'note': 'Pandas - the workhorse of data analysis.'},
            11: {'status': 'focus', 'note': 'Machine learning with scikit-learn.'},
        },
    },
}

# Experience level display names
LEVEL_DISPLAY_NAMES = {
    'complete_beginner': 'Complete Beginner',
    'some_experience': 'Some Programming Experience',
    'python_beginner': 'Python Beginner',
    'intermediate': 'Intermediate Python',
}

# Badge styling for chapter status
STATUS_BADGES = {
    'focus': {'class': 'bg-primary', 'icon': 'bi-star-fill', 'label': 'Focus'},
    'recommended': {'class': 'bg-success', 'icon': 'bi-check-circle', 'label': 'Recommended'},
    'review': {'class': 'bg-warning text-dark', 'icon': 'bi-arrow-repeat', 'label': 'Quick Review'},
    'optional': {'class': 'bg-secondary', 'icon': 'bi-dash-circle', 'label': 'Optional'},
}


def get_learning_plan(python_level):
    """Get the learning plan for a given Python level."""
    return LEARNING_PLANS.get(python_level, LEARNING_PLANS['complete_beginner'])


def get_chapter_recommendation(python_level, chapter_order):
    """Get the recommendation for a specific chapter based on user level."""
    plan = get_learning_plan(python_level)
    chapter_info = plan['chapters'].get(chapter_order, {})
    return {
        'status': chapter_info.get('status', 'recommended'),
        'note': chapter_info.get('note', ''),
        'badge': STATUS_BADGES.get(chapter_info.get('status', 'recommended'), STATUS_BADGES['recommended']),
    }


def get_start_chapter(python_level):
    """Get the recommended starting chapter for a given level."""
    plan = get_learning_plan(python_level)
    return plan.get('start_chapter', 1)


def get_level_display_name(python_level):
    """Get the display name for a Python level."""
    return LEVEL_DISPLAY_NAMES.get(python_level, 'Complete Beginner')
