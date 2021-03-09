from enum import Enum as e

from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Boolean,
	String,
	Enum
)

from ExpenseReportSystemBE.models.meta import Base

class UserRolesEnum(e):
	member = 0
	headOfDepartment = 1
	headOfDepartmentOfFinance = 2
	elderOfDepartmentOfFinance = 3
	siteAdmin = 4

class User(Base):
	__tablename__ = 'user'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	lastKorName = Column('lastKorName', Text, nullable=False)
	firstKorName = Column('firstKorName', Text, nullable=False)
	lastLegalName = Column('lastLegalName', Text, nullable=False)
	firstLegalName = Column('firstLegalName', Text, nullable=False)
	email = Column('email', String(350), nullable=False, unique=True)
	approved = Column('approved', Boolean, nullable=False, default=False)
	role = Column(Enum(UserRolesEnum), nullable=False, default=UserRolesEnum.member)

Index('email_index', User.email, unique=True, mysql_length=320)
