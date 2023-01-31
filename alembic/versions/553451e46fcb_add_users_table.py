"""add users table

Revision ID: 553451e46fcb
Revises: 517890268edd
Create Date: 2023-01-31 15:54:12.836873

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '553451e46fcb'
down_revision = '517890268edd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
