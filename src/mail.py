import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class emailHelper:
	def __init__(self, config):
		self.config = config
		self.emailFrom = config['SMTP']['From']
		self.emailTo = config['SMTP']['To']
		self.smtpServer = config['SMTP']['Server']
		self.smtpPort = config['SMTP']['Port']		

	def sendEmail(self, ovhServer):
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "OVH server available"
		msg['From'] = self.emailFrom
		msg['To'] = self.emailTo
		
		ovhServerLink = self.config['Server']['Link'] + ovhServer.hardware	
		
		html = """\
		<html>
		  <head></head>
		  <body>
			<p>Hi!<br>
			   New server <b>""" + ovhServer.hardware + """</b> available !<br>
			   Go <a href=\"""" + ovhServerLink + """\">""" + ovhServerLink + """.
			</p>
		  </body>
		</html>
		"""
		
		msg.attach(MIMEText(html, 'html'))
		
		s = smtplib.SMTP(self.smtpServer, self.smtpPort)
		#s = smtplib.SMTP('smtp.gmail.com', 587)
		#s.starttls()
		#s.login("YOUR_GMAIL_ADDRESS", "YOUR_GMAIL_PASSWORD")
		#s.send_message(msg)
		s.sendmail(self.emailFrom, self.emailTo, msg.as_string())
		s.quit()