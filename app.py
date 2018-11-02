import hashlib
import sys
import sqlite3
from flask import Flask, render_template, request, url_for, redirect, send_from_directory, abort
import os
from urllib.parse import urlparse, urlsplit


app = Flask(__name__)
db = sqlite3.connect('db.sqlite', check_same_thread=False)
cursor = db.cursor()

#cursor.execute(''' CREATE TABLE url(id INTEGER PRIMARY KEY, baseUrl TEXT, hashedUrl TEXT)''')
id = 10

def shorten(input):
	parse = urlsplit(input)

	if parse.scheme == '':
		input = 'http://' + input

	print(input)
	hash = hashlib.md5(input.encode())
	print(hash.hexdigest()[:8])

	return(hash.hexdigest()[:8])

def insert(hashedUrl,url):
	cursor.execute('''INSERT INTO URL(baseUrl,hashedUrl) VALUES(?,?)''', (url, hashedUrl))
	result = cursor.fetchall()
	db.commit()

	return result

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<string:url>')
def serveUrl(url):
	cursor.execute('''SELECT baseUrl, hashedUrl FROM url WHERE hashedUrl = ?''', (url,))
	test = cursor.fetchone()
	if test is None:
		error = "This URL does not exist in our database"
		return render_template("error.html", message=error)
		#return abort(404)
	print(test[0])
	return redirect("http://" + test[0])

@app.route('/')
def index():
   return render_template("index.html")

@app.route("/submit", methods=["POST"])
def convert():

	url = request.form.get('url')
	hashedUrl = shorten(url)
	result = insert(hashedUrl, url)


	return render_template("success.html", url=hashedUrl)
