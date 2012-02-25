from codekarma import app
from database import db_session
from models import Cleanup, get_latest_cleanups
from flask import jsonify


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    db_session.remove()


@app.route('/api/cleanups')
def get_cleanups():
    cleanups = Cleanup.query.order_by(Cleanup.revision.desc()).limit(20)
    return __jsonify_cleanups(cleanups)


@app.route('/api/cleanups', methods=['POST'])
def update_cleanups():
    cleanups = get_latest_cleanups()
    for c in cleanups:
        db_session.add(c)
    db_session.commit()
    return __jsonify_cleanups(cleanups)


def __jsonify_cleanups(cleanups):
    j = [dict(author=c.author, message=c.message,
          score=c.score, time=c.time.isoformat()) for c in cleanups]
    return jsonify(results=j)
