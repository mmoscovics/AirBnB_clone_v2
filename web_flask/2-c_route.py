#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Displays C followed by text"""
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0')
