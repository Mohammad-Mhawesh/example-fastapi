"""add content column to posts table

Revision ID: 2d08b9e07cbe
Revises: c9d9941f55d3
Create Date: 2023-06-20 22:35:34.939356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d08b9e07cbe'
down_revision = 'c9d9941f55d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(),nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
