from sqlalchemy import Column, Integer, String, DateTime, func
from codekarma.database import Base, db_session
from codekarma import app
from datetime import datetime
from subversion_api import get_revisions
import random


class Cleanup(Base):
    __tablename__ = 'cleanups'
    revision = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    message = Column(String(300), nullable=False)
    score = Column(Integer, default=0)
    time = Column(DateTime, nullable=False)

    def __init__(self, revision, author, message, score, time):
        self.revision = revision
        self.author = author
        self.message = message
        self.score = score
        self.time = time

    def __repr__(self):
        return '%s - %s - score: %s' % (self.author, self.time, self.score)

def calculate_score(message):
    return random.randint(1, 10)

def get_latest_cleanups():
    revision = get_latest_revision()
    logs = get_revisions(revision)
    return map(log_to_cleanup, logs)


def get_latest_revision():
    latest_revision = db_session.query(func.max(Cleanup.revision)).scalar()
    return latest_revision if latest_revision is not None else app.config['MIN_REVISION']


def log_to_cleanup(log):
    score = calculate_score(log.message)
    return Cleanup(author = log.author, revision = log.revision.number,
            message=log.message, time=datetime.fromtimestamp(log.date), score=score)
