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
    radius_mi = request.form.get('radius')
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


    # test_json_dict = yelp_api.request_resturants(yelp_api.test_payload)
    # print "You just made a request to the Yelp API!"

    # test_json_dict = yelp_api.test_response_dict  # Pre-requested dict


    # The REAL request:
    payload = yelp_api.create_payload(location, radius_mi, limit, price_list, open_now, diet_restrict_list, taste_list, temp_list)

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