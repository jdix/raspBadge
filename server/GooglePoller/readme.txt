you need to have MongoDB running before running ./run.sh

install pip with: sudo apt-get install pip

then
sudo pip install pymongo

To install mongo see: 

http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian/

Currently set up to run GooglePoller on a minutely cron job which cleans out all 'googlecalendar' Notifications for the given user.
Dumps result into MongoDB for Notifications server to provide to our Pi Clients.


The calendar is at: https://www.google.com/calendar/embed?src=bHZuYTVidTJybGZicGo2ZDNjazJqamJnbHNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ
although it looks like only i can edit it.

If you want to add another user + calendar, add your fake sidd + url to ./googleusers.csv
http://fullcalendar.io/docs/google_calendar/


