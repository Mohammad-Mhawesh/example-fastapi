"""add rest of columns to posts table

Revision ID: bb7891aafe18
Revises: d03999857b94
Create Date: 2023-06-21 11:32:19.168692

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = 'bb7891aafe18'
down_revision = 'dad82f95c8db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean,
                  nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=text('now()')))
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), sa.ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False))
    pass


def downgrade() -> None:

    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'owner_id')
    pass
