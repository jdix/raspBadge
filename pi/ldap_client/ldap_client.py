#!/bin/bash

class LDAPClient:
	def resolveRFID(self, rfid):
		if rfid == "A36F5F74":
			return "smallo"
		elif rfid == "CCB932D4":
			return "jdixon"
		elif rfid == "BBIDSDFS":
			return "spitch"
		elif rfid == "12345":
			return "smallo"
		else:
			return "unknown"

	
