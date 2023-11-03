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

     def move(self):
          self.fd(self.speed)

class Player(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.speed = 4
          self.lives = 3
     
     def turn_left(self):
          self.lt(45)
     def turn_right(self):
          self.rt(45)
     def faster(self):
          self.speed += 1
     def slower(self):
          self.speed -= 1


#Sprite creation
player = Player("arrow", "green", 0, 0)

#key bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.faster, "Up")
turtle.onkey(player.slower, "Down")
turtle.onkey(player.shoot, "Space")
turtle.listen()


#primary game loop
while True:
     player.move()





delay = input("Press Enter to quit.")