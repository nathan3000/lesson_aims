from flask import Flask

from models import db, Group

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db.init_app(app)

with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
    db.create_all()
    db.session.add(Group('Diggers', 'Preschool'))
	db.session.add(Group('Discoverers', 'Year R-2'))
	db.session.add(Group('Explorers', 'Years 3-6'))
	db.session.commit()

import controllers