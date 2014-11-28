#!/bin/python


from libs.ScheduleLayout import EInkImage

image = EInkImage("./fonts")

image.add_header("Seat 63")
image.add_item("1 happened", "3pm", "4pm", "Room 1")
image.add_item("2 happened", "3pm", "4pm", "Park Bench")

image.add_item(title="Scala Meetup", start="6pm", location="Cafe", important=1)

image.render()
