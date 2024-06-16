#!/usr/bin/python3
"""
Flask web application that displays 'Hello HBNB!', 'HBNB', and 'C <text>'
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C ' followed by the value of <text>"""
    return "C " + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
