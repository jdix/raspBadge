import json
import bottle
from bottle import route, run, request, abort
from pymongo import Connection, DESCENDING
 
connection = Connection('localhost', 27017)
db = connection.notifications
 
@route('/notifications/:username', method='GET')
def get_document(username):
	try:

		dbResult = db.notification.find({"username": username}, {"time": 1, "display": 1, "source": 1, "_id": 0, "dateOfIngest": 1}).sort([("time", DESCENDING)])
		
		entity = [entry for entry in dbResult]
		if not entity:
	        	abort(404, 'User not found %s' % username)
		out = json.dumps({"results": entity}, sort_keys=True, indent=4, separators=(',', ': '))
		print out
	    	return out
	except ValueError:
		print "An error occurred"
 
run(host='localhost', port=8080)
