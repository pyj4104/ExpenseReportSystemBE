# Import libraries
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

# Import data
from ExpenseReportSystemBE.models.usr import User

# import mailer
from ExpenseReportSystemBE.components.mailer.mailerLogic import sendMail as sm

# import constants
import constants.validatorConstants as vc
import constants.webCommunications as wcc
from constants.services import LOGIN

def isEmailRegistered(dbsession: Session, email: str) -> bool:
	"""
		Checks if the email is registered.
		
		input: email string
		output: boolean value indicating whether the user was registered or not
	"""
	users = dbsession.query(User).filter_by(email=email)
	if users.count() > 1:
		raise IntegrityError
	user = users.first()
	if not user or not (user.approved):
		return False
	return True
