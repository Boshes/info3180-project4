"""empty message

Revision ID: 213264aded57
Revises: 363c95029955
Create Date: 2016-03-27 19:28:29.267034

"""

# revision identifiers, used by Alembic.
revision = '213264aded57'
down_revision = '363c95029955'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tokens',
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('token', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['userid'], ['persons.id'], ),
    sa.PrimaryKeyConstraint('token')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tokens')
    ### end Alembic commands ###