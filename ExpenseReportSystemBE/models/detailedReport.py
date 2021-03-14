from sqlalchemy import (
	Column,
	Integer,
	Text,
	ForeignKey,
	Numeric,
	Date
)

from ExpenseReportSystemBE.models.meta import Base

class DetailedReport(Base):
	__tablename__ = 'DetailedReport'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	formID = Column('formID', Integer, ForeignKey('ExpenseReport.id'), nullable=False)
	categoryID = Column('categoryID', Integer, ForeignKey('Categories.id'), nullable=False)
	date = Column('date', Date, nullable=False)
	amount = Column('amountSpent', Numeric(12,2), nullable=False)
	breakdown = Column('breakdown', Text, nullable=True)

