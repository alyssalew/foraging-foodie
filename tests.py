
import unittest
from server import app

import yelp_api

class FlaskTests(unittest.TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True


        # Make a mock for Yelp API request
        def _mock_request_restaurants(search_criteria):
            return yelp_api.test_response_dict_vegan_spicy

        yelp_api.request_restaurants = _mock_request_restaurants


    def tearDown(self):
        """Stuff to do after each test."""

    def test_render_root(self):
        """Testing the Root route"""
        
        print "test_render_root"

        result = self.client.get('/foraging-foodie')
        # print result.data
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h1 id="welcome"> Welcome to The Foraging Foodie </h1>', result.data)

    def test_render_register(self):
        """Testing the Register route"""

        print "test_render_register"

        result = self.client.get('/foraging-foodie/register')
        # print result.data
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h3>Register</h3>', result.data)


    def test_render_login(self):
        """Testing the Login route"""

        print "test_render_login"

        result = self.client.get('/foraging-foodie/login')
        # print result.data
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h3>Login</h3>', result.data)

    # def test_login(self):
    #     """Test login page."""

    #     print "test_login"

    #     result = self.client.post("/foraging-foodie/verify-login",
    #                               data={"email": "alyssa@example.com", "password": "123"},
    #                               follow_redirects=True)
    #     self.assertIn('<ul class="flashes">Hi Alyssa, you are now logged in!</ul>', result.data)


    # To send real request to Yelp API, comment out '_mock_request_restaurants' ^^
    def test_search(self):
        """Testing the restaurant search"""

        print "test_search"

        result = self.client.post('/foraging-foodie/results',
                                data={"location": "San Francisco", "radius": 5,
                                        "limit": 5, "diet_restrict":['vegan'], "taste":['spicy']})
        # print result.data
        self.assertIn('<div class="restaurant_name"> Gracias Madre', result.data)



if __name__ == "__main__":
    unittest.main()
