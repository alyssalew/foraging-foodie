# Foraging Foodie

Have you ever had a craving for something, but don’t know where to go? 

Foraging Foodie helps users find the perfect restaurants to satisfy their cravings. The app uses advanced search criteria such as taste, food temperature, and dietary restrictions, and integrates the Yelp Fusion API to generate suggestions. Once logged in, users can also track their restaurant visit history, personal restaurant ratings, add addresses and specify food preferences on their profile.

Foraging Foodie is powered by Python and Flask. The elegant and responsive web pages are built with Javascript and Bootstrap. User profile information is stored in a PostgreSQL database.

![Homepage](https://user-images.githubusercontent.com/4656934/123515642-12225d80-d64d-11eb-96bd-1aa66f2a132c.mov)

## Table of Contents
- [Technology Stack](#tech-stack)
- [Setup/Installation](#setup-install)
- [Additional Resources](#additional-resources)

## <a name="tech-stack"></a>Technology Stack
**Backend:**
- [Python] -- 2.7
- [Flask]
- [SQLAlchemy] 
- [Flask-SQLAlchemy]
- [PostgreSQL]
- [Requests]

**Frontend:**
- HTML/CSS
- [Jinja]
- [Bootstrap]
- Javascript
- [jQuery]

**APIs:**
- [Yelp Fusion API]
- [Slack API]

**Oher:**
- [Bcrypt] -- For password encryption
- [Font Awesome] -- For the awesome icons!

## <a name="setup-install"></a> Setup/Installation
**Prerequisites:**
- Python 2.7
- [Yelp Developer Account](https://www.yelp.com/developers)
    - [Yelp Fusion API Key](https://www.yelp.com/developers/documentation/v3/authentication)
- Slack workspace
    - [Incoming WebHooks App](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks)

** To host the project remotely you will need AWS EC2 server or equivalent **

**[Project Diagrams](https://github.com/alyssalew/foraging-foodie/wiki/Project-Diagrams)** :bar_chart:

### To run the app locally on your computer:
**1. Clone the repository:**
```
$ git clone https://github.com/alyssalew/foraging-foodie.git
```
**2. Create a virtual environment:**
```
$ virtualenv env
```
**3. Activate the virtual environment:**
```
$ source env/bin/activate
```
**4. Install dependencies:**
```
$ pip install -r requirements.txt
```
**5. Create a `secrets.sh` file:**
In this file put the following info (also in `template_secrets.sh`):
```
export APP_KEY="A_RANDOM_STRING"
export CLIENT_ID="YOUR_YELP_CLIENT_ID"
export YELP_API_KEY="YOUR_YELP_API_KEY (THE REALLY LONG STRING!)"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/xxxxxxxx/xxxxxxx/xxxxxxxxxxxxx"
```
**6. Create a database:**
```
$ createdb foraging-foodie
```
**7. Create your database tables and seed example data:**
```
$ python model.py

$ python seed.py
```

**8. Add your keys as environment variables:**
```
$ source secrets.sh
```
**9. Run the app:**
```
$ python server.py
```
After the initial setup, follow this pattern to start up the app:
```
$ source env/bin/activate
$ source secrets.sh
$ python server.py
```

---

If you want to use SQLAlchemy to query the database, run it in interactive mode:
```
$ python -i model.py
```
You can also query the database using PostgreSQL:
```
$ psql foraging-foodie
foraging-foodie=# SELECT * FROM users;
```

## <a name=“additional-resources”></a> Additional Resources
- [Yelp Fusion API - Business Search]
- [Yelp Fusion API - Categories]
- [Slack API - Messages]


[//]: # (Shoutout to Dillinger.io for README formatting!)

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

[Python]: <https://www.python.org/>
[Flask]: <http://flask.pocoo.org/>
[Requests]: <http://docs.python-requests.org/en/latest/>
[SQLAlchemy]: <https://www.sqlalchemy.org/>
[Flask-SQLAlchemy]: <http://flask-sqlalchemy.pocoo.org/2.3/>
[PostgreSQL]: <https://www.postgresql.org/>

[Jinja]: <http://jinja.pocoo.org/>
[Bootstrap]: <https://getbootstrap.com/> 
[jQuery]: <http://jquery.com>

[Yelp Fusion API]: <https://www.yelp.com/developers/documentation/v3>
[Yelp Fusion API - Business Search]: <https://www.yelp.com/developers/documentation/v3/business_search>
[Yelp Fusion API - Categories]: <https://www.yelp.com/developers/documentation/v3/all_category_list>

[Slack API]: <https://api.slack.com/>
[Slack API - Messages]: <https://api.slack.com/docs/messages>

[Bcrypt]: <https://pypi.org/project/bcrypt/>
[Font Awesome]: <https://fontawesome.com/>

