#!/bin/python 


import urllib2
import json 
import itertools
from datetime import datetime, timedelta

import dateutil.parser
from collections import OrderedDict
from itertools import islice

class NotificationsClient:

	url="http://ec2-54-173-81-247.compute-1.amazonaws.com:8080/notifications/"

	def getForSIDD(self, sidd):
		output = urllib2.urlopen(self.url  + sidd).read()
		notificationsForUser = json.loads(output)

		return Notifications(notificationsForUser)		
	
class Notifications:
	def __init__(self, json):
		events=json['results']
		self.todayEvents = []		
		self.tomorrowEvents = []
		self.yesterdayEvents = []
		count = 0
		for event in events:
			eventDisplay = event['display']
			start = self.parseDay(event['time']['start'])
			end = self.parseDay(event['time']['end'])
			
			today = self.formatDay(datetime.today())
			tomorrow = self.formatDay(datetime.today() + timedelta(days=1))
			yesterday = self.formatDay(datetime.today() + timedelta(days=-1))
			if (start.date() == today.date()):
				self.todayEvents.append(eventDisplay)
			
			if (start.date() == tomorrow.date()):
				self.tomorrowEvents.append(eventDisplay)
			if (start.date() == yesterday.date()):
				self.yesterdayEvents.append(eventDisplay)

	def getMostRelevent(self, num):
		retVal = self.create("Today", self.todayEvents[:num])

		todayCount = len(retVal[0]["notifications"])
		if todayCount < num:
			retVal = retVal + self.create("Tomorrow", self.tomorrowEvents[:num - todayCount])
		if len(retVal) == 0:
			retVal = self.create("Yesterday", self.yesterdayEvents[:num])
		return retVal

	def create(self, day, n):
		 return [ { "day": day, "notifications": n } ]
	def parseDay(self, dateString):
		return self.formatDay(dateutil.parser.parse(dateString))
		
	def formatDay(self, time):
		return dateutil.parser.parse(time.strftime("%Y-%m-%d"))
	
	def slice(self, listToSlice, num):
		list(islice(listToSlices, 0, num - 1))
