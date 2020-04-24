#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Displays Python is cool or Python followed by text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Displays integer followed by is a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def template(n):
    """Displays HTML page with integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """Displays HTML page with integer as odd or even"""
    if n % 2 == 0:
        value = "even"
    else:
        value = "odd"
    return render_template('6-number_odd_or_even.html', n=n, value=value)

if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0')
