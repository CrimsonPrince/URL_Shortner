import hashlib
import sys
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
db = sqlite3.connect(':memory:')
cursor = db.cursor()

cursor.execute(''' CREATE TABLE url(id INTEGER PRIMARY KEY, baseUrl TEXT, hashedUrl TEXT)''')
id = 10

def shorten(input):

	hash = hashlib.md5(input.encode())
	print(hash.hexdigest()[:8])

	return(hash.hexdigest()[:8])

def insert(hashedUrl,url):
	cursor.execute('''INSERT INTO URL(id,baseUrl,hashedUrl) VALUES(?,?,?)''', (id,url, hashedUrl))
	"""cursor.execute('''SELECT baseUrl, hashedUrl FROM url WHERE id = ?''', (id,))
	test = cursor.fetchone()
	print(test[0])
	print(test[1])"""
	return(True)

@app.route("/", methods=["POST"])
def convert():
	'''Main function runs '''
	url = request.form.get('url')
	hashedUrl = shorten(url)
	switch = insert(hashedUrl, url)
	
	if switch:
		print("Worked Yay")

@app.route("/flights/<String:url>")
def redirect(url):

	cursor.execute('''SELECT baseUrl, hashedUrl FROM url WHERE hashedUrl = ?''', (url,))
	test = cursor.fetchall()
	if len(test) = 0:
		print("Error")

	return redirect(test[0], code=302)


main()
