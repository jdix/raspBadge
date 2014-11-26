#!/bin/python

import sys

sys.path.append("display/test2")

from schedule_layout import EInkImage

class EInkDisplay:
	
	def drawJSON(self, json):
		image = EInkImage("display/test2")

		image.addHeader("Boobies")
		print json
		for notifications in json['notifications']:
			title = notifications['title']
			start = notifications['start']
			end = notifications['end']
			location = notifications['location']
			image.addItem(title, location, start, end)
		image.render()		
