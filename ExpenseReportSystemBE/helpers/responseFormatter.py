# Import constants
from constants.webCommunications import DEFAULTHEADER

def addHeaders(response, headers: dict = DEFAULTHEADER):
	for headerKey, headerVal in headers.items():
		response.headers[headerKey] = headerVal

def formatResponse(response, stat):
	"""
		Formats response. Adds security measures too.
		inputs: response, status code
		output: response
	"""
	response.status = stat
	response.status_int = stat
	return response
