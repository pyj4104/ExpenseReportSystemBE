"""Uinque constraints on the ministry name

Revision ID: cbddfc2c434b
Revises: c74e945c021d
Create Date: 2021-03-15 16:18:29.308989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbddfc2c434b'
down_revision = 'c74e945c021d'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Ministries',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ministry', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Ministries')),
    sa.UniqueConstraint('ministry', name=op.f('uq_Ministries_ministry'))
    )
    op.create_table('UserRoles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('ministryID', sa.Integer(), nullable=False),
    sa.Column('role', sa.Enum('member', 'head', 'elder', name='userrolesenum'), nullable=False),
    sa.ForeignKeyConstraint(['ministryID'], ['Ministries.id'], name=op.f('fk_UserRoles_ministryID_Ministries')),
    sa.ForeignKeyConstraint(['userID'], ['User.id'], name=op.f('fk_UserRoles_userID_User')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_UserRoles'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserRoles')
    op.drop_table('Ministries')
    # ### end Alembic commands ###