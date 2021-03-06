# -*- coding: utf-8 -*-
"""
    Code Karma - a dev group code analysis web application
    ~~~~~~

"""
from flask import Flask
from codekarma.database import db_session

# configuration
DATABASE = '/tmp/codekarma.db'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'default'
MIN_REVISION = 27355


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('CODEKARMA_SETTINGS', silent=True)

import codekarma.views
