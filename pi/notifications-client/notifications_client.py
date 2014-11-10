#!/bin/python 


import urllib2
import json 

class NotificationsClient:

	url="http://localhost:8080/notifications/"

	def getForSIDD(self, sidd):
		output = urllib2.urlopen(self.url  + sidd).read()
		notificationsForUser = json.loads(output)
		return notificationsForUser		
	
