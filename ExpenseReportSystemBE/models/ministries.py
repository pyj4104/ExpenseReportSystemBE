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
	ministryName = Column('ministryName', String(50), nullable=False, unique=True)
	deprecated = Column('deprecated', Boolean, nullable=False, default=False)

def initialize(dbsession):
	items = dbsession.query(Ministries).all()
	for item in items:
		print("Deleting {}".format(item.ministryName))
		item.deprecated = True
	dbsession.flush()
	for ministry in ministries:
		isIn = dbsession.query(Ministries).filter_by(ministryName=ministry).first()
		if not isIn:
			print("Adding {}".format(ministry))
			entry = Ministries(ministryName=ministry)
			dbsession.add(entry)
		else:
			if isIn.deprecated:
				print("Reviving {}".format(ministry))
				isIn.deprecated = False
