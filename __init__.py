from flask import Flask

from models import db

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db.init_app(app)

with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()

import controllers