""" All the Yelp requests related things """


#########################################################################
##### Imports #####

import requests
import os


#########################################################################
##### SETUP FOR YELP API REQUESTS #####

yelp_api_key = os.environ['YELP_API_KEY']

search_url = "https://api.yelp.com/v3/businesses/search"
headers = {"Authorization": "Bearer {}".format(yelp_api_key)}


#########################################################################
test_payload = {
            "location":"san francisco",
            "limit": 10,
            "open_now": "true",
            "categories":["korean", "mexican", "indpak"]
    }



def create_payload(location, radius_mi, limit, price_list, open_now, diet_restrict_list, taste_list, temp_list):
    """ Given form data make appropiate payload for Yelp API request"""

    ### Processing the form data to get ready for request ###

    yelp_categories = []

    # Add categories for dietary restrictions
    yelp_categories.extend(diet_restrict_list)


    # Getting categories for taste
    for taste in taste_list:
        if taste == "spicy":
            yelp_categories.extend(TASTE_SPICY)

        elif taste == "salty":
            yelp_categories.extend(TASTE_SALTY)

        elif taste == "sweet":
            yelp_categories.extend(TASTE_SWEET)

        elif taste == "umami":
            yelp_categories.extend(TASTE_UMAMI)

        # elif taste == "sour":


    # Getting categories for temp
    for temp in temp_list:
        if temp == "hot":
            yelp_categories.extend(TEMP_HOT)
        elif temp == "cold":
            yelp_categories.extend(TEMP_COLD)

    yelp_categories = list(set(yelp_categories))

    print "Categories: ", yelp_categories


    radius = int(miles_to_meters(radius_mi))

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
    return payload



def request_resturants(search_criteria):
    """ Request the Yelp API for restaurants with search criteria"""

    r = requests.get(search_url, headers=headers, params=search_criteria)  # r is type JSON
    print (r.url)

    return r.json()  # Convert r to dictionary


##########################################################################
##### HELPER FUNCTIONS #####
def miles_to_meters(number):
    """ Convert a number in miles to meters

        >> miles_to_meters(10)
        16093.4

        >>> miles_to_meters(2)
        3218.68

    """

    num_meters = float(number) * 1609.34
    return num_meters

#########################################################################
##### CATEGORY DEFINITIONS #####

# Tastes (mine --> Yelp categories):

TASTE_SPICY = ["korean", "mexican", "indpak"]
TASTE_SALTY = ["japanese", "thai", "vietnamese", "chinese", "pizza"]
TASTE_SWEET = ["icecream", "cakeshop", "donuts", "desserts", "chocolate", "cupcakes", "bakeries"]
TASTE_UMAMI = ["japanese", "thai", "vietnamese", "chinese"]

# Temperature (mine --> Yelp categories):

TEMP_HOT = ["soup", "ramen", "hotpot"]
TEMP_COLD = ["icecream", "salad", "sushi", "acaibowls"]




#########################################################################
##### SAMPLE DATA FOR TESTING #####

