#!/usr/bin/python3
"""
A Flask web application with various routes.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by the value of the text variable.
    Replace underscore symbols with a space.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display 'Python ' followed by the value of the text variable.
    Replace underscore symbols with a space.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Display 'n is a number' only if n is an integer.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display an HTML page only if n is an integer.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display an HTML page only if n is an integer.
    Display if the number is odd or even.
    """
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even="odd" if n % 2 else "even")


@app.teardown_appcontext
def teardown(exception):
    """
    Method to handle teardown of the app context.
    """
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
