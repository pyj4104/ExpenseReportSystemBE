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

ministries = [
	"Children",
	"Hi-C",
	"Young Adults",
	"Finance",
	"Mission",
]

class Ministries(Base):
	__tablename__ = 'Ministries'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	ministry = Column('ministry', String(50), nullable=False, unique=True)

	def initialize(dbsession):
		for ministry in ministries:
			entry = Ministries(ministry=ministry)
			dbsession.add(entry)
