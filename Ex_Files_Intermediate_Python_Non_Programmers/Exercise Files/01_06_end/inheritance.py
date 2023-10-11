import random

class Animal:
    info = "a living organism that feeds on organic matter"

    def __init__(self, name):
        print("An animal is created")
        self.name = name

class Dog(Animal):
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."


    def __init__(self, name):
        super().__init__(name)
        print("A dog is created")
        self.lucky_number = random.randint(1,10)
        self.fur = ""


    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")

class Bulldog(Dog):

    def __init__(self, name):
        super().__init__(name)
        print("A bulldog is created")

dog1 = Bulldog("Fido")

# In your previous class, add a parent
# or a child class
class Shape:
    side = 1

class Square(Shape):
    sides = 4

    def __init__(self):
        self.height = 0

    def area(self):
        return self.height * self.height

my_shape = Square()
my_shape.height = 10
print(my_shape.area())
