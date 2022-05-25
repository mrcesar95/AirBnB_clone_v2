#!/usr/bin/python3
"""Module flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Remove the current SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_cities(id=None):
    """List all states"""
    states = storage.all(State).values()
    if id is not None:
        for state in states:
            if state.id == id:
                return(render_template("9-states.html", states=state))
        return(render_template("9-states.html"))
    return(render_template("9-states.html", states=states, variable=True))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
