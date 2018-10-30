import hashlib
import sys
import sqlite3

db = sqlite3.connect(':memory:')
cursor = db.cursor()

cursor.execute(''' CREATE TABLE url(id INTEGER PRIMARY KEY, baseUrl TEXT, hashedUrl TEXT)''')
id = random(11000)

def shorten(input):

	hash = hashlib.md5(input.encode())
	print(hash.hexdigest()[:8])

	return(hash.hexdigest()[:8])

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

	hashedUrl = shorten(url)
	switch = insert(hashedUrl, url)

def insert(hashedUrl,url):
	crusor.execute('''INSERT INTO URL(id,baseUrl,hashedUrl) VALUES(?,?,?)''', (id,url, hashedUrl)


main()
