#!/bin/python

from pymongo import MongoClient
from time import gmtime, strftime

class Database:
	def __init__(self):
		connection = MongoClient("localhost")
		self.db = connection.notifications.notification

	def deleteOldForUser(self, username, source):
		command={"source": source, "username": username}
		self.db.remove(command)

	def insertEvent(self, username, source, time, display): 
		dbEvent = {
			"username": username,
			"source": source,
			"time": time, 
			"display": display,
			"dateOfIngest": strftime("%Y-%m-%d %H:%M:%S", gmtime())
		}
	 	self.db.insert(dbEvent)



