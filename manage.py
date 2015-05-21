from flask import Flask
from flask.ext.script import Manager
from models import db, Group

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db.init_app(app)

manager = Manager(app)

@manager.command
def seed():
	db.drop_all()
	db.create_all()
	db.session.add(Group('Diggers', 'Preschool'))
	db.session.add(Group('Discoverers', 'Year R-2'))
	db.session.add(Group('Explorers', 'Years 3-6'))
	db.session.commit()

if __name__ == "__main__":
    manager.run()