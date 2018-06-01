"""Models and database functions for Foraging Foodie project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """Users of Foraging Foodie website. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    user_type_id = db.Column(db.Integer, nullable=True)  # Will be a foreign key to Profiles table later
    diet = db.Column(db.Integer, nullable=True)  # Might have foreign key to association table

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id={} first_name={} last_name={} email={}>".format(self.user_id,
                                                                        self.first_name, self.last_name, self.email)

  
class Address(db.Model):
    """ User addresses for Foraging Foodie website. """

    __tablename__ = 'addresses'

    address_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    address_label = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    # Define a relationship
    user = db.relationship("User", backref=db.backref("addresses"))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Address address_id={} user_id={} address_label={} address={} >".format(self.address_id, self.user_id,
                                                                self.address_label, self.address)







class Profile(db.Model):
    """ User profiles of Foraging Foodie website. """

    __tablename__ = "profiles"

    user_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    profile_name = db.Column(db.String(40), nullable=False)
    profiles_define = db.Column(db.String(40), nullable=False)
    # Need to finish this one


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Profile user_type={}".format(self.user_type)


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
