""" Foraging Foodie """


#########################################################################
##### Imports #####
import os

from jinja2 import StrictUndefined

import yelp_api  # Import the things needed to use the Yelp API, personal category definitions

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
##### Routes #####

@app.route('/')
def index():
    """ Homepage """

    return render_template('homepage.html')


@app.route('/search-handler', methods=['POST'])
def search_form_processing():
    """ Processing the fields from the search form"""

    print request.form

    location = request.form.get('location')
    curr_location = request.form.get('current_location')
    radius_mi = float(request.form.get('radius'))
    limit = request.form.get('limit')
    price_list = request.form.getlist('price')
    open_now = request.form.get('open_now')
    diet_restrict_list = request.form.getlist('diet_restrict')
    taste_list = request.form.getlist('taste')
    temp_list = request.form.getlist('temp')


    print type(radius_mi)


    # print "location:", location
    # print "current_loc:", curr_location
    # print "radius:", radius_mi
    # print "limit:", limit
    # print "price:" , price_list
    # print "open", open_now
    # print "diet:", diet_restrict_list
    # print "taste:", taste_list
    # print "temp:", temp_list


### Processing the form data to get ready for request ###

    yelp_categories = []

    # Add categories for dietary restrictions
    yelp_categories.extend(diet_restrict_list)


    # Getting categories for taste
    for taste in taste_list:
        if taste == "spicy":
            yelp_categories.extend(yelp_api.TASTE_SPICY)

        elif taste == "salty":
            yelp_categories.extend(yelp_api.TASTE_SALTY)

        elif taste == "sweet":
            yelp_categories.extend(yelp_api.TASTE_SWEET)

        elif taste == "umami":
            yelp_categories.extend(yelp_api.TASTE_UMAMI)

        # elif taste == "sour":


    # Getting categories for temp
    for temp in temp_list:
        if temp == "hot":
            yelp_categories.extend(yelp_api.TEMP_HOT)
        elif temp == "cold":
            yelp_categories.extend(yelp_api.TEMP_COLD)

    yelp_categories = list(set(yelp_categories))

    print "Categories: ", yelp_categories


    radius = int(yelp_api.miles_to_meters(radius_mi))

### Request payload ###

    payload = {
            "location": location,
            "radius": radius,
            "limit": limit,
            "price": price_list,
            "open_now": open_now,
            "categories": yelp_categories
    }

    print "Payload:", payload


    # test_json_dict = yelp_api.request_resturants(yelp_api.test_payload)
    # print "You just made a request to the Yelp API!"

    # test_json_dict = yelp_api.test_response_dict  # Pre-requested dict


    # The REAL request:
    json_dict = yelp_api.request_resturants(payload)
    print "You just made a request to the Yelp API!"


    return render_template('results.html',
                                location=location,
                                curr_location=curr_location,
                                radius=radius_mi,
                                limit=limit,
                                price= price_list,
                                open_now=open_now,
                                diet_restrict=diet_restrict_list,
                                taste=taste_list,
                                temp=temp_list,
                                # test_response_info=test_json_dict
                                response_info=json_dict
                            )


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