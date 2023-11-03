import os
import random

import turtle
turtle.fd(0)      #show game window
turtle.speed(0)  #animation speed
turtle.bgcolor("black")  #background color
turtle.ht()     #hide deault turtle
turtle.setundobuffer(1)  #save to memory
turtle.tracer(1)  #drawing speed

class Sprite(turtle.Turtle):
     def __init__(self, spriteshape, color, startx, starty):
          turtle.Turtle.__init__(self, shape = spriteshape)
          self.speed(0)
          self.penup()
          self.color(color)
          self.fd(0)
          self.goto(startx, starty)
          self.speed = 1

#Sprite creation
player = Sprite("arrow", "green", 0, 0)




delay = input("Press Enter to quit.")