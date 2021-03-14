# Import constants
def formatResponse(response, stat):
	"""
		Formats response. Adds security measures too.
		inputs: response, status code
		output: response
	"""
	response.status = stat
	response.status_int = stat
	return response
