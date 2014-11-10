#!/bin/python 



from notifications_client import NotificationsClient

print "------------------------"
print "This is a test app for the NotificationsClient just to see it run in the console"
print "Running against /notifications/scmallo"
print "------------------------"

print NotificationsClient().getForSIDD("scmallo")
