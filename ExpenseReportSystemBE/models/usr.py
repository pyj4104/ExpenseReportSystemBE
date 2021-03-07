from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Boolean,
	String,
)

from ExpenseReportSystemBE.models.meta import Base

class User(Base):
	__tablename__ = 'user'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	lastKorName = Column('lastKorName', Text, nullable=False)
	firstKorName = Column('firstKorName', Text, nullable=False)
	lastLegalName = Column('lastLegalName', Text, nullable=False)
	firstLegalName = Column('firstLegalName', Text, nullable=False)
	email = Column('email', String(350), nullable=False, unique=True)
	approved = Column('approved', Boolean, nullable=False, default=False)

Index('email_index', User.email, unique=True, mysql_length=320)
