from sqlalchemy import inspect

def modelToDict(obj, columnNames: [str] = None):
	if columnNames:
		return {colName: getattr(obj, colName) for colName in columnNames}
	return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
