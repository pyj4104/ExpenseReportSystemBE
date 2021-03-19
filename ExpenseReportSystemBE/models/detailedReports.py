from datetime import date

from sqlalchemy import (
	Column,
	Integer,
	Text,
	ForeignKey,
	Numeric,
	Date
)

from ExpenseReportSystemBE.models.meta import Base

class DetailedReports(Base):
	__tablename__ = 'DetailedReports'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	categoryID = Column('categoryID', Integer, ForeignKey('Categories.id'), nullable=False)
	date = Column('date', Date, nullable=False, default=date.today())
	amount = Column('amount', Numeric(12,2), nullable=False)
	breakdown = Column('breakdown', Text, nullable=True)
