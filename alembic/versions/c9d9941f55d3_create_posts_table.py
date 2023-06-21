"""create posts table

Revision ID: c9d9941f55d3
Revises: 
Create Date: 2023-06-20 22:22:48.085084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9d9941f55d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
