

class wordStruct:

"""This will be used to store data about each word as it is entered into the list"""
	
	wordlen = 0
	wordcount = 0
	wordindex = 0

	def __init__(self, theword):
		self.theword = theword # this should make each object equal to the word name

	def incrementwordcount(self):
		wordcount = wordcount + 1

	def setwordlength (self):
		wordlen = len(self.theword)

	def getwordlen(self):
		"""do some stuff to return the wordlen"""

	def getwordcount(self):
		"""do some stuff to return the word count"""


