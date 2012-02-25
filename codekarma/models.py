from sqlalchemy import Column, Integer, String, DateTime, func
from codekarma.database import Base, db_session
from datetime import datetime


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


def get_latest_cleanups():
    revision = get_latest_revision()
    print revision
    revision += 1
    return [Cleanup(revision , 'liorh',
        'stam %s' % revision, revision % 5, datetime.now())]

def get_latest_revision():
    return db_session.query(Cleanup.revision).order_by(Cleanup.revision.desc()).limit(1).one()[0]
