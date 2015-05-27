import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def gethtmlContent(aims):
	for aim in aims:
		segment = []
		segment.append("<p>Dear parent <br/><br/>")
		segment.append("It is our joy to be able to partner with you in teaching your child(ren) great spiritual truths from God's Word. In order to help you reinforce this week's teaching below you will find details of what the children learnt and a few questions or activities that you may find helpful:<br/><br/>")
		segment.append("<strong>%s %s</strong><br/>" % (aim.group.group_name, aim.group.school_year))
		if aim.series:
			segment.append("%s Week<br/>" % aim.series.series_name)
		if aim.bible_passage:
			segment.append("Bible Passage: %s <br />" % aim.bible_passage)
		if aim.what_they_learnt:
			segment.append("Today your child learned that: %s <br/>" % aim.what_they_learnt)
		if aim.lesson_aim:
			segment.append("Our teaching aim was: %s <br/>" % aim.lesson_aim)
		if aim.group.group_name == 'Diggers':
			segment.append("To reinforce this lesson this week: <br/>")
			segment.append("<ol>")
			if aim.tip1:
				segment.append("<li>Idea 1: %s</li>" % aim.tip1)
			if aim.tip2:
				segment.append("<li>Idea 2: %s</li>" % aim.tip2)
			segment.append("</ol>")
		if (aim.group.group_name == 'Discoverers') and (aim.group.group_name == 'Explorers'):
			segment.append("Here's 2 questions that you could ask your child")
			segment.append("<ol>")
			if aim.tip1:
				segment.append("<li>%s</li>" % aim.tip1)
			if aim.tip2:
				segment.append("<li>%s</li>" % aim.tip2)
			segment.append("</ol>")
			segment.append("Our memory verse for this teaching series is: %s" % aim.series.memory_verse)
		

	return ''.join(segment)


def mailer(aims, to):

	print "Mailer:"

	msg = MIMEMultipart('alternative')

	msg['Subject'] = "Hello from Treasure Seekers"
	msg['From']    = "Nathan Fisher <nathan@christchurchsouthampton.org.uk>" # Your from name and email address
	msg['To']      = to['email']

	part1 = MIMEText(gethtmlContent(aims), 'html')

	#html = "<em>Mandrill speaks <strong>HTML</strong></em>"
	#part2 = MIMEText(html, 'html')

	username = os.environ['MANDRILL_USERNAME']
	password = os.environ['MANDRILL_PASSWORD']

	msg.attach(part1)
	#msg.attach(part2)

	s = smtplib.SMTP('smtp.mandrillapp.com', 587)

	s.login(username, password)

	print "Sending mail..to " + to['email']

	s.sendmail(msg['From'], msg['To'], msg.as_string())

	s.quit()