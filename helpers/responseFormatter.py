# Formats response and decorates it with the code passed into the function
def formatResponse(response, stat):
	response.status = stat
	response.status_int = stat
	return response
