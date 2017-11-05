class node:
    """This will be used to store data about each word as it is entered into
    the list. I did it as an exercise in using classes - don't judge :D"""

    def __init__(self, theword):
        self.wordlen = 0
        self.wordcount = 0
        self.wordindex = 0
        self.next
        self.prev
        self.setdata(theword)
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

    def setData(self, data):
        self.theword = data

    def getTheWord(self):
        return self.theword
