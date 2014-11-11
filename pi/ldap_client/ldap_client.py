#!/bin/bash

class LDAPClient:
	def resolveRFID(self, rfid):
		if rfid == "12345":
			return "scmallo"
		else:
			return "unknown"

	
