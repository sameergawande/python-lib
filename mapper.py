#!/usr/bin/python3
import sys
def read_input(file):
	for line in file:
		yield line.split()

def main(seperator='\t'):
	data = read_input(sys.stdin)
	for words in data:	
		for word in words:
			print ({}{}{}.format(word,seperator,1)

if __name__ == "__main__:
	main()
