import smtplib
from .mail import emailHelper

class simpleEmailHelper(emailHelper):
	def __init__(self, config):
		super().__init__(config)		
		self.smtpServer = config['SMTP']['Server']
		self.smtpPort = config['SMTP']['Port']
		
	def sendEmail(self, message):		
		s = smtplib.SMTP(self.smtpServer, self.smtpPort)		
		s.sendmail(self.emailFrom, self.emailTo, message.as_string())
		s.quit()