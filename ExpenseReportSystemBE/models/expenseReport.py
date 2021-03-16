from datetime import date

from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Enum,
	ForeignKey,
	Numeric,
	Date
)

from ExpenseReportSystemBE.models.meta import Base

class ExpenseReport(Base):
	__tablename__ = 'ExpenseReport'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	userID = Column('userID', Integer, ForeignKey("User.id"), nullable=True)
	ministryID = Column('ministryID', Integer, ForeignKey("Ministries.id"), nullable=False)
	korName = Column('korName', Text, nullable=False)
	legalName = Column('legalName', Text, nullable=False)
	amount = Column('amount', Numeric(12,2), nullable=False)
	date = Column('date', Date, nullable=False, default=date.today())
