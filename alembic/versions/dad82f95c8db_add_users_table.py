"""add users table

Revision ID: dad82f95c8db
Revises: 2d08b9e07cbe
Create Date: 2023-06-20 22:39:50.960398

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = 'dad82f95c8db'
down_revision = '2d08b9e07cbe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(),
                              primary_key=True, nullable=False),
                    sa.Column('email', sa.String(),
                              nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              nullable=False, server_default=text('now()')))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
