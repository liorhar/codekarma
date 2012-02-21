# -*- coding: utf-8 -*-
"""
    Code Karma - a dev group code analysis web application
    ~~~~~~

"""
from __future__ import with_statement
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from codekarma.models import Cleanup
from codekarma.database import db_session



# configuration
DATABASE = '/tmp/codekarma.db'
DEBUG = True
SECRET_KEY = 'kenshooooooo123'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('CODEKARMA_SETTINGS', silent=True)


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    db_session.remove()


@app.route('/api/cleanups')
def get_cleanups():
    cur = g.db.execute('select author, time, message, score from commits order by id desc')
    return jsonify()


@app.route('/api/cleanups', methods=['POST'])
def update_cleanups():
    c = cleanups.Cleanups().get_cleanups()
    return "ok"

