##!/bin/python

import urllib2
import json 
from database import Database
from time import strftime
import datetime, dateutil.parser

source="googlecalendar"

class GooglePoller:
	def __init__(self):
		self.database = Database()

	def poll(self, url, username):
		try:
			calendarJson=json.loads(urllib2.urlopen(url).read())
			events=calendarJson['feed']['entry']
			self.database.deleteOldForUser(username, source)

			for event in events:
				title=event['title']['$t']
				loc=""
				start=""
				end=""
				time=""
				for where in event['gd$where']:
					location=where['valueString']
					if (location != ""):
						 loc = " Location: " + location
				for when in event['gd$when']:
					time = self.convertGoogleTime(when['startTime'])
					start = " - " + self.convertGoogleTimeToDisplay(when['startTime'])
					end= " until " + self.convertGoogleTimeToDisplay(when['endTime'])
		
				display = title + loc + start + end
		
				self.database.insertEvent(username, source, time, display)
		
		except ValueError:
			print("Error occurred while polling user")
		

	def convertGoogleTime(self, time):
		return format(dateutil.parser.parse(time))
		
	def convertGoogleTimeToDisplay(self, time):
		time = self.convertGoogleTime(time)
		today = format(datetime.date.today())
		tomorrow = format(datetime.date.today() + datetime.timedelta(days=1))
		
		if today in time:
			time = time.replace(today, "Today ")
		if tomorrow in time:
			time = time.replace(tomorrow, "Tomorrow ")
		return time

	def format(self, time):
		return strftime("%Y-%m-%d %H:%M:%S", time)
	

