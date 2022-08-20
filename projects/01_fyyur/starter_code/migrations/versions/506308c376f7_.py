"""empty message

Revision ID: 506308c376f7
Revises: d5826169bc95
Create Date: 2022-08-20 21:47:44.329307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '506308c376f7'
down_revision = 'd5826169bc95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('Artist', 'seeking_performance_venue')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_performance_venue', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
