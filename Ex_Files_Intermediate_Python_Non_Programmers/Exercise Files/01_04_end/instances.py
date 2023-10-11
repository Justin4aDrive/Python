import random

class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."


    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

dog1 = Dog("Fido")
dog2 = Dog("Sarah")

print(dog1.name)
print(dog2.name)

# Whatever your previous class was,
# make an instance of it and add an instance variable/attribute to it

class Square:
    sides = 4

my_shape = Square()
my_shape.height = 10
