This is the client library for running against the notifications restful service running on the EC2 box.l

include into your app with:

from '../notifications_client/notifications_client' import NotificationsClient
NotificationsClient().getForSIDD("scmallo").getMostRelevent(5)

This will take the 5 most relevent events in the following order,

1) today
2) tomorrow
3) yesterday (if none of the above appear - i'm not sure if we even need this feature)

Therefore if there are 3 events for today and 3 tomorrow, it will take 3 + 2.

Outputs the most relevent in json format:
[ {
	'notifications': [ 
		'another - 18:30 until 19:30', 
	   	'A Meeting Location: Desk 123 - 20:00 until 21:00'
	 ],
	'day': 'Today'
  },
 {
	'notifications': [
		'tomrrow one - 19:30 until 20:30'
	],
	'day': 'Tomorrow'
} ]


OR 

Run a sample query from the command line with ./run.sh
