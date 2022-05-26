# simple pong game in python 3
# By Jonathan Caldwell

import turtle

wn = turtle.Screen()
wn.title("Pong by Jonathan Caldwell")
wn.bgcolor("blue")
wn.setup(width = 1024, height = 768)
wn.tracer(0)

# Main Loop

while True:
    wn.update()