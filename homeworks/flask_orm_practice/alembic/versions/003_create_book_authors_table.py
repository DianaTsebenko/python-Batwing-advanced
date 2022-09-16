"""003_create_book_authors_table
Revision ID: 003_create_book_authors_table
Revises: 002_create_authors_table
Create Date: 2022-07-15 11:47:59.069101
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_create_book_authors_table'
down_revision = '002_create_authors_table'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.create_table(
        "book_authors",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("book_id", sa.Integer, sa.ForeignKey("book.book_id")),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("authors.authors_id"))
    )


def downgrade() -> None:
    op.drop_table("books_authors")