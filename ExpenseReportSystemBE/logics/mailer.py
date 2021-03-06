# for mailing services
import yagmail

def sendMail(receiver: str):
	yag = yagmail.SMTP(user="kwchurchinhouseapptest@gmail.com", password="1Plo126HDUC9t9li649G")
	yag.send(
		to=receiver,
		subject="Yagmail Test",
		contents="Hello World!",
	)
