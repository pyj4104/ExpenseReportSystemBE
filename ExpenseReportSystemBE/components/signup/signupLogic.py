# Import libraries
from sqlalchemy.exc import IntegrityError

# Import constants
import constants.webCommunications as wcc

# Import data
from ExpenseReportSystemBE.models.usr import User

def createUser(dbsession, email: str, lastKorName: str, firstKorName: str,
		lastLegalName: str, firstLegalName: str) -> int:

	newUser = User(
		email=email,
		lastKorName=lastKorName,
		firstKorName=firstKorName,
		lastLegalName=lastLegalName,
		firstLegalName=firstLegalName
	)

	if len(dbsession.query(User.email).filter_by(email=email).all()) > 0:
		return wcc.CONFLICT

	dbsession.add(newUser)

	return wcc.ACCEPTED
