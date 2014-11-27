#!/bin/python


import sys

sys.path.append("test2")

from schedule_layout import EInkImage

image = EInkImage("./test2")

image.add_header("blah blah")
image.add_item("1 happened", "3pm", "4pm", "BSF")
image.add_item("2 happened", "3pm", "4pm", "BSF")

image.add_item("4 happened", "6pm", "4pm", "BSFsdfsd")

image.render()
