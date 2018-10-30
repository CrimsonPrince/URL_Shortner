from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Url(db.model):
	__tablename__ = "URLS"
	originalUrl = db.column(db.String, primary_key = True)
	hashedUrl = db.column(db.String, nullable = False)

	def add_Url(self,baseUrl, inputHashed):
