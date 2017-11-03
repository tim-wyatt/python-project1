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
        if (inline[chars] == " " or inline[chars] == "."):
            '''we found a space or a full stop, so the previous characters were a word'''
            '''need to save the index of the last whitespace char'''
            word = inline[wsIndex:chars]
            print(word)

            if (inline[chars] == "."):
                chars +=  1
            wsIndex = chars
