"""The aim of this project is to take a file of text and sort the words based
on the last letter of each word. This is the main entry point"""

import sys
import time
from parsefile import parsetext


def main():
    timeStart = None
    timeEnd = None
    execTime = None

    timeStart = time.time()
    try:
        newfile = open(sys.argv[1], 'r')
    except IndexError:
        print(
             "sort_word requires an input file\nPlease run python sort_word.py <file_to_sort>"
        )
        exit()

    parsetext(newfile)
    '''Now need to read each word into a wordStruct class and then add that to a
    list (linked list?)'''

    timeEnd = time.time()
    execTime = timeEnd - timeStart
    print("\n\nTotal time to execute script == " + str(execTime))


if __name__ == '__main__':
    main()
