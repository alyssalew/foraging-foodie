
import unittest
from server import app

class FlaskTests(unittest.TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        """Stuff to do after each test."""

    def test_root(self):
        """Testing the root route"""

        result = self.client.get('/')
        # print result.data
        self.assertIn('<h1> Welcome to The Foraging Foodie </h1>', result.data)


    # def test2(self):
    #     """Some other test"""


if __name__ == "__main__":
    unittest.main()
