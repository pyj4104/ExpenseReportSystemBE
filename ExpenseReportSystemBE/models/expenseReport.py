from enum import Enum as e

from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Enum,
	ForeignKey,
	Numeric
)

from ExpenseReportSystemBE.models.meta import Base

class Ministries(e):
	children = 0
	hiC = 1
	youngPeople = 2

class ExpenseReport(Base):
	__tablename__ = 'ExpenseReport'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	userID = Column('userID', Integer, ForeignKey("User.id"), nullable=True)
	ministry = Column(Enum(Ministries), nullable=False)
	korName = Column('korName', Text, nullable=False)
	legalName = Column('legalName', Text, nullable=False)
	amount = Column('amountSpent', Numeric(12,2), nullable=False)
