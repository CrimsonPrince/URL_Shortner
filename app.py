import hashlib
import sys
import SQLalchemy

def shorten(input):

	hash = hashlib.md5(input.encode())
	print(hash.hexdigest()[:8])

	return(hash)

def main():

	'''Main function runs '''

	#Checks if the number of arguments matches one
	try:
		url = sys.argv[1]
	except IndexError:
		print("Please Submit an argument in the form of a valid URL")
		sys.exit(2)

	if len(sys.argv) > 2:
		print("Too many arguments submitted please submit an argument in the form of the direct link to the file")
		sys.exit(2)

	shortenurl = shorten(url)


if __name__ == '__main__':
	main()
