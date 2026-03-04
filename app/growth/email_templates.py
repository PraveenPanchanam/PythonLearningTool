"""
HTML email templates for the growth engine.

Each function returns a tuple of (subject, html_body, text_body).
Templates are styled inline for maximum email client compatibility.
"""


def _base_template(title, body_html, cta_url=None, cta_text=None):
    """Wrap content in a branded email layout."""
    cta_block = ''
    if cta_url and cta_text:
        cta_block = f'''
        <div style="text-align: center; margin: 30px 0;">
            <a href="{cta_url}" style="
                display: inline-block;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #ffffff;
                text-decoration: none;
                padding: 14px 32px;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
            ">{cta_text}</a>
        </div>'''

    return f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="margin: 0; padding: 0; background-color: #f4f4f7; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <!-- Header -->
        <div style="text-align: center; padding: 20px 0;">
            <h1 style="margin: 0; color: #667eea; font-size: 24px;">
                &#128013; Python Learning Tool
            </h1>
        </div>

        <!-- Main Card -->
        <div style="background: #ffffff; border-radius: 12px; padding: 32px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
            <h2 style="color: #1a1a2e; margin-top: 0; font-size: 20px;">{title}</h2>
            {body_html}
            {cta_block}
        </div>

        <!-- Footer -->
        <div style="text-align: center; padding: 20px 0; color: #999; font-size: 12px;">
            <p>Python Learning Tool — Learn Python for Data Science</p>
            <p>You are receiving this email because you registered on our platform.</p>
        </div>
    </div>
