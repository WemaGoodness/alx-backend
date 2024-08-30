#!/usr/bin/env python3
"""Flask app displaying the current time"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Return user dictionary or None if not found."""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """Set user in global variable."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Select the best match for the user's preferred language."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Select the best match for the user's timezone."""
    timezone = request.args.get('timezone')
    if not timezone and g.user:
        timezone = g.user.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """Route to render the home page."""
    current_time = datetime.now(pytz.timezone(get_timezone())).strftime('%c')
    return render_template('index.html', 
                           home_title=_("home_title"), 
                           home_header=_("home_header"),
                           logged_in_as=_("logged_in_as") if g.user else _("not_logged_in"),
                           current_time_is=_("current_time_is") % {'current_time': current_time})


if __name__ == "__main__":
    app.run(debug=True)
