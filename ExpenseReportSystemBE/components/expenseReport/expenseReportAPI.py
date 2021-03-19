# Import libraries
import json, requests
from cerberus import Validator
from decimal import Decimal
from pyramid.view import view_config
from pyramid.response import Response

# Import logic
import ExpenseReportSystemBE.components.expenseReport.expenseReportLogic as logic

# Import data
from ExpenseReportSystemBE.models.expenseReports import ExpenseReports
from ExpenseReportSystemBE.models.users import Users

# Import functions
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse

# Import constants
import constants.session as sc
import constants.validatorConstants as vc
import constants.webCommunications as wcc
from constants.services import EXPENSEREPORT

validatorSchema = {
	ExpenseReports.ministryID.name: {
		vc.TYPEOFINPUT: vc.INTEGER
	},
	Users.lastKorName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXKORNAME
	},
	Users.firstKorName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXKORNAME
	},
	Users.lastLegalName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXLEGALNAME
	},
	Users.firstLegalName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXLEGALNAME
	},
	ExpenseReports.amount.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXMONEY
	}
}

@view_config(route_name=EXPENSEREPORT, request_method=wcc.POST)
def submitReport(request):
	"""
		API for submitting expense report
		Access Method: POST
		Input: none
		Output: response that tells the user whether it succeeded or not.
	"""
	# Set the return type
	request.response.headers[wcc.CONTENTTYPE] = wcc.JSON

	# Validate
	inputs = request.json_body
	validator = Validator(validatorSchema)
	if not validator.validate(inputs):
		return formatResponse(request.response, wcc.INVALIDINPUT)

	# Get input params
	ministryID = inputs[ExpenseReports.ministryID.name]
	korName = inputs[Users.lastKorName.name] + inputs[Users.firstKorName.name]
	legalName = inputs[Users.firstLegalName.name] + " " + inputs[Users.lastLegalName.name]
	amount = Decimal(inputs[ExpenseReports.amount.name])

	# Put into DB
	reportID = logic.submitReport(request.dbsession, ministryID=ministryID, korName=korName, legalName=legalName, amount=amount)
	request.response.json_body = {ExpenseReports.id.name: reportID}

	return formatResponse(request.response, wcc.OK)
