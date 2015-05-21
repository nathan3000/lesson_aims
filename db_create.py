#!flask/bin/python
from app import db
from models import Aim, Group, Series

db.drop_all()
db.create_all()
db.session.add(Group('Diggers', 'Preschool'))
db.session.add(Group('Discoverers', 'Year R-2'))
db.session.add(Group('Explorers', 'Years 3-6'))
db.session.commit()