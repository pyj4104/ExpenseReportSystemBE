"""With expense report tables

Revision ID: e5b5d6b996b8
Revises: 7262a55f098d
Create Date: 2021-03-14 01:49:11.219308

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e5b5d6b996b8'
down_revision = '7262a55f098d'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lastKorName', sa.Text(), nullable=False),
    sa.Column('firstKorName', sa.Text(), nullable=False),
    sa.Column('lastLegalName', sa.Text(), nullable=False),
    sa.Column('firstLegalName', sa.Text(), nullable=False),
    sa.Column('email', sa.String(length=350), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=False),
    sa.Column('role', sa.Enum('member', 'headOfDepartment', 'headOfDepartmentOfFinance', 'elderOfDepartmentOfFinance', 'siteAdmin', name='userrolesenum'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_User')),
    sa.UniqueConstraint('email', name=op.f('uq_User_email'))
    )
    op.create_index('email_index', 'User', ['email'], unique=True, mysql_length=320)
    op.drop_index('email_index', table_name='user')
    op.drop_index('uq_user_email', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=350), nullable=False),
    sa.Column('approved', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('firstKorName', mysql.TEXT(), nullable=False),
    sa.Column('firstLegalName', mysql.TEXT(), nullable=False),
    sa.Column('lastKorName', mysql.TEXT(), nullable=False),
    sa.Column('lastLegalName', mysql.TEXT(), nullable=False),
    sa.Column('role', mysql.ENUM('member', 'headOfDepartment', 'headOfDepartmentOfFinance', 'elderOfDepartmentOfFinance', 'siteAdmin'), nullable=False),
    sa.CheckConstraint('(`approved` in (0,1))', name='ck_user_approved'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('uq_user_email', 'user', ['email'], unique=True)
    op.create_index('email_index', 'user', ['email'], unique=True)
    op.drop_index('email_index', table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###