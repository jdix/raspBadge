you need to have MongoDB running before running ./run.sh

install pip with: sudo apt-get install pip

then
sudo pip install pymongo

To install mongo see: 

http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian/


Notifications Server
Restful service which serves up the contents of the Notifications MongoDB database for the given user.
go to service with http://HOSTNAME:8080/notifications/scmallo
provides data in the following format:
{
  "results": [{
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

If you want to add another user + calendar, add your fake sidd + url to ./googleusers.txt


