import configparser
import ovh
import mail

config = configparser.ConfigParser()   
config.read("config.txt")

api = ovh.api(config)
server = api.getServer(config['Server']['hardware'], config['Server']['region'])

if(server) is None:
	print(config['Server']['hardware'] + " not found")	
elif(server.isAvailable) == True:
	emailHelper = mail.emailHelper(config)
	emailHelper.sendEmail(server)
	print(server.hardware + " is available in " + server.region)
else:
	print(server.hardware + " is not available in " + server.region)
