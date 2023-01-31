"""add last few columns to posts table

Revision ID: 7a555079b92e
Revises: 2f3915ac6107
Create Date: 2023-01-31 16:10:26.001196

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '7a555079b92e'
down_revision = '2f3915ac6107'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
