"""002_create_authors_table
Revision ID: 002_create_authors_table
Revises: 001_create_book_table
Create Date: 2022-07-15 09:30:16.188006
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '002_create_authors_table'
down_revision = '001_create_book_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "authors",
        sa.Column("authors_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name_surname", sa.String(300), nullable=False, unique=True)
    )


def downgrade() -> None:
    op.drop_table("authors")
