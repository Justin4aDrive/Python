import os
from pygame import mixer
import random
import time
import turtle

os.chdir(os.path.dirname(os.path.abspath(__file__)))

turtle.fd(0)      #show game window
turtle.title("Space Shooter")
turtle.speed(0)  #animation speed
turtle.bgcolor("black")  #background color
turtle.bgpic("image/galaxy.gif")
turtle.ht()     #hide deault turtle
turtle.setundobuffer(1)  #save to memory
turtle.tracer(0)  #drawing speed

mixer.init()  #initialize mixer for sound
mixer.music.load('sound/grooving.mp3')
mixer.music.set_volume(0.1)
mixer.music.play()

missile_sound = mixer.Sound("sound/missile.mp3")
missile_sound.set_volume(0.05)
crash_sound = mixer.Sound("sound/collision.mp3")
crash_sound.set_volume(0.5)
explosion_sound = mixer.Sound("sound/explosion.mp3")
explosion_sound.set_volume(0.8)

turtle.register_shape("diamond", ((0, 0), (10, 10), (20, 0), (10, -10)))

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
          if self.ycor() > 290:
               self.sety(290)
               self.rt(60)
          if self.ycor() < -290:
               self.sety(-290)
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
          self.shapesize(stretch_wid=0.7, stretch_len=1.5, outline=None)
          self.speed = 4
          #self.lives = 3
     
     def turn_left(self):
          self.lt(45)
     def turn_right(self):
          self.rt(45)
     def faster(self):
          self.speed += 1
     def slower(self):
          self.speed -= 1

class Ally(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.shapesize(stretch_wid=0.3, stretch_len=1.2, outline=None)
          self.speed = 8
          self.setheading(random.randint(0,360))

class Enemy(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.shapesize(stretch_wid=0.5, stretch_len=1.2, outline=None)
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
               mixer.Sound.play(missile_sound)
               self.goto(player.xcor(), player.ycor())
               self.setheading(player.heading())
               self.status = "fired"
     def move(self):
          if self.status == "ready":
               self.goto(-1000, 1000)
          if self.status == "fired":
               self.fd(self.speed)
          if self.xcor() > 390 or self.xcor() < -390 or \
               self.ycor() > 290 or self.ycor() < -290:  #boundry detection
               self.goto(-1000,1000)
               self.status = "ready"

class Explosion(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
          self.goto(-1000,-1000)
          self.frame = 0
     def explode(self, startx, starty):
          self.goto(startx,starty)
          self.setheading(random.randint(0,360))
          self.frame = 1
     def move(self):
          if self.frame > 0:
               self.fd(10)
               self.frame += 1
          if self.frame > 15:
               self.frame = 0
               self.goto(-1000, -1000)



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
          self.pen.goto(-400,300)
          self.pen.pendown()
          for side in range(2):
               self.pen.fd(800)
               self.pen.rt(90)
               self.pen.fd(600)
               self.pen.rt(90)
          self.pen.penup()
          self.pen.ht()
          self.pen.pendown()

     def show_status(self):
          self.pen.undo()
          msg = "Score: %s" %(self.score) + "    " + "Lives: %s" %(self.lives) 
          self.pen.color("red")
          self.pen.penup()
          self.pen.goto(-400,328)
          self.pen.write(msg, font=("Arial", 16, "bold"))


game = Game()       #Game object creation
game.draw_border()     #Drawing field border
game.show_status()  #game status

#Sprite creation
player = Player("arrow", "green", 0, 0)
#ally = Ally("square", "white", 0, 0)
#enemy = Enemy("circle", "yellow", -100, 0)
missile = Missile("arrow", "green", 0, 0)
explosions = []
for i in range (20):
     explosions.append(Explosion("circle", "orange", 0,0)) 
allies=[]
for i in range (6):
     allies.append(Ally("square", "white", 100, 0))
enemies=[]
for i in range (6):
     enemies.append(Enemy("circle", "yellow", -100, 0))

#key bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.faster, "Up")
turtle.onkey(player.slower, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()


#primary game loop
while game.lives > 0:
     
     turtle.update()
     time.sleep(0.05)
     player.move()
     #ally.move()
     #enemy.move()
     missile.move()
     for ally in allies:
          ally.move()
          if missile.is_collision(ally):
               mixer.Sound.play(explosion_sound)
               x = random.randint(-250,250)
               y = random.randint(-250,250)
               ally.goto(x,y)
               missile.status="ready"
               game.score -= 100  #decrease score
               game.show_status()
               for explosion in explosions:  #adding explosion effect
                    explosion.explode(missile.xcor(), missile.ycor())         

     for enemy in enemies:
          enemy.move()
          if player.is_collision(enemy):  #collision detection
               mixer.Sound.play(crash_sound)
               x = random.randint(-250,250)
               y = random.randint(-250,250)
               enemy.goto(x,y)
               game.score -= 50  #decrease score
               game.lives -= 1
               game.show_status()

          if missile.is_collision(enemy):
               mixer.Sound.play(explosion_sound)
               x = random.randint(-250,250)
               y = random.randint(-250,250)
               enemy.goto(x,y)
               missile.status="ready"
               game.score += 100  #increase score
               game.show_status()
               for explosion in explosions:  #adding explosion effect
                    explosion.explode(missile.xcor(), missile.ycor())
     
     for explosion in explosions:
          explosion.move()



delay = input("Press Enter to quit.")