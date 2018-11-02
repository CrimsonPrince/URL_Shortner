import hashlib
import sys
import sqlite3
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
db = sqlite3.connect('db.sqlite', check_same_thread=False)
cursor = db.cursor()

#cursor.execute(''' CREATE TABLE url(id INTEGER PRIMARY KEY, baseUrl TEXT, hashedUrl TEXT)''')
id = 10

def shorten(input):

	hash = hashlib.md5(input.encode())
	print(hash.hexdigest()[:8])

	return(hash.hexdigest()[:8])

def insert(hashedUrl,url):
	cursor.execute('''INSERT INTO URL(baseUrl,hashedUrl) VALUES(?,?)''', (url, hashedUrl))
	db.commit()
	if len(result) == 0:
		return render_template("error.html", message="Errror Inserting URL into DB")

	message = "Your Shortened URL is" + hashedUrl
	return render_template("success.html", message=message)

@app.route('/')
def index():
   return render_template("index.html")

@app.route("/submit", methods=["POST"])
def convert():
	'''Main function runs '''
	url = request.form.get('url')
	hashedUrl = shorten(url)
	switch = insert(hashedUrl, url)


@app.route("/<url>")
def redirect(url):
	cursor.execute('''SELECT baseUrl, hashedUrl FROM url''')
	test = cursor.fetchall()
	if len(test) == 0:
		print("Not in DB")
		print(test)
		return ('', 204)
	return ('', 204)
