# -*- coding: utf-8 -*-
"""

    Tests the codekarma application.

"""
import os
import codekarma
import unittest
import tempfile


class CodeKarmaTestCase(unittest.TestCase):

    def setUp(self):
        """Before each test, set up a blank database"""
        self.db_fd, codekarma.app.config['DATABASE'] = tempfile.mkstemp()
        codekarma.app.config['TESTING'] = True
        self.app = codekarma.app.test_client()
        codekarma.init_db()

    def tearDown(self):
        """Get rid of the database again after each test."""
        os.close(self.db_fd)
        os.unlink(codekarma.app.config['DATABASE'])

    # testing functions

    def test_empty_db(self):
        """Start with a blank database."""
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data


    def messages(self):
        """Test that messages work"""
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data


if __name__ == '__main__':
    unittest.main()
