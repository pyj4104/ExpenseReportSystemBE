from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Boolean,
	String,
	Enum,
	ForeignKey
)

from ExpenseReportSystemBE.models.enum.userRolesEnum import UserRolesEnum

from ExpenseReportSystemBE.models.meta import Base

class UserRoles(Base):
	__tablename__ = 'UserRoles'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	userID = Column('userID', Integer, ForeignKey("Users.id"), nullable=False)
	ministry = Column('ministryID', Integer, ForeignKey("Ministries.id"), nullable=False)
	role = Column(Enum(UserRolesEnum), nullable=False, default=UserRolesEnum.member)
