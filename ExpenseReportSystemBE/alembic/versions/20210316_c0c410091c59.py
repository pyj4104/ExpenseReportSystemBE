"""Fixed typo

Revision ID: c0c410091c59
Revises: e891b1f76d92
Create Date: 2021-03-16 12:45:02.742428

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c0c410091c59'
down_revision = 'e891b1f76d92'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Categories', sa.Column('amount', sa.Numeric(precision=12, scale=2), nullable=False))
    op.drop_column('Categories', 'amountSpent')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Categories', sa.Column('amountSpent', mysql.DECIMAL(precision=12, scale=2), nullable=False))
    op.drop_column('Categories', 'amount')
    # ### end Alembic commands ###
