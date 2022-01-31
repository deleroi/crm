"""empty message

Revision ID: ca9e1f5aef8c
Revises: 49ee153853fe
Create Date: 2022-01-28 12:34:33.998009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca9e1f5aef8c'
down_revision = '49ee153853fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('countrys', 'value',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('countrys', 'value',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###