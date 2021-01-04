from flask import Flask

import resources
from ext import database


def create_app():
    app = Flask(__name__)
    resources.init_app(app)
    database.init_app(app)
    return app
