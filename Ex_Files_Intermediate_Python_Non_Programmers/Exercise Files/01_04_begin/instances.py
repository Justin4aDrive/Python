import random

class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."
    
    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = (random.randint(1,10))
        self.name = name

## print(Dog.info)


dog1 = Dog("Fido")
dog2 = Dog("Sarah")

print(dog1.name)
print(dog2.name)


class TV:
    manufacturer = "Samsung."

    def __init__(self, size):
        self.size = size

tv1 = TV("55")
tv2 = TV("46")

print(tv1.size)
print(tv2.size)