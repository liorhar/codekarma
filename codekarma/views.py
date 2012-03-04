from codekarma import app
from database import db_session
from models import Cleanup, get_latest_cleanups
from flask import jsonify, request, session, redirect, url_for, abort, \
     render_template
from sqlalchemy import func


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    db_session.remove()


@app.route('/api/cleanups')
def get_cleanups():
    n = request.args.get('n', 20)
    author = request.args.get('author', None)
    if author:
        cleanups = Cleanup.query.filter(Cleanup.author == author).\
            order_by(Cleanup.revision.desc()).limit(n)
    else:
        cleanups = Cleanup.query.order_by(Cleanup.revision.desc()).limit(n)
    return __jsonify_cleanups(cleanups)


@app.route('/api/cleanups', methods=['POST'])
def update_cleanups():
    cleanups = get_latest_cleanups()
    for c in cleanups:
        db_session.add(c)
    db_session.commit()
    return __jsonify_cleanups(cleanups)


@app.route('/api/cleanups/stats/')
def get_stats():
    stats = db_session.query(Cleanup.author,
        func.sum(Cleanup.score), func.count(Cleanup.author)).group_by(Cleanup.author).all()
    return jsonify(results=[dict(author=s[0], score=s[1], commits=s[2]) for s in stats])


@app.route('/review')
def review():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    n = request.args.get('n', 20)
    cleanups = Cleanup.query.order_by(Cleanup.revision.desc()).limit(n)
    return render_template('review.html', cleanups=cleanups)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('review'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return  "logged out"


def __jsonify_cleanups(cleanups):
    j = [dict(author=c.author, message=c.message,
          score=c.score, time=c.time.isoformat()) for c in cleanups]
    return jsonify(results=j)
