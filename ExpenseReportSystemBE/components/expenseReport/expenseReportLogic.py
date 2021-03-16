# Import libraries
from decimal import Decimal

# Import data
from ExpenseReportSystemBE.models.expenseReport import ExpenseReport

# Import constants
import constants.webCommunications as wcc

# Import data
from ExpenseReportSystemBE.models.usr import User

def submitReport(dbsession, ministryID: int, korName: str, legalName: str,
	amount: Decimal, userID: int = None) -> int:
	
	newReport = ExpenseReport(
		ministryID=ministryID,
		korName=korName,
		legalName=legalName,
		amount=amount,
		userID=userID
	)

	dbsession.add(newReport)
	dbsession.flush()

	return newReport.id
