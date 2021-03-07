# Import data
from ExpenseReportSystemBE.models.usr import User

# import mailer
from ExpenseReportSystemBE.components.mailer.mailerLogic import sendMail

# import constants
import constants.validatorConstants as vc
import constants.webCommunications as wcc
from constants.services import LOGIN

def isEmailRegistered(dbsession, email: str) -> bool:
	"""
		Checks if the email is registered.
		
		input: email string
		output: boolean value indicating whether the user was registered or not
	"""
	pass
