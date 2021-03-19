# Import Libraries
from decimal import Decimal
import json

# Import helper
from ExpenseReportSystemBE.helpers.strToDate import toDate

# Import data
from ExpenseReportSystemBE.models.detailedReports import DetailedReports

def submitDetailedReport(dbsession, inputs: [json]):
	for report in inputs:
		row = DetailedReports(
			categoryID=report[DetailedReports.categoryID.name],
			date= toDate(report[DetailedReports.date.name]),
			amount=Decimal(report[DetailedReports.amount.name]),
			breakdown=report[DetailedReports.breakdown.name]
		)
		dbsession.add(row)
