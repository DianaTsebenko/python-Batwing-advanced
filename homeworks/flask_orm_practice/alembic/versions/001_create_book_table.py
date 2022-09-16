"""001_create_book_table
Revision ID: 001_create_books_table
Revises:
Create Date: 2022-07-15 07:49:50.441813
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '001_create_book_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book",
        sa.Column("book_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("book_name", sa.String(300), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("book")
