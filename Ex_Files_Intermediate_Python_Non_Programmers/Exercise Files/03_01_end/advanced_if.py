
age = 90
height = 120

# and
if age >= 8 and height >= 135:
    print("You can ride the ride!")

# or
if age >= 17 or height >= 160:
    print("You can ride the super ride!")

# elif (else if)
if height < 120:
    print("You can't ride any rides :(")
elif height < 135:
    print("You can ride level-1 rides.")
elif height < 200:
    print("You can ride any ride!")
else:
    print("Too tall to ride the rides :(")

# Create an if statement with both "and" and "or"
if age % 2 == 0 and age > 100 or age == 0:
    print("You have an interesting age :)")
