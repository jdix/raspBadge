you need to have MongoDB running before running ./run.sh

install pip with: sudo apt-get install pip

then
sudo pip install pymongo
sudo pip install bottle
To install mongo see: 

http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian/
http://c-mobberley.com/wordpress/2013/10/14/raspberry-pi-mongodb-installation-the-working-guide/

'mongod' needs to be running before starting the './run.sh' script.

Notifications Server
Restful service which serves up the contents of the Notifications MongoDB database for the given user.
go to service with http://HOSTNAME:8080/notifications/scmallo

Provides data in the following format:
{
  "results": [{
      "dateOfIngest": "2014-11-07 21:59:02",
      "display": "Chat about stuff. Location: Room 123 - 14:30 until 15:30",
      "source": "googlecalendar",
      "time": {
        "start": "2014-11-01 14:30:00", 
        "end": "2014-11-01 15:00:00"
      }
  },
  {
    ...
  }]
}

-- dateOfIngest: The time that the data was ingested
-- display: The string which will appear on the screen.
-- source: Where the data came from, i.e. desk booking, nude websites etc
-- time: The start and end time of the event. 

All data pollers should squeeze their data into this format. 
If we find that we need more data later for other sources then we can always update the other poller(s).

