#forms.py
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required


class NewPostForm(Form):
	title = TextField('title', validators = [Required(message="Give your post a title")])
	author = TextField('author', validators = [Required(message="Tell us who you are!")])
	content = TextAreaField('content', validators = [Required(message="Write something!")])
