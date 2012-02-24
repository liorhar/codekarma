from sqlalchemy import Column, Integer, String, DateTime
from codekarma.database import Base


class Cleanup(Base):
    __tablename__ = 'cleanups'
    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    message = Column(String(300), nullable=False)
    score = Column(Integer, default=0)
    time = Column(DateTime, nullable=False)

    def __init__(self, author, message, score, time):
        self.author = author
        self.message = message
        self.score = score
        self.time = time

    def __repr__(self):
        return '%s - %s - score: %s' % (self.author, self.time, self.score)
