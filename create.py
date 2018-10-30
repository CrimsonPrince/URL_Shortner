import sqlite3

def main():
	db = sqlite3.connect(':memory:')
	cursor = db.cursor()
	id = 10
	baseUrl = "Hello"
	hashedUrl = "Great"
	cursor.execute(''' CREATE TABLE url(id INTEGER PRIMARY KEY, baseUrl TEXT, hashedUrl TEXT)''')
	cursor.execute('''INSERT INTO url(id, baseUrl, hashedUrl) VALUES(?,?,?)''', (id,baseUrl, hashedUrl))
	cursor.execute('''SELECT id, baseUrl, hashedUrl FROM url WHERE ? = id''', (id,))
	test = cursor.fetchone()
	print(test[0])

main()
