"""Change column name from desicrption to description

Revision ID: 4e982922f970
Revises: 10f956d156f7
Create Date: 2023-05-04 01:09:27.427722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e982922f970'
down_revision = '10f956d156f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.alter_column('categories', 'desicrption', new_column_name='description')

        batch_op.drop_column('desicrption')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('desicrption', sa.VARCHAR(length=80), nullable=True))
        batch_op.drop_column('description')

    # ### end Alembic commands ###
