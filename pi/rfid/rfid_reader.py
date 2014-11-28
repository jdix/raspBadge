#!/bin/python
import rfid

class RFID:
    def __init__(self):
       	self.cards = {
 		"2B53B49B"       : "whaleygeek", 
 		"04982B29EE0280" : "elektor RFID card", 
  		"EAC85517"       : "white card 1",
  		"24B1E145"       : "white card 2",
  		"C2091F58"       : "label 1",
  		"22F51E58"       : "label 2"
	} 
	

    def wait_for_next(self):
        # Import this module to gain access to the RFID driver

	# fill in this map with the names of your card ID's

  	# wait for a card to be detected as present
  	print("Waiting for a card...")
  	rfid.waitTag()
  	print("Card present")

  	# This demo only uses Mifare cards
  	if not rfid.readMifare():
    		print("This is not a mifare card")
  	else:
    	# What type of Mifare card is it? (there are different types)
    	print("Card type:" + rfid.getTypeName())

    	# look up the unique ID to see if we recognise the user
    	uid = rfid.getUniqueId()

  	# wait for the card to be removed
  	print("Waiting for card to be removed...")
  	rfid.waitNoTag()
  	print("Card removed")

	return uid
