import json
import bottle
from bottle import route, run, request, abort
from pymongo import Connection, ASCENDING
 
connection = Connection('localhost', 27017)

db = connection.notifications
 
@route('/notifications/:username', method='GET')
def get_document(username):
	try:

		print "Serving request for: ", username
		dbResult = db.notification.find({"username": username}, {"time": 1, "display": 1, "_id": 0,}).sort([("time.start", 1), ("time.end", 1)])
		
		entity = [entry for entry in dbResult]
		if not entity:
	        	abort(405, 'User not found %s' % username)
		out = json.dumps({"results": entity}, sort_keys=True, indent=4, separators=(',', ': '))
		
		print out
	    	return out
	except ValueError:
		print "An error occurred"
 
run(host='0.0.0.0', port=8080)
