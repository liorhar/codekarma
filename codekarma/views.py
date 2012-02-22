from codekarma import app
from database import db_session
from models import Cleanup
from flask import jsonify


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    db_session.remove()


@app.route('/api/cleanups')
def get_cleanups():
    cleanups = Cleanup.query.all()
    return jsonify(cleanups)


@app.route('/api/cleanups', methods=['POST'])
def update_cleanups():
    return "ok"