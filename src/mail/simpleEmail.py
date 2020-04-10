import smtplib
from .mail import emailHelper

class simpleEmailHelper(emailHelper):
	def __init__(self, config):
		super().__init__(config)		
		self.smtpServer = config['SMTP']['Server']
		self.smtpPort = config['SMTP']['Port']
		self.username = config['SMTP']['username']
		self.password = config['SMTP']['password']
		
	def sendEmail(self, message):	
		s = smtplib.SMTP_SSL(self.smtpServer, self.smtpPort)
		s.ehlo()
		s.login(self.username, self.password)		
		s.sendmail(self.emailFrom, self.emailTo, message.as_string())
		s.close()