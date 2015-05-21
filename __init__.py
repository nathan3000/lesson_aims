from flask import Flask

from models import db

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db.init_app(app)

import controllers