#models.py

#connect to the database created in postgres
from app import db

#create a datamodel for the members table
class Members(db.Model):
	member_id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))
	email = db.Column(db.String(75))
	password = db.Column(db.String(30))

#create a datamodel for the events table
class Events(db.Model):
	event_id = db.Column(db.Integer, primary_key = True)
	event_name = db.Column(db.String(50))
	date = db.Column(db.DateTime)
	city = db.Column(db.String(100))
	attendance = db.Column(db.Integer)



