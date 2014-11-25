#!/bin/python

from schedule_layout import EInkImage

image = EInkImage()

image.addHeader("blah blah")
image.addItem("1 happened", "3pm", "4pm", "BSF")
image.addItem("2 happened", "3pm", "4pm", "BSF") 

image.addItem("4 happened", "6pm", "4pm", "BSFsdfsd") 

image.render()
