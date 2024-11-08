#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel


class config:
    """ configuration settings for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app, configure_jinja=False)


@app.route('/', strict_slashes=False)
def home():
    """ home page """
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run()