# Import libraries
import json, requests
from cerberus import Validator
from pyramid import httpexceptions
from pyramid.view import view_config
from pyramid.response import Response

# Import helper
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse as fr

# Import constants
from constants.services import SIGNUP
import constants.validatorConstants as vc
import constants.webCommunications as wcc

# Import logics
from .signupLogic import createUser

# Import data
from ExpenseReportSystemBE.models.users import Users

validatorSchema = {
	Users.email.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXEMAIL,
	},
	Users.firstKorName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXKORNAME
	},
	Users.firstLegalName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXLEGALNAME
	},
	Users.lastKorName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXKORNAME
	},
	Users.lastLegalName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXLEGALNAME
	},
}

@view_config(route_name=SIGNUP, request_method=wcc.POST)
def signUp(request):
	"""
		Registers user
		input: with json body, please pass in both first and last Korean name, first and last legal name,
				and email
		output: either 200 OK, 500 internal server error, 422 invalid input, or 503 service unavailable
	"""
	inputs = request.json_body
	validator = Validator(validatorSchema)
	if not validator.validate(inputs):
		return fr(request.response, wcc.INVALIDINPUT)

	code = createUser(request.dbsession, inputs[Users.email.name],
		inputs[Users.lastKorName.name], inputs[Users.firstKorName.name],
		inputs[Users.lastLegalName.name], inputs[Users.firstLegalName.name]
	)
	
	return fr(request.response, code)
