"""003_create_user_event_table
Revision ID: 003_create_user_event_table
Revises: 002_create_event_table
Create Date: 2022-07-19 16:25:07.111440
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '003_create_user_event_table'
down_revision = '002_create_event_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user_event',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('event_id', sa.Integer(), sa.ForeignKey('event.id'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user_event')
