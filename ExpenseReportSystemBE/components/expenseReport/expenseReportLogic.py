# Import libraries
from decimal import Decimal

# Import data
from ExpenseReportSystemBE.models.expenseReports import ExpenseReports

# Import constants
import constants.webCommunications as wcc

# Import data
from ExpenseReportSystemBE.models.users import Users

def submitReport(dbsession, ministryID: int, korName: str, legalName: str,
	amount: Decimal, userID: int = None) -> int:
	
	newReport = ExpenseReports(
		ministryID=ministryID,
		korName=korName,
		legalName=legalName,
		amount=amount,
		userID=userID
	)

	dbsession.add(newReport)
	dbsession.flush()

	return newReport.id
