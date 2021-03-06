# Import libraries
import json, requests
from functools import partial
from pyramid.view import view_config
from sqlalchemy.orm import load_only

# Import functions
from ExpenseReportSystemBE.helpers.modelToDict import modelToDict
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse

# Import models
from ExpenseReportSystemBE.models.ministries import Ministries

# Import constants
import constants.webCommunications as wcc
from constants.services import MINISTRIES

@view_config(route_name=MINISTRIES, request_method=wcc.GET)
def submitReport(request):
	"""
		API for getting the list of ministries
		Access Method: GET
		Input: none
		Output: list of ministries in json format
	"""
	request.response.headers[wcc.CONTENTTYPE] = wcc.JSON
	dataModel = [Ministries.id.name, Ministries.ministryName.name]
	ministries = list(map(partial(modelToDict,columnNames=dataModel),
		(request.dbsession.query(Ministries.id, Ministries.ministryName)
		.order_by(Ministries.id)
		.all())))
	request.response.json_body = ministries

	return formatResponse(request.response, wcc.OK)
