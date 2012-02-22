# -*- coding: utf-8 -*-
"""

    Tests the application.

"""
import os
from codekarma import app
import database
import tempfile
from flask import Flask
from flaskext.testing import TestCase
from mock import MagicMock, patch


class CodeKarmaTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app


    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        database.init_db()


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    # testing functions
    def test_empty_db(self):
        """Start with a blank database."""
        response = self.client.get('/api/cleanups')
        print response.data
        self.assertEquals(response.json, dict())
        

    def XXXt_update_cleanups(self):
        """Test Cleanups are updated"""
        with patch('cleanups.Cleanups') as mock:
            instance = mock.return_value
            instance.get_cleanups.return_value
            response = self.client.post('/api/cleanups')
            instance.get_cleanups.assert_called_once_with()

        self.assert200(response)


if __name__ == '__main__':
    unittest.main()
