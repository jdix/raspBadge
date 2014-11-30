#!/bin/python


import sys, pygame, time

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
	try:
		sound_file = "/home/pi/raspBadge/pi/sound/beep1.ogg"
                pygame.mixer.init(44100, -16, 1, 1024)
		sound = pygame.mixer.Sound(sound_file)
                sound.play(loops = 1)
        except pygame.error, message:
                print "Cannot load sound: ", message, sound_file
	print "Swiped RFID: ", swiped_rfid

	time.sleep(2)

        sidd = self.ldapServer.resolveRFID(swiped_rfid)

        print "Resolved to SIDD: " + sidd

        if sidd != "unknown":
            notifications = self.notificationsServer.getForSIDD(sidd).getMostRelevent(5)
            self.display.draw_json(notifications)
           # self.sounder.playSound()
	    sound_file2 = "/home/pi/raspBadge/pi/sound/match5.wav"
	    sound2 = pygame.mixer.Sound(sound_file2)
            sound2.play(loops = 2)

        else:
            print "Error - unknown User"
            #self.sounder.playError()
	    sound_file3 = "/home/pi/raspBadge/pi/sound/badswap.wav"
	    sound3 = pygame.mixer.Sound(sound_file3)
            sound3.play(loops = 3)


cac = CommandAndControl()
while True:
    cac.next()
