"""Add Fortune

Revision ID: ec151a783dad
Revises: 857e9445e819
Create Date: 2019-10-25 10:41:54.230914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec151a783dad'
down_revision = '857e9445e819'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fortunes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('sign', sa.String(), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('item', sa.String(), nullable=False),
    sa.Column('money', sa.Integer(), nullable=False),
    sa.Column('job', sa.Integer(), nullable=False),
    sa.Column('love', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date', 'sign', name='unique_idx_date_sign')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fortunes')
    # ### end Alembic commands ###
