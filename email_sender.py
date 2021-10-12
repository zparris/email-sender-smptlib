import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Zahir Parris'
email['to'] = 'zahirparrispsn@gmail.com'
email['subject'] = 'You won £1,000,000!'

email.set_content(html.substitute({'name': 'Rio'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('parriszahir@gmail.com', 'KenelOGMafioso2016')
	smtp.send_message(email)
	print('all good my G!')