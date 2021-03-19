"""Added deprecated column to the ministries table

Revision ID: 1eb1d18c40a0
Revises: 20f1d6eef87b
Create Date: 2021-03-19 13:58:47.039896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eb1d18c40a0'
down_revision = '20f1d6eef87b'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Ministries', sa.Column('deprecated', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Ministries', 'deprecated')
    # ### end Alembic commands ###
