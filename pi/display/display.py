#!/bin/python

import sys

sys.path.append("display/test2")

from schedule_layout import EInkImage


class EInkDisplay:
    def __init__(self):
        pass

    def draw_json(self, json):
        """
        :param json: string
        """
        image = EInkImage("display/test2")

        image.add_header("Bobbles")
        print json
        for notifications in json['notifications']:
            title = notifications['title']
            start = notifications['start']
            end = notifications['end']
            location = notifications['location']
            image.add_item(title, location, start, end)
        image.render()
