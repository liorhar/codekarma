from codekarma import app
from models import Cleanup
from flask import jsonify
from codekarma import db


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    db.session.remove()


@app.route('/api/cleanups')
def get_cleanups():
    cleanups = Cleanup.query.all()
    return jsonify(cleanups)


@app.route('/api/cleanups', methods=['POST'])
def update_cleanups():
    return "ok"
