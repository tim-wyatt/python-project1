

class node:

	"""This will be used to store data about each word as it is entered into the list.
	I did it as an exercise in using classes - don't judge :D"""

	def __init__(self, theword):
		self.wordlen = 0
		self.wordcount = 0
		self.wordindex = 0
		self.theword = theword # this should make each object equal to the word name
		self.incrementwordcount()
		self.setwordlength()

	def incrementwordcount(self):
		self.wordcount += 1

	def setwordlength(self):
		self.wordlen = len(self.theword)

	def getwordlen(self):
		return self.wordlen

	def getwordcount(self):
		return self.wordcount
