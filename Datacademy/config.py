#============================================================
#config.py
#============================================================

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#tells the app where to find the database and how to login 
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/datacademydb'