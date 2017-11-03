import sys

def parsetext(newfile):

    lines = newfile.readline()
    extractword(lines)


def extractword(inline):
    wsIndex = 0
    chars = None
    torange = None

    torange = len(inline)  - 1
    for chars in range (0, torange):
        if inline[chars] == " "
            '''we found a space, so the previous characters were a word'''
            '''need to save the index of the last whitespace char'''
            wsIndex = chars
            
