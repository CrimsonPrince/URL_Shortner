from flask import Flask, render_template, jsonify, request
import hashlib
import os

def shorten(input):

	hash = hashlib.md5(input.encode())
	print(hash.hexdigits())

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


if name = '__main__':
	app = Flask(__name__)
	main()
