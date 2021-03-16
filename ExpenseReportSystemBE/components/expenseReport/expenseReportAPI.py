# Import libraries
import json, requests
from cerberus import Validator
from decimal import Decimal
from pyramid.view import view_config
from pyramid.response import Response

# Import logic
import ExpenseReportSystemBE.components.expenseReport.expenseReportLogic as logic

# Import data
from ExpenseReportSystemBE.models.expenseReport import ExpenseReport
from ExpenseReportSystemBE.models.usr import User

# Import functions
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse

# Import constants
import constants.session as sc
import constants.validatorConstants as vc
import constants.webCommunications as wcc
from constants.services import EXPENSEREPORT

validatorSchema = {
	ExpenseReport.ministryID.name: {
		vc.TYPEOFINPUT: vc.INTEGER
	},
	User.lastKorName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXKORNAME
	},
	User.firstKorName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXKORNAME
	},
	User.lastLegalName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXLEGALNAME
	},
	User.firstLegalName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXLEGALNAME
	},
	ExpenseReport.amount.name: {
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
	ministryID = inputs[ExpenseReport.ministryID.name]
	korName = inputs[User.lastKorName.name] + inputs[User.firstKorName.name]
	legalName = inputs[User.firstLegalName.name] + " " + inputs[User.lastLegalName.name]
	amount = Decimal(inputs[ExpenseReport.amount.name])

	# Put into DB
	reportID = logic.submitReport(request.dbsession, ministryID=ministryID, korName=korName, legalName=legalName, amount=amount)
	request.response.json_body = {ExpenseReport.id.name: reportID}

	return formatResponse(request.response, wcc.OK)
