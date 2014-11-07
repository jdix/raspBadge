RaspBadge Server software - currently deployed on EC2 box.


Google Calendar Poller

Currently set up to run GooglePoller on a minutely cron job which cleans out all 'googlecalendar' Notifications for the given user.
Dumps result into MongoDB for Notifications server to provide to our Pi Clients.


Notifications Server
Restful service which serves up the contents of the Notifications MongoDB database for the given user.

go to service with http://HOSTNAME:8080/notifications/scmallo

provides data in the following format:

{
    "results": [
        {
            "dateOfIngest": "2014-11-07 21:59:02",
            "display": "A thing - 2014-11-01 14:30:00+00:00 until 2014-11-01 15:30:00+00:00",
            "source": "googlecalendar",
            "time": "2014-11-01 14:30:00+00:00"
        }, 
	{
		...
	}]
}

The calendar is at: https://www.google.com/calendar/embed?src=bHZuYTVidTJybGZicGo2ZDNjazJqamJnbHNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ
although it looks like only i can edit it. 



