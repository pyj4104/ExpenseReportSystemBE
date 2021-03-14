from ExpenseReportSystemBE.models.usr import User, UserRolesEnum

class Sessions:
	usrTokenDict: dict
	tokenUsrDict: dict

	def __init__(self):
		self.usrTokenDict = dict()
		self.tokenUsrDict = dict()

	def startSession(self, token: str, user: User):
		self.__removeUsr__(user.email)
		self.usrTokenDict[user.email] = token
		self.tokenUsrDict[token] = user

	def isLoggedIn(self, token: str):
		if token in self.tokenUsrDict:
			return True
		return False

	def __removeUsr__(self, userEmail: str):
		if userEmail in self.usrTokenDict:
			token = self.usrTokenDict[userEmail]
			del self.usrTokenDict[userEmail]
			if token in self.tokenUsrDict:
				del self.tokenUsrDict[token]

def getUser(dbsession, email: str) -> User:
	"""
		Checks if the email is registered.
		
		input: email string
		output: boolean value indicating whether the user was registered or not
	"""
	users = dbsession.query(User).filter_by(email=email)
	if users.count() > 1:
		raise IntegrityError
	user = users.first()
	return user

currentSessions = Sessions()
