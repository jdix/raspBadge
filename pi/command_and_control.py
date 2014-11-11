#!/bin/python


import sys
sys.path.append('notifications_client')
sys.path.append('rfid')
sys.path.append('ldap_client')
sys.path.append('sound')
sys.path.append('display')

from notifications_client import NotificationsClient
from rfid_reader import RFID
from ldap_client import LDAPClient
from sound import Sound
from display import EInkDisplay

class CommandAndControl:
	notificationsServer = NotificationsClient()
	rfidReader = RFID()
	ldapServer = LDAPClient()
	sounder = Sound()
	display = EInkDisplay()

	def next(self):
		print "Waiting for next swipe.."
		
		swipedRFID = self.rfidReader.waitForNext()
		print "Swiped RFID: ",  swipedRFID

		sidd = self.ldapServer.resolveRFID(swipedRFID)

		print "Resolved to SIDD: " + sidd

		if sidd != "unknown":
			notifications = self.notificationsServer.getForSIDD(sidd).getMostRelevent(5)
			self.display.drawJSON(notifications)
			self.sounder.playSound()
		else:
			print "Error - unknown User"
			self.sounder.playError()

cac = CommandAndControl()
while(True):
	cac.next()	
