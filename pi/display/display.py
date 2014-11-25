#!/bin/python

class EInkDisplay:
	def drawJSON(self, json):
		for notifications in json['notifications']:
			title = notifications['title']
			start = notifications['start']
			end = notifications['end']
			location = notifications['location']
			
			print title, location, start, end
		
