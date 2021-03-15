"""divided authorization

Revision ID: c74e945c021d
Revises: c7e7c9a1aecb
Create Date: 2021-03-15 00:47:15.375038

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c74e945c021d'
down_revision = 'c7e7c9a1aecb'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Ministries',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ministry', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Ministries'))
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
    op.drop_column('User', 'role')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('role', mysql.ENUM('member', 'headOfDepartment', 'headOfDepartmentOfFinance', 'elderOfDepartmentOfFinance', 'siteAdmin'), nullable=False))
    op.drop_table('UserRoles')
    op.drop_table('Ministries')
    # ### end Alembic commands ###
