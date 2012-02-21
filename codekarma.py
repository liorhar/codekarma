# -*- coding: utf-8 -*-
"""
    Code Karma - a dev group code analysis web application
    ~~~~~~

"""
from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
import cleanups

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


def connect_db():
    """Returns a new connection to the database."""
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    """Creates the database tables."""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/api/cleanups')
def get_cleanups():
    cur = g.db.execute('select author, time, message, score from commits order by id desc')
    return jsonify()


@app.route('/api/cleanups', methods=['POST'])
def update_cleanups():
    c = cleanups.Cleanups().get_cleanups()
    return "ok"

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
