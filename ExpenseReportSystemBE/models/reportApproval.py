from enum import Enum as e

from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Enum,
	ForeignKey,
	Numeric,
	Boolean
)

from ExpenseReportSystemBE.models.meta import Base

class ReportApproval(Base):
	__tablename__ = 'ReportApproval'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	formID = Column('formID', Integer, ForeignKey("ExpenseReport.id"), nullable=False)
	headOfDepartment = Column('headOfDepartment', Boolean, nullable=False, default=False)
	headOfFinancial = Column('headOfFinancial', Boolean, nullable=False, default=False)
	financialElder = Column('financialElder', Boolean, nullable=False, default=False)
