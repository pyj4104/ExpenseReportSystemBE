from datetime import date

from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Enum,
	ForeignKey,
	Numeric,
	Date,
	Boolean
)

from ExpenseReportSystemBE.models.meta import Base

class ExpenseReports(Base):
	__tablename__ = 'ExpenseReports'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	userID = Column('userID', Integer, ForeignKey("Users.id"), nullable=True)
	ministryID = Column('ministryID', Integer, ForeignKey("Ministries.id"), nullable=False)
	korName = Column('korName', Text, nullable=False)
	legalName = Column('legalName', Text, nullable=False)
	amount = Column('amount', Numeric(12,2), nullable=False)
	date = Column('date', Date, nullable=False, default=date.today())
	submitted = Column('submitted', Boolean, nullable=False, default=False)
