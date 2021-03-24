# Import libraries
import json, requests
from bs4 import BeautifulSoup
from cerberus import Validator
from functools import partial
from pyramid.view import view_config
from pyramid.response import Response

# Import logic
import ExpenseReportSystemBE.components.categories.categoriesLogic as logic

# Import data
from ExpenseReportSystemBE.models.categories import Categories

# Import functions
from ExpenseReportSystemBE.helpers.modelToDict import modelToDict
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse

# Import constants
import constants.session as sc
import constants.validatorConstants as vc
import constants.webCommunications as wcc
from constants.services import CATEGORIES

validatorSchema = {
	Categories.__tablename__: {
		vc.TYPEOFINPUT: vc.LIST,
		vc.SCHEMA: {
			vc.TYPEOFINPUT: vc.DICT,
			vc.SCHEMA: {
				Categories.formID.name: {vc.TYPEOFINPUT: vc.INTEGER},
				Categories.categoryName.name: {vc.TYPEOFINPUT: vc.STRING, vc.REGEX: vc.REGEXCATEGORIES},
				Categories.amount.name: {vc.TYPEOFINPUT: vc.STRING,vc.REGEX: vc.REGEXMONEY},
				Categories.remarks.name: {vc.TYPEOFINPUT: vc.STRING},
			}
		}
	}
}

@view_config(route_name=CATEGORIES, request_method=wcc.POST)
def submitReport(request):
	"""
		API for submitting expense report
		Access Method: POST
		Input: none
		Output: response that tells the user whether it succeeded or not.
	"""
	# Set the return type
	request.response.headers[wcc.CONTENTTYPE] = wcc.JSON

	# Validate
	inputs = request.json_body
	validator = Validator(validatorSchema)
	if not validator.validate(inputs):
		print(validator.errors)
		return formatResponse(request.response, wcc.INVALIDINPUT)

	# Sanitize input
	for category in inputs[Categories.__tablename__]:
		if Categories.remarks.name in category:
			soup = BeautifulSoup(category[Categories.remarks.name], features='html.parser')
			category[Categories.remarks.name] = soup.get_text()
	
	if not inputs[Categories.__tablename__]:
		request.response.json_body = {"error": "Please submit at least one category"}
		return formatResponse(request.response, wcc.OK)

	# Put into DB
	logic.submitCategories(request.dbsession, inputs[Categories.__tablename__])

	return formatResponse(request.response, wcc.OK)

@view_config(route_name=CATEGORIES, request_method=wcc.GET)
def getCategories(request):
	# Set the return type
	request.response.headers[wcc.CONTENTTYPE] = wcc.JSON
	
	inputs = dict(request.GET)

	schema = {
		Categories.formID.name: {
			vc.TYPEOFINPUT: vc.STRING,
			vc.REGEX: vc.REGEXINTEGER
		}
	}
	
	validator = Validator(schema)
	if not validator.validate(inputs):
		return formatResponse(request.response, wcc.INVALIDINPUT)

	formID = int(inputs[Categories.formID.name])
	
	dataModel = [Categories.id.name, Categories.categoryName.name]
	categories = (
		request.dbsession.query(
			Categories.id,
			Categories.categoryName
		).filter(
			Categories.formID==formID
		).all()
	)

	categoriesDict = list(
		map(
			partial(modelToDict,columnNames=dataModel), categories
		)
	)

	request.response.json_body = categoriesDict

	return formatResponse(request.response, wcc.OK)