import random

class Animal:
    info = "a living organizm that feeds on organic matter."

    def __init__(self, name):
        print("An animal is created.")
        self.name = name

class Dog(Animal):
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."

    def __init__(self, name):
        super().__init__(name)
        print("A dog is created!")
        self.lucky_number = random.randint(1,10)
        self.fur = ""

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")

class Bulldog(Dog):
    def __init__(self,name):
        super().__init__(name)
        print("A bulldog is created.")

#dog1 = Bulldog("Fido")

class Electronics:
    def __init__(self, brand):
        self.brand = brand

class TV(Electronics):
    def __init__(self, brand):
        super().__init__(brand)
        self.size = ""

    def description(self):
        pass
       # print(f"The TV size is {self.size}")

class LCD(TV):
    def __init__(self, brand, size):
        super().__init__(brand)
        super().__init__(size)
        print(f"The TV is a {size} inch {brand} LCD.")

tv1 = LCD("Samsung","55")
tv2 = LCD("Samsung", "46")

tv1.description()
tv2.description()
