# Import libraries
import json, requests
from cerberus import Validator
from pyramid.view import view_config
from pyramid.response import Response

# Import logic
from . import loginLogic as logic

# Import classes
import ExpenseReportSystemBE.components.secCheck.secCheckLogic as secCode

# Import data
from ExpenseReportSystemBE.models.usr import User

# Import functions
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse, addHeaders
from ExpenseReportSystemBE.helpers.tokenGenerator import tokenGenerator as tg
from ExpenseReportSystemBE.components.mailer.mailerLogic import sendMail as sm

# Import constants
from constants.services import LOGIN
import constants.validatorConstants as vc
import constants.webCommunications as wcc

validatorSchema = {
	User.email.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXEMAIL,
	},
}

@view_config(route_name=LOGIN, request_method=wcc.POST)
def logInPost(request):
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
	email = inputs[User.email.name]
	if not logic.isEmailRegistered(request.dbsession, email):
		return formatResponse(request.response, wcc.NOTREGISTERED)

	token = tg(6)
	
	secCode.currentSecCodes.initiateLogInProcedure(email, token)
	sm(request, email, token)

	return formatResponse(request.response, wcc.OK)

@view_config(route_name=LOGIN, request_method=wcc.OPTIONS)
def logInOptions(request):
	"""
		Set CORS policy
		Access Method = OPTIONS
		Input: none
		Output: returns headers that will allow the access control
	"""
	response = request.response
	addHeaders(response)

	return formatResponse(response, wcc.OK)
