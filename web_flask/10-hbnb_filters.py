#!/usr/bin/python3
"""Module flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Remove the current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states_and_cities():
    """List all states"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    dict = {"states": states, "amenities": amenities}
    return(render_template("10-hbnb_filters.html", **dict))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
