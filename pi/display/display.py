#!/bin/python

from libs.ScheduleLayout import EInkImage


class EInkDisplay:
    def __init__(self):
        pass

    def draw_json(self, json):
        """
        :param json: string
        """
        image = EInkImage("display/fonts")
	print "got json", json
        image.add_header("Desk: B")
        print json
        for notifications in json['notifications']:
            title = notifications['title']
            start = notifications['start']
            end = notifications['end']
            location = notifications['location']
            image.add_item(title=title, location=location, start=start, end=end)
        image.render()
