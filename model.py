"""Models and database functions for Foraging Foodie project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import date

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """ Users of Foraging Foodie website. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(75), nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('profiles.user_type_id'), nullable=False)

   # Define a relationship
    profile = db.relationship("Profile", uselist=False, backref=db.backref("user"))
    diet = db.relationship("Diet", secondary="users_diets", backref=db.backref("user"))
    address = db.relationship("Address", backref=db.backref("user"))
    favorite = db.relationship("Favorite", backref=db.backref("user"))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id={} first_name={} last_name={} email={}>".format(
                                                                        self.user_id,
                                                                        self.first_name,
                                                                        self.last_name,
                                                                        self.email
                                                                        )



class Address(db.Model):
    """ User addresses for Foraging Foodie website. """

    __tablename__ = 'addresses'

    address_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    address_label = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Address address_id={} user_id={} address_label={} address={} >".format(
                                                                                self.address_id,
                                                                                self.user_id,
                                                                                self.address_label,
                                                                                self.address
                                                                                )



class Profile(db.Model):
    """ User profiles of Foraging Foodie website. """

    __tablename__ = "profiles"

    user_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_name = db.Column(db.String(40), nullable=False, unique=True)
    type_taste = db.Column(db.ARRAY(db.String(50)), nullable=False, default=[])
    type_price = db.Column(db.ARRAY(db.String(50)), nullable=False, default=[])
    type_temp = db.Column(db.ARRAY(db.String(50)), nullable=False, default=[])
    type_diet = db.Column(db.ARRAY(db.String(50)), nullable=False, default=[])



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Profile user_type_id={} type_name={} [type_taste] [type_price] [type_temp] [type_diet]>".format(self.user_type_id,
                                                            self.type_name
                                                            )



class Diet(db.Model):
    """ Diets of Foraging Foodie website. """

    __tablename__ = "diets"

    diet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    diet_name = db.Column(db.String(20), nullable=False, unique=True)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Diet diet_id={} diet_name={}>".format(self.diet_id, self.diet_name)



class UserDiet(db.Model):
    """ Association table connecting Users to Diets. """

    __tablename__ = "users_diets"

    user_diet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    diet_id = db.Column(db.Integer, db.ForeignKey('diets.diet_id'), nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<UserDiet user_diet_id={} user_id={} diet_id={}>".format(self.user_diet_id,
                                                                    self.user_id, self.diet_id
                                                                    )



class Favorite(db.Model):
    """ User favorites of Foraging Foodie website. """

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'), nullable=False)
    favorite = db.Column(db.Boolean, nullable=False, default=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Favorite favorite_id={} user_id={} restaurant_id={} favorite={}>".format(
                                                                                self.favorite_id,
                                                                                self.user_id,
                                                                                self.restaurant_id,
                                                                                self.favorite
                                                                                )



class Visit(db.Model):
    """ Visits for Foraging Foodie website. """

    __tablename__ = 'visits'

    visit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    rating_id = db.Column(db.Integer, db.ForeignKey('ratings.rating_id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'), nullable=False)
    visit_date = db.Column(db.Date, nullable=True)


    # Define a relationship
    user = db.relationship("User", backref=db.backref("visit"))
    rating = db.relationship("Rating", backref=db.backref("visit"))
    restaurant = db.relationship("Restaurant", backref=db.backref("visit"))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Visit visit_id={} user_id={} restaurant_id={} visit_date={}>".format(
                                                                                self.visit_id,
                                                                                self.user_id,
                                                                                self.restaurant_id,
                                                                                self.visit_date
                                                                                )



class Rating(db.Model):
    """ Ratings for Foraging Foodie website. """

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating rating_id={} visit_id={} rating={}>".format(self.rating_id,
                                                            self.visit_id, self.score
                                                            )



class Restaurant(db.Model):
    """ Restaurants for Foraging Foodie website. """

    __tablename__ = 'restaurants'

    restaurant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    yelp_biz_id = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=True)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Restaurant restaurant_id={} yelp_biz_id={} name={}>".format(self.restaurant_id,
                                                                    self.yelp_biz_id, self.name
                                                                    )



##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///foraging-foodie'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
