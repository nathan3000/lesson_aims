from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

class Aim(db.Model):
	__tablename__ = 'aims'
	id = db.Column(db.Integer, primary_key=True)
	group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
	group = db.relationship('Group', backref=backref('aim', uselist=False))
	series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
	series = db.relationship('Series', backref=backref('aim', uselist=False))
	what_they_learnt = db.Column(db.String(250))
	lesson_aim = db.Column(db.String(250))
	bible_passage = db.Column(db.String(100))
	tip1 = db.Column(db.String(200))
	tip2 = db.Column(db.String(200))
	scheduled_date = db.Column(db.Date)

	def __init__(self, group, series, what_they_learnt=None, lesson_aim=None, bible_passage=None, tip1=None, tip2=None, scheduled_date=None):
		self.group = group
		self.series = series
		self.what_they_learnt = what_they_learnt
		self.lesson_aim = lesson_aim
		self.bible_passage = bible_passage
		self.tip1 = tip1
		self.tip2 = tip2
		self.scheduled_date = scheduled_date

	def __repr__(self):
		return '<Aims %r' % self.lesson_aim

class Group(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	group_name = db.Column(db.String(80), unique=True)
	school_year = db.Column(db.String(20), unique=True)

	def __init__(self, group_name, school_year):
		self.group_name = group_name
		self.school_year = school_year

	def __repr__(self):
		return self.group_name

class Series(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	series_name = db.Column(db.String(80), unique=True)
	memory_verse = db.Column(db.String(80))

	def __init__(self, series_name, memory_verse):
		self.series_name = series_name
		self.memory_verse = memory_verse

	def __repr__(self):
		return self.series_name


	


