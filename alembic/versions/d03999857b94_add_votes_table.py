"""add votes table

Revision ID: d03999857b94
Revises: dad82f95c8db
Create Date: 2023-06-21 11:15:15.009709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd03999857b94'
down_revision = 'dad82f95c8db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes', sa.Column('user_id', sa.Integer(), sa.ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True, nullable = False),
        sa.Column('post_id', sa.Integer(), sa.ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True, nullable = False))
    pass


def downgrade() -> None:
    op.drop_table("votes")
    pass
