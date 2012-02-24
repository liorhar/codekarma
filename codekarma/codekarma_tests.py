# -*- coding: utf-8 -*-
"""

    Tests the application.

"""
import os
from datetime import datetime
from codekarma import db
from models import Cleanup
import tempfile
from flask import Flask
from flaskext.testing import TestCase
from mock import MagicMock, patch


class CodeKarmaTestCase(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    TESTING = True

    def create_app(self):
        app = Flask(__name__)
        app.config.from_object(self)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # testing functions
    def test_empty_db(self):
        """Start with a blank database."""
        response = self.client.get('/api/cleanups')
        self.assertEquals(response.json, dict())

    def test_get_one_item(self):
        cleanup = Cleanup('liorh', 'stam', 0,
            datetime(2007, 12, 6, 15, 29, 43, 79060))
        db.session.add(cleanup)
        db.session.commit()
        response = self.client.get('/api/cleanups')
        self.assertEquals(len(response.json), 1)


if __name__ == '__main__':
    unittest.main()
