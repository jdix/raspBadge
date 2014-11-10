#!/bin/python

import traceback
import urllib2
import json 
from database import Database
from time import strftime
import datetime, dateutil.parser
import dateutil.parser

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
				time_display=""
				start_time=""
				end_time=""
				for where in event['gd$where']:
					location=where['valueString']
					if (location != ""):
						 loc = " Location: " + location
				for when in event['gd$when']:
					start=when['startTime']
					end=when['endTime']

					start_time = self.convertGoogleTime(start)
					end_time = self.convertGoogleTime(end)
					time_display = self.datesToDisplay(start, end)

				display = title + loc + time_display
		
				self.database.insertEvent(username, source, start_time, end_time, display)
		
		except ValueError:
			print("Error occurred while polling user")

	def datesToDisplay(self, start, end):
		start_display = self.convertToTimeOfDay(start) 
		end_display = self.convertToTimeOfDay(end)
		return " - " + start_display + " until " + end_display

	def convertGoogleTime(self, time):
		return self.formatDate("%Y-%m-%d %H:%M:%S",time)
		
	def convertToTimeOfDay(self, time):
		return self.formatDate("%H:%M", time)

	def formatDate(self, f, time):
		return dateutil.parser.parse(time).strftime(f)
