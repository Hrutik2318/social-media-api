"""add content column to posts table

Revision ID: 517890268edd
Revises: e02ab07924bb
Create Date: 2023-01-31 15:31:02.409263

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '517890268edd'
down_revision = 'e02ab07924bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
