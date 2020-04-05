from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class emailHelper:
	def __init__(self, config):
		self.config = config
		self.emailFrom = config['SMTP']['From']
		self.emailTo = config['SMTP']['To']

	def createEmail(self, ovhServer):
		msg = MIMEMultipart()
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
		
		return msg