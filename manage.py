from flask import Flask
from flask.ext.script import Manager
from models import db, Aim, Series, Group

import mailer
import elvanto

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

@manager.command
def scheduler():
	#aims = Aim.query.filter_by(scheduled_date=datetime.date.today())
	aims = Aim.query.all()
	print aims
	contacts = elvanto.get_contacts('Treasure Seeker')
	for contact in contacts:
		mailer.mailer(aims, contact)


if __name__ == "__main__":
    manager.run()