# Import libraries
import json, requests
from cerberus import Validator
from pyramid.view import view_config
from pyramid.response import Response

# Import logic
from . import loginLogic

# Import data
from ExpenseReportSystemBE.models.usr import User

# Import functions
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse as fr
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
def login(request):
	"""
		LogIn API
		Access Method: GET
		Input: none
		Output: response that says to check email
	"""
	inputs = request.json_body
	validator = Validator(validatorSchema)
	if not validator.validate(inputs):
		return fr(Response(), wcc.INVALIDINPUT)
	print(type(request.dbsession))
	
	sm("pyj4104@hotmail.com")

	return fr(Response(), wcc.OK)
