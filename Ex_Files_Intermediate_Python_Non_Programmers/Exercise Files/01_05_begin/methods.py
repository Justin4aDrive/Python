import random

class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."


    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"woof!  My name is {self.name} and my number is {self.lucky_number}")

dog1 = Dog("Fido")
dog2 = Dog("Sarah")

dog1.bark()
dog2.bark()


class TV:
    manufacturer = "Samsung"

    def __init__(self, size):
        self.size = size

    def description(self):
        print(f"The TV size is {self.size}")

tv1 = TV("55")
tv2 = TV("46")

tv1.description()
tv2.description()