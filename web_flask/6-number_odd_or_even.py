#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return ("{} is odd".format(n) if n % 2 != 0
            else "{} is even".format(n))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
