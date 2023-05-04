"""Add user_id to categories

Revision ID: 10f956d156f7
Revises: 
Create Date: 2023-05-03 23:40:59.325248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10f956d156f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('categories', sa.Column('description', sa.String))

    # ### end Alembic commands ###


def downgrade():
    op.drop_column('categories', 'description')

    # ### end Alembic commands ###
