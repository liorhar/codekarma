from codekarma.models import calculate_score
from nose.tools import eq_


def test_score_assignment():
    scores = [(0, "xxxx yyy")
            , (1, "bla bla [remove commented code]")
            , (1, "xx remove commented   code")
            , (1, "xxx remove COMMENTED CODE bla bla")
            , (2, "xxx aaa remove method zxcz")]
    for score in scores:
        validate_score(score[0], score[1])


def validate_score(score, message):
    calc_score = calculate_score(message)
    eq_(calc_score, score, 
            "message: %s was scored %s, expected: %s" % (message, calc_score, score))


