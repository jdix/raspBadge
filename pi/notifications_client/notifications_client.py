#!/bin/python 


import urllib2
import json 
import itertools
from datetime import datetime, timedelta

import dateutil.parser
from collections import OrderedDict
from itertools import islice

class NotificationsClient:

	url="http://localhost:8080/notifications/"

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
		return { "title": title, "location": location, "start": self.format(start), "end": self.format(end) }

        def formatDate(self, f, time):
                return dateutil.parser.parse("%H:%M").strftime(f)



class Notifications:
	def __init__(self, json):
		events=json['results']
		self.todayEvents = []		
		for event in events:
			title = event['title']
			location = event['location']
			start = self.parseDay(event['time']['start'])
			end = self.parseDay(event['time']['end'])
			
			today = self.formatDay(datetime.today())
			if (start.date() == today.date()):
				self.todayEvents.append(Event(title, location, start, end).toJSON())
			
	def getMostRelevent(self, num):
		return self.create("Today", self.todayEvents[:num])

	def create(self, day, n):
		 return [ { "day": day, "notifications": n } ]

	def parseDay(self, dateString):
		return self.formatDay(dateutil.parser.parse(dateString))
		
	def formatDay(self, time):
		return dateutil.parser.parse(time.strftime("%Y-%m-%d"))
	
	def slice(self, listToSlice, num):
		list(islice(listToSlices, 0, num - 1))
