#!/bin/python

import csv
import sys
from google_poller import GooglePoller
 
poller = GooglePoller()

fileStream = open("googleusers.csv", 'rt')
try:
    reader = csv.reader(fileStream)
    for row in reader:
        url=row[0]
	username=row[1]
	
	print "Polling for user: " + username + " URL: " + url
	poller.poll(url, username)

finally:
    fileStream.close()

