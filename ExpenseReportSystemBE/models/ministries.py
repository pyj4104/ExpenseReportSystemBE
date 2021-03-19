from sqlalchemy.exc import IntegrityError
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

ministries = set([
	"Children",
	"Hi-C",
	"Young Adults",
	"Finance",
	"Mission",
])

class Ministries(Base):
	__tablename__ = 'Ministries'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	ministry = Column('ministry', String(50), nullable=False, unique=True)

def initialize(dbsession):
	items = dbsession.query(Ministries).all()
	for item in items:
		if item.ministry not in ministries:
			print("Deleting {}".format(item.ministry))
			dbsession.delete(item)
			dbsession.flush()
	for ministry in ministries:
		isIn = dbsession.query(Ministries).filter_by(ministry=ministry).first()
		if not isIn:
			entry = Ministries(ministry=ministry)
			dbsession.add(entry)
			print("Adding {}".format(ministry))
