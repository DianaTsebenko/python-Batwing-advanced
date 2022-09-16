"""004_add_invitation_status.py
Revision ID: 004_add_invitation_status.py
Revises: 003_create_user_event_table
Create Date: 2022-07-23 19:13:54.200297
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Enum
from sqlalchemy.dialects import postgresql

revision = '004_add_invitation_status.py'
down_revision = '003_create_user_event_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    inv_status = postgresql.ENUM('accepted', 'declined', 'pending', name='inv_status')
    inv_status.create(op.get_bind())

    op.add_column('user_event', sa.Column('invitation_status', sa.Enum('accepted',
                                                                       'declined',
                                                                       'pending',
                                                                       name='inv_status'),
                                          nullable=True))


def downgrade() -> None:
    op.drop_column('user_event', 'invitation_status')
