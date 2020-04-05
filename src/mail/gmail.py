from __future__ import print_function
import base64
import pickle
import os
import mimetypes
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors
from .mail import emailHelper

class gmailHelper(emailHelper):
	def __init__(self, config):
		super().__init__(config)		
		
		# If modifying these scopes, delete the file token.pickle.
		SCOPES = ['https://www.googleapis.com/auth/gmail.send']
		
		creds = None
		# The file token.pickle stores the user's access and refresh tokens, and is
		# created automatically when the authorization flow completes for the first
		# time.
		if os.path.exists('mail/gmail/token.pickle'):
			with open('mail/gmail/token.pickle', 'rb') as token:
				creds = pickle.load(token)
		# If there are no (valid) credentials available, let the user log in.
		if not creds or not creds.valid:
			if creds and creds.expired and creds.refresh_token:
				creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file('mail/gmail/credentials.json', SCOPES)
				creds = flow.run_local_server(port=0)
			# Save the credentials for the next run
			with open('token.pickle', 'wb') as token:
				pickle.dump(creds, token)

		self.service = build('gmail', 'v1', credentials=creds)		
		
	def sendEmail(self, message):		
		b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
		b64_string = b64_bytes.decode()
		body = {'raw': b64_string}
	
		try:
			message = (self.service.users().messages().send(userId='me', body=body).execute())
			print('Message Id: %s' % message['id'])
			return message
		except errors.HttpError as error:
			print('An error occurred: %s' % error)