"""add foreign key to posts table

Revision ID: 2f3915ac6107
Revises: 553451e46fcb
Create Date: 2023-01-31 16:01:27.319164

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '2f3915ac6107'
down_revision = '553451e46fcb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", local_cols=[
                          "owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
