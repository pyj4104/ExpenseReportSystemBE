# RESTful API standard operations
POST = 'POST'
GET = 'GET'
PUT = 'PUT'
DELETE = 'DELETE'
PATCH = 'PATCH'
OPTIONS = 'OPTIONS'

# HTTP Response Status Codes
OK = 200
ACCEPTED = 201
NOTREGISTERED = 403
PAGENOTFOUND = 404
CONFLICT = 409
INVALIDINPUT = 422
INTERNALSERVERERROR = 500
SERVICEUNAVAILABLE = 503

# Error Messages
SERVERTIMEOUT = 'The endpoint server is down. Please try again later.'
INVALIDPATH = {"error":"The page requested is not found. Please check the URL."}

# Headers
DEFAULTHEADER = {
	'Access-Control-Allow-Origin': "*",
	'Access-Control-Allow-Methods': "GET, POST, DELETE, PUT",
	'Access-Control-Allow-Headers': "Content-Type, Authorization",
}
