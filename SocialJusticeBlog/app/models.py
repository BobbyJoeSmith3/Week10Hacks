#models.py

from app import db

class Post(db.Model):
	title = db.Column(db.String(50))
	author = db.Column(db.String(50))
	content = db.Column(db.Text)