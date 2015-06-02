import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import render_template, Markup

from premailer import transform

def gethtmlContent(aims, parent):
	segment = []
	segment.append("<p>Dear parent, <br/><br/>")
	segment.append("It is our joy to be able to partner with you in teaching your child(ren) great spiritual truths from God's Word. In order to help you reinforce this week's teaching below you will find details of what the children learnt and a few questions or activities that you may find helpful:</p>")
	segment.append("<h2>Today's Teaching</h2>")
	for aim in aims:
		if aim.group.group_name in parent['group']:
			segment.append("<h3>%s (%s)</h3>" % (aim.group.group_name, aim.group.school_year))
			if aim.series:
				segment.append("<strong>Series:</strong> %s<br/>" % aim.series.series_name)
			if aim.bible_passage:
				segment.append("<strong>Bible Passage:</strong> %s <br />" % aim.bible_passage)
			if aim.what_they_learnt:
				segment.append("<strong>Today your child learned that:</strong> %s <br/>" % aim.what_they_learnt)
			if aim.lesson_aim:
				segment.append("<strong>Our teaching aim was:</strong> %s <br/>" % aim.lesson_aim)
			if aim.group.group_name == 'Diggers':
				segment.append("<strong>To reinforce this lesson this week:</strong>")
				segment.append("<ol>")
				if aim.tip1:
					segment.append("<li>%s</li>" % aim.tip1)
				if aim.tip2:
					segment.append("<li>%s</li>" % aim.tip2)
				segment.append("</ol></p>")
			if (aim.group.group_name == 'Discoverers') or (aim.group.group_name == 'Explorers'):
				segment.append("<strong>Here's 2 questions that you could ask your child</strong>")
				segment.append("<ol>")
				if aim.tip1:
					segment.append("<li>%s</li>" % aim.tip1)
				if aim.tip2:
					segment.append("<li>%s</li>" % aim.tip2)
				segment.append("</ol>")
				segment.append("<strong>Our memory verse for this teaching series is:</strong> %s</p>" % aim.series.memory_verse)
				
	segment.append("<p>Any questions please do feel free to contact me.</p>")
	segment.append("<p>Every blessing</p>")
	segment.append("<p>Amanda</p>")

	return Markup(''.join(segment))


def mailer(aims, parent):
	msg = MIMEMultipart('alternative')

	msg['Subject'] = "Today in Treasure Seekers"
	msg['From']    = "Nathan Fisher <nathan@christchurchsouthampton.org.uk>" # Your from name and email address
	msg['To']      = parent['email']

	html = transform(render_template('email.html', body=gethtmlContent(aims, parent)))

	part1 = MIMEText(html, 'html')

	#html = "<em>Mandrill speaks <strong>HTML</strong></em>"
	#part2 = MIMEText(html, 'html')

	username = os.environ['MANDRILL_USERNAME']
	password = os.environ['MANDRILL_PASSWORD']

	msg.attach(part1)
	#msg.attach(part2)

	s = smtplib.SMTP('smtp.mandrillapp.com', 587)

	s.login(username, password)

	print "Sending mail..to " + parent['email']

	s.sendmail(msg['From'], msg['To'], msg.as_string())

	s.quit()