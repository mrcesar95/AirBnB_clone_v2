#!/usr/bin/python3
"""Module flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Close sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def show_states_list():
    """States list"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
