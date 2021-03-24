# Import libraries
import json, os, requests, shutil
from cerberus import Validator
from functools import partial
from pathlib import Path
from pyramid.view import view_config
from sqlalchemy.orm import load_only

# Import functions
from ExpenseReportSystemBE.helpers.modelToDict import modelToDict
from ExpenseReportSystemBE.helpers.responseFormatter import formatResponse

# Import models
from ExpenseReportSystemBE.models.expenseReports import ExpenseReports
from ExpenseReportSystemBE.models.receipts import Receipts

# Import constants
import constants.validatorConstants as vc
import constants.webCommunications as wcc
from constants.services import RECEIPTS
from constants.serviceSpecificConstants.uploadReceipts import FILEPATH, FOLDERPATH

@view_config(route_name=RECEIPTS, request_method=wcc.POST)
def submitReport(request):
	"""
		API for posting receipts and storing them to the server
		Access Method: GET
		Input: none
		Output: none
	"""
	sp = request.tm.savepoint()
	formID = request.POST['formID']
	fileDatas = request.POST.getall('file')

	try:
		formIDInInt = int(formID)
	except:
		return formatResponse(request.response, wcc.INVALIDINPUT)

	if str(formIDInInt) != formID:
		return formatResponse(request.response, wcc.INVALIDINPUT)

	for fileData in fileDatas:
		newFile = Receipts(
			formID = formID
		)
		request.dbsession.add(newFile)
		request.dbsession.flush()
		fileID = newFile.id
		userID = request.dbsession.query(ExpenseReports.userID).filter(ExpenseReports.id==formID).first()
		userID = userID if userID[0] else "unknown"
		fileType = fileData.filename.split(".")[-1]
		if fileType not in vc.ACCEPTEDEXT:
			sp.rollback()
			return formatResponse(request.response, wcc.INVALIDINPUT)
		folderPath = FOLDERPATH.format(uID=userID, fID=formID)
		if not os.path.exists(folderPath):
			os.makedirs(folderPath)
		path = FILEPATH.format(uID=userID, fID=formID, id=fileID, type=fileType)
		with open(path, 'wb+') as outputFile:
			outputFile.write(fileData.file.read())

	return formatResponse(request.response, wcc.OK)
