import datetime

def next_sunday():
	today = datetime.date.today()
	return today + datetime.timedelta( (6-today.weekday()) % 7 )