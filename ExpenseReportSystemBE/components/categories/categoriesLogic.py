# Import Libraries
from decimal import Decimal
import json

# Import data
from ExpenseReportSystemBE.models.categories import Categories

def submitCategories(dbsession, inputs: [json]):
	print(inputs)
	for category in inputs:
		row = Categories(
			formID=category[Categories.formID.name],
			categoryName=category[Categories.categoryName.name],
			amount=Decimal(category[Categories.amount.name]),
		)
		if Categories.remarks.name in category:
			row.remarks = category[Categories.remarks.name]
		dbsession.add(row)