</body>
</html>'''


def render_welcome_email(user, app):
    """Welcome email sent after registration."""
    base_url = app.config.get('BASE_URL', 'https://python-learning-tool.onrender.com')

    subject = f"Welcome to Python Learning Tool, {user.username}!"

    body = f'''
    <p style="color: #333; line-height: 1.6;">
        Hi <strong>{user.username}</strong>,
    </p>
    <p style="color: #333; line-height: 1.6;">
        Welcome to Python Learning Tool! You have taken the first step toward
        mastering Python for data science. Here is what awaits you:
    </p>

    <div style="margin: 20px 0;">
        <div style="padding: 12px 16px; background: #f0f4ff; border-radius: 8px; margin-bottom: 10px;">
            <strong style="color: #667eea;">&#128202; 11 Structured Chapters</strong>
            <span style="color: #666;"> — from basics to machine learning</span>
        </div>
        <div style="padding: 12px 16px; background: #f0f4ff; border-radius: 8px; margin-bottom: 10px;">
            <strong style="color: #667eea;">&#127919; Hands-on Assignments</strong>
            <span style="color: #666;"> — auto-graded with instant feedback</span>
        </div>
        <div style="padding: 12px 16px; background: #f0f4ff; border-radius: 8px; margin-bottom: 10px;">
            <strong style="color: #667eea;">&#128640; Data Science Focus</strong>
            <span style="color: #666;"> — NumPy, Pandas, and Scikit-Learn</span>
        </div>
    </div>

    <p style="color: #333; line-height: 1.6;">
        <strong>Recommended starting point:</strong> Chapter 1 covers Python fundamentals.
        If you already know Python basics, jump to Chapter 9 (NumPy) to dive into data science.
    </p>
    '''

    html = _base_template(
        f"Welcome, {user.username}!",
        body,
        cta_url=f"{base_url}/chapters/",
        cta_text="Start Learning Now",
    )

    text = (
        f"Welcome to Python Learning Tool, {user.username}!\n\n"
        f"You've taken the first step toward mastering Python for data science.\n\n"
        f"Start learning: {base_url}/chapters/\n"
    )

    return subject, html, text


def render_milestone_email(user, chapter, app):
    """Congratulations email for completing a chapter."""
    base_url = app.config.get('BASE_URL', 'https://python-learning-tool.onrender.com')

    subject = f"Congratulations! You completed {chapter.title}"

    body = f'''
    <p style="color: #333; line-height: 1.6;">
        Hi <strong>{user.username}</strong>,
    </p>
    <p style="color: #333; line-height: 1.6;">
        Amazing work! You have completed <strong>{chapter.title}</strong> — all assignments
        passed and all lessons finished. That is a real achievement!
    </p>

    <div style="text-align: center; margin: 24px 0; padding: 20px; background: linear-gradient(135deg, #f0f4ff 0%, #e8f0fe 100%); border-radius: 12px;">
        <div style="font-size: 48px; margin-bottom: 8px;">&#127942;</div>
        <div style="font-size: 18px; font-weight: 600; color: #1a1a2e;">Chapter Complete!</div>
        <div style="color: #666; margin-top: 4px;">{chapter.title}</div>
    </div>

    <p style="color: #333; line-height: 1.6;">
        <strong>Claim your certificate!</strong> Visit your dashboard to get a shareable
        certificate that you can add to your LinkedIn profile.
    </p>
    '''

    html = _base_template(
        f"You completed {chapter.title}!",
        body,
        cta_url=f"{base_url}/dashboard/",
        cta_text="Claim Your Certificate",
    )

    text = (
        f"Congratulations, {user.username}!\n\n"
        f"You completed {chapter.title}. Claim your certificate at: {base_url}/dashboard/\n"
    )

    return subject, html, text


def render_nudge_email(user, days_inactive, app):
    """Re-engagement email for inactive users."""
    base_url = app.config.get('BASE_URL', 'https://python-learning-tool.onrender.com')

    subject = f"We miss you, {user.username}! Your Python journey awaits"

    body = f'''
    <p style="color: #333; line-height: 1.6;">
        Hi <strong>{user.username}</strong>,
    </p>
    <p style="color: #333; line-height: 1.6;">
        It has been {days_inactive} days since your last visit. Your Python learning
        journey is waiting for you!
    </p>

    <div style="margin: 20px 0; padding: 16px; background: #fff8e1; border-radius: 8px; border-left: 4px solid #ffc107;">
        <strong style="color: #856404;">Did you know?</strong>
        <p style="color: #856404; margin: 8px 0 0 0;">
            Consistent practice — even 15 minutes a day — is the most effective way
            to learn programming. Small steps add up to big results.
        </p>
    </div>

    <p style="color: #333; line-height: 1.6;">
        Pick up where you left off and keep building your data science skills.
        NumPy, Pandas, and Scikit-Learn are waiting!
    </p>
    '''

    html = _base_template(
        "Your Python journey awaits!",
        body,
        cta_url=f"{base_url}/dashboard/",
        cta_text="Continue Learning",
    )

    text = (
        f"Hi {user.username},\n\n"
        f"It's been {days_inactive} days since your last visit.\n"
        f"Continue learning: {base_url}/dashboard/\n"
    )

    return subject, html, text


def render_first_assignment_email(user, app):
    """Encouragement for users who haven't tried any assignment yet."""
    base_url = app.config.get('BASE_URL', 'https://python-learning-tool.onrender.com')

    subject = f"Ready for your first challenge, {user.username}?"

    body = f'''
    <p style="color: #333; line-height: 1.6;">
        Hi <strong>{user.username}</strong>,
    </p>
    <p style="color: #333; line-height: 1.6;">
        You have registered but have not tried any assignments yet. Our auto-graded
        assignments are the best way to solidify your Python skills!
    </p>

    <div style="margin: 20px 0;">
        <div style="padding: 12px 16px; background: #e8f5e9; border-radius: 8px; margin-bottom: 10px;">
            <strong style="color: #2e7d32;">&#9989; Instant feedback</strong>
            <span style="color: #666;"> — see results immediately</span>
        </div>
        <div style="padding: 12px 16px; background: #e8f5e9; border-radius: 8px; margin-bottom: 10px;">
            <strong style="color: #2e7d32;">&#128221; Safe sandbox</strong>
            <span style="color: #666;"> — your code runs in a secure environment</span>
        </div>
        <div style="padding: 12px 16px; background: #e8f5e9; border-radius: 8px;">
            <strong style="color: #2e7d32;">&#128170; Build confidence</strong>
            <span style="color: #666;"> — start easy, grow gradually</span>
        </div>
    </div>

    <p style="color: #333; line-height: 1.6;">
        Start with Chapter 1 — the first assignments are designed to be approachable
        and build your confidence.
    </p>
    '''

    html = _base_template(
        "Try your first assignment!",
        body,
        cta_url=f"{base_url}/chapters/",
        cta_text="Start Your First Assignment",
    )

    text = (
        f"Hi {user.username},\n\n"
        f"Ready for your first Python challenge?\n"
        f"Start here: {base_url}/chapters/\n"
    )

    return subject, html, text


def render_stuck_email(user, assignment, attempts, app):
    """Encouragement for users stuck on an assignment."""
    base_url = app.config.get('BASE_URL', 'https://python-learning-tool.onrender.com')

    subject = f"Need a hand with {assignment.title}?"

    body = f'''
    <p style="color: #333; line-height: 1.6;">
        Hi <strong>{user.username}</strong>,
    </p>
    <p style="color: #333; line-height: 1.6;">
        We noticed you have attempted <strong>{assignment.title}</strong> {attempts} times.
        Getting stuck is completely normal — it is part of the learning process!
    </p>

    <div style="margin: 20px 0; padding: 16px; background: #e3f2fd; border-radius: 8px; border-left: 4px solid #2196f3;">
        <strong style="color: #1565c0;">Tips to get unstuck:</strong>
        <ul style="color: #1565c0; margin: 8px 0 0 0; padding-left: 20px;">
            <li>Re-read the lesson for this topic carefully</li>
            <li>Break the problem into smaller steps</li>
            <li>Test your code with simple inputs first</li>
            <li>Check for common mistakes (typos, wrong variable names, off-by-one errors)</li>
        </ul>
    </div>

    <p style="color: #333; line-height: 1.6;">
        Every expert programmer has been stuck many times. The key is persistence.
        You are closer to the solution than you think!
    </p>
    '''

    html = _base_template(
        f"Tips for {assignment.title}",
        body,
        cta_url=f"{base_url}/chapters/",
        cta_text="Try Again",
    )

    text = (
        f"Hi {user.username},\n\n"
        f"Stuck on {assignment.title}? Here are some tips:\n"
        f"1. Re-read the lesson\n2. Break the problem into smaller steps\n"
        f"3. Test with simple inputs\n\n"
        f"Try again: {base_url}/chapters/\n"
    )

    return subject, html, text


def render_reengagement_email(user, app):
    """Welcome back email for returning users."""
    from app.models.blog_post import BlogPost

    base_url = app.config.get('BASE_URL', 'https://python-learning-tool.onrender.com')

    subject = f"Welcome back, {user.username}!"

    # Get latest blog posts for "what's new" section
    recent_posts = BlogPost.query.filter_by(is_published=True).order_by(
        BlogPost.published_at.desc()
    ).limit(3).all()

    posts_html = ''
    if recent_posts:
        posts_items = ''.join(
            f'<li style="margin-bottom: 6px;"><a href="{base_url}/blog/{p.slug}" '
            f'style="color: #667eea; text-decoration: none;">{p.title}</a></li>'
            for p in recent_posts
        )
        posts_html = f'''
        <div style="margin: 20px 0;">
            <strong style="color: #333;">Latest from our blog:</strong>
            <ul style="color: #666; padding-left: 20px; margin-top: 8px;">
                {posts_items}
            </ul>
        </div>'''

    body = f'''
    <p style="color: #333; line-height: 1.6;">
        Hi <strong>{user.username}</strong>,
    </p>
    <p style="color: #333; line-height: 1.6;">
        Great to see you back! Your learning progress is saved and ready for you
        to pick up where you left off.
    </p>
    {posts_html}
    <p style="color: #333; line-height: 1.6;">
        Jump back into your dashboard to continue building your Python and data science skills.
    </p>
    '''

    html = _base_template(
        f"Welcome back, {user.username}!",
        body,
        cta_url=f"{base_url}/dashboard/",
        cta_text="Continue Learning",
    )

    text = (
        f"Welcome back, {user.username}!\n\n"
        f"Your progress is saved. Continue learning: {base_url}/dashboard/\n"
    )

    return subject, html, text
