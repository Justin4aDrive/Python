import random

class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."


    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")

dog1 = Dog("Fido")
dog2 = Dog("Sarah")

dog1.bark()
dog2.bark()

# In your previous class, add a method
# that uses one of the instance variables

class Square:
    sides = 4

    def __init__(self):
        self.height = 0

    def area(self):
        return self.height * self.height

my_shape = Square()
my_shape.height = 10
print(my_shape.area())
