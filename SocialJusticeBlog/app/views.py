#====================================================
#views.py
#====================================================

#Allow for app to recognize and use characters from different languages
# -*- coding: utf-8 -*-

from app import app, db		#import our app and db components from other files
from flask import Flask, render_template, redirect
from models import Post
from forms import NewPostForm

#This is the landing page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#This is the posts page
@app.route('/post_page', methods = ['GET', 'POST'])
def post_page():
	form = NewPostForm()
	if form.validate_on_submit():
		post = Post()
		form.populate_obj(post)
		db.session.add(post)
		db.session.commit()
		return redirect('/post_page')	
	return render_template('post_page.html', form = form)


