#====================================================
#views.py
#====================================================

#Allow for app to recognize and use characters from different languages
# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template
from models import Members, Events

#This is the landing page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#This is the page that displays the Member info
@app.route('/members', methods = ['GET', 'POST'])
def members():
	members = Members.query.all()
	return render_template('members.html', members = members)

@app.route('/events', methods = ['GET', 'POST'])
def events():
	events = Events.query.all()
	return render_template('events.html', events = events)
