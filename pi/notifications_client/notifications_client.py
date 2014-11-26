#!/bin/python 


import urllib2
import json 
import itertools
from datetime import datetime, timedelta

import dateutil.parser
from collections import OrderedDict
from itertools import islice

class NotificationsClient:

	url="http://raspberrypi:8080/notifications/"

	def getForSIDD(self, sidd):
		output = urllib2.urlopen(self.url  + sidd).read()
		notificationsForUser = json.loads(output)
		
		return Notifications(notificationsForUser)		
	
class Event:	
	def __init__(self, title, location, start, end):
		self.title = title
		self.location = location
		self.start = start
		self.end = end
	def toJSON(self):
		return { "title": self.title, "location": self.location, "start": self.format(self.start), "end": self.format(self.end) }

        def format(self, time):
                return dateutil.parser.parse(time).strftime('%H:%M')



class Notifications:
	def __init__(self, json):
		events=json['results']
		self.todayEvents = []		
		for event in events:
			title = event['title']
			location = event['location']
			start= event['time']['start']
			end = event['time']['end']
			
			today = self.formatDay(datetime.today())
			if (self.parseDay(start).date() == today.date()):
				self.todayEvents.append(Event(title, location, start, end).toJSON())
			
	def getMostRelevent(self, num):
		return self.create(self.todayEvents[:num])

	def create(self, n):
		 return {"notifications": n } 

	def parseDay(self, dateString):
		return self.formatDay(dateutil.parser.parse(dateString))
		
	def formatDay(self, time):
		return dateutil.parser.parse(time.strftime("%Y-%m-%d"))
	
	def slice(self, listToSlice, num):
		list(islice(listToSlices, 0, num - 1))
