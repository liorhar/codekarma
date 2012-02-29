from sqlalchemy import create_engine
from codekarma.models import calculate_score
from nose.tools import eq_
from unittest import TestCase
from codekarma.database import db_session


def test_score_assignment():
    scores = [(0, "xxxx yyy"),
        (1, "bla bla [remove commented code]"),
        (1, "xx remove commented   code"),
        (1, "xxx remove COMMENTED CODE bla bla"),
        (2, "xxx aaa remove method zxcz")]
    for score in scores:
        validate_score(score[0], score[1])


def validate_score(score, message):
    calc_score = calculate_score(message)
    eq_(calc_score, score,
            "message: %s was scored %s, expected: %s" \
                % (message, calc_score, score))


class TestCleanups(TestCase):
    def setup():
        engine = create_engine('sqlite:///:memory:')
        session.configure(bind=engine)
        # You probably need to create some tables and
        # load some test data, do so here.

        # To create tables, you typically do:
        model.metadata.create_all(engine)

    def teardown():
        session.remove()

    def test(self):
        pass
