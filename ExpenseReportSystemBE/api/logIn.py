# imort libraries
from pyramid.response import Response
from pyramid.view import view_config

# import helper functions
from helpers.responseFormatter import formatResponse as fr

# import constants
import constants.webCommunications as wcc
from constants.services import LOGIN

@view_config(route_name=LOGIN, request_method=wcc.POST)
def login(request):
	"""
		LogIn API
	"""
	response = fr(Response(), wcc.OK)
	return response
