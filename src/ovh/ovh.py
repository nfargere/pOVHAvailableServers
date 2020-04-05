import requests
import json

class api:
	def __init__(self, config):
		self.url = config['API']['url']
		self.data = None

	def getData(self):
		if(self.data is None):
			self.loadData()
			
		return self.data

	def loadData(self):
		self.data = None
		
		try:
			response = requests.get(self.url)
			if(response.status_code == 200):
				self.data = response.json()
			else:
				raise Exception('Could not get data from the OVH API') 
		except Exception as e: print(e)		
		
	def getServer(self, hardware, region):
		data = self.getData()

		if(data is not None):
			server = None;
			i = 0		
			while i < len(data) and server is None:
				if data[i]['hardware'].lower() == hardware.lower() and data[i]['region'].lower() == region.lower():			
					server = data[i]
				i += 1	
			
			if server is not None:
				ovhServer = Server(hardware, region)
				ovhServer.isAvailable = self.isServerAvailable(server)
				return ovhServer
		
		return None		

	def isServerAvailable(self, server):
		isAvailable = False	
		
		i = 0
		while i < len(server['datacenters']) and isAvailable == False:
			datacenter = server['datacenters'][i]
			if datacenter['availability'].lower() != "unavailable":
				isAvailable = True
			i += 1
			
		return isAvailable

class Server:
	def __init__(self, hardware, region):
		self.hardware = hardware
		self.region = region
		self.isAvailable = False
