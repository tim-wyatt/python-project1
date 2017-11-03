
"""The aim of this project is to take a file of text and sort the words based on the last
letter of each word. This is the main entry point"""



import sys
import wordcharsstruc
from parsefile import parsetext

def main ():

	"""first thing we need to do is read in a file that is passed in as the programme is
	executed"""
	print(sys.argv[1])
	newfile = open(sys.argv[1],'r')
	parsetext(newfile)
	#Now need to read each word into a wordStruct class and then add that to a list (linked list?)



if __name__ == '__main__':
	main()
