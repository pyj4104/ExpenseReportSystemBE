# Import libraries
import json, requests
from cerberus import Validator
from pyramid.view import view_config
from pyramid.response import Response

# Import logic
from . import secCheckLogic as logic

# Import data
from ExpenseReportSystemBE.models.usr import User

# Import functions
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse, addHeaders
from ExpenseReportSystemBE.helpers.tokenGenerator import tokenGenerator as tg

# Import constants
from constants.services import SECCHECK
import constants.session as sc
import constants.validatorConstants as vc
import constants.webCommunications as wcc
import constants.serviceSpecificConstants.secCheck as c

validatorSchema = {
	c.SECCODE: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXSECCODE,
	},
}

@view_config(route_name=SECCHECK, request_method=wcc.POST)
def submitSecCodePOST(request):
	"""
		LogIn API
		Access Method: POST
		Input: none
		Output: response that says to check email
	"""
	addHeaders(request.response)
	inputs = request.json_body
	validator = Validator(validatorSchema)
	if not validator.validate(inputs):
		return formatResponse(request.response, wcc.INVALIDINPUT)
	code = inputs[c.SECCODE]
	if not logic.currentSecCodes.isSecCodeIn(code):
		return formatResponse(request.response, wcc.NOTREGISTERED)
	
	request.session[sc.AUTHORIZATION] = tg(32)
	logic.currentSecCodes.removeSecCode(token = code)

	return formatResponse(request.response, wcc.OK)

@view_config(route_name=SECCHECK, request_method=wcc.OPTIONS)
def submitSecCodeOPTIONS(request):
	"""
		Set CORS policy
		Access Method = OPTIONS
		Input: none
		Output: returns headers that will allow the access control
	"""
	response = request.response
	addHeaders(response)

	return formatResponse(response, wcc.OK)
