"""
Flask CLI commands for the growth engine.

Usage:
    flask growth publish-next
    flask growth publish-scheduled
    flask growth run-engagement
    flask growth refresh-analytics
    flask growth status
    flask growth seed-content
"""

import click
from flask import current_app
from flask.cli import AppGroup

growth_cli = AppGroup('growth', help='Growth engine commands')


@growth_cli.command('publish-next')
def publish_next():
    """Publish the next pre-written blog post."""
    from app.growth.content_pipeline import publish_next_post
    from app.models.user import User

    admin = User.query.filter_by(is_admin=True).first()
    author_id = admin.id if admin else None

    post = publish_next_post(author_id=author_id)
    if post:
        click.echo(f'Published: "{post.title}" at /blog/{post.slug}')
    else:
        click.echo('No pending posts to publish. All 15 growth posts are live.')


@growth_cli.command('publish-scheduled')
def publish_scheduled():
    """Publish posts where scheduled_at <= now."""
    from app.growth.content_pipeline import publish_scheduled_posts

    count = publish_scheduled_posts()
    click.echo(f'Published {count} scheduled post(s).')


@growth_cli.command('run-engagement')
def run_engagement():
    """Run all engagement rules."""
    from app.growth.engagement_rules import run_all_rules

    app = current_app._get_current_object()
    results = run_all_rules(app)

    click.echo('Engagement rule results:')
    for rule_name, count in results.items():
        status = f'{count} actions' if isinstance(count, int) else count
        click.echo(f'  {rule_name}: {status}')


@growth_cli.command('refresh-analytics')
def refresh_analytics():
    """Refresh blog view counts and analytics data."""
    from app.growth.seo_optimizer import refresh_view_counts

    updated = refresh_view_counts()
    click.echo(f'Refreshed view counts for {updated} post(s).')


@growth_cli.command('status')
def status():
    """Print current growth KPIs."""
    from app.growth.analytics import get_growth_kpis
    from app.models.blog_post import BlogPost
    from app.growth.content_pipeline import get_pending_posts

    kpis = get_growth_kpis(days=30)

    click.echo('\n=== Growth Engine Status (Last 30 Days) ===\n')
    click.echo(f'  Total Users:        {kpis["total_users"]}')
    click.echo(f'  New Registrations:   {kpis["new_registrations"]}')
    click.echo(f'  Active Users:        {kpis["active_users"]}')
    click.echo(f'  Submissions:         {kpis["total_submissions"]}')
    click.echo(f'  Pass Rate:           {kpis["pass_rate"]}%')
    click.echo(f'  Blog Views:          {kpis["blog_views"]}')
    click.echo(f'  Certificates Issued: {kpis["certificates_issued"]}')

    total_posts = BlogPost.query.count()
    published = BlogPost.query.filter_by(is_published=True).count()
    scheduled = BlogPost.query.filter(
        BlogPost.scheduled_at != None,  # noqa: E711
        BlogPost.is_published == False,  # noqa: E712
    ).count()
    pending = len(get_pending_posts())

    click.echo(f'\n  Blog Posts:')
    click.echo(f'    Published:  {published}')
    click.echo(f'    Scheduled:  {scheduled}')
    click.echo(f'    In Queue:   {pending} (not yet in DB)')
    click.echo(f'    Total:      {total_posts}')
    click.echo('')


@growth_cli.command('seed-content')
def seed_content():
    """Load all 15 pre-written posts as scheduled drafts."""
    from app.growth.content_pipeline import seed_scheduled_posts
    from app.models.user import User

    admin = User.query.filter_by(is_admin=True).first()
    author_id = admin.id if admin else None

    count = seed_scheduled_posts(author_id=author_id, interval_days=3)
    if count:
        click.echo(f'Seeded {count} blog post(s) as scheduled drafts (one every 3 days).')
    else:
        click.echo('All growth posts already exist in database. Nothing to seed.')


@growth_cli.command('seo-report')
def seo_report():
    """Run an SEO audit on all published blog posts."""
    from app.growth.seo_optimizer import get_seo_report

    report = get_seo_report()
    click.echo(f'\n=== SEO Report ===\n')
    click.echo(f'  Total published posts: {report["total_posts"]}')
    click.echo(f'  Posts with issues:     {report["posts_with_issues"]}')

    if report['issues']:
        click.echo('\n  Issues found:')
        for item in report['issues']:
            click.echo(f'\n    "{item["title"]}" (/blog/{item["slug"]})')
            for issue in item['issues']:
                click.echo(f'      - {issue}')
    else:
        click.echo('  No issues found. All posts are SEO-ready!')
    click.echo('')
