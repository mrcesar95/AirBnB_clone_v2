#!/usr/bin/python3
"""Module flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Hello route Flask"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """HBNB route Flask"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_ctext(text):
    """Print a variable rule <text>"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
