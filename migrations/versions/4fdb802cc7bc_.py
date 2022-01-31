"""empty message

Revision ID: 4fdb802cc7bc
Revises: 5a220a182911
Create Date: 2022-01-26 22:05:30.587041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fdb802cc7bc'
down_revision = '5a220a182911'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('company_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contact', 'company', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contact', type_='foreignkey')
    op.drop_column('contact', 'company_id')
    # ### end Alembic commands ###