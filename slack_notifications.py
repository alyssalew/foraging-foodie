
import os
import requests
from datetime import datetime
import pytz

webhook_URL = os.environ['SLACK_WEBHOOK_URL']

## TEST DATA ##

first_name = "Alyssa"
last_name = "Lew"
email = "alyssa@example.com"

test_payload = {
            "location":"san francisco",
            "limit": 10,
            "open_now": "true",
            "categories":["korean", "mexican", "indpak"]
    }


################################################################

## BUILD ATTACHMENTS ##

def get_timestamp_attachment():

    pacific = pytz.timezone('US/Pacific')
    now = datetime.now(tz=pacific)
    format_now = now.strftime('%-m/%-d/%Y, %-I:%0M %p')

    # print timestamp

    timestamp = {
                    "title": "Timestamp",
                    "value": "{}".format(format_now),
                    "short": False
                }
    return timestamp

def name_attachment(first_name, last_name):

    name = {
                "title": "Name",
                "value": "{} {}".format(first_name, last_name),
                "short": True
            }
    return name


def email_attachment(email):

    email = {
                "title": "Email",
                "value": "{}".format(email),
                "short": True
            }
    return email


def search_attachment(search_payload):
    search = {
                "title": "Search Terms",
                "value": "{}".format(str(search_payload)),
                "short": False
            }

    return search


################################################################

def new_user(first_name, last_name, email):
    payload = {
        "attachments": [
            {
                "title": "New User Registration!! ",
                "color": "#e32072",
                "fields": [
                        get_timestamp_attachment(),
                        name_attachment(first_name, last_name),
                        email_attachment(email)
                ]
            }
        ]
    }

    print payload

    return requests.post(webhook_URL, json=payload)

def user_login(first_name, last_name, email, kind="NEW"):
    payload = {
        "attachments": [
            {
                "title": "User Login!! [{}]".format(kind),
                "color": "#7CD197",
                "fields": [
                        get_timestamp_attachment(),
                        name_attachment(first_name, last_name),
                        email_attachment(email)
                ]
            }
        ]
    }

    print payload

    return requests.post(webhook_URL, json=payload)

def user_search(search_payload):
    payload = {
        "attachments": [
            {
                "title": "User Search!!",
                "color": "#439FE0",
                "fields": [
                        get_timestamp_attachment(),
                        search_attachment(search_payload)
                ]
            }
        ]
    }

    print payload

    return requests.post(webhook_URL, json=payload)
