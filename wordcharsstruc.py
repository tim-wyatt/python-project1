

class wordStruct:

	"""This will be used to store data about each word as it is entered into the list"""


	def __init__(self, theword):
		wordlen = 0
		wordcount = 0
		wordindex = 0
		self.theword = theword # this should make each object equal to the word name

	def incrementwordcount(self):
		wordcount = wordcount + 1

	def setwordlength (self):
		wordlen = len(self.theword)

	def getwordlen(self):
		return self.wordlen

	def getwordcount(self):
		return self.wordcount

