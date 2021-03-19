# Import libraries
import json, requests
from bs4 import BeautifulSoup
from cerberus import Validator
from decimal import Decimal
from pyramid.view import view_config
from pyramid.response import Response

# Import logic
import ExpenseReportSystemBE.components.detailedReport.detailedReportLogic as logic

# Import data
from ExpenseReportSystemBE.models.detailedReports import DetailedReports

# Import functions
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse

# Import constants
import constants.session as sc
import constants.validatorConstants as vc
import constants.webCommunications as wcc
from constants.services import DETAILEDREPORTS

validatorSchema = {
	DetailedReports.__tablename__: {
		vc.TYPEOFINPUT: vc.LIST,
		vc.SCHEMA: {
			vc.TYPEOFINPUT: vc.DICT,
			vc.SCHEMA: {
				DetailedReports.categoryID.name: {vc.TYPEOFINPUT: vc.INTEGER},
				DetailedReports.date.name: {vc.TYPEOFINPUT: vc.STRING, vc.REGEX: vc.REGEXDATE},
				DetailedReports.amount.name: {vc.TYPEOFINPUT: vc.STRING, vc.REGEX: vc.REGEXMONEY},
				DetailedReports.breakdown.name: {vc.TYPEOFINPUT: vc.STRING},
			}
		}
	}
}

@view_config(route_name=DETAILEDREPORTS, request_method=wcc.POST)
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
		print(validator.errors)
		return formatResponse(request.response, wcc.INVALIDINPUT)

	# Sanitize input
	for detailedReport in inputs[DetailedReports.__tablename__]:
		soup = BeautifulSoup(detailedReport[DetailedReports.breakdown.name], features='lxml')
		detailedReport[DetailedReports.breakdown.name] = soup.get_text()

	if not inputs[DetailedReports.__tablename__]:
		request.response.json_body = {"error": "Please submit at least one category"}
		return formatResponse(request.response, wcc.OK)

	# Put into DB
	logic.submitDetailedReport(request.dbsession, inputs[DetailedReports.__tablename__])

	return formatResponse(request.response, wcc.OK)
