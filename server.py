""" Foraging Foodie """


#########################################################################
##### Imports #####
import os

import requests

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ['APP_KEY']

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

#########################################################################
##### SETUP FOR YELP API REQUESTS #####

yelp_api_key = os.environ['YELP_API_KEY']

search_url = "https://api.yelp.com/v3/businesses/search"
headers = {"Authorization": "Bearer {}".format(yelp_api_key)}


#########################################################################
# payload = {}  # Payload that I will build from form response

test_payload = {
            "location":"san francisco",
            "limit": 10,
            "open_now": "true",
            "categories":["korean", "mexican", "indpak"]
    }


def request_resturants(search_criteria):
    """ Request the Yelp API for restaurants with search criteria"""

    r = requests.get(search_url, headers=headers, params=test_payload)
    print (r.url)

    return r.json()


#########################################################################
##### Routes #####

@app.route('/')
def index():
    """ Homepage """

    return render_template('homepage.html')


@app.route('/search-handler', methods=['POST'])
def search_form_processing():
    """ Processing the fields from the search form"""

    location = request.form.get('location')
    curr_location = request.form.get('current_location')
    radius = request.form.get('radius')
    limit = request.form.get('limit')
    price = request.form.getlist('price')
    open_now = request.form.get('open_now')
    diet_restrict = request.form.getlist('diet_restrict')
    taste = request.form.getlist('taste')
    temp = request.form.getlist('temp')


    # print "location:", location
    # print "current_loc:", curr_location
    # print "radius:", radius
    # print "limit:", limit
    # print "price:" , price
    # print "open", open_now
    # print "diet:", diet_restrict
    # print "taste:", taste
    # print "temp:", temp

    return render_template('results.html',
                                location=location,
                                curr_location=curr_location,
                                radius=radius,
                                limit=limit,
                                price= price,
                                open_now=open_now,
                                diet_restrict=diet_restrict,
                                taste=taste,
                                temp=temp
                            )

##########################################################################
def miles_to_meters(number):
    """ Convert a number in miles to meters

        >> miles_to_meters(10)
        16093.4

        >>> miles_to_meters(2)
        3218.68

    """

    num_meters = number * 1609.34
    return num_meters


#########################################################################
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app) <<  Uncomment when have a DB to connect to

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')