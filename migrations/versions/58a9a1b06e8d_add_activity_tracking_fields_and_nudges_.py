"""Add activity tracking fields and nudges table

Revision ID: 58a9a1b06e8d
Revises:
Create Date: 2026-03-02 18:33:24.394009

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


# revision identifiers, used by Alembic.
revision = '58a9a1b06e8d'
down_revision = None
branch_labels = None
depends_on = None


def column_exists(table_name, column_name):
    """Check if a column already exists in a table."""
    bind = op.get_bind()
    inspector = inspect(bind)
    columns = [c['name'] for c in inspector.get_columns(table_name)]
    return column_name in columns


def table_exists(table_name):
    """Check if a table already exists."""
    bind = op.get_bind()
    inspector = inspect(bind)
    return table_name in inspector.get_table_names()


def upgrade():
    # Add activity tracking columns to users table (idempotent)
    if not column_exists('users', 'last_active_at'):
        op.add_column('users', sa.Column('last_active_at', sa.DateTime(), nullable=True))
    if not column_exists('users', 'last_ip'):
        op.add_column('users', sa.Column('last_ip', sa.String(length=45), nullable=True))
    if not column_exists('users', 'last_location'):
        op.add_column('users', sa.Column('last_location', sa.String(length=100), nullable=True))

    # Create nudges table (idempotent)
    if not table_exists('nudges'):
        op.create_table(
            'nudges',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=False),
            sa.Column('message', sa.String(length=500), nullable=False),
            sa.Column('nudge_type', sa.String(length=30), nullable=True),
            sa.Column('created_at', sa.DateTime(), nullable=True),
            sa.Column('read_at', sa.DateTime(), nullable=True),
            sa.ForeignKeyConstraint(['user_id'], ['users.id']),
            sa.PrimaryKeyConstraint('id'),
        )


def downgrade():
    if table_exists('nudges'):
        op.drop_table('nudges')
    if column_exists('users', 'last_location'):
        op.drop_column('users', 'last_location')
    if column_exists('users', 'last_ip'):
        op.drop_column('users', 'last_ip')
    if column_exists('users', 'last_active_at'):
        op.drop_column('users', 'last_active_at')
