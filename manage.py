from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager, Command, Option
from flask.ext.migrate import Migrate, MigrateCommand
from models import db, Aim, Series, Group

import mailer
import elvanto
import helpers

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)

class Seed(Command):
	"Seeds database"

	def run(self):
		db.drop_all()
		db.create_all()
		db.session.add(Group('Diggers', 'Preschool'))
		db.session.add(Group('Discoverers', 'Year R-2'))
		db.session.add(Group('Explorers', 'Years 3-6'))
		db.session.commit()

class Scheduler(Command):
	"Send lesson aims to parents emails"

	option_list = (
        Option('--test', '-t', dest='test'),
    )

	def run(self, test):
		#aims = Aim.query.filter_by(scheduled_date=datetime.date.today())
		aims = Aim.query.filter_by(scheduled_date=helpers.next_sunday())

		groups = []
		for aim in aims:
			groups.append(str(aim.group))

		parents = {}
		parents = elvanto.get_parents_list(groups)

		if test:
			print "This is a test"
			parents = {
				u'1dd766fa-162c-11e3-99d1-f98cd173cdaa': {'group': ['Diggers', 'Discoverers', 'Explorers'], 'email': u'nathan@christchurchsouthampton.org.uk', 'firstname': u'Nathan'}
			}

		for uid,parent in parents.items():
			mailer.mailer(aims, parent)


if __name__ == "__main__":
	manager.add_command('seed', Seed())
	manager.add_command('scheduler', Scheduler())
	manager.add_command('db', MigrateCommand)
	manager.run()