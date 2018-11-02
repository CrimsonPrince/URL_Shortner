import sqlite3
from pprint import pprint

db = sqlite3.connect('db.sqlite', check_same_thread=False)
cursor = db.cursor()

cursor.execute("select * from url")
results  = cursor.fetchall()

pprint(results)
