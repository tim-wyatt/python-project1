def parsetext(newfile):
    currentWordList = []

    while True:
        lines = newfile.readline()
        if not lines:
            break
        if len(lines) > 1:
            newWordlist = extractword(lines, currentWordList)
            currentWordList = newWordlist

    print(currentWordList)
    print(len(currentWordList))

def extractword(inline, wordList):
    wsIndex = 0
    chindex = 0
    torange = None


    torange = len(inline) - 1
    while chindex < torange:
        if (inline[chindex] == " " or inline[chindex] == "." or inline[chindex]=="\r"):
            '''we found a space or a full stop, so the previous characters were
            a word'''

            word = inline[wsIndex:chindex]

            addWordtoList(word, wordList)

            '''need to save the index of the last whitespace char'''
            wsIndex = chindex + 1
'''this is a test'''
        if (inline[chindex] == "."):
            chindex += 2
            wsIndex += 1
        else:
            chindex += 1
    return wordList

def addWordtoList(word, wordList):
    lastLetter = 0
    counter = 0
    checkStringLast = None
    checkString = None

    lastLetter = len(word) - 1
    # Base case where list is empty
#    if (len(wordList) == 0):
#        wordList.append(word)
#    else:
        # Now we need to add each word in order of the last letter
    while counter <= len(wordList) - 1:
        checkString = wordList[counter]
        checkStringLast = len(checkString) - 1
        if(word[lastLetter] <= checkString[checkStringLast]):
            wordList.insert(counter, word)
            return None
        counter += 1

    wordList.append(word)
