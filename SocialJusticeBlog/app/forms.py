#forms.py
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required


class NewPostForm(Form):
	title = TextField('title', validators = [Required()])
	author = TextField('author', validators = [Required()])
	content = TextAreaField('content', validators = [Required()])
