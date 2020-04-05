import configparser
from ovh import ovh
from mail import simpleEmail
from mail import gmail

config = configparser.ConfigParser()   
config.read("config.txt")

api = ovh.api(config)
server = api.getServer(config['Server']['hardware'], config['Server']['region'])

if(server) is None:
	print(config['Server']['hardware'] + " not found")
elif(server.isAvailable) == True:
	print(server.hardware + " is available in " + server.region)
	
	if(config['SMTP'].getboolean('UseGmail')) == True:
		emailHelper = gmail.gmailHelper(config)
	else:
		emailHelper = simpleEmail.simpleEmailHelper(config)
	
	message = emailHelper.createEmail(server)
	emailHelper.sendEmail(message)
else:
	print(server.hardware + " is not available in " + server.region)
