from pyramid.request import Request

# for mailing services
import yagmail

def sendMail(request: Request, receiver: str, token: str):
	mailBody = "Security token: " + token
	email = request.registry.settings['mail.username']
	password = request.registry.settings['mail.password']
	yag = yagmail.SMTP(user=email, password=password)
	yag.send(
		to=receiver,
		subject="Here's your security token",
		contents=mailBody,
	)
