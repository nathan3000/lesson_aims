from flaskext.mysql import MySQL
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import datetime
import config

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
app.config.from_envvar('LessonAims_Settings')

# mysql
mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()

@app.route('/aims/add', methods=['POST'])
def add():
	try:
		conn = mysql.connect()
		cursor = conn.cursor()

		if request.form['aim']:
			 error = 'Please fill in an aim.'

		today = datetime.date.today()
		scheduledDate = today + datetime.timedelta( (6-today.weekday()) % 7 )

		cursor.execute('insert into aims (text, group_name, scheduled_date) values (%s, %s, %s)',
			[request.form['aim'], request.form['groupName'], scheduledDate])
		conn.commit()
		flash('Success! Your aim has been submitted :)')
	except mysql.connect().Error as error:
		error = "Oops! Something went wrong."
	
	return redirect(url_for('index'))

def test_db():
	cur = g.db.execute('SELECT * from aims')
	data = cur.fetchone()
	print data

#@app.route('/aims/edit', methods=['POST'])
#def edit():


#@app.route('/aims/delete', methods=['POST'])
#def delete():


@app.route('/aims/', methods=['GET'])
def show_aims():
	try:
		cursor = mysql.get_db().cursor()
		cursor.execute('select * from aims')
		aims = [dict(text=row[2], group_name=row[4]) for row in cursor.fetchall()]
		return render_template('show.html', aims=aims)
	except mysql.get_db().Error as error:
		flash('Error')

if __name__ == '__main__':
	app.run()