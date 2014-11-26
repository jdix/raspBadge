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
			events=calendarJson['items']
			self.database.deleteOldForUser(username, source)

			for event in events:
				title=event['summary']
				loc=""
				start_time=""
				end_time=""
				
				location=event.get('location', '')
				if (location != ""):
					loc = location
				start=event['start']['dateTime']
				end=event['end']['dateTime']

				start_time = self.convertGoogleTime(start)
				end_time = self.convertGoogleTime(end)

				self.database.insertEvent(username, source, title, start_time, end_time, loc)
		
		except ValueError:
			print("Error occurred while polling user")

	def datesToDisplay(self, start, end):
		start_display = self.convertToTimeOfDay(start) 
		end_display = self.convertToTimeOfDay(end)
		return " " + start_display + " ~ " + end_display

	def convertGoogleTime(self, time):
		return self.formatDate("%Y-%m-%d %H:%M:%S",time)
		
	def convertToTimeOfDay(self, time):
		return self.formatDate("%H:%M", time)

	def formatDate(self, f, time):
		return dateutil.parser.parse(time).strftime(f)
