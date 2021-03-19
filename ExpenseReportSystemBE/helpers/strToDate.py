import datetime

def toDate(dateInStr: str) -> datetime.date:
	dateObj = datetime.datetime.strptime(dateInStr, '%Y-%m-%d')
	return dateObj.date()
