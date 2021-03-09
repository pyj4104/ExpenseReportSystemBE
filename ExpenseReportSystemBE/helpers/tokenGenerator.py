import random

def tokenGenerator(length: int) -> str:
	"""
		Generates security code composed of digit numbers and letters given length

		Output: security code with numbers and letters of given length
	"""
	possCombs = [str(i) for i in range(10)] + [chr(ord('a')+i) for i in range(26)] + \
		[chr(ord('A')+i) for i in range(26)]

	return ''.join([possCombs[random.randint(0, len(possCombs)-1)] for i in range(length)])
