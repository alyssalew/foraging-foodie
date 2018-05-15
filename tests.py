
from unittest import TestCase
from server import app

class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        """Stuff to do after each test."""

    def test1(self):
        """Testing the root route"""

        client = app.test_client()
        result = client.get('/')
        self.assertIn('<h1> Welcome to The Foraging Foodie </h1>', result)


    def test2(self):
        """Some other test"""
