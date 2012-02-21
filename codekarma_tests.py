# -*- coding: utf-8 -*-
"""

    Tests the codekarma application.

"""
import os
import codekarma
import tempfile
from flask import Flask
from flaskext.testing import TestCase


class CodeKarmaTestCase(TestCase):
    def create_app(self):
        codekarma.app.config['TESTING'] = True
        return codekarma.app
    # testing functions

    def test_empty_db(self):
        """Start with a blank database."""
        response = self.client.get('/api/cleanups')
        print response.data
        self.assertEquals(response.json, dict())
        


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
