# Import libraries
from pyramid import httpexceptions
from pyramid.view import notfound_view_config

# Import constants
import constants.webCommunications as wcc

@notfound_view_config()
def notfound_view(request):
	"""
		When a user try to access undefined path.
		Input: request
		Output: response with error code 404
	"""
	return httpexceptions.exception_response(wcc.PAGENOTFOUND, json=wcc.INVALIDPATH)
