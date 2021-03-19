from sqlalchemy import (
	Column,
	Integer,
	Text,
	ForeignKey,
	Numeric
)

from ExpenseReportSystemBE.models.meta import Base

class Categories(Base):
	__tablename__ = 'Categories'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	formID = Column('formID', Integer, ForeignKey("ExpenseReports.id"), nullable=False)
	categoryName = Column('categoryName', Text, nullable=False)
	amount = Column('amount', Numeric(12,2), nullable=False)
	remarks = Column('remarks', Text, nullable=True)
