import time

class SecCodeSession:
	userEmail: str
	created: int
	expires: int

	def __init__(self, email: str):
		self.userEmail = email
		self.created = int(time.time())
		self.expires = self.created + 600

class SecCodes:
	secCodesDict: dict # security codes to user data
	usrCodesDict: dict # user email to security codes data

	def __init__(self):
		self.secCodesDict = dict()
		self.usrCodesDict = dict()

	def initiateLogInProcedure(self, userEmail: str, token: str):
		"""
			Based on the generated token, creates double relationship from token to user and user to token.

			Inputs: userEmail, token
		"""
		self.removeSecCode(userEmail=userEmail)
		self.secCodesDict[token] = SecCodeSession(userEmail)
		self.usrCodesDict[userEmail] = token

	def retrieveUser(self, token: str) -> str:
		"""
			When either token or user email is passed in, returns the user email.
			Raises ValueError when either is empty or when both are passed in.

			Inputs: token in str, userEmail in str

		"""
		return self.secCodesDict[token].userEmail

	def isSecCodeIn(self, token: str) -> bool:
		"""
			Checks whether the security code is active or not.

			Input: token with the length of 6
			Output: True if the session is active. False if the session is not active
				or the token is wrong
		"""
		if token not in self.secCodesDict:
			return False
		if int(time.time()) > self.secCodesDict[token].expires:
			return False
		return True

	def removeSecCode(self, userEmail: str = None, token: str = None):
		if userEmail and userEmail in self.usrCodesDict and not token:
			token = self.usrCodesDict[userEmail]
		elif not userEmail and token and token in self.secCodesDict:
			userEmail = self.secCodesDict[token].userEmail
		elif not userEmail and not token:
			raise ValueError("Both fields cannot be empty")

		self.__removeToken__(token)
		self.__removeUserEmail__(userEmail)

	def __removeToken__(self, token: str):
		if token in self.secCodesDict:
			del(self.secCodesDict[token])

	def __removeUserEmail__(self, email: str):
		if email in self.usrCodesDict:
			del(self.usrCodesDict[email])

currentSecCodes = SecCodes()
