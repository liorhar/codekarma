# -*- coding: utf-8 -*-
"""
    Code Karma - a dev group code analysis web application
    ~~~~~~

"""
from flask import Flask
from codekarma.database import db_session
from flaskext.sqlalchemy import SQLAlchemy


# configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/codekarma.db'
DEBUG = True
SECRET_KEY = 'kenshooooooo123'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

import codekarma.views

def init_db():
    import codekarma.models
    db.create_all()
