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
    def __init__(self):
        pass

    notificationsServer = NotificationsClient()
    rfid_reader = RFID()
    ldapServer = LDAPClient()
    sounder = Sound()
    display = EInkDisplay()

    def next(self):
        print "Waiting for next swipe.."

        swiped_rfid = self.rfid_reader.wait_for_next()
        print "Swiped RFID: ", swiped_rfid

        sidd = self.ldapServer.resolveRFID(swiped_rfid)

        print "Resolved to SIDD: " + sidd

        if sidd != "unknown":
            notifications = self.notificationsServer.getForSIDD(sidd).getMostRelevent(5)
            self.display.draw_json(notifications)
            self.sounder.playSound()
        else:
            print "Error - unknown User"
            self.sounder.playError()


cac = CommandAndControl()
while True:
    cac.next()