test_response_dict = {u'region': {u'center': {u'latitude': 37.76089938976322, u'longitude': -122.43644714355469}}, u'total': 355, u'businesses': [{u'rating': 4.0, u'review_count': 4338, u'name': u'El Farolito', u'transactions': [], u'url': u'https://www.yelp.com/biz/el-farolito-san-francisco-2?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$', u'distance': 1848.3253463643052, u'coordinates': {u'latitude': 37.75265, u'longitude': -122.41812}, u'alias': u'el-farolito-san-francisco-2', u'image_url': u'https://s3-media1.fl.yelpcdn.com/bphoto/OPnKCvgBR2-lQ1-yahrpiA/o.jpg', u'categories': [{u'alias': u'mexican', u'title': u'Mexican'}, {u'alias': u'seafood', u'title': u'Seafood'}, {u'alias': u'sandwiches', u'title': u'Sandwiches'}], u'display_phone': u'(415) 824-7877', u'phone': u'+14158247877', u'id': u'SGRmnarrNuVEsAjYdEoA0w', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'2779 Mission St', u'San Francisco, CA 94110'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'2779 Mission St', u'zip_code': u'94110'}}, {u'rating': 4.0, u'review_count': 3369, u'name': u'La Taqueria', u'transactions': [], u'url': u'https://www.yelp.com/biz/la-taqueria-san-francisco-2?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$', u'distance': 1958.4726910319168, u'coordinates': {u'latitude': 37.750883, u'longitude': -122.418123}, u'alias': u'la-taqueria-san-francisco-2', u'image_url': u'https://s3-media4.fl.yelpcdn.com/bphoto/owapw7nAz7VmnAFG2NcMBQ/o.jpg', u'categories': [{u'alias': u'mexican', u'title': u'Mexican'}], u'display_phone': u'(415) 285-7117', u'phone': u'+14152857117', u'id': u'JARsJVKLPgs_yC3cwDnp7g', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'2889 Mission St', u'San Francisco, CA 94110'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'2889 Mission St', u'zip_code': u'94110'}}, {u'rating': 4.0, u'review_count': 2285, u'name': u'HRD', u'transactions': [u'delivery'], u'url': u'https://www.yelp.com/biz/hrd-san-francisco-4?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$$', u'distance': 4255.584833618084, u'coordinates': {u'latitude': 37.7811065758548, u'longitude': -122.395329724426}, u'alias': u'hrd-san-francisco-4', u'image_url': u'https://s3-media4.fl.yelpcdn.com/bphoto/ImvLt9I8ACHwfYthZw8vVw/o.jpg', u'categories': [{u'alias': u'korean', u'title': u'Korean'}, {u'alias': u'asianfusion', u'title': u'Asian Fusion'}, {u'alias': u'mexican', u'title': u'Mexican'}], u'display_phone': u'(415) 543-2355', u'phone': u'+14155432355', u'id': u'bUr4iq2mKKiBOu2HKynylg', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'521A 3rd St', u'San Francisco, CA 94107'], u'country': u'US', u'address2': None, u'address3': u'', u'state': u'CA', u'address1': u'521A 3rd St', u'zip_code': u'94107'}}, {u'rating': 4.0, u'review_count': 3717, u'name': u'Tropisue\xf1o', u'transactions': [u'restaurant_reservation'], u'url': u'https://www.yelp.com/biz/tropisue%C3%B1o-san-francisco-3?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$$', u'distance': 3941.5902762189608, u'coordinates': {u'latitude': 37.7853008468227, u'longitude': -122.403918653727}, u'alias': u'tropisue\xf1o-san-francisco-3', u'image_url': u'https://s3-media2.fl.yelpcdn.com/bphoto/hUZgDmue1VRfvIXai6I0wg/o.jpg', u'categories': [{u'alias': u'mexican', u'title': u'Mexican'}, {u'alias': u'cocktailbars', u'title': u'Cocktail Bars'}], u'display_phone': u'(415) 243-0299', u'phone': u'+14152430299', u'id': u'_EncdQezAzcShATMFXL0dA', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'75 Yerba Buena Ln', u'San Francisco, CA 94103'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'75 Yerba Buena Ln', u'zip_code': u'94103'}}, {u'rating': 4.0, u'review_count': 1663, u'name': u"Don Pisto's", u'transactions': [], u'url': u'https://www.yelp.com/biz/don-pistos-san-francisco-2?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$$', u'distance': 5089.089100642661, u'coordinates': {u'latitude': 37.80078, u'longitude': -122.40784}, u'alias': u'don-pistos-san-francisco-2', u'image_url': u'https://s3-media2.fl.yelpcdn.com/bphoto/9oDu7WFzaLXhNblXfvr1NA/o.jpg', u'categories': [{u'alias': u'mexican', u'title': u'Mexican'}], u'display_phone': u'(415) 395-0939', u'phone': u'+14153950939', u'id': u'voFE8DTKsTFi1Vzm_zzd0Q', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'510 Union St', u'San Francisco, CA 94133'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'510 Union St', u'zip_code': u'94133'}}, {u'rating': 4.5, u'review_count': 1038, u'name': u'Tacorea', u'transactions': [], u'url': u'https://www.yelp.com/biz/tacorea-san-francisco?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$', u'distance': 3930.491179354393, u'coordinates': {u'latitude': 37.789806, u'longitude': -122.410709}, u'alias': u'tacorea-san-francisco', u'image_url': u'https://s3-media2.fl.yelpcdn.com/bphoto/rHxbA24tQgh8eIDrHGhCOA/o.jpg', u'categories': [{u'alias': u'mexican', u'title': u'Mexican'}, {u'alias': u'korean', u'title': u'Korean'}, {u'alias': u'latin', u'title': u'Latin American'}], u'display_phone': u'(415) 885-1325', u'phone': u'+14158851325', u'id': u'u39mZEYojBiNic3lqKhPNw', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'809 Bush St', u'San Francisco, CA 94108'], u'country': u'US', u'address2': u'', u'address3': None, u'state': u'CA', u'address1': u'809 Bush St', u'zip_code': u'94108'}}, {u'rating': 4.0, u'review_count': 2638, u'name': u'DOSA on Fillmore', u'transactions': [u'pickup', u'restaurant_reservation'], u'url': u'https://www.yelp.com/biz/dosa-on-fillmore-san-francisco-3?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$$$', u'distance': 2739.555675095702, u'coordinates': {u'latitude': 37.78535, u'longitude': -122.43284}, u'alias': u'dosa-on-fillmore-san-francisco-3', u'image_url': u'https://s3-media2.fl.yelpcdn.com/bphoto/yRQT1qg44iAdAdKkONJ9Ig/o.jpg', u'categories': [{u'alias': u'indpak', u'title': u'Indian'}], u'display_phone': u'(415) 441-3672', u'phone': u'+14154413672', u'id': u'U1TgSEKZwgdTftTOxCtFOQ', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'1700 Fillmore St', u'San Francisco, CA 94115'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'1700 Fillmore St', u'zip_code': u'94115'}}, {u'rating': 4.0, u'review_count': 3062, u'name': u"Nick's Crispy Tacos", u'transactions': [u'pickup', u'delivery', u'restaurant_reservation'], u'url': u'https://www.yelp.com/biz/nicks-crispy-tacos-san-francisco-2?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$', u'distance': 4115.017206768006, u'coordinates': {u'latitude': 37.79607, u'longitude': -122.42196}, u'alias': u'nicks-crispy-tacos-san-francisco-2', u'image_url': u'https://s3-media4.fl.yelpcdn.com/bphoto/hVCVrVFjEHwZqA5ujDfxfg/o.jpg', u'categories': [{u'alias': u'mexican', u'title': u'Mexican'}, {u'alias': u'sportsbars', u'title': u'Sports Bars'}], u'display_phone': u'(415) 409-8226', u'phone': u'+14154098226', u'id': u'ziVej4oW2JpUConTE_Y_mg', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'1500 Broadway', u'San Francisco, CA 94109'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'1500 Broadway', u'zip_code': u'94109'}}, {u'rating': 4.0, u'review_count': 2776, u'name': u'Gracias Madre', u'transactions': [u'pickup', u'delivery'], u'url': u'https://www.yelp.com/biz/gracias-madre-san-francisco?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$$', u'distance': 1514.5832835114525, u'coordinates': {u'latitude': 37.761606, u'longitude': -122.419241}, u'alias': u'gracias-madre-san-francisco', u'image_url': u'https://s3-media4.fl.yelpcdn.com/bphoto/Yy2vzxq0fAJUA5Q0cpziFw/o.jpg', u'categories': [{u'alias': u'vegan', u'title': u'Vegan'}, {u'alias': u'mexican', u'title': u'Mexican'}], u'display_phone': u'(415) 683-1346', u'phone': u'+14156831346', u'id': u'rwiL8C8989DlHMD88bxi3A', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'2211 Mission St', u'San Francisco, CA 94110'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'2211 Mission St', u'zip_code': u'94110'}}, {u'rating': 4.0, u'review_count': 2231, u'name': u'Pancho Villa Taqueria', u'transactions': [u'pickup', u'delivery'], u'url': u'https://www.yelp.com/biz/pancho-villa-taqueria-san-francisco?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$', u'distance': 1419.6056739594994, u'coordinates': {u'latitude': 37.764857, u'longitude': -122.4210934}, u'alias': u'pancho-villa-taqueria-san-francisco', u'image_url': u'https://s3-media3.fl.yelpcdn.com/bphoto/O2SSf_9ES8CsH5lnXvGT-Q/o.jpg', u'categories': [{u'alias': u'mexican', u'title': u'Mexican'}], u'display_phone': u'(415) 864-8840', u'phone': u'+14158648840', u'id': u'UjjNgzBFAVXF3iVXPVjH_Q', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'3071 16th St', u'San Francisco, CA 94103'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'3071 16th St', u'zip_code': u'94103'}}]}
test_response_dict_all = {u'region': {u'center': {u'latitude': 37.76089938976322, u'longitude': -122.43644714355469}}, u'total': 1600, u'businesses': [{u'rating': 4.5, u'review_count': 9184, u'name': u'Bi-Rite Creamery', u'transactions': [], u'url': u'https://www.yelp.com/biz/bi-rite-creamery-san-francisco?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$', u'distance': 944.5063435745504, u'coordinates': {u'latitude': 37.7615877, u'longitude': -122.4257548}, u'alias': u'bi-rite-creamery-san-francisco', u'image_url': u'https://s3-media2.fl.yelpcdn.com/bphoto/orW7CXAlnSwOFcXZ2kB-lg/o.jpg', u'categories': [{u'alias': u'icecream', u'title': u'Ice Cream & Frozen Yogurt'}, {u'alias': u'bakeries', u'title': u'Bakeries'}], u'display_phone': u'(415) 626-5600', u'phone': u'+14156265600', u'id': u'wGl_DyNxSv8KUtYgiuLhmA', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'3692 18th St', u'San Francisco, CA 94110'], u'country': u'US', u'address2': None, u'address3': u'', u'state': u'CA', u'address1': u'3692 18th St', u'zip_code': u'94110'}}, {u'rating': 4.0, u'review_count': 7134, u'name': u'Tartine Bakery & Cafe', u'transactions': [], u'url': u'https://www.yelp.com/biz/tartine-bakery-and-cafe-san-francisco?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$$', u'distance': 1091.249585562033, u'coordinates': {u'latitude': 37.7614250022004, u'longitude': -122.424051321456}, u'alias': u'tartine-bakery-and-cafe-san-francisco', u'image_url': u'https://s3-media1.fl.yelpcdn.com/bphoto/vTLu8G86IqIazm7BRqIH4g/o.jpg', u'categories': [{u'alias': u'bakeries', u'title': u'Bakeries'}, {u'alias': u'cafes', u'title': u'Cafes'}, {u'alias': u'desserts', u'title': u'Desserts'}], u'display_phone': u'(415) 487-2600', u'phone': u'+14154872600', u'id': u'ri7UUYmx21AgSpRsf4-9QA', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'600 Guerrero St', u'San Francisco, CA 94110'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'600 Guerrero St', u'zip_code': u'94110'}}, {u'rating': 4.5, u'review_count': 3602, u'name': u"Mitchell's Ice Cream", u'transactions': [], u'url': u'https://www.yelp.com/biz/mitchells-ice-cream-san-francisco?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$', u'distance': 2207.086160001414, u'coordinates': {u'latitude': 37.7442315, u'longitude': -122.422816}, u'alias': u'mitchells-ice-cream-san-francisco', u'image_url': u'https://s3-media2.fl.yelpcdn.com/bphoto/ttfrmolywd0rLpcYJmf7Uw/o.jpg', u'categories': [{u'alias': u'icecream', u'title': u'Ice Cream & Frozen Yogurt'}, {u'alias': u'customcakes', u'title': u'Custom Cakes'}], u'display_phone': u'(415) 648-2300', u'phone': u'+14156482300', u'id': u'76smcUUGRvq3k1MVPUXbnA', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'688 San Jose Ave', u'San Francisco, CA 94110'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'688 San Jose Ave', u'zip_code': u'94110'}}, {u'rating': 4.0, u'review_count': 4339, u'name': u'El Farolito', u'transactions': [], u'url': u'https://www.yelp.com/biz/el-farolito-san-francisco-2?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$', u'distance': 1848.3253463643052, u'coordinates': {u'latitude': 37.75265, u'longitude': -122.41812}, u'alias': u'el-farolito-san-francisco-2', u'image_url': u'https://s3-media1.fl.yelpcdn.com/bphoto/OPnKCvgBR2-lQ1-yahrpiA/o.jpg', u'categories': [{u'alias': u'mexican', u'title': u'Mexican'}, {u'alias': u'seafood', u'title': u'Seafood'}, {u'alias': u'sandwiches', u'title': u'Sandwiches'}], u'display_phone': u'(415) 824-7877', u'phone': u'+14158247877', u'id': u'SGRmnarrNuVEsAjYdEoA0w', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'2779 Mission St', u'San Francisco, CA 94110'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'2779 Mission St', u'zip_code': u'94110'}}, {u'rating': 4.5, u'review_count': 1970, u'name': u'B Patisserie', u'transactions': [], u'url': u'https://www.yelp.com/biz/b-patisserie-san-francisco-2?adjust_creative=9gRH7knlnW1mT4NXafHkcQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9gRH7knlnW1mT4NXafHkcQ', u'price': u'$$', u'distance': 3019.0169808458404, u'coordinates': {u'latitude': 37.78783, u'longitude': -122.44073}, u'alias': u'b-patisserie-san-francisco-2', u'image_url': u'https://s3-media2.fl.yelpcdn.com/bphoto/JSpohxMdt431tYAe2sZhQQ/o.jpg', u'categories': [{u'alias': u'bakeries', u'title': u'Bakeries'}, {u'alias': u'cakeshop', u'title': u'Patisserie/Cake Shop'}, {u'alias': u'macarons', u'title': u'Macarons'}], u'display_phone': u'(415) 440-1700', u'phone': u'+14154401700', u'id': u'2XQm-uFcTS7oc8MFP-8olA', u'is_closed': False, u'location': {u'city': u'San Francisco', u'display_address': [u'2821 California St', u'San Francisco, CA 94115'], u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'2821 California St', u'zip_code': u'94115'}}]}





