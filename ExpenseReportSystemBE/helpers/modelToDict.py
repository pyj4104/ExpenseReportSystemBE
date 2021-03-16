from sqlalchemy import inspect

def modelToDict(obj):
	return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}