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
from ExpenseReportSystemBE.logics.signup import createUser

# Import data
from ExpenseReportSystemBE.models.usr import User

validatorSchema = {
	User.email.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXEMAIL,
	},
	User.firstKorName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXKORNAME
	},
	User.firstLegalName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXLEGALNAME
	},
	User.lastKorName.name: {
		vc.TYPEOFINPUT: vc.STRING,
		vc.REGEX: vc.REGEXKORNAME
	},
	User.lastLegalName.name: {
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
		print(validator.errors)
		return fr(Response(), wcc.INVALIDINPUT)

	code = createUser(request.dbsession, inputs[User.email.name],
		inputs[User.lastKorName.name], inputs[User.firstKorName.name],
		inputs[User.lastLegalName.name], inputs[User.firstLegalName.name]
	)
	
	return fr(Response(), code)
