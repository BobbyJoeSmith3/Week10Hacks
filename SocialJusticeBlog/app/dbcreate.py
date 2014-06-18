#dbcreate.py
#Go ahead, make my day....tabase.

#Creates the database based on the models defined in models.py

from config import SQLALCHEMY_DATABASE_URI
from app import db
db.create_all()