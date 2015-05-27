from LessonAims import app, db
from flask import request, session, g, redirect, url_for, abort, render_template, flash, Markup
import datetime
from forms import AimsForm
from models import Aim, Series, Group


@app.route('/', methods=('GET', 'POST'))
def add_aim():
	form = AimsForm()

	error = None	

	form.groupName.choices = [ (-1, '-- Choose a group from the list --')]
	form.groupName.choices.extend([(group.id, group.group_name) for group in Group.query.all()])

	form.seriesName.choices = [ (-1, '-- Choose a series from the list --'), (0, '-- Create a new series --')]
	form.seriesName.choices.extend([(series.id, series.series_name) for series in Series.query.all()])

	if request.method == 'POST' and form.validate():

		try:

			group = Group.query.get(request.form['groupName'])

			seriesId = request.form['seriesName']

			series = None

			if seriesId == '0':
				series = db.session.add(Series(request.form['newSeriesName']))
				db.session.commit()
			else:
				series = Series.query.get(seriesId)

			scheduledDate = next_sunday()

			aim = Aim(
				group, 
				series, 
				what_they_learnt=request.form['whatTheyLearnt'], 
				lesson_aim=request.form['lessonAim'],
				bible_passage=request.form['biblePassage'],
				tip1=request.form['tip1'],
				tip2=request.form['tip2'],
				scheduled_date=scheduledDate
			)
			
			db.session.add(aim)
			db.session.commit()

			flash(Markup('<strong>Success!</strong> Your aim has been submitted and is scheduled to be sent to parents on: <strong>%s</strong>' % scheduledDate.strftime("%A %-d %B %Y")))

			return redirect(url_for('show_aims'))

		except Exception as err:
			error = "Something went wrong {}".format(err)

	return render_template('index.html', form=form, error=error)

#@app.route('/aims/edit', methods=['POST'])
#def edit():


#@app.route('/aims/delete', methods=['POST'])
#def delete():


@app.route('/aims', methods=['GET'])
def show_aims():
	aims = Aim.query.filter_by(scheduled_date=next_sunday())
	return render_template('show.html', aims=aims)


def next_sunday():
	today = datetime.date.today()
	return today + datetime.timedelta( (6-today.weekday()) % 7 )
	

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()
