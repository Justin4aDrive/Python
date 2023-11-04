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

          if self.xcor() > 390:  #boundry detection
               self.setx(390)
               self.rt(60)
          if self.xcor() < -390:
               self.setx(-390)
               self.rt(60)
          if self.ycor() > 315:
               self.sety(315)
               self.rt(60)
          if self.ycor() < -275:
               self.sety(-275)
               self.rt(60)
     
     def is_collision(self, other):
          if (self.xcor() >= (other.xcor() -20)) and \
          (self.xcor() <= (other.xcor() +20)) and \
          (self.ycor() >= (other.ycor() -20)) and \
          (self.ycor() <= (other.ycor() +20)):
               return True
          else:
               return False


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

class Enemy(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.speed = 6
          self.setheading(random.randint(0,360))

class Missile(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
          self.speed = 20
          self.status = "ready"
          self.goto(-1000, 1000)

     def fire(self):
          if self.status == "ready":
               self.goto(player.xcor(), player.ycor())
               self.setheading(player.heading())
               self.status = "fired"
     def move(self):
          if self.status == "ready":
               self.goto(-1000, 1000)
          if self.status == "fired":
               self.fd(self.speed)
          if self.xcor() > 390 or self.xcor() < -390 or \
               self.ycor() > 315 or self.ycor() < -275:  #boundry detection
               self.goto(-1000,1000)
               self.status = "ready"


class Game():
     def __init__(self):
          self.level = 1
          self.score = 0
          self.state = "playing"
          self.pen = turtle.Turtle()
          self.lives = 3                ### duplicate to player?

     def draw_border(self):        #game field border
          self.pen.speed(0)
          self.pen.color("white")
          self.pen.pensize(3)
          self.pen.penup()
          self.pen.goto(-400,320)
          self.pen.pendown()
          for side in range(2):
               self.pen.fd(800)
               self.pen.rt(90)
               self.pen.fd(600)
               self.pen.rt(90)
          self.pen.penup()
          self.pen.ht()

     

#Game opbject creation
game = Game()

#Drawing field border
game.draw_border()

#Sprite creation
player = Player("arrow", "green", 0, 0)
enemy = Enemy("circle", "yellow", -100, 0)
missile = Missile("arrow", "green", 0, 0)

#key bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.faster, "Up")
turtle.onkey(player.slower, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()


#primary game loop
while True:
     player.move()
     enemy.move()
     missile.move()

     if player.is_collision(enemy):  #collision detection
          x = random.randint(-250,250)
          y = random.randint(-250,250)
          enemy.goto(x,y)
     
     if missile.is_collision(enemy):
          x = random.randint(-250,250)
          y = random.randint(-250,250)
          enemy.goto(x,y)
          missile.status="ready"


delay = input("Press Enter to quit.")