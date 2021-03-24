from sqlalchemy.exc import IntegrityError
from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Boolean,
	String,
	Enum,
    ForeignKey,
)
from ExpenseReportSystemBE.models.meta import Base
from ExpenseReportSystemBE.models.expenseReports import ExpenseReports

class Receipts(Base):
	__tablename__ = 'Receipts'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	formID = Column('formID', Integer, ForeignKey('ExpenseReports.id'), nullable=False)
