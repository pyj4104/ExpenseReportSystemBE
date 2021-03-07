# imort libraries
import json, requests
from pyramid.view import view_config
from pyramid.response import Response

# import mailer
from ExpenseReportSystemBE.logics.mailer import sendMail

# import helper functions
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse as fr

# import constants
import constants.webCommunications as wcc
from constants.services import LOGIN

@view_config(route_name=LOGIN, request_method=wcc.POST)
def login(request):
	"""
		LogIn API
		Access Method: GET
		Input: none
		Output: response that says to check email
	"""
	response = fr(Response(), wcc.OK)
	
	sendMail("pyj4104@hotmail.com")

	return response
