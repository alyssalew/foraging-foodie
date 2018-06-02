from sqlalchemy import func
from model import Diet

from model import connect_to_db, db
from server import app


def load_diets():
    """ Load the diets into the DB """

    print "Diets"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Diet.query.delete()

    DIETS = ['vegan', 'vegetarian', 'gluten_free', 'kosher', 'halal']

    for item in DIETS:

        diet = Diet(diet_name=item)

        # We need to add to the session or it won't ever be stored
        db.session.add(diet)

    # Once we're done, we should commit our work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_diets()

