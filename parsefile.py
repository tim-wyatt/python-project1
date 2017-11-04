def parsetext(newfile):

    while True:
        lines = newfile.readline()
        if not lines:
            break
        extractword(lines)


def extractword(inline):
    wsIndex = 0
    chindex = 0
    torange = None

    torange = len(inline) - 1
    # for chindex in range(0, torange):
    while chindex < torange:
        if (inline[chindex] == " " or inline[chindex] == "."):
            '''we found a space or a full stop, so the previous characters were
            a word'''

            word = inline[wsIndex:chindex]

            print(word)

            '''need to save the index of the last whitespace char'''
            wsIndex = chindex + 1

        if (inline[chindex] == "."):
            chindex += 2
            wsIndex += 1
        else:
            chindex += 1
